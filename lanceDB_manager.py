from glob import glob
import os
import lancedb
from lancedb.pydantic import LanceModel, Vector
from lancedb.embeddings import get_registry
import pandas as pd

tmp_path = "db.lance"


class lanceDB_manager:
    def __init__(self) -> None:
        self.db = lancedb.connect(tmp_path)
        self.func_image = get_registry().get("open-clip").create()
        self.func_text = get_registry().get("sentence-transformers").create(name="BAAI/bge-small-en-v1.5", device="cuda")

        class Images(LanceModel):
            # label: str  = self.func_text.SourceField()
            image_uri: str
            image_bytes: bytes = self.func_image.SourceField()
            # vector_text: Vector(self.func_text.ndims()) = self.func_text.VectorField() # vector column 
            vector_image: Vector(self.func_image.ndims()) = self.func_image.VectorField() # Another vector column 

        self.schema = Images
        self.create_table()
        print("DB created")


    
    def create_table(self):
        if "images" in self.db.table_names():
            tbl = self.db.open_table("images")
            tbl.create_fts_index(["image_uri"], replace=True)
            
            images_uris = glob("images/*.jpg")
            images_uris = [i for i in images_uris if i not in tbl.search(i, query_type="fts").to_pandas()["image_uri"].tolist()]

            print(f"{len(images_uris)} images to add")
            image_bytes = [open(uri, "rb").read() for uri in images_uris]
            if len(images_uris) > 0:
                tbl.add(
                    pd.DataFrame({"image_uri": images_uris, "image_bytes": image_bytes})
                )
            return tbl

        tbl = self.db.create_table("images", schema=self.schema)

        # read image bytes from local files
        images_uris = glob("images/*.jpg")
        image_bytes = [open(uri, "rb").read() for uri in images_uris]
        tbl.add(
            pd.DataFrame({"image_uri": images_uris, "image_bytes": image_bytes})
        )
        return tbl

    def search(self, query):
        results = self.db.open_table("images").search(query, vector_column_name="vector_image").limit(5).to_pydantic(self.schema)
        return [i.image_uri for i in results]
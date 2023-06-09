import logging
import pandas as pd

import azure.functions as func
from io import BytesIO


def main(myblob: func.InputStream, outputblob:func.Out[str]):
    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {myblob.name}\n"
                 f"Blob Size: {myblob.length} bytes")

    extention = myblob.name.split('.')[1]
    logging.info(f"extention is {extention}")

    if extention == "txt":
        ## 行いたい処理
        # テキスト読み込み
        input_text = myblob.read(size=-1).decode("utf-8")
        # hoge追加
        output_text = input_text + "hoge"
        # ファイル保存
        outputblob.set(output_text)
    elif extention == "csv":
        df = pd.read_csv(BytesIO(myblob.read()))
        for idx in df.index:
            for col in df.columns:
                df.loc[idx,col] = str(df.loc[idx,col]) + 'hoge'
        logging.info(f"csv contents \n {df.to_string()}")
        outputblob.set(df.to_string())


    else:
        logging.warn("Not defined the process for {extention}")


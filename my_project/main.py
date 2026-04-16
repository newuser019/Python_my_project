# my_project/my_project/main.py
from fastapi import FastAPI
import pandas as pd

app = FastAPI(title="Poetry Project Demo", version="0.1.0")  # 补充项目信息，自动文档更友好

@app.get("/", summary="根路由测试")
def read_root():
    return {"Hello": "Poetry Project"}

@app.get("/pandas-test", summary="Pandas 数据测试")  # 新增接口，直接在API里测试Pandas
def pandas_test():
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    return df.to_dict(orient="records")  # 把DataFrame转成JSON返回，直接在接口测试

def main():
    # 本地运行脚本时的测试逻辑
    print("Pandas DataFrame 测试：")
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    print(df)

if __name__ == "__main__":
    import uvicorn
    main()  # 先执行Pandas测试
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)  # 直接运行服务，不用手动输命令
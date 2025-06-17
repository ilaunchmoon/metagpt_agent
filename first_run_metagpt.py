import asyncio
from metagpt.software_company import generate_repo
from metagpt.utils.project_repo import ProjectRepo

def main():
    # 使用新的简化 API
    repo: ProjectRepo = generate_repo("开发一个刷题程序")
    print(repo)  # 打印项目结构和文件
    print("项目已生成在 ./workspace 目录中")

if __name__ == "__main__":
    main()

    # python 3.10.18
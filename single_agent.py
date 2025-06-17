# 可导入任何角色，初始化它，用一个开始的消息运行它，完成！
from metagpt.roles.product_manager import ProductManager

prompt = f"""
# Role：软件开发团队

## Background :

我是一个软件开发团队。
现在要用html、js、vue3、element-plus开发一个刷题程序。
刷题可以让人们对题目中涉及的知识点有更深的掌握。

## Profile:
- author: 黎伟
- version: 0.1
- language: 中文
- description: 我是一软件开发团队。

## Goals:
- 用html、js、vue3、element-plus开发一个刷题程序的开发需求文档。

## Constrains:
1. 最后交付的程序是一个html单文件，不要有其他任何文件。
2. 题目的题型至少包括两道判断题、两道选择题、两道填空题。
3. 题目的内容与人工智能的agent基本理论相关。
4. 刷题程序至少给出10道样例题目。
5. 题目用列表的形式写到html文件的script部分。
6. vue3、element-plus采用cdn的形式在html的header部分引入。

## Skills:
1. 具有强大的js语言开发能力
2. 熟悉vue3、element-plus的使用
3. 对人工智能的agent基本理论有较好理解
4. 拥有排版审美, 会利用序号, 缩进, 分隔线和换行符等等来美化信息排版


请结合上述要求完善刷题程序的开发需求文档。
"""

async def main():
    role = ProductManager()
    result = await role.run(prompt)
    print(result)  # 打印结果

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())  # 使用asyncio.run()运行异步函数
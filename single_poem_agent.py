from metagpt.actions import Action

class TangPoem(Action):
    PROMPT_TEMPLATE: str = """
    根据主题{msg}写一首五言绝句的唐诗。只返回生成诗的内容，不要有其他文字。
    """
    async def run(self, msg: str):
        prompt = self.PROMPT_TEMPLATE.format(msg = msg)
        rsp = await self._aask(prompt)
        return rsp

async def main():
    tangshi = TangPoem()
    rst = await tangshi.run('写一首表达上班很辛苦的唐诗')
    print(rst)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())  # 使用asyncio.run()运行异步函数
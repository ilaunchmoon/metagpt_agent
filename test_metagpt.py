from metagpt.config2 import Config 
def print_llm_config():
    # 加载默认配置
    config = Config.default()

    # 获取LLM配置
    llm_config = config.llm
    # 打印LLM配置的详细信息
    if llm_config:
        print(f"API类型: {llm_config.api_type}")
        print(f"API密钥: {llm_config.api_key}")
        print(f"模型: {llm_config.model}")
    else:
        print("没有配置LLM")

if __name__ == "__main__":
    print_llm_config()
# 1. 本项目要求使用Linux配置、安装、运行
# 2. 安装如下步骤操作

    第 0: 使用git clone 下载 MetaGPT的源码到本地:
        git clone https://github.com/geekan/MetaGPT
    
    第一: 将当前文件夹下所有非MetaGPT项目下的文件都移动到 MetaGPT文件夹根目录下

    第二：创建一个虚拟环境, 要求 python3.10.18, 并激活该虚拟环境

    第三: 目录切换到MetaGPT下, 执行如下命令安装依赖包
            pip install -e . 
    
    第四: 执行如下命令安装上面几个python文件需要的依赖
            pip install -r run_requirements.txt
    

# 3. 执行几个python文件前

    先在目录 ./MetaGPT/config 找到 config2.yaml文件, 配置如下信息

        llm:
            api_type: 'zhipuai'
            api_key: '你的模型API-KEY'
            model: 'glm-4'


# 4. 注意:

    关于subscribe_agent包中, 只需运行subscribe_agent.py即可, 其他都是网络数据下载和分享
    如果没有下载网页数据则执行如下命令下载即可:
        wget https://github.com/trending -O github-trending-raw.html

    
    关于werewolves_millers_hollow_agent.py模块因为包依赖冲突的问题目前无法执行

# 5. 项目原始地址
    
     https://github.com/datawhalechina/wow-agent/blob/main/notebooks/
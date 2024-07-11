# liftrolu

![](./asset/camp.png)


一个用于生活的常识问答模型

#wordcount.py
用于分割实现统计英文字符串中每个单词出现的次数，返回一个字典

模型设置
在使用提示词的时候，您会通过 API 或者网页版与大语言模型进行交互，将这些参数、设置调整到最佳程度会提高使用大语言模型时候的体验感和效果，下面就是一些常见的设置：
1. Temperature
temperature 参数值越小，模型就会返回越确定的一个结果。较高的 temperature 值会增加随机性，使得模型更可能选择不那么常见的选项，从而产生更多样化和创造性的输出。在实际应用时，如果是 QA，可以用比较小的 temperature，如果是文学作品、诗歌写作，可以用比较大的temperature。
2. Top_p
这是一种称为nucleus sampling的文本生成策略，它限制了模型在生成下一个词时考虑的候选词的数量。具体来说，Top_p参数决定了在生成时考虑的候选词的累积概率上限。例如，如果设置Top_p为0.9，那么只有累积概率最高的前10%的词会被考虑用于生成。
3. Max Length
这个参数指定了生成文本的最大长度，即模型在停止生成新词之前可以生成的最多字符数或词数。
4. Frequency Penalty
这个参数用于控制常见词和不常见词在生成过程中的相对概率。增加频率惩罚会降低常见词被选中的概率，从而鼓励模型生成更多样化的文本。
5. Presence Penalty
这个参数影响已经生成的词再次出现的概率。增加存在惩罚会减少这些词再次被选中的机会，有助于生成更多样化的文本，避免重复。

Q：如何添加新的conda环境
A：
第一步，将新的conda环境创建到/share/conda_envs下
>> conda create -p /share/conda_envs/xxx python=3.1x

conda activate

第二步，将本机/root/.conda/pkgs下的文件拷贝到/share/pkgs中，重新压缩并替换(此步骤是为了把conda创建过程中大的公共包存储起来，避免重复下载)
>> cp -r -n /root/.conda/pkgs/* /share/pkgs/
>> cd /share && tar -zcvf pkgs.tar.gz pkgs

第三步，更新install_conda_env.sh中的list函数，增加新的conda环境说明



我们可以使用conda create -n name python=3.10创建虚拟环境，这里表示创建了python版本为3.10、名字为name的虚拟环境。创建后，可以在.conda目录下的envs目录下找到。
[图片]
在不指定python版本时，会自动创建基于最新python版本的虚拟环境。同时我们可以在创建虚拟环境的同时安装必要的包：conda create -n name numpy matplotlib python=3.10（但是不建议大家这样用）
创建虚拟环境的常用参数如下：
- -n 或 --name：指定要创建的环境名称。
- -c 或 --channel：指定额外的软件包通道。
- --clone：从现有的环境克隆来创建新环境。
- -p 或 --prefix：指定环境的安装路径（非默认位置）。


conda activate
conda deactivate


#获得环境中的所有配置
conda env export --name myenv > myenv.yml
#重新还原环境
conda env create -f  myenv.yml


使用studio-conda 来复制一个环境
  说明: 用于快速clone预设的conda环境

  使用: 
  
    1. studio-conda env -l/list 打印预设的conda环境列表
  
    2. studio-conda <target-conda-name> 快速clone: 默认拷贝internlm-base conda环境
    
    3. studio-conda -t <target-conda-name> -o <origin-conda-name> 将预设的conda环境拷贝到指定的conda环境

---------------------------------- 欢迎使用 InternStudio 开发机 ------------------------------

+--------+------------+----------------------------------------------------------------------+
|  目录  |    名称    |                              简介                                    |
+--------+------------+----------------------------------------------------------------------+
|   /    |  系统目录  | 每次停止开发机会将其恢复至系统（镜像）初始状态。不建议存储数据。     |
+--------+------------+----------------------------------------------------------------------+
| /root  | 用户家目录 | 您的所有开发机共享此目录，不受开发机的启停影响。强烈建议将 conda     |
|        |            | 环境、代码仓库等所有数据存储在此目录下。                             |
|        |            | 【注意】该目录有存储限额，超过限额后新写入的数据会被静默删除！       |
+--------+------------+----------------------------------------------------------------------+
| /share |  共享目录  | 常用微调数据集、模型仓库、教程、xtuner 配置文件都存放在此。
    Tips:

1. 快速从本地上传文件:
   scp -o StrictHostKeyChecking=no -r -P {端口} {本地目录} root@ssh.intern-ai.org.cn:{开发机目录}
   *注：在开发机 SSH 连接功能查看端口号 

2. 避免因终端关闭或 SSH 连接断开导致任务终止, 强烈建议使用 tmux 将实验进程与终端窗口分离：
   https://www.ruanyifeng.com/blog/2019/10/tmux.html

3. 查看 GPU 显存和算力使用率: studio-smi 

4. 使用InternStudio开箱即用的conda环境:
   studio-conda -h

5. 将conda环境一键添加到jupyterlab:
   lab add {YOUR_CONDA_ENV_NAME}

#CorruptedEnvironmentError: The target environment has been corrupted. Corrupted environments most commonly
occur when the conda process is force-terminated while in an unlink-link
transaction.
删除错误的文件就行，再执行就没有问题了
apt-get install tmux
# 使用会话编号
$ tmux attach -t 0
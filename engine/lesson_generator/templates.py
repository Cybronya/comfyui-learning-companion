NODE_LESSON_TEMPLATES = {


"KSampler":

{

"title":
"理解 KSampler：扩散采样核心",


"content":

"""
KSampler 是 Stable Diffusion
生成图片的核心节点。

它负责将随机噪声逐步转换为
符合 Prompt 的图片。

重点理解：

- steps
- cfg
- sampler

""",


"exercise":[

"修改 steps 从20调整到40",

"比较不同 sampler 的效果"

]

},



"CheckpointLoaderSimple":

{

"title":
"理解 Checkpoint：模型来源",


"content":

"""
Checkpoint 是 Stable Diffusion
已经训练好的模型。

它决定：

- 图片风格
- 人物特征
- 生成能力

""",


"exercise":[

"替换不同 Checkpoint",

"比较生成结果"

]

}

}

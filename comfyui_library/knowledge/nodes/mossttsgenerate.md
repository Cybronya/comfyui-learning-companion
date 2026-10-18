# MossTTSGenerate

## 节点类型

`MossTTSGenerate`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `moss_pipe:MOSS_TTS_PIPE`（1 次）
- `reference_audio:AUDIO`（1 次）
- `language:COMBO`（1 次）
- `text:STRING`（1 次）
- `seed:INT`（1 次）
- `temperature:FLOAT`（1 次）
- `top_p:FLOAT`（1 次）
- `top_k:INT`（1 次）
- `repetition_penalty:FLOAT`（1 次）
- `max_new_tokens:INT`（1 次）

## 输出

- `audio:AUDIO`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["auto", "有些人喜欢被照顾，\n而我更习惯照亮自己。\n\n不是不需要依靠，\n只是明白——\n真正能陪你走到最后的，\n从来都不是运气。\n\n我见过凌晨四点的城市，\n也见过掌声散去后的安静。\n那些看起来毫不费力的从容，\n`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)

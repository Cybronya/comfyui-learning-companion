# MossTTSVoiceDesign

## 节点类型

`MossTTSVoiceDesign`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `moss_pipe:MOSS_TTS_PIPE`（1 次）
- `language:COMBO`（1 次）
- `text:STRING`（1 次）
- `instruction:STRING`（1 次）
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

- `["auto", "天哪天哪天哪！我中了！我真的中了！一等奖！妈你快来看！", "年轻女性，狂喜尖叫，激动到语无伦次", 1067288335978672, "randomize", 1.5, 0.6, 50, 1.1, 4096, 0, `（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)

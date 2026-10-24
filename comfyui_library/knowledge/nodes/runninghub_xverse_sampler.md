# RunningHub XVerse Sampler

## 节点类型

`RunningHub XVerse Sampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 9 个 workflow 中。

## 输入

- `pipeline:XVersePipeline`（9 次）
- `img:IMAGE`（9 次）
- `img2:IMAGE`（9 次）
- `img3:IMAGE`（9 次）
- `prompt:STRING`（9 次）
- `caption:STRING`（5 次）
- `caption2:STRING`（5 次）

## 输出

- `IMAGE:IMAGE`（9 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["a woman", true, "ENT1 is holding ENT2 standing in a room", 28, 768, 768, 256, 4, 4, 0.9, 1.3, 975072288172137, "random`（1 次）
- `["a man", true, "ENT1 and ENT2 standing together in a park.", 28, 1024, 768, 256, 4, 4, 0.9, 1.3, 83709970200684, "rando`（1 次）
- `["a woman", true, "ENT1 is holding ENT2 standing in a room", 28, 768, 768, 256, 4, 4, 0.9, 1.3, 363375626692591, "random`（1 次）
- `["a man", true, "ENT1 and ENT2 standing together in a park.", 28, 1024, 768, 256, 4, 4, 0.9, 1.3, 463640452641427, "rand`（1 次）
- `["a women", true, "", 28, 768, 768, 256, 4, 5, 1, 1.3, 414055445349157, "randomize", "a man", true, "a women", true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)

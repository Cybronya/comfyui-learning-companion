# IndexTTSProNode

## 节点类型

`IndexTTSProNode`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `narrator_audio:AUDIO`（1 次）
- `character1_audio:AUDIO`（1 次）
- `character2_audio:AUDIO`（1 次）
- `character3_audio:AUDIO`（1 次）
- `character4_audio:AUDIO`（1 次）
- `character5_audio:AUDIO`（1 次）
- `structured_text:STRING`（1 次）
- `model_version:COMBO`（1 次）
- `language:COMBO`（1 次）
- `speed:FLOAT`（1 次）

## 输出

- `audio:AUDIO`（1 次）
- `seed:INT`（1 次）
- `Subtitle:STRING`（1 次）
- `SimplifiedSubtitle:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["<正文>这是一段正文示例。<角色1>你好。<正文>他说道。", "IndexTTS-1.5", "zh", 0.8, 399, "fixed", 1, 0.8, 30, 10, 0, 3, 600]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)

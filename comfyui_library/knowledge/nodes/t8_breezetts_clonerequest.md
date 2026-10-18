# T8_BreezeTTS_CloneRequest

## 节点类型

`T8_BreezeTTS_CloneRequest`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 6 个 workflow 中。

## 输入

- `reference_audio:AUDIO`（5 次）
- `text:STRING`（5 次）
- `reference_text:STRING`（5 次）
- `instruction:STRING`（5 次）
- `cfg_scale:FLOAT`（5 次）
- `text:WILDCARD`（1 次）
- `reference_audio:WILDCARD`（1 次）
- `reference_text:WILDCARD`（1 次）
- `instruction:WILDCARD`（1 次）

## 输出

- `request:BREEZE_T8_REQUEST`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["很高兴再次听到你的声音。", "请替换为参考音频的准确逐字稿。", "Speak clearly and naturally.", 1]`（2 次）
- `["", "请替换为参考音频的准确逐字稿。", "Speak clearly and naturally.", 1]`（2 次）
- `["青海、甘肃、内蒙古、华北及东北等地有小到中雨，局地大雨或暴雨。", "请替换为参考音频的准确逐字稿。", "Speak clearly and naturally.", 1]`（1 次）
- `[1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)

# T8_BreezeTTS_DirectionRequest

## 节点类型

`T8_BreezeTTS_DirectionRequest`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `reference_audio:AUDIO`（2 次）
- `text:STRING`（2 次）
- `reference_text:STRING`（2 次）
- `direction:STRING`（2 次）
- `cfg_scale:FLOAT`（2 次）

## 输出

- `request:BREEZE_T8_REQUEST`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["我们需要认真讨论一下昨晚发生的事情。", "请替换为参考音频的准确逐字稿。", "语速放慢，语气克制而严肃。", 4]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)

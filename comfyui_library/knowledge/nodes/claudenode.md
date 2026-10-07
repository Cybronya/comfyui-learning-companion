# ClaudeNode

## 节点类型

`ClaudeNode`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 6 个 workflow 中。

## 输入

- `images.image_1:IMAGE`（6 次）
- `images.image_2:IMAGE`（6 次）
- `prompt:STRING`（5 次）
- `images.image_3:IMAGE`（1 次）

## 输出

- `STRING:STRING`（6 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Describe this image", "Opus 4.7", 32768, 1, "off", 0, "randomize", ""]`（1 次）
- `["", "Fable 5", 32768, "high", 1299859456, "randomize", ""]`（1 次）
- `["", "Fable 5.1", 32768, "high", 1299859456, "randomize", ""]`（1 次）
- `["", "Opus 5", 32768, "high", 1299859456, "randomize", ""]`（1 次）
- `["", "Opus 5.5", 32768, "high", 534380505, "randomize", ""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)

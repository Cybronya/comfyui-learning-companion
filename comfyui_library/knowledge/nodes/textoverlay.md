# TextOverlay

## 节点类型

`TextOverlay`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `images:IMAGE`（12 次）
- `text:STRING`（12 次）
- `font_size:FLOAT`（12 次）
- `color:COLOR`（12 次）
- `position:COMBO`（12 次）
- `align:COMBO`（12 次）
- `outline:BOOLEAN`（12 次）

## 输出

- `images:IMAGE`（12 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["lightx2v_turbo_8step_v1.0  + Realism-People-LoRA（8step≈40s）", 5, "#cc9600", "top", "left", true]`（2 次）
- `["lightx2v_turbo_8step_v1.0（8step≈40s）", 5, "#cc9600", "top", "left", true]`（2 次）
- `["Original + Realism-People-LoRA（25step≈120s）", 5, "#000000", "top", "left", true]`（2 次）
- `["Original（25step≈135s）", 5, "#000000", "top", "left", true]`（2 次）
- `["lightx2v_turbo_4step_v1.0（4step≈20s）", 5, "#00d100", "top", "left", true]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)

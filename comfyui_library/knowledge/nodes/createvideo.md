# CreateVideo

## 节点类型

`CreateVideo`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 20 个 workflow 中。

## 输入

- `images:IMAGE`（27 次）
- `audio:AUDIO`（27 次）
- `fps:FLOAT`（27 次）
- `bit_depth:COMBO`（27 次）
- `color_space:COMBO`（27 次）
- `codec:COMBO`（27 次）

## 输出

- `VIDEO:VIDEO`（27 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[24, 8, "sRGB", "none"]`（15 次）
- `[24, "auto", "sRGB", "none"]`（6 次）
- `[12.42864990234375, 8, "sRGB", "none"]`（5 次）
- `[24, 8, "sRGB", "h264"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)

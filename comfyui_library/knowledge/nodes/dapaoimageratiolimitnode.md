# DapaoImageRatioLimitNode

## 节点类型

`DapaoImageRatioLimitNode`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `🔢 百万像素:COMBO`（1 次）
- `📐 宽高比:COMBO`（1 次）
- `🔢 整除倍数:COMBO`（1 次）
- `🔘 启用自定义比例:BOOLEAN`（1 次）
- `✏️ 自定义宽高比:STRING`（1 次）

## 输出

- `↔️ 宽度:INT`（1 次）
- `↕️ 高度:INT`（1 次）
- `📝 分辨率信息:STRING`（1 次）
- `🖼️ 预览图:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["2.0", "9:16 (手机竖屏)", "64", false, "1:1"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)

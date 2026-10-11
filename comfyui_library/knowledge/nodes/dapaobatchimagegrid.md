# DapaoBatchImageGrid

## 节点类型

`DapaoBatchImageGrid`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `🖼️ 图像批次:IMAGE`（1 次）
- `📊 列数:INT`（1 次）
- `🧱 行数:INT`（1 次）
- `↔️ 单图宽度:INT`（1 次）
- `↕️ 单图高度:INT`（1 次）
- `📏 间距:INT`（1 次）
- `✂️ 裁剪模式:COMBO`（1 次）
- `🎨 背景类型:COMBO`（1 次）
- `🎨 背景颜色:STRING`（1 次）
- `📏 限制最长边:INT`（1 次）

## 输出

- `🖼️ 拼接图像:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1, 0, 0, 0, 0, "原比例", "透明", "#FFFFFF", 0]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)

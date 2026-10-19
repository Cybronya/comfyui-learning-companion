# SingleImageLayoutNode

## 节点类型

`SingleImageLayoutNode`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `相纸宽:FLOAT`（1 次）
- `相纸高:FLOAT`（1 次）
- `分辨率:INT`（1 次）
- `文件名:STRING`（1 次）
- `照片间距:FLOAT`（1 次）
- `字体:COMBO`（1 次）
- `字体大小:INT`（1 次）
- `描边:INT`（1 次）
- `安全边距:FLOAT`（1 次）

## 输出

- `排版图像:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[12.7, 8.9, 350, "孤海排版", 0.2, "华文细黑.ttf", 0, 1, 0.2, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)

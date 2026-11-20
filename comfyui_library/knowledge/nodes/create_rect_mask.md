# Create Rect Mask

## 节点类型

`Create Rect Mask`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `copy_image_size:IMAGE`（4 次）

## 输出

- `IMAGE:IMAGE`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["percent", "bottomleft", 50, 0, 50, 100, 512, 512]`（2 次）
- `["percent", "bottomleft", 0, 0, 100, 50, 512, 512]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)

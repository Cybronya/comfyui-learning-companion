# AdvancedImageSelector

## 节点类型

`AdvancedImageSelector`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `image1:IMAGE`（5 次）
- `image2:IMAGE`（5 次）
- `image3:IMAGE`（5 次）
- `image4:IMAGE`（5 次）
- `image5:IMAGE`（5 次）
- `image6:IMAGE`（5 次）
- `image7:IMAGE`（5 次）
- `image8:IMAGE`（5 次）
- `image9:IMAGE`（5 次）
- `image10:IMAGE`（5 次）

## 输出

- `image:IMAGE`（5 次）
- `selected_index:INT`（5 次）
- `info:STRING`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["索引选择", 0, "fixed", 0]`（1 次）
- `["索引选择", 325540685159733, "randomize", 2]`（1 次）
- `["索引选择", 842285744347503, "randomize", 1]`（1 次）
- `["索引选择", 581077736514326, "randomize", 0]`（1 次）
- `["索引选择", 192127694484041, "randomize", 5]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)

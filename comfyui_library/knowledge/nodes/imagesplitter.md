# ImageSplitter

## 节点类型

`ImageSplitter`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `split_mode:COMBO`（1 次）
- `split_direction:COMBO`（1 次）
- `name_prefix:STRING`（1 次）
- `save_to_folder:BOOLEAN`（1 次）
- `output_folder:STRING`（1 次）
- `pos_1_name:STRING`（1 次）
- `pos_2_name:STRING`（1 次）
- `pos_3_name:STRING`（1 次）
- `pos_4_name:STRING`（1 次）

## 输出

- `images:IMAGE`（1 次）
- `split_info:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["three_equal_parts", "vertical", "bob", false, "output/split_images", "headf", "headb", "heads", "head34l", "front", "h`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)

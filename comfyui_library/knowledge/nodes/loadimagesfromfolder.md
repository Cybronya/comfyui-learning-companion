# LoadImagesFromFolder

## 节点类型

`LoadImagesFromFolder`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `path_type:COMBO`（1 次）
- `mode:COMBO`（1 次）
- `seed:INT`（1 次）
- `image_index:INT`（1 次）
- `folder_name:COMBO`（1 次）
- `custom_path:STRING`（1 次）
- `label:STRING`（1 次）
- `output_filename:COMBO`（1 次）
- `allow_RGBA:COMBO`（1 次）
- `image_pattern:STRING`（1 次）

## 输出

- `image:IMAGE`（1 次）
- `filename:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["input_dir", "single", 484752972793521, "randomize", 0, "<root>", "C:/Users/Pictures", "batch 001", "true", "false", "*`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)

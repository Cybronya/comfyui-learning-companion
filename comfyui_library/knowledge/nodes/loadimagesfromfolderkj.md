# LoadImagesFromFolderKJ

## 节点类型

`LoadImagesFromFolderKJ`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 7 个 workflow 中。

## 输入

- `folder:STRING`（7 次）
- `width:INT`（7 次）
- `height:INT`（7 次）
- `keep_aspect_ratio:COMBO`（7 次）
- `image_load_cap:INT`（7 次）
- `start_index:INT`（7 次）
- `include_subfolders:BOOLEAN`（7 次）

## 输出

- `image:IMAGE`（7 次）
- `mask:MASK`（7 次）
- `count:INT`（7 次）
- `image_path:STRING`（7 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["output/picture/zx", 960, 544, "crop", 0, 0, false]`（4 次）
- `["output/picture/zx", 707, 544, "crop", 0, 0, false]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)

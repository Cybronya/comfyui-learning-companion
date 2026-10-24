# SGUNLoadImageBatch

## 节点类型

`SGUNLoadImageBatch`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `batch_path:STRING`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）
- `resize_short_side:INT`（1 次）
- `upscale_method:COMBO`（1 次）
- `keep_proportion:COMBO`（1 次）
- `crop_position:COMBO`（1 次）
- `divisible_by:INT`（1 次）

## 输出

- `IMAGE:IMAGE`（1 次）
- `MASK:MASK`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["f3c25b33ea405ee1e208add546d21eaa1b4351154ac8a9ed21e7c24a306da669.zip", 1280, 1280, 0, "lanczos", "crop", "center", 3, `（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)

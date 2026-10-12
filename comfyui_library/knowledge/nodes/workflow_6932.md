# workflow>勿动

## 节点类型

`workflow>勿动`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `get_image_size:IMAGE`（1 次）
- `start:INT`（1 次）
- `length:INT`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）
- `upscale_method:COMBO`（1 次）
- `keep_proportion:BOOLEAN`（1 次）
- `divisible_by:INT`（1 次）
- `crop:COMBO`（1 次）

## 输出

- `IMAGE:IMAGE`（1 次）
- `ImageResizeKJ IMAGE:IMAGE`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, 20, 512, 768, "lanczos", false, 8, "center"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)

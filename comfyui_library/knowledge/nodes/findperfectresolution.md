# FindPerfectResolution

## 节点类型

`FindPerfectResolution`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `image:IMAGE`（2 次）
- `desired_width:INT`（2 次）
- `desired_height:INT`（2 次）
- `divisible_by:INT`（2 次）
- `upscale:BOOLEAN`（2 次）
- `upscale_method:COMBO`（2 次）
- `small_image_mode:COMBO`（2 次）
- `pad_color:STRING`（2 次）
- `mask:MASK`（1 次）

## 输出

- `resolution_info:STRING`（3 次）
- `width:INT`（2 次）
- `height:INT`（2 次）
- `IMAGE:IMAGE`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[512, 512, 16, false, "lanczos", "none", "#000000"]`（1 次）
- `[512, 512, 16, false, "lanczos", "none", "#000000", "<tr><td>Output: </td><td><b>1280</b> x <b>720</b> | 10.55MB | 921,6`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)

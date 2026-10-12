# workflow>面部与姿势检测

## 节点类型

`workflow>面部与姿势检测`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 6 个 workflow 中。

## 输入

- `image:IMAGE`（16 次）
- `ImageResizeKJv2 image:IMAGE`（16 次）
- `layer_mask:MASK`（16 次）
- `model:POSEMODEL`（16 次）
- `retarget_image:IMAGE`（16 次）
- `width:INT`（16 次）
- `height:INT`（16 次）
- `upscale_method:COMBO`（16 次）
- `keep_proportion:COMBO`（16 次）
- `pad_color:STRING`（16 次）

## 输出

- `IMAGE:IMAGE`（16 次）
- `face_images:IMAGE`（16 次）
- `pose_images:IMAGE`（16 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[512, 512, "nearest-exact", "stretch", "0, 0, 0", "center", 8, "cpu", 1, 0, 512, 512, "lanczos", "pad_edge_pixel", "0, 0`（16 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)

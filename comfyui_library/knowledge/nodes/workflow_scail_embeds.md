# workflow>Scail embeds

## 节点类型

`workflow>Scail embeds`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `vae:WANVAE`（1 次）
- `参考图像:IMAGE`（1 次）
- `clip_vision:CLIP_VISION`（1 次）
- `姿势视频:IMAGE`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）
- `num_frames:INT`（1 次）
- `ratio:FLOAT`（1 次）
- `strength_1:FLOAT`（1 次）
- `strength_2:FLOAT`（1 次）

## 输出

- `image_embeds:WANVIDIMAGE_EMBEDS`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[832, 480, 81, 0.5, 1, 1, "center", "average", true, 0, 1, 0, 1, 1, 0, 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)

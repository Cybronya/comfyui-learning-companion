# H3PerFrameDenoise

## 节点类型

`H3PerFrameDenoise`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `model:MODEL`（3 次）
- `av_latent:LATENT`（3 次）
- `transform:H3FACEXFORM`（3 次）
- `denoise_multiplier_small_face:FLOAT`（3 次）
- `denoise_multiplier_large_face:FLOAT`（3 次）
- `scale_mode:COMBO`（3 次）
- `face_px_small:FLOAT`（3 次）
- `face_px_large:FLOAT`（3 次）
- `gamma:FLOAT`（3 次）
- `smooth_frames:INT`（3 次）

## 输出

- `av_latent:LATENT`（3 次）
- `report:STRING`（3 次）
- `model:MODEL`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1, 0.35, "absolute_px", 30, 120, 1, 9]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)

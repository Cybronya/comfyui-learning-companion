# LTXIdentityTransfer

## 节点类型

`LTXIdentityTransfer`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（2 次）
- `positive:CONDITIONING`（2 次）
- `negative:CONDITIONING`（2 次）
- `vae:VAE`（2 次）
- `latent:LATENT`（2 次）
- `reference_image:IMAGE`（2 次）
- `source_id:FLOAT`（2 次）
- `phase_scale:FLOAT`（2 次）
- `ref_resize_mode:COMBO`（2 次）
- `debug_log:BOOLEAN`（2 次）

## 输出

- `model:MODEL`（2 次）
- `positive:CONDITIONING`（2 次）
- `negative:CONDITIONING`（2 次）
- `latent:LATENT`（2 次）
- `debug:STRING`（2 次）
- `ref_preview:IMAGE`（2 次）
- `crop_overlay:IMAGE`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[2, 1, "native_resolution", false, "center", "overlap", 1]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)

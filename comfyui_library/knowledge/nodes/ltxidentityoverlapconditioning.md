# LTXIdentityOverlapConditioning

## 节点类型

`LTXIdentityOverlapConditioning`

## 分类

Conditioning

## 作用

条件处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 6 个 workflow 中。

## 输入

- `model:MODEL`（9 次）
- `positive:CONDITIONING`（9 次）
- `negative:CONDITIONING`（9 次）
- `vae:VAE`（9 次）
- `latent:LATENT`（9 次）
- `source_id:FLOAT`（9 次）
- `phase_scale:FLOAT`（9 次）
- `debug_log:BOOLEAN`（9 次）
- `reference_image:IMAGE`（5 次）
- `ref_resize_mode:COMBO`（5 次）

## 输出

- `model:MODEL`（9 次）
- `positive:CONDITIONING`（9 次）
- `negative:CONDITIONING`（9 次）
- `latent:LATENT`（9 次）
- `debug:STRING`（9 次）
- `ref_preview:IMAGE`（5 次）
- `crop_overlay:IMAGE`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["None", 2, 1, 1, "auto_adjust", false]`（3 次）
- `[2, 1, "match_target", false, "center", "overlap", 1]`（3 次）
- `["None", 2, 1, 1, "disable", false]`（1 次）
- `[2, 1, "native_resolution", false, "center", "overlap", 1]`（1 次）
- `[2, 1, "native_resolution", false, "center", "overlap", 1.1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)

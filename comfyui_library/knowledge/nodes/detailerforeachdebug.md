# DetailerForEachDebug

## 节点类型

`DetailerForEachDebug`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `segs:SEGS`（1 次）
- `model:MODEL`（1 次）
- `clip:CLIP`（1 次）
- `vae:VAE`（1 次）
- `positive:CONDITIONING`（1 次）
- `negative:CONDITIONING`（1 次）
- `detailer_hook:DETAILER_HOOK`（1 次）
- `scheduler_func_opt:SCHEDULER_FUNC`（1 次）
- `guide_size:FLOAT`（1 次）

## 输出

- `image:IMAGE`（1 次）
- `cropped:IMAGE`（1 次）
- `cropped_refined:IMAGE`（1 次）
- `cropped_refined_alpha:IMAGE`（1 次）
- `cnet_images:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1024, true, 2048, 180238172262324, "fixed", 20, 1, "euler", "kl_optimal", 0.4000000000000001, 5, true, true, "", 1, fal`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)

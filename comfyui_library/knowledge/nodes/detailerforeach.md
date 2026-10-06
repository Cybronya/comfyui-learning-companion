# DetailerForEach

## 节点类型

`DetailerForEach`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `image:IMAGE`（3 次）
- `segs:SEGS`（3 次）
- `model:MODEL`（3 次）
- `clip:CLIP`（3 次）
- `vae:VAE`（3 次）
- `positive:CONDITIONING`（3 次）
- `negative:CONDITIONING`（3 次）
- `detailer_hook:DETAILER_HOOK`（3 次）
- `scheduler_func_opt:SCHEDULER_FUNC`（3 次）
- `guide_size:FLOAT`（1 次）

## 输出

- `IMAGE:IMAGE`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[512, true, 1024, 61107425659942, "randomize", 18, 6, "er_sde", "simple", 0.24, 5, true, true, "", 1, false, 32, false, `（1 次）
- `[512, true, 1024, 586689866809080, "randomize", 20, 1, "euler", "sgm_uniform", 0.8, 5, true, true, "", 1, false, 20]`（1 次）
- `[512, true, 768, 693981433796475, "randomize", 20, 5, "dpmpp_3m_sde_gpu", "karras", 0.24999999999999978, 5, true, true, `（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)

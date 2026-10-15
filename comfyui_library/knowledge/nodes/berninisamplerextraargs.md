# BerniniSamplerExtraArgs

## 节点类型

`BerniniSamplerExtraArgs`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 6 个 workflow 中。

## 输入

- `feta_args:FETAARGS`（6 次）
- `context_options:WANVIDCONTEXT`（6 次）
- `cache_args:CACHEARGS`（6 次）
- `slg_args:SLGARGS`（6 次）
- `loop_args:LOOPARGS`（6 次）
- `experimental_args:EXPERIMENTALARGS`（6 次）
- `unianimate_poses:UNIANIMATE_POSE`（6 次）
- `fantasytalking_embeds:FANTASYTALKING_EMBEDS`（6 次）
- `uni3c_embeds:UNI3C_EMBEDS`（6 次）
- `multitalk_embeds:MULTITALK_EMBEDS`（6 次）

## 输出

- `extra_args:WANVIDSAMPLEREXTRAARGS`（6 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, "comfy", "apg", 0.5, -0.5, 50]`（6 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)

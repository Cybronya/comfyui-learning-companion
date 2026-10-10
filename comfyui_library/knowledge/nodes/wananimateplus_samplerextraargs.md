# WanAnimatePlus SamplerExtraArgs

## 节点类型

`WanAnimatePlus SamplerExtraArgs`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `feta_args:FETAARGS`（2 次）
- `context_options:WANVIDCONTEXT`（2 次）
- `cache_args:CACHEARGS`（2 次）
- `slg_args:SLGARGS`（2 次）
- `loop_args:LOOPARGS`（2 次）
- `experimental_args:EXPERIMENTALARGS`（2 次）
- `unianimate_poses:UNIANIMATE_POSE`（2 次）
- `fantasytalking_embeds:FANTASYTALKING_EMBEDS`（2 次）
- `uni3c_embeds:UNI3C_EMBEDS`（2 次）
- `multitalk_embeds:MULTITALK_EMBEDS`（2 次）

## 输出

- `extra_args:WANVIDSAMPLEREXTRAARGS`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, "comfy"]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)

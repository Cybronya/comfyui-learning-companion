# TimestepKeyframe

## 节点类型

`TimestepKeyframe`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `control_net_weights:CONTROL_NET_WEIGHTS`（2 次）
- `t2i_adapter_weights:T2I_ADAPTER_WEIGHTS`（2 次）
- `latent_keyframe:LATENT_KEYFRAME`（2 次）
- `prev_timestep_keyframe:TIMESTEP_KEYFRAME`（2 次）

## 输出

- `TIMESTEP_KEYFRAME:TIMESTEP_KEYFRAME`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, 1, 0, true, true, ""]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)

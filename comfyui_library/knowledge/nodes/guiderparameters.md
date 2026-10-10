# GuiderParameters

## 节点类型

`GuiderParameters`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `parameters:GUIDER_PARAMETERS`（2 次）
- `modality:COMBO`（2 次）
- `cfg:FLOAT`（2 次）
- `stg:FLOAT`（2 次）
- `perturb_attn:BOOLEAN`（2 次）
- `rescale:FLOAT`（2 次）
- `modality_scale:FLOAT`（2 次）
- `skip_step:INT`（2 次）
- `cross_attn:BOOLEAN`（2 次）

## 输出

- `GUIDER_PARAMETERS:GUIDER_PARAMETERS`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["AUDIO", 1, 1, true, 0.7, 0, 0, true]`（1 次）
- `["VIDEO", 1, 1, true, 0.7, 0, 0, true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)

# ConditioningSetPropertiesAndCombine

## 节点类型

`ConditioningSetPropertiesAndCombine`

## 分类

Conditioning

## 作用

条件处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `cond:CONDITIONING`（1 次）
- `cond_NEW:CONDITIONING`（1 次）
- `mask:MASK`（1 次）
- `hooks:HOOKS`（1 次）
- `timesteps:TIMESTEPS_RANGE`（1 次）
- `strength:FLOAT`（1 次）
- `set_cond_area:COMBO`（1 次）

## 输出

- `CONDITIONING:CONDITIONING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1, "default"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)

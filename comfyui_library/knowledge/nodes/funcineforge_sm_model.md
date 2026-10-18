# FunCineForge_SM_Model

## 节点类型

`FunCineForge_SM_Model`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `flow:COMBO`（2 次）
- `llm:COMBO`（2 次）
- `voc:COMBO`（2 次）
- `dtype:COMBO`（2 次）

## 输出

- `model:MODEL`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["flow/mp_rank_00_model_states.pt", "llm/mp_rank_00_model_states.pt", "vocoder/avg_5_removewn.pt", "bf16"]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)

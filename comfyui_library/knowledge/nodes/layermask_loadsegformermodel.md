# LayerMask: LoadSegformerModel

## 节点类型

`LayerMask: LoadSegformerModel`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `model_name:COMBO`（2 次）
- `device:COMBO`（2 次）

## 输出

- `segfromer_model:LS_SEGFORMER_MODEL`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["segformer_b3_clothes", "cuda"]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)

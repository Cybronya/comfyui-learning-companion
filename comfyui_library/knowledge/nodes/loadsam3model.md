# LoadSAM3Model

## 节点类型

`LoadSAM3Model`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `model_name:COMBO`（3 次）
- `use_gpu_cache:BOOLEAN`（2 次）
- `hf_token:STRING`（2 次）

## 输出

- `sam3_model:SAM3_MODEL`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["sam3.pt", ""]`（2 次）
- `[true]`（1 次）
- `["cuda"]`（1 次）
- `["sam3.pt"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)

# BreezeTTS2LoadModel

## 节点类型

`BreezeTTS2LoadModel`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 14 个 workflow 中。

## 输入

- `model:COMBO`（20 次）
- `dtype:COMBO`（20 次）
- `device:COMBO`（20 次）
- `attention:COMBO`（20 次）
- `decode_mode:COMBO`（20 次）
- `download_if_missing:BOOLEAN`（20 次）

## 输出

- `breeze_model:BREEZE_TTS2_MODEL`（20 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["bf16 (best quality)", "auto", "auto", "auto", "cuda_graphs", false]`（16 次）
- `["int8 hybrid (recommended)", "auto", "auto", "auto", "eager", false]`（3 次）
- `["int8 hybrid (recommended)", "auto", "auto", "auto", "eager", true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)

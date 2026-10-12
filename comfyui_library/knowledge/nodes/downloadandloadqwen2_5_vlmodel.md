# DownloadAndLoadQwen2_5_VLModel

## 节点类型

`DownloadAndLoadQwen2_5_VLModel`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:COMBO`（1 次）
- `quantization:COMBO`（1 次）
- `attention:COMBO`（1 次）

## 输出

- `Qwen2_5_VL_model:QWEN2_5_VL_MODEL`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Qwen/Qwen2.5-VL-3B-Instruct", "8bit", "flash_attention_2"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)

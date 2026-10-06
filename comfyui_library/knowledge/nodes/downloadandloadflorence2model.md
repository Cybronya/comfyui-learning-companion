# DownloadAndLoadFlorence2Model

## 节点类型

`DownloadAndLoadFlorence2Model`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `lora:PEFTLORA`（3 次）

## 输出

- `florence2_model:FL2MODEL`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["microsoft/Florence-2-base", "bf16", "sdpa"]`（1 次）
- `["microsoft/Florence-2-large", "fp16", "sdpa"]`（1 次）
- `["gokaygokay/Florence-2-Flux-Large", "fp16", "sdpa"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)

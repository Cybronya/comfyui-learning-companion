# ZFPromptDirectorLocalLLM

## 节点类型

`ZFPromptDirectorLocalLLM`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `llama_model:LLAMACPPMODEL`（4 次）
- `parameters:LLAMACPPARAMS`（4 次）
- `image1:IMAGE`（4 次）
- `image2:IMAGE`（4 次）
- `image3:IMAGE`（4 次）
- `image4:IMAGE`（4 次）
- `image5:IMAGE`（4 次）
- `image6:IMAGE`（4 次）
- `image7:IMAGE`（4 次）
- `image8:IMAGE`（4 次）

## 输出

- `response:STRING`（4 次）
- `raw_response:STRING`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "", 0.15, 8192, 1, 0, 0, 512, 42, "fixed", false, false, 8]`（2 次）
- `["", "", 0.8, 4096, 0.9, 1, 0, 512, 42, "fixed", true, false, 8]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)

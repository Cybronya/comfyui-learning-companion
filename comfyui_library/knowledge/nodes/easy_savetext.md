# easy saveText

## 节点类型

`easy saveText`

## 分类

Output

## 作用

输出类节点：把结果写到磁盘（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 18 个 workflow 中。

## 输入

- `text:STRING`（22 次）
- `image:IMAGE`（22 次）
- `output_file_path:STRING`（22 次）
- `file_name:STRING`（22 次）
- `file_extension:COMBO`（22 次）
- `overwrite:BOOLEAN`（22 次）

## 输出

- `text:STRING`（22 次）
- `image:IMAGE`（22 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "", "txt", true]`（17 次）
- `["output/软件/文本", "文本", "txt", true]`（3 次）
- `["r-q3-vllm-aijuxi", "v2t-llm-aijuxi", "txt", true]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)

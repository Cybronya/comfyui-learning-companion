# ZFImageReferenceAnalyzer

## 节点类型

`ZFImageReferenceAnalyzer`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `llama_model:LLAMACPPMODEL`（1 次）
- `parameters:LLAMACPPARAMS`（1 次）
- `analysis_result:STRING`（1 次）
- `enabled:BOOLEAN`（1 次）
- `reference_scope:COMBO`（1 次）
- `reference_strength:FLOAT`（1 次）
- `extract_text:BOOLEAN`（1 次）
- `protect_identity:BOOLEAN`（1 次）
- `max_size:INT`（1 次）

## 输出

- `reference_instruction:STRING`（1 次）
- `analysis_json:STRING`（1 次）
- `reference_summary:STRING`（1 次）
- `reference_image:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[true, "综合提取（元素、创意、构图）", 0.75, true, true, 768, 1010161235005754, "", ""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)

# MOSSPromptEnhancerLocal

## 节点类型

`MOSSPromptEnhancerLocal`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `request:STRING`（1 次）
- `model_name:COMBO`（1 次）
- `output_mode:COMBO`（1 次）
- `language:COMBO`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）
- `seed:INT`（1 次）
- `max_tokens:INT`（1 次）
- `context_size:INT`（1 次）
- `temperature:FLOAT`（1 次）

## 输出

- `prompt:STRING`（1 次）
- `draft_json:STRING`（1 次）
- `info:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["清晨的早点摊，招牌写着‘老街早餐’，自然纪实摄影。", "Huihui-Qwen3-VL-8B-Instruct-abliterated.Q8_0.gguf", "caption", "中文", 1024, 1024, 999, "fi`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)

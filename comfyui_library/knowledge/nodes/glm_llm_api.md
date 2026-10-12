# GLM_LLM_API

## 节点类型

`GLM_LLM_API`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `model:COMBO`（2 次）
- `api_key:STRING`（2 次）
- `max_tokens:INT`（2 次）
- `temperature:FLOAT`（2 次）
- `top_p:FLOAT`（2 次）
- `system_prompt:STRING`（2 次）
- `user_prompt:STRING`（2 次）

## 输出

- `reasoning_content:STRING`（2 次）
- `answer:STRING`（2 次）
- `tokens_usage:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["glm-4-flash", "668e178595a9461b98ba3542969cd7b1.8kGRiTjVVexJOyfQ", 2048, 0.8, 0.6, "# WanVideo自适应提示词Agent\n⚠️ 格式错误会导致工`（1 次）
- `["glm-4-flash", "668e178595a9461b98ba3542969cd7b1.8kGRiTjVVexJOyfQ", 2049, 1.6000000000000003, 0.6, "# WanVideo自适应提示词Age`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)

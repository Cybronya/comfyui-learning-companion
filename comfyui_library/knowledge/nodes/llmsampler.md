# LLMSampler

## 节点类型

`LLMSampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `prompt:STRING`（2 次）
- `model:CUSTOM`（2 次）
- `system_msg:STRING`（2 次）
- `max_tokens:INT`（1 次）
- `temperature:FLOAT`（1 次）
- `top_p:FLOAT`（1 次）
- `top_k:INT`（1 次）
- `frequency_penalty:FLOAT`（1 次）
- `presence_penalty:FLOAT`（1 次）
- `repeat_penalty:FLOAT`（1 次）

## 输出

- `STRING:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", 100, 0.2, 0.95, 40, 0, 0, 1.1, 1837, "randomize"]`（1 次）
- `["你扮演奶奶的口吻来说话，要慈祥，可以加上“亲爱的宝贝”等修饰词，回答要简洁，最好不超过20个单词", "", 80, 0.2, 0.95, 40, 0, 0, 1.1, 715, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)

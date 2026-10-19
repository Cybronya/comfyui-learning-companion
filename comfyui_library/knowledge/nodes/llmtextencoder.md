# LLMTextEncoder

## 节点类型

`LLMTextEncoder`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:LLM_MODEL`（2 次）
- `tokenizer:LLM_TOKENIZER`（2 次）
- `text:STRING`（2 次）
- `system_prompt:STRING`（2 次）
- `skip_first:INT`（2 次）

## 输出

- `hidden_states:LLM_HIDDEN_STATES`（2 次）
- `info:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["luo tianyi,sitting on boat,alternate_costume,(artist:atdan:0.9),(artist:torino_aqua:0.8),(artist:izumi_tsubasu:0.9),(a`（1 次）
- `["worst quality", "You are expert in understanding of user prompts for image generations. Create an image according to t`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)

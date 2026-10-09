# PromptRelayEncode

## 节点类型

`PromptRelayEncode`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（1 次）
- `clip:CLIP`（1 次）
- `latent:LATENT`（1 次）
- `relay_options:RELAY_OPTIONS`（1 次）
- `global_prompt:STRING`（1 次）
- `local_prompts:STRING`（1 次）
- `segment_lengths:STRING`（1 次）
- `epsilon:FLOAT`（1 次）

## 输出

- `model:MODEL`（1 次）
- `positive:CONDITIONING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["<Subject 1> is the woman in <Picture 1>, wearing a blue patterned jacket with flame-like motifs at the hem, with long `（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)

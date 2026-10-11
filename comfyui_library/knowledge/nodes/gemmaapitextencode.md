# GemmaAPITextEncode

## 节点类型

`GemmaAPITextEncode`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `api_key:STRING`（6 次）
- `prompt:STRING`（6 次）
- `ckpt_name:COMBO`（6 次）
- `enhance_prompt:BOOLEAN`（4 次）

## 输出

- `conditioning:CONDITIONING`（6 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "", "ltx-2.3-22b-dev.safetensors"]`（1 次）
- `["", "pc game, console game, video game, cartoon, childish, ugly", false]`（1 次）
- `["", "", "ltx-2.3-22b-dev.safetensors", "ltx-2.3-22b-dev.safetensors"]`（1 次）
- `["", "pc game, console game, video game, cartoon, childish, ugly", false, "ltx-2.3-22b-dev.safetensors"]`（1 次）
- `["", "", "ltx-2.3-22b-dev.safetensors", null]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)

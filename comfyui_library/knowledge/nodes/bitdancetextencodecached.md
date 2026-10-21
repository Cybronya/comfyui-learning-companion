# BitDanceTextEncodeCached

## 节点类型

`BitDanceTextEncodeCached`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 7 个 workflow 中。

## 输入

- `text_encoder:BITDANCE_TEXT_ENCODER`（7 次）
- `model_to_offload:BITDANCE_MODEL`（7 次）
- `positive_prompt:STRING`（7 次）
- `negative_prompt:STRING`（7 次）
- `force_offload:BOOLEAN`（7 次）
- `device:COMBO`（7 次）

## 输出

- `positive:BITDANCE_TEXT_EMBEDS`（7 次）
- `negative:BITDANCE_TEXT_EMBEDS`（7 次）
- `positive_prompt:STRING`（7 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["A wine glass full of tiny red pandas wearing blue hats.", "", true, "gpu"]`（2 次）
- `["", "", true, "gpu"]`（1 次）
- `["一位长发美人穿着白色狐裘，几缕发丝凌乱缠绕，斑驳的光影穿过稀疏的枯叶和密集的雪尘洒在脸上，奇幻场景，印象派，超广角镜头，朦胧，抽象艺术，艺术氛围浓厚，高饱和对比，大师光影，非常规独特构图，视觉艺术，获奖作品风格，呈现裘毛细雪结晶冰霜光泽`（1 次）
- `["Half-length composition, close-up shot, realistic close-up portrait, cool white skin tone, intricate black layered upd`（1 次）
- `["一个古装女孩", "", true, "gpu"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)

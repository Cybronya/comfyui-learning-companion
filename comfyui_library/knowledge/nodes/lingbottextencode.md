# LingBotTextEncode

## 节点类型

`LingBotTextEncode`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `image:IMAGE`（2 次）
- `encoder_name:COMBO`（2 次）
- `prompt:STRING`（2 次）
- `negative_prompt:STRING`（2 次）
- `keep_encoder_loaded:COMBO`（2 次）
- `i2v_width:INT`（2 次）
- `i2v_height:INT`（2 次）

## 输出

- `LINGBOT_EMBEDS:LINGBOT_EMBEDS`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["LingBot_text-encoder.safetensors", "{\n  \"comprehensive_description\": {\n    \"scene_content_description\": \"A man `（1 次）
- `["LingBot_text-encoder.safetensors", "{\n\n\"comprehensive_description\": {\n\n\"scene_content_description\": \"A red fo`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)

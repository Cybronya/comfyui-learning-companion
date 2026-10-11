# FishS2MultiSpeakerTTS

## 节点类型

`FishS2MultiSpeakerTTS`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `model_path:COMBO`（2 次）
- `text:STRING`（2 次）
- `language:COMBO`（2 次）
- `device:COMBO`（2 次）
- `precision:COMBO`（2 次）
- `attention:COMBO`（2 次）
- `max_new_tokens:INT`（2 次）
- `chunk_length:INT`（2 次）
- `temperature:FLOAT`（2 次）
- `top_p:FLOAT`（2 次）

## 输出

- `audio:AUDIO`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["s2-pro-bnb-nf4", "", "auto", "auto", "auto", "auto", 0, 200, 0.7, 0.7, 1.2, 42, "fixed", true, true, false, 0.3, "2", `（1 次）
- `["s2-pro", "[speaker_1]: 你叫我狐狸？\n[speaker_2]: 对不起，应该是白狐夫人。\n[speaker_1]: 以前陪我在雪山吃酱板鸭的时候，叫人家小狐狐。现在你有酱板鸭了，叫人家白狐夫人。\n", "au`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)

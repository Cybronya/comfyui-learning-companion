# FantasyTalkingWav2VecEmbeds

## 节点类型

`FantasyTalkingWav2VecEmbeds`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `wav2vec_model:WAV2VECMODEL`（1 次）
- `fantasytalking_model:FANTASYTALKINGMODEL`（1 次）
- `audio:AUDIO`（1 次）
- `num_frames:INT`（1 次）
- `audio_cfg_scale:FLOAT`（1 次）

## 输出

- `fantasytalking_embeds:FANTASYTALKING_EMBEDS`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[81, 25, 1, 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)

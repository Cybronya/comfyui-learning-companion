# MegaTTS3

## 节点类型

`MegaTTS3`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `input_text:STRING`（3 次）
- `language:COMBO`（3 次）
- `generation_quality:INT`（3 次）
- `pronunciation_strength:FLOAT`（3 次）
- `voice_similarity:FLOAT`（3 次）
- `reference_voice:COMBO`（3 次）

## 输出

- `generated_audio:AUDIO`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["清晨的雾还没散时，就想去公园捡最完整的银杏叶给你做书签。你说街角的糖炒栗子香得犯规，", "en", 32, 1.4, 3, "2.可爱台腔Haa.wav"]`（1 次）
- `["清晨的雾还没散时，就想去公园捡最完整的银杏叶给你做书签。你说街角的糖炒栗子香得犯规，", "en", 32, 1.4, 3, "Angiee.wav"]`（1 次）
- `["清晨的雾还没散时，就想去公园捡最完整的银杏叶给你做书签。你说街角的糖炒栗子香得犯规，", "en", 32, 1.4, 3, "2023-11-01 E姐04.wav_0025609920_0025779840.wav"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)

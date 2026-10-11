# LtoJ_ThreeReferenceAudioManager

## 节点类型

`LtoJ_ThreeReferenceAudioManager`

## 分类

Audio

## 作用

音频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `audio_1:LTOJ_H3_AUDIO_REFERENCE_ITEM`（1 次）
- `audio_2:LTOJ_H3_AUDIO_REFERENCE_ITEM`（1 次）
- `audio_3:LTOJ_H3_AUDIO_REFERENCE_ITEM`（1 次）
- `enabled:COMBO`（1 次）

## 输出

- `三路参考声音:LTOJ_H3_AUDIO_REFERENCE_PACK`（1 次）
- `可用声音引用清单:STRING`（1 次）
- `有效参考声音数:INT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["禁止"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)

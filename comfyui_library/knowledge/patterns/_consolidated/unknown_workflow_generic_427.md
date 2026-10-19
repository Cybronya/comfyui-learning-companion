---
name: unknown_workflow_generic_427
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.969667
common_nodes: [CR Prompt Text, Float, LoadAudio, SaveAudio, T8_IndexTTS25_EmotionControl, T8_IndexTTS25_Generate, T8_IndexTTS25_ModelLoader]
problems: []
missing: []
members: [图片生成/文生图/声音克隆IndexTTS2.5情感参考_2102959457717276673.json, 数字人/数字人/IndexTTS 2.5情感文本控制语音克隆_2105621844203233282.json, 视频生成/文生视频/IndexTTS 2.5情感文本控制语音克隆_2100454570265767937.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_427

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/声音克隆IndexTTS2.5情感参考_2102959457717276673.json、数字人/数字人/IndexTTS 2.5情感文本控制语音克隆_2105621844203233282.json、视频生成/文生视频/IndexTTS 2.5情感文本控制语音克隆_2100454570265767937.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 3 个 workflow 都包含：
- `CR Prompt Text`
- `Float`
- `LoadAudio`
- `SaveAudio`
- `T8_IndexTTS25_EmotionControl`
- `T8_IndexTTS25_Generate`
- `T8_IndexTTS25_ModelLoader`

**可变部分**（部分 workflow 才有）：
- `T8_IndexTTS25_SamplingConfig` —— 2/3 个有
- `EmptyImage` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `SaveAudioNode` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

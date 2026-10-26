---
name: unknown_workflow_generic_872
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.8935
common_nodes: [CR Prompt Text, LoadAudio, NormalizeAudioLoudness, Qwen3ASRLoader, Qwen3ASRTranscribe, SaveAudio, SaveAudioMP3]
problems: []
missing: []
members: [音频生成/音频生成/LongCat AudioDiT + Qwen3-ASR 语音克隆（单人+多人）极速版_2041410531860422657.json, 音频生成/音频生成/LongCat 有声书极速语音克隆三方案合集_2039610252290691074.json, 音频生成/音频生成/LongCat-AudioDiT-双人语音克隆对话TTS-目前综合效果最好-速度快_2040629647699873793.json, 音频生成/音频生成/LongCat-AudioDiT单人语音克隆TTS-目前综合效果最好-速度快_2040618415932579841.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_872

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（音频生成/音频生成/LongCat AudioDiT + Qwen3-ASR 语音克隆（单人+多人）极速版_2041410531860422657.json、音频生成/音频生成/LongCat 有声书极速语音克隆三方案合集_2039610252290691074.json、音频生成/音频生成/LongCat-AudioDiT-双人语音克隆对话TTS-目前综合效果最好-速度快_2040629647699873793.json、音频生成/音频生成/LongCat-AudioDiT单人语音克隆TTS-目前综合效果最好-速度快_2040618415932579841.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 4 个 workflow 都包含：
- `CR Prompt Text`
- `LoadAudio`
- `NormalizeAudioLoudness`
- `Qwen3ASRLoader`
- `Qwen3ASRTranscribe`
- `SaveAudio`
- `SaveAudioMP3`

**可变部分**（部分 workflow 才有）：
- `LongCatMultiSpeakerTTS` —— 3/4 个有
- `LongCatVoiceCloneTTS` —— 3/4 个有
- `ShowText|pysssss` —— 3/4 个有
- `FL_Audio_Separation` —— 2/4 个有
- `LongCatTTS` —— 2/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `PreviewAudio` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

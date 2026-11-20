---
name: unknown_workflow_generic_1192
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.892667
common_nodes: [LoadAudio, NormalizeAudioLoudness, Qwen3ASRLoader, Qwen3ASRTranscribe, SaveAudioMP3, ShowText|pysssss, easy cleanGpuUsed]
problems: []
missing: []
members: [音频生成/音频生成/LongCat-AudioDiT-单人语音克隆  情绪迁移 文生音频超自然 碾压index-tts2_2039705382821564418.json, 音频生成/音频生成/LongCat-AudioDiT-单人语音克隆_2039554832759005185.json, 音频生成/音频生成/LongCat-AudioDiT双人语音克隆对话TTS 优化版 不吃字不多字无杂音 情绪音色迁移_2039710328308633601.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1192

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（音频生成/音频生成/LongCat-AudioDiT-单人语音克隆  情绪迁移 文生音频超自然 碾压index-tts2_2039705382821564418.json、音频生成/音频生成/LongCat-AudioDiT-单人语音克隆_2039554832759005185.json、音频生成/音频生成/LongCat-AudioDiT双人语音克隆对话TTS 优化版 不吃字不多字无杂音 情绪音色迁移_2039710328308633601.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
- `LoadAudio`
- `NormalizeAudioLoudness`
- `Qwen3ASRLoader`
- `Qwen3ASRTranscribe`
- `SaveAudioMP3`
- `ShowText|pysssss`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 2/3 个有
- `LongCatVoiceCloneTTS` —— 2/3 个有
- `TrimAudioDuration` —— 2/3 个有
- `CR Prompt Text` —— 1/3 个有
- `LongCatMultiSpeakerTTS` —— 1/3 个有
- `SaveAudio` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

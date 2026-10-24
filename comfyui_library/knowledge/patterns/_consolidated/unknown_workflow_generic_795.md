---
name: unknown_workflow_generic_795
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.82875
common_nodes: [LoadAudio, LongCatVoiceCloneTTS, NormalizeAudioLoudness, Qwen3ASRLoader, Qwen3ASRTranscribe, SaveAudioMP3, easy showAnything]
problems: []
missing: []
members: [音频生成/音频生成/LongCat AudioDIT TTS 单人双人 高相似度语音克隆_2100480847823589378.json, 音频生成/音频生成/LongCat-AudioDiT 语音克隆_2041738987102019586.json, 音频生成/音频生成/LongCat-AudioDiT单_双人语音克隆TTS_2039290948785545217.json, 音频生成/音频生成/影视真人台词感-单人语音克隆--LongCat-AudioDiT（翻译）_2039728236652924929.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_795

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（音频生成/音频生成/LongCat AudioDIT TTS 单人双人 高相似度语音克隆_2100480847823589378.json、音频生成/音频生成/LongCat-AudioDiT 语音克隆_2041738987102019586.json、音频生成/音频生成/LongCat-AudioDiT单_双人语音克隆TTS_2039290948785545217.json、音频生成/音频生成/影视真人台词感-单人语音克隆--LongCat-AudioDiT（翻译）_2039728236652924929.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 4 个 workflow 都包含：
- `LoadAudio`
- `LongCatVoiceCloneTTS`
- `NormalizeAudioLoudness`
- `Qwen3ASRLoader`
- `Qwen3ASRTranscribe`
- `SaveAudioMP3`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 3/4 个有
- `LongCatMultiSpeakerTTS` —— 2/4 个有
- `SaveAudio` —— 2/4 个有
- `RunningHub SeedXPro Translator` —— 1/4 个有
- `Text Multiline` —— 1/4 个有
- `忽略多组孤海` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

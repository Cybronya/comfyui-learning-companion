---
name: unknown_workflow_generic_175
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.856909
common_nodes: [Audio To Text (mtb), CR Prompt Text, Load Whisper (mtb), LoadAudio, SaveAudioMP3]
problems: []
missing: []
members: [音频生成/音频生成/LongCat-AudioDiT-单人语音克隆_2039303040481632258.json, 音频生成/音频生成/LongCat-AudioDiT-音频生成-v2+全节点注释_2042480932396994561.json, 音频生成/音频生成/LongCat-AudioDiT-音频生成-v2_2042473151765942274.json, 音频生成/音频生成/LongCat-AudioDiT单人语音克隆TTS_2039208806344826881.json, 音频生成/音频生成/LongCat-AudioDiT单人语音克隆TTS_2039293692409815042.json, 音频生成/音频生成/LongCat-AudioDiT单人语音克隆TTS_2039309185434783746.json, 音频生成/音频生成/LongCat-AudioDiT单人语音克隆TTS_2039694725573255170.json, 音频生成/音频生成/LongCat-AudioDiT双人语音克隆对话TTS_2039215676392480769.json, 音频生成/音频生成/LongCat-AudioDiT双人语音克隆对话TTS_2039696306108633089.json, 音频生成/音频生成/单人语音克隆TTS_2044697057641897985.json, 音频生成/音频生成/双人语音克隆对话_2044482244785475586.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_175

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（音频生成/音频生成/LongCat-AudioDiT-单人语音克隆_2039303040481632258.json、音频生成/音频生成/LongCat-AudioDiT-音频生成-v2+全节点注释_2042480932396994561.json、音频生成/音频生成/LongCat-AudioDiT-音频生成-v2_2042473151765942274.json、音频生成/音频生成/LongCat-AudioDiT单人语音克隆TTS_2039208806344826881.json、音频生成/音频生成/LongCat-AudioDiT单人语音克隆TTS_2039293692409815042.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 11 个 workflow 都包含：
- `Audio To Text (mtb)`
- `CR Prompt Text`
- `Load Whisper (mtb)`
- `LoadAudio`
- `SaveAudioMP3`

**可变部分**（部分 workflow 才有）：
- `SaveAudio` —— 10/11 个有
- `NormalizeAudioLoudness` —— 9/11 个有
- `LongCatVoiceCloneTTS` —— 8/11 个有
- `LongCatMultiSpeakerTTS` —— 3/11 个有
- `TrimAudioDuration` —— 2/11 个有
- `TDQwen3TTSDefineSpeaker` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

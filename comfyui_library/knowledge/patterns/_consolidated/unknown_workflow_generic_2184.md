---
name: unknown_workflow_generic_2184
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.795
common_nodes: [AudioCrop, CR Prompt Text, LoadAudio, LongCatVoiceCloneTTS, NormalizeAudioLoudness, PreviewAudio, Qwen3ASRLoader, Qwen3ASRTranscribe, SaveAudioMP3]
problems: []
missing: []
members: [音频生成/音频生成/单人文字转音频工作流_2077368923833585666.json, 音频生成/音频生成/单人语音克隆_2042506511330582529.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_2184

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/单人文字转音频工作流_2077368923833585666.json、音频生成/音频生成/单人语音克隆_2042506511330582529.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：80%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioCrop`
- `CR Prompt Text`
- `LoadAudio`
- `LongCatVoiceCloneTTS`
- `NormalizeAudioLoudness`
- `PreviewAudio`
- `Qwen3ASRLoader`
- `Qwen3ASRTranscribe`
- `SaveAudioMP3`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Muter (rgthree)` —— 1/2 个有
- `RHExtractAudio` —— 1/2 个有
- `VHS_LoadVideo` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

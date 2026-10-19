---
name: unknown_workflow_generic_793
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8605
common_nodes: [Apply Whisper, LoadAudio, PreviewAny, Qwen3TTSModelLoader, Qwen3TTSVoiceClone, SaveAudio, Text]
problems: []
missing: []
members: [音频生成/音频生成/DG(3-30)_Qwen3 TTS语音克隆V1_2038434439209947137.json, 音频生成/音频生成/Qwen3 TTS语音克隆_2015070394163662850.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_793

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/DG(3-30)_Qwen3 TTS语音克隆V1_2038434439209947137.json、音频生成/音频生成/Qwen3 TTS语音克隆_2015070394163662850.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `Apply Whisper`
- `LoadAudio`
- `PreviewAny`
- `Qwen3TTSModelLoader`
- `Qwen3TTSVoiceClone`
- `SaveAudio`
- `Text`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 1/2 个有
- `AudioSeparation` —— 1/2 个有
- `CR Prompt Text` —— 1/2 个有
- `VHS_LoadVideo` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

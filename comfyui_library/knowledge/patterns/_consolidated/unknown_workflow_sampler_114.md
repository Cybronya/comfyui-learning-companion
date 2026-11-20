---
name: unknown_workflow_sampler_114
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.917
common_nodes: [LongCatVoiceCloneTTS, MelBandRoFormerModelLoader, MelBandRoFormerSampler, PreviewAny, PreviewAudio, Qwen3ASRLoader, Qwen3ASRTranscribe, SaveAudioAdvanced]
problems: []
missing: []
members: [音频生成/音频生成/简单换单词_2072195152751456258.json, 音频生成/音频生成/简单换单词v2_2084900520828952577.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_114

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/简单换单词_2072195152751456258.json、音频生成/音频生成/简单换单词v2_2084900520828952577.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `LongCatVoiceCloneTTS`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `PreviewAny`
- `PreviewAudio`
- `Qwen3ASRLoader`
- `Qwen3ASRTranscribe`
- `SaveAudioAdvanced`

**可变部分**（部分 workflow 才有）：
- `AudioAdjustVolume` —— 1/2 个有
- `LoadAudio` —— 1/2 个有
- `LoadAudioUI` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `SaveImage` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

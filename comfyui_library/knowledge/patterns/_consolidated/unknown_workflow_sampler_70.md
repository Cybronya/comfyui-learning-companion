---
name: unknown_workflow_sampler_70
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.917
common_nodes: [LongCatVoiceCloneTTS, MelBandRoFormerModelLoader, MelBandRoFormerSampler, PreviewAny, PreviewAudio, Qwen3ASRLoader, Qwen3ASRTranscribe, SaveAudioAdvanced]
problems: []
missing: []
members: [平台全量/简单换单词v2_2117228163389550594.json, 音频生成/音频生成/简单换单词_2072195152751456258.json, 音频生成/音频生成/简单换单词v2_2084900520828952577.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_70

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/简单换单词v2_2117228163389550594.json、音频生成/音频生成/简单换单词_2072195152751456258.json、音频生成/音频生成/简单换单词v2_2084900520828952577.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 3 个 workflow 都包含：
- `LongCatVoiceCloneTTS`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `PreviewAny`
- `PreviewAudio`
- `Qwen3ASRLoader`
- `Qwen3ASRTranscribe`
- `SaveAudioAdvanced`

**可变部分**（部分 workflow 才有）：
- `AudioAdjustVolume` —— 2/3 个有
- `LoadAudio` —— 2/3 个有
- `LoadAudioUI` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `SaveImage` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

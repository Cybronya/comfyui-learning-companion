---
name: unknown_workflow_sampler_104
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9395
common_nodes: [Apply Whisper, LoadAudio, RunningHub StepAudioEditX ModelLoader, RunningHub StepAudioEditX Sampler(Clone), RunningHub StepAudioEditX Sampler(Denoise), RunningHub StepAudioEditX Sampler(Emotion), RunningHub StepAudioEditX Sampler(Paralinguistic), RunningHub StepAudioEditX Sampler(Style), SaveAudio, ShowText]
problems: []
missing: []
members: [音频生成/音频生成/StepAudioEditX音频编辑_1990663602531176450.json, 音频生成/音频生成/StepAudioEditX音频编辑工作流_1989187773158535169.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_104

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/StepAudioEditX音频编辑_1990663602531176450.json、音频生成/音频生成/StepAudioEditX音频编辑工作流_1989187773158535169.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 2 个 workflow 都包含：
- `Apply Whisper`
- `LoadAudio`
- `RunningHub StepAudioEditX ModelLoader`
- `RunningHub StepAudioEditX Sampler(Clone)`
- `RunningHub StepAudioEditX Sampler(Denoise)`
- `RunningHub StepAudioEditX Sampler(Emotion)`
- `RunningHub StepAudioEditX Sampler(Paralinguistic)`
- `RunningHub StepAudioEditX Sampler(Style)`
- `SaveAudio`
- `ShowText`

**可变部分**（部分 workflow 才有）：
- `KepStringLiteral` —— 1/2 个有
- `SoundFlow_TrimAudio` —— 1/2 个有
- `TrimAudio` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

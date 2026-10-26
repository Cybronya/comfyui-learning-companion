---
name: unknown_workflow_sampler_107
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.613
common_nodes: [AudioCombine, GetNode, HeartMuLa_Generate, INTConstant, JWStringSplit, JoinStrings, LoadAudio, MelBandRoFormerModelLoader, MelBandRoFormerSampler, Qwen3_VQA, SaveAudioMP3, SeedVCRun, SetNode, ShellAgentPluginOutputText, TextInput_, easy showAnything]
problems: []
missing: []
members: [音频生成/音频生成/HeartMuLa强化版歌曲生成+音色替换（附自动生歌词）_2016577029856043009.json, 音频生成/音频生成/HeartMuLa强化版歌曲生成（附自动生歌词）_2016629405614874625.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_107

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/HeartMuLa强化版歌曲生成+音色替换（附自动生歌词）_2016577029856043009.json、音频生成/音频生成/HeartMuLa强化版歌曲生成（附自动生歌词）_2016629405614874625.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：61%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioCombine`
- `GetNode`
- `HeartMuLa_Generate`
- `INTConstant`
- `JWStringSplit`
- `JoinStrings`
- `LoadAudio`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `Qwen3_VQA`
- `SaveAudioMP3`
- `SeedVCRun`
- `SetNode`
- `ShellAgentPluginOutputText`
- `TextInput_`
- `easy showAnything`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

---
name: unknown_workflow_sampler_95
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [IndexTTS2Run, JWStringMultiline, LoadAudio, MelBandRoFormerModelLoader, MelBandRoFormerSampler, PreviewAudio]
problems: []
missing: []
members: [数字人/数字人/IndexTTS-2.0声音&音色克隆实践_1965630163675435009.json, 音频生成/音频生成/IndexTTS-2音色克隆_2036450175434104833.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_95

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/IndexTTS-2.0声音&音色克隆实践_1965630163675435009.json、音频生成/音频生成/IndexTTS-2音色克隆_2036450175434104833.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `IndexTTS2Run`
- `JWStringMultiline`
- `LoadAudio`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `PreviewAudio`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 1/2 个有
- `SaveAudioMP3` —— 1/2 个有
- `SaveImage` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

---
name: unknown_workflow_sampler_unet_vae_209
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.789
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadAudio, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SaveAudioAdvanced, StringFormat, UNETLoader, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [音频生成/音频生成/minimax-H3-单音频-声音克隆_2099008776971051009.json, 音频生成/音频生成/minimax-H3-单音频-声音克隆_2109827821043535873.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_209

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/minimax-H3-单音频-声音克隆_2099008776971051009.json、音频生成/音频生成/minimax-H3-单音频-声音克隆_2109827821043535873.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：79%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadAudio`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveAudioAdvanced`
- `StringFormat`
- `UNETLoader`
- `VAEDecodeAudio`
- `VAELoader`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

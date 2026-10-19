---
name: unknown_workflow_lora_sampler_unet_81
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9535
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadAudio, LoadImage, Lora Loader Stack (rgthree), MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, PixaromaSaveMp4, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SigmasToFloat, SplitSigmas, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3  8.20_2084615308018540545.json, 视频生成/图生视频/MiniMax H3  8.22_2091004876800217090.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_81

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3  8.20_2084615308018540545.json、视频生成/图生视频/MiniMax H3  8.22_2091004876800217090.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadAudio`
- `LoadImage`
- `Lora Loader Stack (rgthree)`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `PixaromaSaveMp4`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SigmasToFloat`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced` —— 1/2 个有
- `MiniMaxH3TwoPassDetailMixerT8Advanced` —— 1/2 个有
- `MinimaxH3LatentUpscaler3D` —— 1/2 个有
- `MinimaxH3LatentUpscalerNode3D` —— 1/2 个有
- `SolAttnMiniMax` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

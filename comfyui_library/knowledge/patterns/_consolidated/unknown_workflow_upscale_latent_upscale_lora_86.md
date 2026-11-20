---
name: unknown_workflow_upscale_latent_upscale_lora_86
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.758
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, CreateVideo, LoadImage, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3LearnedLatentUpscaleT8Advanced, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3TwoPassDetailMixerT8Advanced, MiniMaxH3TwoPassLatentReconcileT8Advanced, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/四只兔子_H3_高动态双采放大专属_2096882401648668673.json, 视频生成/文生视频/BUNNY_H3_高动态双采放大专属_FL2VA_REF2VA_2095962479263309826.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_86

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/四只兔子_H3_高动态双采放大专属_2096882401648668673.json、视频生成/文生视频/BUNNY_H3_高动态双采放大专属_FL2VA_REF2VA_2095962479263309826.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：76%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `LoadImage`
- `LoraLoaderBypassModelOnly`
- `LoraLoaderModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3DualClockSamplerT8`
- `MiniMaxH3LearnedLatentUpscaleT8Advanced`
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3TwoPassDetailMixerT8Advanced`
- `MiniMaxH3TwoPassLatentReconcileT8Advanced`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 1/2 个有
- `VHS_LoadVideo` —— 1/2 个有
- `easy loraStack` —— 1/2 个有
- `easy loraStackApply` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

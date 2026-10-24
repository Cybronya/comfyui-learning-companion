---
name: unknown_workflow_lora_sampler_unet_154
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8666
common_nodes: [BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, MiniMaxLowVRAMAttention, ModelPreviewOverrideKJ, PrimitiveFloat, PrimitiveStringMultiline, ResolutionSelector, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/超自然超细节-H3的服装展示(dasiwa)_2101210281803337729.json, 视频生成/文生视频/Dasiwa+H3 taomate 3步加速 中远距离不崩脸_2101450830070247426.json, 视频生成/文生视频/DsiwaV2 +selflift二采+小脸优化_2101450792984207362.json, 视频生成/文生视频/H3 dasiwaV3+高动态支持+特殊运镜_2107756287479074818.json, 视频生成/文生视频/H3 dasiwaV3+高动态支持+特殊运镜_2108505430593986562.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_154

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/超自然超细节-H3的服装展示(dasiwa)_2101210281803337729.json、视频生成/文生视频/Dasiwa+H3 taomate 3步加速 中远距离不崩脸_2101450830070247426.json、视频生成/文生视频/DsiwaV2 +selflift二采+小脸优化_2101450792984207362.json、视频生成/文生视频/H3 dasiwaV3+高动态支持+特殊运镜_2107756287479074818.json、视频生成/文生视频/H3 dasiwaV3+高动态支持+特殊运镜_2108505430593986562.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `MiniMaxLowVRAMAttention`
- `ModelPreviewOverrideKJ`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 4/5 个有
- `SelfLiftAvatarH3Sampler` —— 4/5 个有
- `easy seed` —— 4/5 个有
- `MiniMaxH3TurboLoRA` —— 3/5 个有
- `LoadAudio` —— 2/5 个有
- `BasicGuider` —— 1/5 个有
- `H3SigmaRefiner` —— 1/5 个有
- `LoraLoaderBypassModelOnly` —— 1/5 个有
- `RandomNoise` —— 1/5 个有
- `SamplerCustomAdvanced` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

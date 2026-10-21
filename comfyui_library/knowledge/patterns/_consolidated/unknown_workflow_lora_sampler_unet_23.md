---
name: unknown_workflow_lora_sampler_unet_23
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.825571
common_nodes: [BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, PrimitiveFloat, PrimitiveStringMultiline, ResolutionSelector, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/超自然超细节-H3的服装展示(dasiwa)_2101210281803337729.json, 视频生成/文生视频/Dasiwa+H3 taomate 3步加速 中远距离不崩脸_2101450830070247426.json, 视频生成/文生视频/DsiwaV2 +selflift二采+小脸优化_2101450792984207362.json, 视频生成/文生视频/H3 dasiwaV3+高动态支持+特殊运镜_2107756287479074818.json, 视频生成/文生视频/H3 dasiwaV3+高动态支持+特殊运镜_2108505430593986562.json, 视频生成/文生视频/Minmax H3参考加速工作流_2086695240752263170.json, 视频生成/文生视频/🔪🔪阶段总结版！MiniMax H3全功能加速工作流拆解系列04集_2091383371724316673.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_23

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/超自然超细节-H3的服装展示(dasiwa)_2101210281803337729.json、视频生成/文生视频/Dasiwa+H3 taomate 3步加速 中远距离不崩脸_2101450830070247426.json、视频生成/文生视频/DsiwaV2 +selflift二采+小脸优化_2101450792984207362.json、视频生成/文生视频/H3 dasiwaV3+高动态支持+特殊运镜_2107756287479074818.json、视频生成/文生视频/H3 dasiwaV3+高动态支持+特殊运镜_2108505430593986562.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelPreviewOverrideKJ` —— 6/7 个有
- `MiniMaxChunkFeedForward` —— 5/7 个有
- `MiniMaxLowVRAMAttention` —— 5/7 个有
- `ConditioningZeroOut` —— 4/7 个有
- `SelfLiftAvatarH3Sampler` —— 4/7 个有
- `easy seed` —— 4/7 个有
- `BasicGuider` —— 3/7 个有
- `H3SigmaRefiner` —— 3/7 个有
- `LoadAudio` —— 3/7 个有
- `MiniMaxH3TurboLoRA` —— 3/7 个有
- `RandomNoise` —— 3/7 个有
- `SamplerCustomAdvanced` —— 3/7 个有
- `ModelAttentionBackend` —— 2/7 个有
- `Int` —— 1/7 个有
- `LoraLoaderBypassModelOnly` —— 1/7 个有
- `SigmasPreview` —— 1/7 个有
- `SolAttnMiniMax` —— 1/7 个有
- `VHS_LoadVideo` —— 1/7 个有
- `孤海注释` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

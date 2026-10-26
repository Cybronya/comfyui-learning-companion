---
name: unknown_workflow_lora_sampler_unet_236
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.429333
common_nodes: [BasicScheduler, CLIPLoader, CM_IntUnaryOperation, ConditioningZeroOut, EmptyImage, GetImageSizeAndCount, GetNode, H3SigmaRefiner, ImageLoader, ImageResizeKJv2, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, Make Image Batch, MemoryCleaner, MiniMaxChunkFeedForward, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MiniMaxLowVRAMAttention, ResolutionSelector, SelfLiftAvatarH3Sampler, SetNode, SimpleMath+, StringFunction|pysssss, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, easy anythingIndexSwitch, easy anythingInversedSwitch, easy int, easy positive, easy saveText, easy seed, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: []
missing: []
members: [图片生成/图生图/生图-任意数量编辑多宫格自动(5图以内)-Minnimax-H3-官方_2100965690554544129.json, 图片生成/图生图/生图-任意数量编辑融合自动(5图以内)-Minnimax-H3-官方_2100964513884495873.json, 视频生成/图生视频/视频-任意数量参考生视频-Minnimax-H3-官方_2084309352525164546.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_236

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/生图-任意数量编辑多宫格自动(5图以内)-Minnimax-H3-官方_2100965690554544129.json、图片生成/图生图/生图-任意数量编辑融合自动(5图以内)-Minnimax-H3-官方_2100964513884495873.json、视频生成/图生视频/视频-任意数量参考生视频-Minnimax-H3-官方_2084309352525164546.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：43%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CM_IntUnaryOperation`
- `ConditioningZeroOut`
- `EmptyImage`
- `GetImageSizeAndCount`
- `GetNode`
- `H3SigmaRefiner`
- `ImageLoader`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderBypassModelOnly`
- `LoraLoaderModelOnly`
- `Make Image Batch`
- `MemoryCleaner`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxLowVRAMAttention`
- `ResolutionSelector`
- `SelfLiftAvatarH3Sampler`
- `SetNode`
- `SimpleMath+`
- `StringFunction|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `easy anythingIndexSwitch`
- `easy anythingInversedSwitch`
- `easy int`
- `easy positive`
- `easy saveText`
- `easy seed`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 2/3 个有
- `ImageFromBatch` —— 2/3 个有
- `Int` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `PrimitiveStringMultiline` —— 2/3 个有
- `SaveImage` —— 2/3 个有
- `VOSR2ModelLoader` —— 2/3 个有
- `VOSR2Upscale` —— 2/3 个有
- `ComfyMathExpression` —— 1/3 个有
- `CreateVideo` —— 1/3 个有
- `ImpactFloat` —— 1/3 个有
- `JWFloatToString` —— 1/3 个有
- `PrimitiveFloat` —— 1/3 个有
- `SaveVideo` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

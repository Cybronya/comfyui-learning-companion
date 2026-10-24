---
name: unknown_workflow_upscale_lora_sampler_80
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.751
common_nodes: [Any Switch (rgthree), Anything Everywhere, BasicScheduler, Bjornulf_ShowInt, CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, GetImageSizeAndCount, INTConstant, Image Comparer (rgthree), Image H264 Compression (mtb), ImagePass, ImageScale, ImageSmartSharpen+, KSamplerSelect, LayerFilter: FilmV2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, RandomNoise, RebatchLatents, ReferenceLatent, RepeatLatentBatch, SamplerCustomAdvanced, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TilePreprocessor, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/图生图/Flux.2 klein + seedvr2.5 Upscaler 参考图像超清放大_2012982565870772226.json, 图片生成/图生图/图片质感恢复及放大 01_2033577334225248258.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_80

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Flux.2 klein + seedvr2.5 Upscaler 参考图像超清放大_2012982565870772226.json、图片生成/图生图/图片质感恢复及放大 01_2033577334225248258.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：75%

## 共有节点

全部 2 个 workflow 都包含：
- `Any Switch (rgthree)`
- `Anything Everywhere`
- `BasicScheduler`
- `Bjornulf_ShowInt`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `GetImageSizeAndCount`
- `INTConstant`
- `Image Comparer (rgthree)`
- `Image H264 Compression (mtb)`
- `ImagePass`
- `ImageScale`
- `ImageSmartSharpen+`
- `KSamplerSelect`
- `LayerFilter: FilmV2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `RebatchLatents`
- `ReferenceLatent`
- `RepeatLatentBatch`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TilePreprocessor`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `ImpactControlBridge` —— 1/2 个有
- `LG_Color_Match_V2` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `easy imageColorMatch` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

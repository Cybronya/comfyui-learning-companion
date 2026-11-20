---
name: unknown_workflow_upscale_lora_sampler_56
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.8105
common_nodes: [Any Switch (rgthree), Anything Everywhere, BasicScheduler, Bjornulf_ShowInt, CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, GetImageSizeAndCount, INTConstant, Image Comparer (rgthree), Image H264 Compression (mtb), ImagePass, ImageScale, ImageSmartSharpen+, KSamplerSelect, LayerFilter: FilmV2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, RandomNoise, RebatchLatents, ReferenceLatent, RepeatLatentBatch, SamplerCustomAdvanced, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TilePreprocessor, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/图生图/Flux.2 klein + seedvr2.5 Upscaler 参考图像超清放大_2012982565870772226.json, 图片生成/图生图/图片质感恢复及放大 01_2033577334225248258.json, 平台全量/Edit R2i模糊图像超高清放大 Flux2 klein +Seedvr2.5 Upscaler_2033050185214988289.json, 平台全量/图像超清放大Flux.2 klein + seedvr2.5 Upscaler  高清修复细节_2035172774754394114.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_56

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Flux.2 klein + seedvr2.5 Upscaler 参考图像超清放大_2012982565870772226.json、图片生成/图生图/图片质感恢复及放大 01_2033577334225248258.json、平台全量/Edit R2i模糊图像超高清放大 Flux2 klein +Seedvr2.5 Upscaler_2033050185214988289.json、平台全量/图像超清放大Flux.2 klein + seedvr2.5 Upscaler  高清修复细节_2035172774754394114.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 4 个 workflow 都包含：
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
- `LG_Color_Match_V2` —— 2/4 个有
- `easy imageColorMatch` —— 2/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `GetNode` —— 1/4 个有
- `ImpactControlBridge` —— 1/4 个有
- `SetNode` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

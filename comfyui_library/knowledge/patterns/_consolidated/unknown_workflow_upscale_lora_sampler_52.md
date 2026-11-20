---
name: unknown_workflow_upscale_lora_sampler_52
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8716
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, ImageResize+, ImageScaleBy, ImageScaleToTotalPixels, KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageSize]
problems: []
missing: []
members: [图片生成/图生图/扩图工作流111111_2079840876804792321.json, 平台全量/Klein高清扩图工作流_2086094525570838530.json, 平台全量/klien放大+PPT+seedvr2放大_2080916662341169153.json, 平台全量/高清放大，无损增加细节_2076651473374633985.json, 数字人/数字人/人像精修-皮肤真实感细节_2070383420349444098.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_52

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/扩图工作流111111_2079840876804792321.json、平台全量/Klein高清扩图工作流_2086094525570838530.json、平台全量/klien放大+PPT+seedvr2放大_2080916662341169153.json、平台全量/高清放大，无损增加细节_2076651473374633985.json、数字人/数字人/人像精修-皮肤真实感细节_2070383420349444098.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `ImageResize+`
- `ImageScaleBy`
- `ImageScaleToTotalPixels`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `ColorMatch` —— 4/5 个有
- `Fast Groups Bypasser (rgthree)` —— 3/5 个有
- `GetNode` —— 3/5 个有
- `Image Comparer (rgthree)` —— 3/5 个有
- `LayerUtility: PurgeVRAM` —— 3/5 个有
- `PreviewImage` —— 3/5 个有
- `SetNode` —— 3/5 个有
- `DrawMaskOnImage` —— 2/5 个有
- `ImageConcanate` —— 2/5 个有
- `ImagePadForOutpaint` —— 2/5 个有
- `LCSColorAnchor` —— 2/5 个有
- `LCSLoadData` —— 2/5 个有
- `LCSSharpnessCalibrate` —— 2/5 个有
- `LCSSharpnessIntervene` —— 2/5 个有
- `Label (rgthree)` —— 2/5 个有
- `easy cleanGpuUsed` —— 2/5 个有
- `easy seed` —— 2/5 个有
- `ImageColorMatch+` —— 1/5 个有
- `ImageCompositeMasked` —— 1/5 个有
- `ImageScale` —— 1/5 个有
- `InvertMask` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

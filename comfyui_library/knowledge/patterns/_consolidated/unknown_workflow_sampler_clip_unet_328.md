---
name: unknown_workflow_sampler_clip_unet_328
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.7575
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Flux2Scheduler, Image Comparer (rgthree), ImageCASharpening+, ImageResize+, ImpactMinMax, KSamplerSelect, LoadImage, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SeedVR2, SimpleMath+, TTP_Image_Assy, TTP_Image_Tile_Batch, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/图生图/Flux2-kelin人物一致性换装_2094700257849462785.json, 平台全量/Flux2-kelin人物一致性换装_2043907440378388482.json, 平台全量/开源模型flux_klein建筑室内外效果图工作流+高清放大_2056269427657756673.json, 平台全量/开源模型flux_klein建筑室内外效果图工作流+高清放大应用2_2057395635455873026.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_328

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Flux2-kelin人物一致性换装_2094700257849462785.json、平台全量/Flux2-kelin人物一致性换装_2043907440378388482.json、平台全量/开源模型flux_klein建筑室内外效果图工作流+高清放大_2056269427657756673.json、平台全量/开源模型flux_klein建筑室内外效果图工作流+高清放大应用2_2057395635455873026.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：76%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Flux2Scheduler`
- `Image Comparer (rgthree)`
- `ImageCASharpening+`
- `ImageResize+`
- `ImpactMinMax`
- `KSamplerSelect`
- `LoadImage`
- `PreviewImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SeedVR2`
- `SimpleMath+`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 2/4 个有
- `DF_Get_image_size` —— 2/4 个有
- `DF_Integer` —— 2/4 个有
- `Get Image Size` —— 2/4 个有
- `GetImageSize` —— 2/4 个有
- `GetNode` —— 2/4 个有
- `ImageConcanate` —— 2/4 个有
- `ImageScaleToTotalPixels` —— 2/4 个有
- `Int` —— 2/4 个有
- `JWFloat` —— 2/4 个有
- `LayerUtility: PurgeVRAM` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `SetNode` —— 2/4 个有
- `AILab_QwenVL_Advanced` —— 1/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 1/4 个有
- `ShowText|pysssss` —— 1/4 个有
- `Text List` —— 1/4 个有
- `Text List to Text` —— 1/4 个有
- `easy positive` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

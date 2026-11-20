---
name: unknown_workflow_sampler_clip_vae_73
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.861
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, FluxGuidance, Image Comparer (rgthree), ImageScale, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SaveImage, SeedVR2BlockSwap, SeedVR2ExtraArgs, SeedVR2GGUF, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, VAEDecode, VAELoader, easy imageBatchToImageList, easy imageListToImageBatch, easy imageSize, easy imageSizeBySide]
problems: []
missing: []
members: [图片生成/图生图/去ai质感高清图生图_1971387760735109122.json, 图片生成/文生图/FLUX SRPO 超精细写实文生图_1975496914173079554.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_73

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/去ai质感高清图生图_1971387760735109122.json、图片生成/文生图/FLUX SRPO 超精细写实文生图_1975496914173079554.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `ImageScale`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `SeedVR2GGUF`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `VAEDecode`
- `VAELoader`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`
- `easy imageSize`
- `easy imageSizeBySide`

**可变部分**（部分 workflow 才有）：
- `AdvancedLyingSigmaSampler` —— 1/2 个有
- `DualCLIPLoader` —— 1/2 个有
- `EmptySD3LatentImage` —— 1/2 个有
- `ImageResize+` —— 1/2 个有
- `LayerUtility: PurgeVRAM` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `ModelSamplingFlux` —— 1/2 个有
- `NunchakuFluxDiTLoader` —— 1/2 个有
- `NunchakuFluxLoraLoader` —— 1/2 个有
- `NunchakuTextEncoderLoader` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `RH_Translator` —— 1/2 个有
- `TeaCache` —— 1/2 个有
- `UNETLoader` —— 1/2 个有
- `VAEEncode` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

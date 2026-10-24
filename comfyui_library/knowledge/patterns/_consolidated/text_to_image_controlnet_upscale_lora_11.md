---
name: text_to_image_controlnet_upscale_lora_11
type: Text To Image
frequency: 2
level: weak
coverage: 0.784
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, CR Text, ConditioningZeroOut, DapaoImageCompressionNode, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetImageSize+, GetImageSizeAndCount, GetNode, ImageResize+, ImageScaleBy, ImageScaleToTotalPixels, ImageUpscaleWithModel, ImpactSwitch, KSampler, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, ModelPatchLoader, PreviewImage, QwenImageDiffsynthControlnet, RH_Captioner, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAELoader, easy cleanGpuUsed, easy ifElse, easy int, easy isNone, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/CN2.1控制洗图_2031038834472914946.json, 图片生成/图生图/🐈Z-image 4K洗图+CN2.1控制🐈_2011983124770590722.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_upscale_lora_11

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/CN2.1控制洗图_2031038834472914946.json、图片生成/图生图/🐈Z-image 4K洗图+CN2.1控制🐈_2011983124770590722.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：78%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `DapaoImageCompressionNode`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize+`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageResize+`
- `ImageScaleBy`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `ImpactSwitch`
- `KSampler`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchLoader`
- `PreviewImage`
- `QwenImageDiffsynthControlnet`
- `RH_Captioner`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy ifElse`
- `easy int`
- `easy isNone`
- `easy showAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 1536 | - | 2 | 100% |
| 采样步数 | 10 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1536，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 10，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

---
name: unknown_workflow_upscale_lora_sampler_59
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.860667
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, GetImageSize+, Image Comparer (rgthree), ImageResize+, ImageResizeKJv2, ImageScaleBy, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux.2-Klein-9b老照片修复照片去AI质感提升工作流 V1.0_2040773448196169729.json, 图片生成/图生图/flux.2-klein-9b老照片修复，照片去AI，质感提升_2028040297262882817.json, 图片生成/图生图/高清修复图像版升级优化_2062083713374187521.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_59

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Flux.2-Klein-9b老照片修复照片去AI质感提升工作流 V1.0_2040773448196169729.json、图片生成/图生图/flux.2-klein-9b老照片修复，照片去AI，质感提升_2028040297262882817.json、图片生成/图生图/高清修复图像版升级优化_2062083713374187521.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `GetImageSize+`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImageResizeKJv2`
- `ImageScaleBy`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
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

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `INTConstant` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `PrimitiveFloat` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `Float` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有
- `easy clearCacheAll` —— 1/3 个有
- `easy imageColorMatch` —— 1/3 个有
- `easy imageScaleDownBy` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 3 | 100% |
| Prompt 约束强度(CFG) | 6 | 4 - 6 | 3 | 82% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | euler | - | 3 | 67% |
| 重绘幅度 | simple | - | 3 | 67% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 6，观测区间 4 - 6，3 个样本，取值集中（一致性 82%）
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，3 个样本，一致性 67%
- 重绘幅度 最常用 simple，3 个样本，一致性 67%

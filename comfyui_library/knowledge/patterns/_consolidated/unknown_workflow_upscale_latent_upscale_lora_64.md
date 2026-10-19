---
name: unknown_workflow_upscale_latent_upscale_lora_64
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.803
common_nodes: [Any Switch (rgthree), CLIPLoader, CLIPTextEncode, CR Prompt Text, ColorMatchV2, ConditioningZeroOut, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetImageSize, GetImageSize+, ImageCASharpening+, ImageResize+, ImageScaleBy, KSamplerAdvanced, LatentUpscaleBy, LoadImage, LoraLoaderModelOnly, PreviewAny, PreviewImage, SaveImage, Seed (rgthree), SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed, easy promptConcat, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: []
missing: []
members: [图片生成/文生图/Krea2 文生图+图推图_2102928700852494337.json, 图片生成/文生图/Krea2_文生图+图推图_2104373697317523457.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_64

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Krea2 文生图+图推图_2102928700852494337.json、图片生成/文生图/Krea2_文生图+图推图_2104373697317523457.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：80%

## 共有节点

全部 2 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `ColorMatchV2`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize`
- `GetImageSize+`
- `ImageCASharpening+`
- `ImageResize+`
- `ImageScaleBy`
- `KSamplerAdvanced`
- `LatentUpscaleBy`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewAny`
- `PreviewImage`
- `SaveImage`
- `Seed (rgthree)`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy promptConcat`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 2 | 100% |
| Prompt 约束强度(CFG) | 7 | - | 2 | 100% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler | - | 2 | 100% |
| 重绘幅度 | simple | - | 2 | 100% |
| 宽度 | 720 | - | 2 | 100% |
| 高度 | 1280 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 7，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，2 个样本，一致性 100%
- 重绘幅度 最常用 simple，2 个样本，一致性 100%
- 宽度 中位数 720，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1280，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

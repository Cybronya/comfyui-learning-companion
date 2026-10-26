---
name: unknown_workflow_upscale_latent_upscale_sampler_19
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.817
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, ColorMatchV2, ConditioningZeroOut, EmptyLatentImage, GetImageSize+, ImageCASharpening+, ImageResize+, ImageScaleBy, KSamplerAdvanced, LatentUpscaleBy, LoadImage, PreviewImage, SaveImage, Seed (rgthree), SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Krea2 双采+高清生图优化流_2078259754073411585.json, 图片生成/文生图/Krea2 图片反推+提示词自动扩写+双采 V2_2070845487900610561.json, 图片生成/文生图/Krea2 文生图+图推图_2102928700852494337.json, 图片生成/文生图/Krea2_文生图+图推图_2104373697317523457.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_sampler_19

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Krea2 双采+高清生图优化流_2078259754073411585.json、图片生成/文生图/Krea2 图片反推+提示词自动扩写+双采 V2_2070845487900610561.json、图片生成/文生图/Krea2 文生图+图推图_2102928700852494337.json、图片生成/文生图/Krea2_文生图+图推图_2104373697317523457.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `ColorMatchV2`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `GetImageSize+`
- `ImageCASharpening+`
- `ImageResize+`
- `ImageScaleBy`
- `KSamplerAdvanced`
- `LatentUpscaleBy`
- `LoadImage`
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

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `PreviewAny` —— 3/4 个有
- `easy cleanGpuUsed` —— 3/4 个有
- `easy promptConcat` —— 3/4 个有
- `llama_cpp_instruct_adv` —— 3/4 个有
- `llama_cpp_model_loader` —— 3/4 个有
- `llama_cpp_parameters` —— 3/4 个有
- `Any Switch (rgthree)` —— 2/4 个有
- `Fast Groups Bypasser (rgthree)` —— 2/4 个有
- `EmptyImage` —— 1/4 个有
- `PrimitiveFloat` —— 1/4 个有
- `SimpleMathDual+` —— 1/4 个有
- `UltimateSDUpscale` —— 1/4 个有
- `UpscaleModelLoader` —— 1/4 个有
- `easy promptList` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 4 | 100% |
| Prompt 约束强度(CFG) | 7 | 7 - 7 | 4 | 100% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | euler | - | 4 | 100% |
| 重绘幅度 | simple | - | 4 | 100% |
| 宽度 | 720 | 720 - 720 | 4 | 100% |
| 高度 | 1280 | 1280 - 1280 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，4 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 7，观测区间 7 - 7，4 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，4 个样本，一致性 100%
- 重绘幅度 最常用 simple，4 个样本，一致性 100%
- 宽度 中位数 720，观测区间 720 - 720，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1280，观测区间 1280 - 1280，4 个样本，取值集中（一致性 100%）

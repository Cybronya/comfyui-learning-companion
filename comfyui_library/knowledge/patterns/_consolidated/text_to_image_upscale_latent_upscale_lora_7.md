---
name: text_to_image_upscale_latent_upscale_lora_7
type: Text To Image
frequency: 6
level: strong
coverage: 0.801167
common_nodes: [Any Switch (rgthree), CLIPLoader, CLIPTextEncode, CR Prompt Text, ColorMatchV2, ConditioningZeroOut, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetImageSize, GetImageSize+, ImageCASharpening+, ImageResize+, ImageScaleBy, JjkText, KSampler, KSamplerAdvanced, LatentUpscaleBy, LoadImage, LoraLoaderModelOnly, PreviewAny, PreviewImage, SaveImage, Seed (rgthree), SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed, easy promptConcat, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/Krea2文生图加图推图，文生图反推提示词图生图多合一工作流_2103587240038457345.json, 图片生成/文生图/Krea2文生图加图推图 文生图图生图二合一方案_2105064611237163009.json, 图片生成/文生图/Krea2文生图加图推图 文生图图生图二合一方案_2105447891073589249.json, 图片生成/文生图/Krea2文生图加图推图双模式｜反推提示词一次配齐_2103105870958780418.json, 图片生成/文生图/Krea2文生图加图推图，文生图反推提示词图生图多合一工作流_2103630586794569730.json, 图片生成/文生图/Krea2文生图加图推图，文生图反推提示词图生图多合一工作流_2103970195332222978.json]
source: knowledge_consolidation
---

# text_to_image_upscale_latent_upscale_lora_7

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/反推提示词/Krea2文生图加图推图，文生图反推提示词图生图多合一工作流_2103587240038457345.json、图片生成/文生图/Krea2文生图加图推图 文生图图生图二合一方案_2105064611237163009.json、图片生成/文生图/Krea2文生图加图推图 文生图图生图二合一方案_2105447891073589249.json、图片生成/文生图/Krea2文生图加图推图双模式｜反推提示词一次配齐_2103105870958780418.json、图片生成/文生图/Krea2文生图加图推图，文生图反推提示词图生图多合一工作流_2103630586794569730.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 6 个 workflow 都包含：
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
- `JjkText`
- `KSampler`
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
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 2/6 个有
- `LoraLoaderModelOnly_Any` —— 2/6 个有
- `easy promptList` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高发问题（8/6 个样本）：Steps较低可能导致细节不足

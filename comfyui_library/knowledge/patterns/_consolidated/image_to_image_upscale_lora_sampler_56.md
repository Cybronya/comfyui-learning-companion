---
name: image_to_image_upscale_lora_sampler_56
type: Image To Image
frequency: 4
level: weak
coverage: 0.945
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, Image Comparer (rgthree), ImageListToImageBatch, ImageScaleToTotalPixels, ImageUpscaleWithModel, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, ReferenceLatent, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy imageBatchToImageList]
problems: []
missing: []
members: [图片生成/图生图/目前最强KONTEXT老照片修复＋Wan2.2 - 14B - 高清细节放大，每个毛孔都能看见。_1958065955215724545.json, 平台全量/【提升皮肤细节】去除AI感 Kontext增加人像皮肤纹理 +wan2.2低噪放大_1981264523049033730.json, 平台全量/毛孔级真实皮肤质感添加 提升皮肤细节 去除AI感 Kontext增加人像皮肤纹理 +wan2.2_2010975539938463745.json, 平台全量/精修-人像摄影类-kontxet_1959138657032679425.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_56

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/目前最强KONTEXT老照片修复＋Wan2.2 - 14B - 高清细节放大，每个毛孔都能看见。_1958065955215724545.json、平台全量/【提升皮肤细节】去除AI感 Kontext增加人像皮肤纹理 +wan2.2低噪放大_1981264523049033730.json、平台全量/毛孔级真实皮肤质感添加 提升皮肤细节 去除AI感 Kontext增加人像皮肤纹理 +wan2.2_2010975539938463745.json、平台全量/精修-人像摄影类-kontxet_1959138657032679425.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `ImageListToImageBatch`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `ReferenceLatent`
- `SaveImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageBatchToImageList`

**可变部分**（部分 workflow 才有）：
- `FluxKontextImageScale` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `Float` —— 2/4 个有
- `ImpactInt` —— 2/4 个有
- `ConstrainImage|pysssss` —— 1/4 个有
- `ImageConcatMulti` —— 1/4 个有
- `ImageStitch` —— 1/4 个有
- `ShellAgentPluginOutputText` —— 1/4 个有
- `ShowText|pysssss` —— 1/4 个有
- `Text Multiline` —— 1/4 个有
- `YANC.ConcatStrings` —— 1/4 个有
- `easy imageToBase64` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 30 | 4 | 42% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | heun | - | 4 | 75% |
| 调度器 | beta | - | 4 | 75% |
| 重绘幅度 | 0.1 | 0.1 - 1 | 4 | 0% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 30，4 个样本，取值分散，一致性仅 42%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 heun，4 个样本，一致性 75%
- 调度器 最常用 beta，4 个样本，一致性 75%
- 重绘幅度 中位数 0.1，观测区间 0.1 - 1，4 个样本，取值分散，一致性仅 0%

---
name: text_to_image_upscale_sampler_clip_8
type: Text To Image
frequency: 13
level: weak
coverage: 0.897615
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, GetImageSize+, ImageResize+, ImageScaleBy, KSampler, ModelSamplingAuraFlow, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-Image文生图_2064637986431660033.json, 图片生成/文生图/Z-Image文生图在线8K直出处理工具_2101022161568878593.json, 图片生成/文生图/Z-Image文生图在线8K直出处理生成工具_2102132899192590337.json, 图片生成/文生图/Z-Image文生图超高清放大处理生成工具_2101767584369700866.json, 图片生成/文生图/Z-Image文生图（_2003443734752706561.json, 图片生成/文生图/Z-Image文生图（_2039874309291778050.json, 图片生成/文生图/Z-Image文生图（可大尺度）_2004890910724943874.json, 图片生成/文生图/Z-Image文生图｜写实人像出图再超高清放大细节拉满_2101540955382960129.json, 图片生成/文生图/Z-Image生图超清8K—阿浩_2039872802718752770.json, 图片生成/文生图/一键生成文生图｜Z-Image在线8K直出_2095597425204482049.json, 图片生成/文生图/文生图Z-Image在线8K直出工作流｜高清放大一步到位出大图_2101928584578424833.json, 图片生成/文生图/文生图在线8K直出｜Z-Image一键高清放大生成_2095842600501735425.json, 图片生成/文生图/自动优化提示词洗图｜文生图+图生图反推提示词工作流_2089378084058394625.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_8

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/文生图/Z-Image文生图_2064637986431660033.json、图片生成/文生图/Z-Image文生图在线8K直出处理工具_2101022161568878593.json、图片生成/文生图/Z-Image文生图在线8K直出处理生成工具_2102132899192590337.json、图片生成/文生图/Z-Image文生图超高清放大处理生成工具_2101767584369700866.json、图片生成/文生图/Z-Image文生图（_2003443734752706561.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `GetImageSize+`
- `ImageResize+`
- `ImageScaleBy`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
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
- `PreviewImage` —— 12/13 个有
- `PrimitiveFloat` —— 10/13 个有
- `Text Multiline` —— 10/13 个有
- `LoraLoaderModelOnly` —— 9/13 个有
- `JjkText` —— 8/13 个有
- `solarL_SaveImagesToZip` —— 8/13 个有
- `孤海注释` —— 8/13 个有
- `DyPE_FLUX` —— 4/13 个有
- `CheckpointLoaderSimple` —— 3/13 个有
- `ConditioningZeroOut` —— 3/13 个有
- `ImageCASharpening+` —— 3/13 个有
- `KSamplerAdvanced` —— 3/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/13 个有
- `easy cleanGpuUsed` —— 3/13 个有
- `easy int` —— 3/13 个有
- `Int` —— 2/13 个有
- `DapaoImageAspectRatioResizeNode` —— 1/13 个有
- `DapaoImageCompressionNode` —— 1/13 个有
- `DapaoImageRatioLimitNode` —— 1/13 个有
- `DapaoSafeSaveImage` —— 1/13 个有
- `Dapao_LlamaChat` —— 1/13 个有
- `ImpactSwitch` —— 1/13 个有
- `LoadImage` —— 1/13 个有
- `Seed (rgthree)` —— 1/13 个有
- `easy positive` —— 1/13 个有
- `easy showAnything` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 9 | 13 | 63% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 13 | 46% |
| 采样算法 | er_sde | - | 13 | 62% |
| 调度器 | beta | - | 13 | 62% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |
| 宽度 | 80 | 80 - 1920 | 13 | 0% |
| 高度 | 80 | 80 - 1920 | 13 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 9，13 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，13 个样本，取值分散，一致性仅 46%
- 采样算法 最常用 er_sde，13 个样本，一致性 62%
- 调度器 最常用 beta，13 个样本，一致性 62%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 1920，13 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1920，13 个样本，取值分散，一致性仅 0%
- 高发问题（18/13 个样本）：Steps较低可能导致细节不足

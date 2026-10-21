---
name: text_to_image_upscale_lora_sampler_2
type: Text To Image
frequency: 16
level: weak
coverage: 0.891813
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, GetImageSize+, ImageResize+, ImageScaleBy, KSampler, LoraLoaderModelOnly, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/图片放大图生图工作流｜低清小图秒变高清大图，细节无损放大_2107335691196788737.json, 图片生成/文生图/Z-Image一键文生图工作流｜8K直出人像写真特效生成_2097486456024559617.json, 图片生成/文生图/Z-Image在线8K直出_2003290778174685185.json, 图片生成/文生图/Z-Image在线8K直出_2058716850577563650.json, 图片生成/文生图/Z-Image在线8K直出_2072664211423064066.json, 图片生成/文生图/Z-Image在线8K直出_2072676192607629314.json, 图片生成/文生图/Z-Image在线8K直出_2073387571807342593.json, 图片生成/文生图/Z-Image在线8K直出_2073387973390983170.json, 图片生成/文生图/Z-Image在线8K直出_2081990378743484418.json, 图片生成/文生图/Z-Image在线8K直出_2081993328593301505.json, 图片生成/文生图/Z-Image文生图8K_2100484708844007425.json, 图片生成/文生图/Z-Image文生图在线8K直出处理工具_2101022161568878593.json, 图片生成/文生图/Z-Image文生图在线8K直出处理生成工具_2102132899192590337.json, 图片生成/文生图/Z-Image文生图超高清放大处理生成工具_2101767584369700866.json, 图片生成/文生图/Z-Image文生图｜写实人像出图再超高清放大细节拉满_2101540955382960129.json, 图片生成/文生图/自动优化提示词洗图｜文生图+图生图反推提示词工作流_2089378084058394625.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_2

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/图生图/图片放大图生图工作流｜低清小图秒变高清大图，细节无损放大_2107335691196788737.json、图片生成/文生图/Z-Image一键文生图工作流｜8K直出人像写真特效生成_2097486456024559617.json、图片生成/文生图/Z-Image在线8K直出_2003290778174685185.json、图片生成/文生图/Z-Image在线8K直出_2058716850577563650.json、图片生成/文生图/Z-Image在线8K直出_2072664211423064066.json…）

- **类型**：Text To Image
- **样本数**：16
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 16 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `GetImageSize+`
- `ImageResize+`
- `ImageScaleBy`
- `KSampler`
- `LoraLoaderModelOnly`
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
- `ModelSamplingAuraFlow` —— 15/16 个有
- `PreviewImage` —— 14/16 个有
- `PrimitiveFloat` —— 12/16 个有
- `Text Multiline` —— 12/16 个有
- `JjkText` —— 7/16 个有
- `solarL_SaveImagesToZip` —— 7/16 个有
- `孤海注释` —— 7/16 个有
- `LoadImage` —— 4/16 个有
- `easy cleanGpuUsed` —— 4/16 个有
- `CheckpointLoaderSimple` —— 3/16 个有
- `ConditioningZeroOut` —— 3/16 个有
- `ImageCASharpening+` —— 3/16 个有
- `KSamplerAdvanced` —— 3/16 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/16 个有
- `easy int` —— 3/16 个有
- `DapaoImageAspectRatioResizeNode` —— 1/16 个有
- `DapaoImageCompressionNode` —— 1/16 个有
- `DapaoImageRatioLimitNode` —— 1/16 个有
- `DapaoSafeSaveImage` —— 1/16 个有
- `Dapao_LlamaChat` —— 1/16 个有
- `ImpactSwitch` —— 1/16 个有
- `Int` —— 1/16 个有
- `LayerUtility: PurgeVRAM V2` —— 1/16 个有
- `SaveImageJPG_GH` —— 1/16 个有
- `Seed (rgthree)` —— 1/16 个有
- `easy clearCacheAll` —— 1/16 个有
- `easy positive` —— 1/16 个有
- `easy showAnything` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 80 - 1080 | 16 | 23% |
| 高度 | 1920 | 80 - 1920 | 16 | 18% |
| 采样步数 | 9 | 4 - 9 | 16 | 64% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 16 | 31% |
| 采样算法 | euler | - | 16 | 56% |
| 调度器 | sgm_uniform | - | 16 | 56% |
| 重绘幅度 | 1 | 1 - 1 | 16 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 19/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1080，观测区间 80 - 1080，16 个样本，取值分散，一致性仅 23%
- 高度 中位数 1920，观测区间 80 - 1920，16 个样本，取值分散，一致性仅 18%
- 采样步数 中位数 9，观测区间 4 - 9，16 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，16 个样本，取值分散，一致性仅 31%
- 采样算法 最常用 euler，16 个样本，一致性 56%
- 调度器 最常用 sgm_uniform，16 个样本，一致性 56%
- 重绘幅度 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 高发问题（19/16 个样本）：Steps较低可能导致细节不足

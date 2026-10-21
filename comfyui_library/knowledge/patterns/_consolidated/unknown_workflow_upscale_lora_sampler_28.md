---
name: unknown_workflow_upscale_lora_sampler_28
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.900667
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetImageSize+, ImageResize+, ImageScaleBy, KSamplerAdvanced, LoraLoaderModelOnly, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/VividMuse真实人像摄影V1_2015351994625564673.json, 图片生成/文生图/VividMuse真实人像摄影V2_2021926025617219585.json, 图片生成/文生图/Z-Image + Z-Image-Turbo realistic photography V3_2057641945413017602.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_28

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/VividMuse真实人像摄影V1_2015351994625564673.json、图片生成/文生图/VividMuse真实人像摄影V2_2021926025617219585.json、图片生成/文生图/Z-Image + Z-Image-Turbo realistic photography V3_2057641945413017602.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize+`
- `ImageResize+`
- `ImageScaleBy`
- `KSamplerAdvanced`
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
- `DF_Text_Box` —— 2/3 个有
- `Image Comparer (rgthree)` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `easy promptList` —— 2/3 个有
- `CFGGuider` —— 1/3 个有
- `Flux2Scheduler` —— 1/3 个有
- `KSamplerSelect` —— 1/3 个有
- `LayerColor: ColorAdapter` —— 1/3 个有
- `ModelSamplingAuraFlow` —— 1/3 个有
- `RandomNoise` —— 1/3 个有
- `ReferenceLatent` —— 1/3 个有
- `SamplerCustomAdvanced` —— 1/3 个有
- `Seed (rgthree)` —— 1/3 个有
- `VAEEncode` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1536 | 1536 - 1536 | 3 | 100% |
| 高度 | 2048 | 2048 - 2048 | 3 | 100% |
| 采样步数 | fixed | - | 3 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 10 | 3 | 89% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | er_sde | - | 3 | 33% |
| 重绘幅度 | kl_optimal | - | 3 | 33% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1536，观测区间 1536 - 1536，3 个样本，取值集中（一致性 100%）
- 高度 中位数 2048，观测区间 2048 - 2048，3 个样本，取值集中（一致性 100%）
- 采样步数 最常用 fixed，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 10，3 个样本，取值集中（一致性 89%）
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 er_sde，3 个样本，一致性 33%
- 重绘幅度 最常用 kl_optimal，3 个样本，一致性 33%

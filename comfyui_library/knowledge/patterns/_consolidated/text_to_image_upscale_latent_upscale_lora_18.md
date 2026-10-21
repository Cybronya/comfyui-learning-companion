---
name: text_to_image_upscale_latent_upscale_lora_18
type: Text To Image
frequency: 3
level: weak
coverage: 0.864333
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, ColorMatchV2, ConditioningZeroOut, Dapao_LlamaCaption, Dapao_LlamaCaptionOptions, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetImageSize, GetImageSize+, ImageScaleToTotalPixels, KSampler, KSamplerAdvanced, LatentUpscaleBy, LoadImage, LoraLoaderModelOnly, PreviewImage, PrimitiveFloat, SaveImage, Seed (rgthree), SimpleMathDual+, UNETLoader, UltimateSDUpscale, UpscaleModelLoader, VAEDecode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/krea2基础工作流文生图工作流_2103772691600863234.json, 图片生成/文生图/krea2基础工作流文生图｜新手友好 文生图入门首选稳定出图_2104092597185765378.json, 图片生成/文生图/krea2基础文生图工作流 新手友好稳定出图_2104327470160896001.json]
source: knowledge_consolidation
---

# text_to_image_upscale_latent_upscale_lora_18

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/krea2基础工作流文生图工作流_2103772691600863234.json、图片生成/文生图/krea2基础工作流文生图｜新手友好 文生图入门首选稳定出图_2104092597185765378.json、图片生成/文生图/krea2基础文生图工作流 新手友好稳定出图_2104327470160896001.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ColorMatchV2`
- `ConditioningZeroOut`
- `Dapao_LlamaCaption`
- `Dapao_LlamaCaptionOptions`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize`
- `GetImageSize+`
- `ImageScaleToTotalPixels`
- `KSampler`
- `KSamplerAdvanced`
- `LatentUpscaleBy`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `PrimitiveFloat`
- `SaveImage`
- `Seed (rgthree)`
- `SimpleMathDual+`
- `UNETLoader`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 2/3 个有
- `solarL_SaveImagesToZip` —— 2/3 个有
- `孤海注释` —— 2/3 个有
- `Label (rgthree)` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 1080 | 3 | 0% |
| 高度 | 80 | 80 - 1440 | 3 | 0% |
| 采样步数 | 4 | 4 - 10 | 3 | 53% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 3 | 51% |
| 采样算法 | er_sde | - | 3 | 67% |
| 调度器 | beta | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 1080，3 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1440，3 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 4，观测区间 4 - 10，3 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，3 个样本
- 采样算法 最常用 er_sde，3 个样本，一致性 67%
- 调度器 最常用 beta，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足

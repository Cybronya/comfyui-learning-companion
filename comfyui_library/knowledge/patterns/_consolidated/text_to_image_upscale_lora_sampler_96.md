---
name: text_to_image_upscale_lora_sampler_96
type: Text To Image
frequency: 3
level: weak
coverage: 0.898333
common_nodes: [CLIPLoader, CLIPTextEncode, DF_Integer, EmptyLatentImage, Fast Groups Bypasser (rgthree), Fast Groups Muter (rgthree), KSampler, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2-Turbo+ LoRA文生图高清放大2K直出工作流（W版本）懂的都懂_2101631409948545026.json, 图片生成/文生图/Krea2-Turbo+LoRA文生图高清放大2K直出｜W版本人像写真商单利器_2101877172779708417.json, 图片生成/文生图/Z-Image Turbo+LoRA文生图高清放大2K直出处理工作流_2102187279212171265.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_96

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Krea2-Turbo+ LoRA文生图高清放大2K直出工作流（W版本）懂的都懂_2101631409948545026.json、图片生成/文生图/Krea2-Turbo+LoRA文生图高清放大2K直出｜W版本人像写真商单利器_2101877172779708417.json、图片生成/文生图/Z-Image Turbo+LoRA文生图高清放大2K直出处理工作流_2102187279212171265.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `DF_Integer`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Muter (rgthree)`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CompressImages` —— 2/3 个有
- `JjkText` —— 2/3 个有
- `ResolutionSelector` —— 2/3 个有
- `solarL_SaveImagesToZip` —— 2/3 个有
- `孤海注释` —— 2/3 个有
- `EmptySD3LatentImage` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 1024 | 3 | 0% |
| 高度 | 80 | 80 - 1024 | 3 | 0% |
| 采样步数 | 4 | 4 - 37 | 3 | 0% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 3 | 51% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 1024，3 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1024，3 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 4，观测区间 4 - 37，3 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，3 个样本
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足

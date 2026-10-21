---
name: text_to_image_lora_sampler_clip_262
type: Text To Image
frequency: 4
level: weak
coverage: 0.906
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2-Turbo+ LoRA文生图高清放大2K直出工作流（W版本）懂的都懂_2101631409948545026.json, 图片生成/文生图/Krea2-Turbo+LoRA文生图高清放大2K直出｜W版本人像写真商单利器_2101877172779708417.json, 图片生成/文生图/Krea2人像写真｜古装汉服肚兜美少女文生图_2101186021638627329.json, 图片生成/文生图/Z-Image Turbo+LoRA文生图高清放大2K直出处理工作流_2102187279212171265.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_262

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Krea2-Turbo+ LoRA文生图高清放大2K直出工作流（W版本）懂的都懂_2101631409948545026.json、图片生成/文生图/Krea2-Turbo+LoRA文生图高清放大2K直出｜W版本人像写真商单利器_2101877172779708417.json、图片生成/文生图/Krea2人像写真｜古装汉服肚兜美少女文生图_2101186021638627329.json、图片生成/文生图/Z-Image Turbo+LoRA文生图高清放大2K直出处理工作流_2102187279212171265.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CompressImages` —— 3/4 个有
- `DF_Integer` —— 3/4 个有
- `Fast Groups Bypasser (rgthree)` —— 3/4 个有
- `Fast Groups Muter (rgthree)` —— 3/4 个有
- `JjkText` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `LayerUtility: PurgeVRAM` —— 3/4 个有
- `ResolutionSelector` —— 3/4 个有
- `SeedVR2LoadDiTModel` —— 3/4 个有
- `SeedVR2LoadVAEModel` —— 3/4 个有
- `SeedVR2VideoUpscaler` —— 3/4 个有
- `solarL_SaveImagesToZip` —— 3/4 个有
- `孤海注释` —— 3/4 个有
- `EmptySD3LatentImage` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 1024 | 4 | 0% |
| 高度 | 80 | 80 - 1024 | 4 | 0% |
| 采样步数 | 4 | 4 - 37 | 4 | 0% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 4 | 58% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 1024，4 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1024，4 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 4，观测区间 4 - 37，4 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，4 个样本
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（5/4 个样本）：Steps较低可能导致细节不足

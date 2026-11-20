---
name: text_to_image_upscale_sampler_clip_12
type: Text To Image
frequency: 9
level: moderate
coverage: 0.964222
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Flux2-Klein9B文生图-洱海风光风景直出2k版_2026827912795660290.json, 图片生成/文生图/Flux2-Klein9B文生图_2012412464368979970.json, 图片生成/文生图/Krea2 - 2K Ultra-clear details_2093616734757543938.json, 图片生成/文生图/Krea2 - 2K Ultra-clear details_2095547125550641153.json, 图片生成/文生图/Krea2-色彩HDR增强VAE+自动调色-增强色彩减轻黄色_2074182890568634369.json, 图片生成/文生图/Krea2文生图4K直出-红潮版_2071083324155711489.json, 图片生成/文生图/Krea2文生图4K直出-红潮版_2072617534146306050.json, 平台全量/AI影视角色资产_2079405580334231553.json, 平台全量/Krea2文生图4K直出_2069705450572046338.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_12

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/Flux2-Klein9B文生图-洱海风光风景直出2k版_2026827912795660290.json、图片生成/文生图/Flux2-Klein9B文生图_2012412464368979970.json、图片生成/文生图/Krea2 - 2K Ultra-clear details_2093616734757543938.json、图片生成/文生图/Krea2 - 2K Ultra-clear details_2095547125550641153.json、图片生成/文生图/Krea2-色彩HDR增强VAE+自动调色-增强色彩减轻黄色_2074182890568634369.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 8/9 个有
- `CR Text` —— 7/9 个有
- `ConditioningZeroOut` —— 7/9 个有
- `LoadImage` —— 5/9 个有
- `TTResolutionSelector` —— 5/9 个有
- `Fast Groups Bypasser (rgthree)` —— 4/9 个有
- `ComfyUI-Krea2T-Enhancer` —— 3/9 个有
- `JWInteger` —— 2/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/9 个有
- `LayerUtility: PurgeVRAM` —— 2/9 个有
- `ReroutePrimitive|pysssss` —— 2/9 个有
- `HAIGC_SaveImagesToZip` —— 1/9 个有
- `LayerColor: AutoAdjustV2` —— 1/9 个有
- `PreviewImage` —— 1/9 个有
- `RH_RhartImageG2ImageToImage` —— 1/9 个有
- `ZML_ImageEncryption` —— 1/9 个有
- `easy int` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 1080 | 9 | 65% |
| 高度 | 512 | 512 - 1920 | 9 | 42% |
| 采样步数 | 8 | 6 - 9 | 9 | 87% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 56% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 1080，9 个样本
- 高度 中位数 512，观测区间 512 - 1920，9 个样本，取值分散，一致性仅 42%
- 采样步数 中位数 8，观测区间 6 - 9，9 个样本，取值集中（一致性 87%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 56%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足

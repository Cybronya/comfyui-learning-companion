---
name: image_to_image_upscale_sampler_clip_50
type: Image To Image
frequency: 2
level: weak
coverage: 0.85
common_nodes: [AILab_QwenVL, CLIPLoader, CLIPTextEncode, DF_Integer, Fast Groups Bypasser (rgthree), Get resolution [Crystools], Image Comparer (rgthree), ImageCASharpening+, ImageFromBatch, ImageResize+, ImageScaleBy, ImageUpscaleWithModel, ImpactMakeAnyList, ImpactMinMax, Int, JWFloat, KSampler, Label (rgthree), Latent Noise Injection, LayerUtility: PurgeVRAM V2, LoadImage, PreviewImage, SaveImage, SeedVR2, SimpleMath+, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UltimateSDUpscaleNoUpscale, Upscale Model Loader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy imageSize, easy int]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/增强真实感增强质感去ai感2.0_2013168387253342210.json, 数字人/数字人/增强真实感增强质感去ai感2.0_2027208631271301121.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_clip_50

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/增强真实感增强质感去ai感2.0_2013168387253342210.json、数字人/数字人/增强真实感增强质感去ai感2.0_2027208631271301121.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `AILab_QwenVL`
- `CLIPLoader`
- `CLIPTextEncode`
- `DF_Integer`
- `Fast Groups Bypasser (rgthree)`
- `Get resolution [Crystools]`
- `Image Comparer (rgthree)`
- `ImageCASharpening+`
- `ImageFromBatch`
- `ImageResize+`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `ImpactMakeAnyList`
- `ImpactMinMax`
- `Int`
- `JWFloat`
- `KSampler`
- `Label (rgthree)`
- `Latent Noise Injection`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `SeedVR2`
- `SimpleMath+`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UltimateSDUpscaleNoUpscale`
- `Upscale Model Loader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageSize`
- `easy int`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 2 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | er_sde | - | 2 | 100% |
| 调度器 | sgm_uniform | - | 2 | 100% |
| 重绘幅度 | 0.15 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 2，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，2 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，2 个样本，一致性 100%
- 重绘幅度 中位数 0.15，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（4/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

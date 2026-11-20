---
name: text_to_image_lora_sampler_clip_557
type: Text To Image
frequency: 3
level: strong
coverage: 0.907
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, Get Image Size, Image Comparer (rgthree), ImageResize+, ImpactMinMax, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, SeedVR2, SimpleMath+, TTP_Image_Assy, TTP_Image_Tile_Batch, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/原图直出高清放大｜无损画质增强细节修复工具_2093513755102638082.json, 图片生成/图生图/原图直出高清放大｜无损画质增强细节修复工具_2093612059454955521.json, 平台全量/SeedVR2万物放大｜文字人像分块加噪点4K_8K画质修复_2094375585119293441.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_557

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/原图直出高清放大｜无损画质增强细节修复工具_2093513755102638082.json、图片生成/图生图/原图直出高清放大｜无损画质增强细节修复工具_2093612059454955521.json、平台全量/SeedVR2万物放大｜文字人像分块加噪点4K_8K画质修复_2094375585119293441.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Get Image Size`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImpactMinMax`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `SeedVR2`
- `SimpleMath+`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `DF_Integer` —— 2/3 个有
- `ImageColorMatchAdobe+` —— 2/3 个有
- `SeedVR2BlockSwap` —— 2/3 个有
- `ImageAddNoise` —— 1/3 个有
- `ImageCASharpening+` —— 1/3 个有
- `ImpactInt` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有
- `孤海注释` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足

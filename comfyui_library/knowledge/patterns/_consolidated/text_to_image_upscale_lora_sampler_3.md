---
name: text_to_image_upscale_lora_sampler_3
type: Text To Image
frequency: 11
level: weak
coverage: 0.982636
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, ImageResize+, ImageScaleBy, KSampler, LoraLoaderModelOnly, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Kook_Krea2_真实幻想 文生图_2106733963392933890.json, 图片生成/文生图/Kook_Krea2_真实幻想 文生图_2106746181916389377.json, 图片生成/文生图/Kook_Krea2_真实幻想_2106672348467392513.json, 图片生成/文生图/Kook_Krea2真实幻想文生图｜写实美少女一键生成_2106936425173315586.json, 图片生成/文生图/krea2基础文生图高清_2102596196979269634.json, 图片生成/文生图/艺术人像摄影-Zimage_4K如梦似幻_2102918572434616322.json, 图片生成/文生图/艺术人像摄影-Zimage_4K如梦似幻_2104375192104562690.json, 图片生成/文生图/艺术人像摄影-Zimage_4K如梦似幻_2104497308594434049.json, 视频生成/图生视频/艺术人像摄影-Zimage_4K_2085548054337380353.json, 视频生成/图生视频/艺术人像摄影-Zimage_Kook版 (2)_2085250585183477762.json, 视频生成/图生视频/艺术人像摄影-Zimage__2084823694760833026.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_3

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/Kook_Krea2_真实幻想 文生图_2106733963392933890.json、图片生成/文生图/Kook_Krea2_真实幻想 文生图_2106746181916389377.json、图片生成/文生图/Kook_Krea2_真实幻想_2106672348467392513.json、图片生成/文生图/Kook_Krea2真实幻想文生图｜写实美少女一键生成_2106936425173315586.json、图片生成/文生图/krea2基础文生图高清_2102596196979269634.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：98%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
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
- `GetImageSize+` —— 10/11 个有
- `ImageCASharpening+` —— 10/11 个有
- `PhotoShakeNode` —— 10/11 个有
- `RunningHub Deepcleaner` —— 10/11 个有
- `CR Text` —— 6/11 个有
- `ConditioningZeroOut` —— 5/11 个有
- `FastFilmGrain` —— 4/11 个有
- `PreviewImage` —— 2/11 个有
- `EmptyImage` —— 1/11 个有
- `GetNode` —— 1/11 个有
- `Image Comparer (rgthree)` —— 1/11 个有
- `JjkText` —— 1/11 个有
- `easy cleanGpuUsed` —— 1/11 个有
- `easy imageSize` —— 1/11 个有
- `solarL_SaveImagesToZip` —— 1/11 个有
- `孤海注释` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 80 - 1080 | 11 | 71% |
| 高度 | 1384 | 80 - 1920 | 11 | 64% |
| 采样步数 | 8 | 4 - 50 | 11 | 0% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 11 | 21% |
| 采样算法 | res_2s_ode | - | 11 | 55% |
| 调度器 | bong_tangent | - | 11 | 55% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1080，观测区间 80 - 1080，11 个样本
- 高度 中位数 1384，观测区间 80 - 1920，11 个样本
- 采样步数 中位数 8，观测区间 4 - 50，11 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，11 个样本，取值分散，一致性仅 21%
- 采样算法 最常用 res_2s_ode，11 个样本，一致性 55%
- 调度器 最常用 bong_tangent，11 个样本，一致性 55%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（12/11 个样本）：Steps较低可能导致细节不足

---
name: text_to_image_upscale_lora_sampler_6
type: Text To Image
frequency: 10
level: moderate
coverage: 0.9355
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, GetImageSize+, ImageResize+, ImageScaleBy, KSampler, LoraLoaderModelOnly, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/KOOK_Qwen_2512_真实人像_2006334912823037953.json, 图片生成/文生图/Kook_Krea2_真实幻想 文生图_2106733963392933890.json, 图片生成/文生图/Kook_Krea2_真实幻想 文生图_2106746181916389377.json, 图片生成/文生图/Kook_Krea2_真实幻想_2106672348467392513.json, 图片生成/文生图/Kook_Krea2真实幻想文生图｜写实美少女一键生成_2106936425173315586.json, 图片生成/文生图/Kook_Krea2真实幻想文生图｜写实美少女一键生成_2107645221126369282.json, 图片生成/文生图/Kook_Zimage_瑶光_2072528894925819906.json, 图片生成/文生图/Qwen Image 2512 Kook 真实人像文生图V1_2008514200146022401.json, 图片生成/文生图/Qwen Image 2512 Kook 真实人像文生图V1_2009133925792227330.json, 图片生成/文生图/无Ai感超强文生图_2076312965044858881.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_6

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/KOOK_Qwen_2512_真实人像_2006334912823037953.json、图片生成/文生图/Kook_Krea2_真实幻想 文生图_2106733963392933890.json、图片生成/文生图/Kook_Krea2_真实幻想 文生图_2106746181916389377.json、图片生成/文生图/Kook_Krea2_真实幻想_2106672348467392513.json、图片生成/文生图/Kook_Krea2真实幻想文生图｜写实美少女一键生成_2106936425173315586.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `GetImageSize+`
- `ImageResize+`
- `ImageScaleBy`
- `KSampler`
- `LoraLoaderModelOnly`
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
- `FastFilmGrain` —— 7/10 个有
- `ImageCASharpening+` —— 7/10 个有
- `RunningHub Deepcleaner` —— 7/10 个有
- `SaveImage` —— 7/10 个有
- `PreviewImage` —— 6/10 个有
- `ConditioningZeroOut` —— 5/10 个有
- `KOOK_SaveJPGImage` —— 5/10 个有
- `PhotoShakeNode` —— 5/10 个有
- `KOOK_ImageCompression` —— 3/10 个有
- `ModelSamplingAuraFlow` —— 3/10 个有
- `JjkText` —— 2/10 个有
- `LatentFrequencyEnhancer_lrzjason` —— 2/10 个有
- `LayerColor: BrightnessContrastV2` —— 2/10 个有
- `solarL_SaveImagesToZip` —— 2/10 个有
- `EmptyImage` —— 1/10 个有
- `Int` —— 1/10 个有
- `MultiLinePromptIndex` —— 1/10 个有
- `孤海注释` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 80 - 1080 | 10 | 55% |
| 高度 | 1920 | 80 - 1920 | 10 | 53% |
| 采样步数 | 8 | 4 - 8 | 10 | 78% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 10 | 18% |
| 采样算法 | res_2s | - | 10 | 50% |
| 调度器 | sgm_uniform | - | 10 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1080，观测区间 80 - 1080，10 个样本
- 高度 中位数 1920，观测区间 80 - 1920，10 个样本
- 采样步数 中位数 8，观测区间 4 - 8，10 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，10 个样本，取值分散，一致性仅 18%
- 采样算法 最常用 res_2s，10 个样本，一致性 50%
- 调度器 最常用 sgm_uniform，10 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（12/10 个样本）：Steps较低可能导致细节不足

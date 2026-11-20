---
name: text_to_image_upscale_lora_sampler_11
type: Text To Image
frequency: 15
level: moderate
coverage: 0.916333
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, GetImageSize+, ImageResize+, ImageScaleBy, KOOK_SaveJPGImage, KSampler, LoraLoaderModelOnly, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/分镜 视图控制 洗图  qwen_image_edit_2511_2046871547033423873.json, 图片生成/图生图/反推提示词 洗图重绘 qwen_image_edit_2511_2043561405831450626.json, 图片生成/图生图/洗图 反推提示词 qwen_image_edit_2511_2043567074399752194.json, 图片生成/图生图/洗图 重绘 反推 提示词 qwen_image_edit_2511_2043567288124706817.json, 图片生成/图生图/角度控制  角度控制器  洗图重绘 qwen_image_edit_2511_2095374472785260546.json, 图片生成/图生图/角度控制_角度控制器_洗图重绘_qwen_image_edit_2511_2096499497357631490.json, 图片生成/图生图/角度控制_角度控制器_洗图重绘_qwen_image_edit_2511_2096802685046575105.json, 图片生成/文生图/KOOK_Qwen_2512_真实人像_2006334912823037953.json, 图片生成/文生图/Kook_Zimage  最接近真实照片效果的LORA_2034909895190913025.json, 图片生成/文生图/Kook_Zimage_瑶光_2072528894925819906.json, 图片生成/文生图/Qwen Image 2512 Kook 真实人像文生图V1_2008514200146022401.json, 图片生成/文生图/Qwen Image 2512 Kook 真实人像文生图V1_2009133925792227330.json, 图片生成/文生图/Z-image 真实照片效果_2037377240018722818.json, 图片生成/文生图/Zimage超级真实人像_2052365553586712578.json, 图片生成/文生图/（Kook版-贞贞lora）Z-Image-Base文生图+高清化_2035938949620830209.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_11

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/图生图/分镜 视图控制 洗图  qwen_image_edit_2511_2046871547033423873.json、图片生成/图生图/反推提示词 洗图重绘 qwen_image_edit_2511_2043561405831450626.json、图片生成/图生图/洗图 反推提示词 qwen_image_edit_2511_2043567074399752194.json、图片生成/图生图/洗图 重绘 反推 提示词 qwen_image_edit_2511_2043567288124706817.json、图片生成/图生图/角度控制  角度控制器  洗图重绘 qwen_image_edit_2511_2095374472785260546.json…）

- **类型**：Text To Image
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `GetImageSize+`
- `ImageResize+`
- `ImageScaleBy`
- `KOOK_SaveJPGImage`
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
- `ImageCASharpening+` —— 12/15 个有
- `PreviewImage` —— 12/15 个有
- `RunningHub Deepcleaner` —— 12/15 个有
- `SaveImage` —— 12/15 个有
- `LayerUtility: ImageReel` —— 7/15 个有
- `LayerUtility: ImageReelComposit` —— 7/15 个有
- `LoadImage` —— 7/15 个有
- `QwenMultiangleCameraNode` —— 7/15 个有
- `TextEncodeQwenImageEditPlus` —— 7/15 个有
- `easy imageSize` —— 7/15 个有
- `FastFilmGrain` —— 5/15 个有
- `LayerColor: BrightnessContrastV2` —— 5/15 个有
- `KOOK_ImageCompression` —— 3/15 个有
- `ModelSamplingAuraFlow` —— 3/15 个有
- `LatentFrequencyEnhancer_lrzjason` —— 2/15 个有
- `HAIGC_SaveImagesToZip` —— 1/15 个有
- `Int` —— 1/15 个有
- `MultiLinePromptIndex` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1280 | 1080 - 1920 | 15 | 83% |
| 高度 | 1080 | 720 - 1920 | 15 | 55% |
| 采样步数 | 8 | 8 - 20 | 15 | 66% |
| Prompt 约束强度(CFG) | 1 | 1 - 1.5 | 15 | 88% |
| 采样算法 | res_2s | - | 15 | 53% |
| 调度器 | beta57 | - | 15 | 47% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1280，观测区间 1080 - 1920，15 个样本，取值集中（一致性 83%）
- 高度 中位数 1080，观测区间 720 - 1920，15 个样本
- 采样步数 中位数 8，观测区间 8 - 20，15 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1.5，15 个样本，取值集中（一致性 88%）
- 采样算法 最常用 res_2s，15 个样本，一致性 53%
- 调度器 最常用 beta57，15 个样本，一致性 47%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 高发问题（14/15 个样本）：Steps较低可能导致细节不足

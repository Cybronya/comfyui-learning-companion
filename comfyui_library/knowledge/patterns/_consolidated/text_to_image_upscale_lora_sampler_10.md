---
name: text_to_image_upscale_lora_sampler_10
type: Text To Image
frequency: 13
level: weak
coverage: 0.954538
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, GetImageSize+, ImageCASharpening+, ImageResize+, ImageScaleBy, KSampler, LoraLoaderModelOnly, RunningHub Deepcleaner, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/分镜 视图控制 洗图  qwen_image_edit_2511_2046871547033423873.json, 图片生成/图生图/反推提示词 洗图重绘 qwen_image_edit_2511_2043561405831450626.json, 图片生成/图生图/洗图 反推提示词 qwen_image_edit_2511_2043567074399752194.json, 图片生成/图生图/洗图 重绘 反推 提示词 qwen_image_edit_2511_2043567288124706817.json, 图片生成/图生图/角度控制  角度控制器  洗图重绘 qwen_image_edit_2511_2095374472785260546.json, 图片生成/图生图/角度控制_角度控制器_洗图重绘_qwen_image_edit_2511_2096499497357631490.json, 图片生成/图生图/角度控制_角度控制器_洗图重绘_qwen_image_edit_2511_2096802685046575105.json, 图片生成/文生图/Kook_Krea2_真实幻想 文生图_2106733963392933890.json, 图片生成/文生图/Kook_Krea2_真实幻想 文生图_2106746181916389377.json, 图片生成/文生图/Kook_Krea2_真实幻想_2106672348467392513.json, 图片生成/文生图/Kook_Krea2真实幻想文生图｜写实美少女一键生成_2106936425173315586.json, 图片生成/文生图/Kook_Krea2真实幻想文生图｜写实美少女一键生成_2107645221126369282.json, 图片生成/文生图/Kook_Zimage_如梦似幻_2049613798604066818.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_10

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/分镜 视图控制 洗图  qwen_image_edit_2511_2046871547033423873.json、图片生成/图生图/反推提示词 洗图重绘 qwen_image_edit_2511_2043561405831450626.json、图片生成/图生图/洗图 反推提示词 qwen_image_edit_2511_2043567074399752194.json、图片生成/图生图/洗图 重绘 反推 提示词 qwen_image_edit_2511_2043567288124706817.json、图片生成/图生图/角度控制  角度控制器  洗图重绘 qwen_image_edit_2511_2095374472785260546.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `GetImageSize+`
- `ImageCASharpening+`
- `ImageResize+`
- `ImageScaleBy`
- `KSampler`
- `LoraLoaderModelOnly`
- `RunningHub Deepcleaner`
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
- `PreviewImage` —— 8/13 个有
- `KOOK_SaveJPGImage` —— 7/13 个有
- `LayerUtility: ImageReel` —— 7/13 个有
- `LayerUtility: ImageReelComposit` —— 7/13 个有
- `LoadImage` —— 7/13 个有
- `QwenMultiangleCameraNode` —— 7/13 个有
- `TextEncodeQwenImageEditPlus` —— 7/13 个有
- `easy imageSize` —— 7/13 个有
- `PhotoShakeNode` —— 6/13 个有
- `ConditioningZeroOut` —— 5/13 个有
- `FastFilmGrain` —— 5/13 个有
- `JjkText` —— 2/13 个有
- `solarL_SaveImagesToZip` —— 2/13 个有
- `EmptyImage` —— 1/13 个有
- `孤海注释` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1280 | 80 - 1280 | 13 | 60% |
| 高度 | 720 | 80 - 1920 | 13 | 34% |
| 采样步数 | 8 | 4 - 8 | 13 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 13 | 18% |
| 采样算法 | euler | - | 13 | 54% |
| 调度器 | beta57 | - | 13 | 54% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1280，观测区间 80 - 1280，13 个样本
- 高度 中位数 720，观测区间 80 - 1920，13 个样本，取值分散，一致性仅 34%
- 采样步数 中位数 8，观测区间 4 - 8，13 个样本，取值集中（一致性 80%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，13 个样本，取值分散，一致性仅 18%
- 采样算法 最常用 euler，13 个样本，一致性 54%
- 调度器 最常用 beta57，13 个样本，一致性 54%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 高发问题（15/13 个样本）：Steps较低可能导致细节不足

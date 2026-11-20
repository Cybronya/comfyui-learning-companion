---
name: text_to_image_upscale_lora_sampler_18
type: Text To Image
frequency: 12
level: weak
coverage: 0.94375
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, GetImageSize+, ImageResize+, ImageScaleBy, KSampler, LoraLoaderModelOnly, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/人像写真丨Krea 2 Turbo＋SeedVR2丨文生图·分块精修_2112107671942950914.json, 图片生成/图生图/超级简单+一键生成-文生图+Z-Image在线8K直出_2079719986809102338.json, 图片生成/文生图/8K究极高清图像极速直出(异域风情性感比基尼)_20款任你挑选_2038860113427042305.json, 图片生成/文生图/Kook_Krea2_真实幻想 文生图_2106733963392933890.json, 图片生成/文生图/Kook_Krea2_真实幻想 文生图_2106746181916389377.json, 图片生成/文生图/Kook_Krea2_真实幻想_2106672348467392513.json, 图片生成/文生图/Kook_Krea2真实幻想文生图｜写实美少女一键生成_2106936425173315586.json, 图片生成/文生图/Kook_Krea2真实幻想文生图｜写实美少女一键生成_2107645221126369282.json, 图片生成/文生图/Z-Image一键文生图工作流｜8K直出人像写真特效生成_2097486456024559617.json, 图片生成/文生图/Z-Image文生图8K_2100484708844007425.json, 图片生成/文生图/艺术人像摄影文生图｜Z-Image Kook版人像写真生成_2097469971596140545.json, 图片生成/文生图/超级简单一键文生图｜Z-Image在线8K直出小白也能跑_2112936127370981378.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_18

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/人像写真丨Krea 2 Turbo＋SeedVR2丨文生图·分块精修_2112107671942950914.json、图片生成/图生图/超级简单+一键生成-文生图+Z-Image在线8K直出_2079719986809102338.json、图片生成/文生图/8K究极高清图像极速直出(异域风情性感比基尼)_20款任你挑选_2038860113427042305.json、图片生成/文生图/Kook_Krea2_真实幻想 文生图_2106733963392933890.json、图片生成/文生图/Kook_Krea2_真实幻想 文生图_2106746181916389377.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `GetImageSize+`
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
- `ImageCASharpening+` —— 7/12 个有
- `PhotoShakeNode` —— 7/12 个有
- `ConditioningZeroOut` —— 6/12 个有
- `FastFilmGrain` —— 6/12 个有
- `PreviewImage` —— 6/12 个有
- `RunningHub Deepcleaner` —— 6/12 个有
- `JjkText` —— 5/12 个有
- `ModelSamplingAuraFlow` —— 5/12 个有
- `Text Multiline` —— 5/12 个有
- `solarL_SaveImagesToZip` —— 5/12 个有
- `PrimitiveFloat` —— 4/12 个有
- `孤海注释` —— 4/12 个有
- `CR Text` —— 1/12 个有
- `ComfySwitchNode` —— 1/12 个有
- `EmptyImage` —— 1/12 个有
- `Float` —— 1/12 个有
- `GetImageSize` —— 1/12 个有
- `ImpactSwitch` —— 1/12 个有
- `easy cleanGpuUsed` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 80 - 1088 | 12 | 26% |
| 高度 | 1920 | 80 - 1920 | 12 | 21% |
| 采样步数 | 8 | 4 - 9 | 12 | 66% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 12 | 30% |
| 采样算法 | er_sde | - | 12 | 42% |
| 调度器 | sgm_uniform | - | 12 | 58% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1080，观测区间 80 - 1088，12 个样本，取值分散，一致性仅 26%
- 高度 中位数 1920，观测区间 80 - 1920，12 个样本，取值分散，一致性仅 21%
- 采样步数 中位数 8，观测区间 4 - 9，12 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，12 个样本，取值分散，一致性仅 30%
- 采样算法 最常用 er_sde，12 个样本，一致性 42%
- 调度器 最常用 sgm_uniform，12 个样本，一致性 58%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 高发问题（17/12 个样本）：Steps较低可能导致细节不足

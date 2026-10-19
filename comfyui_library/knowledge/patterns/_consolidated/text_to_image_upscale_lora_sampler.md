---
name: text_to_image_upscale_lora_sampler
type: Text To Image
frequency: 14
level: weak
coverage: 0.736286
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, INTConstant, ImageScaleToTotalPixels, KSampler, LoraLoaderModelOnly, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea-2 美学视觉文生图+SeedVR2高清出图_2101317926048587777.json, 图片生成/文生图/Krea-2_美学视觉文生图+SeedVR2高清出图_2107464959214055425.json, 图片生成/文生图/Z-image文生图批量工作流直出4K（动漫短剧资产生图抽卡专用）_2102674578551164929.json, 图片生成/文生图/【短剧最佳拍档】支持场景 _ 角色【AI创客训练营】画布功能 _ 角色_2103873978132688897.json, 图片生成/文生图/短剧最佳拍档AI创客训练营｜画布功能支持场景角色创作_2106237793725931522.json, 数字人/数字人/Krea2熟颜世绘Lora模型 写实美少女文生图风格化生成_2099181814492524545.json, 数字人/数字人/krea2熟颜世绘｜尺素数字人文生图美少女生成_2091288163825311745.json, 数字人/数字人/ziamge-【短剧最佳拍档】支持场景 _ 角色_2088664389393145858.json, 数字人/数字人/【尺素】krea2 熟颜世绘_2078697317879865345.json, 数字人/数字人/尺素出品krea2熟颜世绘｜美少女文生图有味道，质感细腻很出片_2099462000886771713.json, 视频生成/图生视频/【最佳短剧生成】支持场景 _ 角色_2098744968851578881.json, 视频生成/图生视频/2067180332339785729.json, 视频生成/图生视频/【短剧最佳拍档】支持场景 _ 角色【AI创客训练营】画布功能 _ 角色_2103873978132688897.json, 视频生成/图生视频/短剧最佳拍档AI创客训练营｜画布功能支持场景角色创作_2106237793725931522.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/文生图/Krea-2 美学视觉文生图+SeedVR2高清出图_2101317926048587777.json、图片生成/文生图/Krea-2_美学视觉文生图+SeedVR2高清出图_2107464959214055425.json、图片生成/文生图/Z-image文生图批量工作流直出4K（动漫短剧资产生图抽卡专用）_2102674578551164929.json、图片生成/文生图/【短剧最佳拍档】支持场景 _ 角色【AI创客训练营】画布功能 _ 角色_2103873978132688897.json、图片生成/文生图/短剧最佳拍档AI创客训练营｜画布功能支持场景角色创作_2106237793725931522.json…）

- **类型**：Text To Image
- **样本数**：14
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：74%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `INTConstant`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 9/14 个有
- `CR Text` —— 8/14 个有
- `Image Comparer (rgthree)` —— 8/14 个有
- `Fast Groups Bypasser (rgthree)` —— 7/14 个有
- `ConditioningZeroOut` —— 6/14 个有
- `GetNode` —— 6/14 个有
- `SetNode` —— 6/14 个有
- `JjkText` —— 5/14 个有
- `solarL_SaveImagesToZip` —— 5/14 个有
- `孤海注释` —— 5/14 个有
- `EmptyImage` —— 1/14 个有
- `PromptBatchQueue` —— 1/14 个有
- `ResolutionSelector` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 80 - 1080 | 14 | 34% |
| 高度 | 1920 | 80 - 1920 | 14 | 30% |
| 采样步数 | 8 | 4 - 8 | 14 | 71% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 14 | 25% |
| 采样算法 | er_sde | - | 14 | 57% |
| 调度器 | kl_optimal | - | 14 | 43% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 19/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1080，观测区间 80 - 1080，14 个样本，取值分散，一致性仅 34%
- 高度 中位数 1920，观测区间 80 - 1920，14 个样本，取值分散，一致性仅 30%
- 采样步数 中位数 8，观测区间 4 - 8，14 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，14 个样本，取值分散，一致性仅 25%
- 采样算法 最常用 er_sde，14 个样本，一致性 57%
- 调度器 最常用 kl_optimal，14 个样本，一致性 43%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 高发问题（19/14 个样本）：Steps较低可能导致细节不足

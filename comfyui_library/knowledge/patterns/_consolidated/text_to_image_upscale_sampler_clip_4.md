---
name: text_to_image_upscale_sampler_clip_4
type: Text To Image
frequency: 15
level: weak
coverage: 0.821867
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Zimage-文生图+高清修复_2011971976901955585.json, 图片生成/文生图/Zimage_瑶光_2095722755646902273.json, 图片生成/文生图/anima文生图_2080943871458107394.json, 图片生成/文生图/anima文生图_2081302154224168962.json, 图片生成/文生图/krea2文生图+seedvr2高清放大_2070353662572060673.json, 图片生成/文生图/krea2文生图+seedvr2高清放大_2070396975937314818.json, 图片生成/文生图/krea2文生图+seedvr2高清放大_2070416550108155905.json, 图片生成/文生图/krea2文生图+seedvr2高清放大_2070429404085444609.json, 图片生成/文生图/【短剧最佳拍档】支持场景 _ 角色【AI创客训练营】画布功能 _ 角色_2103873978132688897.json, 图片生成/文生图/【短剧最佳拍档】支持场景_角色_2098950780144410625.json, 图片生成/文生图/【短剧最佳拍档】支持场景_角色_2099062438128869377.json, 图片生成/文生图/短剧最佳拍档AI创客训练营｜画布功能支持场景角色创作_2106237793725931522.json, 数字人/数字人/Krea2熟颜世绘Lora模型 写实美少女文生图风格化生成_2099181814492524545.json, 数字人/数字人/krea2熟颜世绘｜尺素数字人文生图美少女生成_2091288163825311745.json, 视频生成/图生视频/短剧最佳拍档AI创客训练营｜画布功能支持场景角色创作_2106237793725931522.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_4

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/文生图/Zimage-文生图+高清修复_2011971976901955585.json、图片生成/文生图/Zimage_瑶光_2095722755646902273.json、图片生成/文生图/anima文生图_2080943871458107394.json、图片生成/文生图/anima文生图_2081302154224168962.json、图片生成/文生图/krea2文生图+seedvr2高清放大_2070353662572060673.json…）

- **类型**：Text To Image
- **样本数**：15
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 15 个 workflow 都包含：
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
- `PreviewImage` —— 11/15 个有
- `LoraLoaderModelOnly` —— 10/15 个有
- `Image Comparer (rgthree)` —— 9/15 个有
- `ConditioningZeroOut` —— 7/15 个有
- `Fast Groups Bypasser (rgthree)` —— 7/15 个有
- `INTConstant` —— 7/15 个有
- `ImageScaleToTotalPixels` —— 7/15 个有
- `CR Text` —— 5/15 个有
- `JjkText` —— 4/15 个有
- `PrimitiveInt` —— 4/15 个有
- `solarL_SaveImagesToZip` —— 4/15 个有
- `孤海注释` —— 4/15 个有
- `EmptyImage` —— 2/15 个有
- `GetNode` —— 2/15 个有
- `ImageScaleBy` —— 2/15 个有
- `SetNode` —— 2/15 个有
- `Resolution` —— 1/15 个有
- `Text` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 30 | 15 | 19% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 15 | 30% |
| 采样算法 | er_sde | - | 15 | 67% |
| 调度器 | beta | - | 15 | 40% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |
| 宽度 | 1024 | 80 - 1280 | 15 | 45% |
| 高度 | 1536 | 80 - 1920 | 15 | 42% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 30，15 个样本，取值分散，一致性仅 19%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，15 个样本，取值分散，一致性仅 30%
- 采样算法 最常用 er_sde，15 个样本，一致性 67%
- 调度器 最常用 beta，15 个样本，一致性 40%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 80 - 1280，15 个样本，取值分散，一致性仅 45%
- 高度 中位数 1536，观测区间 80 - 1920，15 个样本，取值分散，一致性仅 42%
- 高发问题（17/15 个样本）：Steps较低可能导致细节不足

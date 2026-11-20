---
name: text_to_image_upscale_lora_sampler_51
type: Text To Image
frequency: 6
level: moderate
coverage: 0.765167
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, INTConstant, ImageScaleToTotalPixels, KSampler, LoraLoaderModelOnly, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/ziamge-【短剧最佳拍档】支持场景 _ 角色_2088664389393145858.json, 数字人/数字人/【尺素】krea2 熟颜世绘_2078697317879865345.json, 数字人/数字人/尺素出品krea2熟颜世绘｜美少女文生图有味道，质感细腻很出片_2099462000886771713.json, 视频生成/图生视频/【最佳短剧生成】支持场景 _ 角色_2098744968851578881.json, 视频生成/图生视频/【短剧最佳助手】支持场景 _ 角色_2067180332339785729.json, 视频生成/图生视频/【短剧最佳拍档】支持场景 _ 角色【AI创客训练营】画布功能 _ 角色_2103873978132688897.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_51

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（数字人/数字人/ziamge-【短剧最佳拍档】支持场景 _ 角色_2088664389393145858.json、数字人/数字人/【尺素】krea2 熟颜世绘_2078697317879865345.json、数字人/数字人/尺素出品krea2熟颜世绘｜美少女文生图有味道，质感细腻很出片_2099462000886771713.json、视频生成/图生视频/【最佳短剧生成】支持场景 _ 角色_2098744968851578881.json、视频生成/图生视频/【短剧最佳助手】支持场景 _ 角色_2067180332339785729.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 6 个 workflow 都包含：
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
- `CR Text` —— 4/6 个有
- `Image Comparer (rgthree)` —— 4/6 个有
- `PreviewImage` —— 4/6 个有
- `Fast Groups Bypasser (rgthree)` —— 3/6 个有
- `ConditioningZeroOut` —— 2/6 个有
- `GetNode` —— 2/6 个有
- `SetNode` —— 2/6 个有
- `JjkText` —— 1/6 个有
- `PromptBatchQueue` —— 1/6 个有
- `ResolutionSelector` —— 1/6 个有
- `solarL_SaveImagesToZip` —— 1/6 个有
- `孤海注释` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 6 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 6 | 18% |
| 采样算法 | res_2s_ode | - | 6 | 67% |
| 调度器 | kl_optimal | - | 6 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 1080 | 80 - 1080 | 6 | 59% |
| 高度 | 1920 | 80 - 1920 | 6 | 57% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，6 个样本，取值分散，一致性仅 18%
- 采样算法 最常用 res_2s_ode，6 个样本，一致性 67%
- 调度器 最常用 kl_optimal，6 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 80 - 1080，6 个样本
- 高度 中位数 1920，观测区间 80 - 1920，6 个样本
- 高发问题（7/6 个样本）：Steps较低可能导致细节不足

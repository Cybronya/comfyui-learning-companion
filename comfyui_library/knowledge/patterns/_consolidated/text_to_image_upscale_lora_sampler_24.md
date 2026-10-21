---
name: text_to_image_upscale_lora_sampler_24
type: Text To Image
frequency: 5
level: strong
coverage: 0.8534
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, Image Comparer (rgthree), KSampler, LoraLoaderModelOnly, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/krea2-文生图_2080226312320544769.json, 数字人/数字人/ziamge-【短剧最佳拍档】支持场景 _ 角色_2088664389393145858.json, 视频生成/图生视频/【最佳短剧生成】支持场景 _ 角色_2098744968851578881.json, 视频生成/图生视频/2067180332339785729.json, 视频生成/图生视频/【短剧最佳拍档】支持场景 _ 角色【AI创客训练营】画布功能 _ 角色_2103873978132688897.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_24

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/krea2-文生图_2080226312320544769.json、数字人/数字人/ziamge-【短剧最佳拍档】支持场景 _ 角色_2088664389393145858.json、视频生成/图生视频/【最佳短剧生成】支持场景 _ 角色_2098744968851578881.json、视频生成/图生视频/2067180332339785729.json、视频生成/图生视频/【短剧最佳拍档】支持场景 _ 角色【AI创客训练营】画布功能 _ 角色_2103873978132688897.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 4/5 个有
- `INTConstant` —— 4/5 个有
- `ImageScaleToTotalPixels` —— 4/5 个有
- `Fast Groups Bypasser (rgthree)` —— 3/5 个有
- `ResolutionSelector` —— 2/5 个有
- `ConditioningZeroOut` —— 1/5 个有
- `Fast Bypasser (rgthree)` —— 1/5 个有
- `LatentUpscaleBy` —— 1/5 个有
- `Mute / Bypass Repeater (rgthree)` —— 1/5 个有
- `PrimitiveStringMultiline` —— 1/5 个有
- `PromptBatchQueue` —— 1/5 个有
- `easy promptConcat` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | res_2s_ode | - | 5 | 80% |
| 调度器 | kl_optimal | - | 5 | 80% |
| 重绘幅度 | 1 | 0.55 - 1 | 5 | 80% |
| 宽度 | 1080 | 1024 - 1080 | 5 | 98% |
| 高度 | 1920 | 1024 - 1920 | 5 | 79% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s_ode，5 个样本，一致性 80%
- 调度器 最常用 kl_optimal，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 0.55 - 1，5 个样本，取值集中（一致性 80%）
- 宽度 中位数 1080，观测区间 1024 - 1080，5 个样本，取值集中（一致性 98%）
- 高度 中位数 1920，观测区间 1024 - 1920，5 个样本
- 高发问题（6/5 个样本）：Steps较低可能导致细节不足

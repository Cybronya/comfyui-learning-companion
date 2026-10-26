---
name: text_to_image_upscale_lora_sampler_58
type: Text To Image
frequency: 5
level: strong
coverage: 0.6366
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, LoraLoaderModelOnly, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/双图姿势迁移＋4K高清放大工作流｜自动跟随构图，换图即可运行_2095860795405070337.json, 图片生成/文生图/Krea 2文生图+高清4K放大_2069681674400653314.json, 图片生成/文生图/Krea-2 美学视觉文生图+SeedVR2高清出图_2101317926048587777.json, 图片生成/文生图/Krea-2_美学视觉文生图+SeedVR2高清出图_2107464959214055425.json, 数字人/数字人/【尺素】krea2 熟颜世绘_2078697317879865345.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_58

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/双图姿势迁移＋4K高清放大工作流｜自动跟随构图，换图即可运行_2095860795405070337.json、图片生成/文生图/Krea 2文生图+高清4K放大_2069681674400653314.json、图片生成/文生图/Krea-2 美学视觉文生图+SeedVR2高清出图_2101317926048587777.json、图片生成/文生图/Krea-2_美学视觉文生图+SeedVR2高清出图_2107464959214055425.json、数字人/数字人/【尺素】krea2 熟颜世绘_2078697317879865345.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：64%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
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
- `INTConstant` —— 4/5 个有
- `ImageScaleToTotalPixels` —— 4/5 个有
- `GetNode` —— 3/5 个有
- `PreviewImage` —— 3/5 个有
- `SetNode` —— 3/5 个有
- `Image Comparer (rgthree)` —— 2/5 个有
- `DWPreprocessor` —— 1/5 个有
- `EmptyImage` —— 1/5 个有
- `GetImageSize` —— 1/5 个有
- `ImageScaleBy` —— 1/5 个有
- `LoadImage` —— 1/5 个有
- `ReferenceLatent` —— 1/5 个有
- `VAEEncode` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 10 | 5 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 60% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 1080 | 768 - 1280 | 5 | 84% |
| 高度 | 1920 | 1344 - 1920 | 5 | 87% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 10，5 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 60%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 768 - 1280，5 个样本，取值集中（一致性 84%）
- 高度 中位数 1920，观测区间 1344 - 1920，5 个样本，取值集中（一致性 87%）
- 高发问题（4/5 个样本）：Steps较低可能导致细节不足

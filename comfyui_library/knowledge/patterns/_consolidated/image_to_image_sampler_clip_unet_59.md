---
name: image_to_image_sampler_clip_unet_59
type: Image To Image
frequency: 7
level: moderate
coverage: 0.810429
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen千问图生图，可生成中文，对标即梦_1952646987956043778.json, 图片生成/图生图/Qwen图生图_洗图+8步出图+教程说明_1959149285885554689.json, 图片生成/图生图/千问2512图生图洗图+SeedVR2高清工作流_2020867500254175234.json, 图片生成/图生图/千问2512洗图+SeedVR2高清放大工作流_2069347143063789569.json, 图片生成/图生图/千问image图生图-洗图_1973967994604883970.json, 图片生成/图生图/图生图洗图修复+SeedVR2高清工作流_2050168318803365889.json, 图片生成/图生图/洗图去ai+放大_1998033674337681409.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_59

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Qwen千问图生图，可生成中文，对标即梦_1952646987956043778.json、图片生成/图生图/Qwen图生图_洗图+8步出图+教程说明_1959149285885554689.json、图片生成/图生图/千问2512图生图洗图+SeedVR2高清工作流_2020867500254175234.json、图片生成/图生图/千问2512洗图+SeedVR2高清放大工作流_2069347143063789569.json、图片生成/图生图/千问image图生图-洗图_1973967994604883970.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 6/7 个有
- `PreviewImage` —— 6/7 个有
- `SeedVR2LoadDiTModel` —— 4/7 个有
- `SeedVR2LoadVAEModel` —— 4/7 个有
- `SeedVR2VideoUpscaler` —— 4/7 个有
- `easy cleanGpuUsed` —— 4/7 个有
- `Image Comparer (rgthree)` —— 3/7 个有
- `LoraLoaderModelOnly` —— 3/7 个有
- `PrimitiveInt` —— 3/7 个有
- `RH_Captioner` —— 3/7 个有
- `LatentUpscale` —— 2/7 个有
- `ImagePadKJ` —— 1/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/7 个有
- `ShowText|pysssss` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 30 | 7 | 61% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 4 | 7 | 54% |
| 采样算法 | euler | - | 7 | 57% |
| 调度器 | simple | - | 7 | 86% |
| 重绘幅度 | 0.5 | 0.27 - 0.65 | 7 | 73% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 30，7 个样本
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 4，7 个样本
- 采样算法 最常用 euler，7 个样本，一致性 57%
- 调度器 最常用 simple，7 个样本，一致性 86%
- 重绘幅度 中位数 0.5，观测区间 0.27 - 0.65，7 个样本

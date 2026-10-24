---
name: image_to_image_sampler_clip_unet_53
type: Image To Image
frequency: 7
level: strong
coverage: 0.879571
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/003.FLUX.2智能综合017.图像高清放大_2035275904460525569.json, 图片生成/图生图/251207-04.Z-image+Qwen反推生图_1997712839517343745.json, 图片生成/图生图/3D模型转写实写实效果图_2079501722829025281.json, 图片生成/图生图/FLUX2高清_2027640980047925250.json, 图片生成/图生图/FLUX2高清修复人像_2086408949896671233.json, 图片生成/图生图/LH-DMT版本-2.生图片类-024.Z-image+Qwen反推生图_2016484501077102593.json, 图片生成/图生图/图像去噪_2078426606925864962.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_53

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/003.FLUX.2智能综合017.图像高清放大_2035275904460525569.json、图片生成/图生图/251207-04.Z-image+Qwen反推生图_1997712839517343745.json、图片生成/图生图/3D模型转写实写实效果图_2079501722829025281.json、图片生成/图生图/FLUX2高清_2027640980047925250.json、图片生成/图生图/FLUX2高清修复人像_2086408949896671233.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 5/7 个有
- `ReferenceLatent` —— 5/7 个有
- `LoraLoaderModelOnly` —— 3/7 个有
- `CR Text` —— 2/7 个有
- `ColorMatch` —— 2/7 个有
- `ImpactInt` —— 2/7 个有
- `Qwen3_VQA` —— 2/7 个有
- `ttN concat` —— 2/7 个有
- `ttN text` —— 2/7 个有
- `LatentUpscaleBy` —— 1/7 个有
- `LoraLoader` —— 1/7 个有
- `easy imageColorMatch` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 10 | 7 | 61% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 0.9 - 1 | 7 | 96% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 10，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.9 - 1，7 个样本，取值集中（一致性 96%）
- 高发问题（5/7 个样本）：Steps较低可能导致细节不足

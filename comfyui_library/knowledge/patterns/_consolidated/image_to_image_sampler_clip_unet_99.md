---
name: image_to_image_sampler_clip_unet_99
type: Image To Image
frequency: 6
level: moderate
coverage: 0.929667
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Image-Edit模型，手办风格-4K直出_1961646663603568641.json, 图片生成/图生图/Qwen-Image-Edit模型，精准编辑图片文字_1957821483923992578.json, 图片生成/图生图/qwen千问图片编辑神器发布v1.0_1957726030365818881.json, 图片生成/图生图/qwen编辑线稿转效果图_1958881314973888513.json, 平台全量/qwen家具换背景_1958162771085053954.json, 视频生成/图生视频/水墨插画qwen_2037441276806701058.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_99

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Qwen-Image-Edit模型，手办风格-4K直出_1961646663603568641.json、图片生成/图生图/Qwen-Image-Edit模型，精准编辑图片文字_1957821483923992578.json、图片生成/图生图/qwen千问图片编辑神器发布v1.0_1957726030365818881.json、图片生成/图生图/qwen编辑线稿转效果图_1958881314973888513.json、平台全量/qwen家具换背景_1958162771085053954.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 5/6 个有
- `LoraLoaderModelOnly` —— 5/6 个有
- `ModelSamplingAuraFlow` —— 5/6 个有
- `easy imageConcat` —— 5/6 个有
- `FluxKontextImageScale` —— 3/6 个有
- `TextEncodeQwenImageEdit` —— 3/6 个有
- `ImageUpscaleWithModel` —— 2/6 个有
- `Int` —— 2/6 个有
- `PreviewImage` —— 2/6 个有
- `TextEncodeQwenImageEditPlus` —— 2/6 个有
- `UpscaleModelLoader` —— 2/6 个有
- `TextEncodeQwenImageEditPlus_lrzjason` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 14 | 8 - 20 | 6 | 57% |
| Prompt 约束强度(CFG) | 1.75 | 1 - 2.5 | 6 | 57% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | normal | - | 6 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 14，观测区间 8 - 20，6 个样本
- Prompt 约束强度(CFG) 中位数 1.75，观测区间 1 - 2.5，6 个样本
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 normal，6 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（3/6 个样本）：Steps较低可能导致细节不足

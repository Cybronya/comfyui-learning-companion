---
name: image_to_image_lora_sampler_unet_137
type: Image To Image
frequency: 5
level: strong
coverage: 0.8648
common_nodes: [CLIPLoader, EmptySD3LatentImage, GetImageSize, KSampler, Krea2EditGroundedEncode, Krea2EditModelPatch, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/图片单图编辑 krea2_2082100507342106626.json, 图片生成/图生图/摄影人物图片换脸 krea2_2080844143437377538.json, 图片生成/文生图/KREA-2-EDIT-One-image-version-1.2-two-image_2080340840479813634.json, 图片生成/文生图/KREA-2-EDIT-One-image-version-1.2_2080315514223681538.json, 图片生成/文生图/双图编辑 ( Krea 2 Identity Edit v1.2_2079971231356506114.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_137

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/图片单图编辑 krea2_2082100507342106626.json、图片生成/图生图/摄影人物图片换脸 krea2_2080844143437377538.json、图片生成/文生图/KREA-2-EDIT-One-image-version-1.2-two-image_2080340840479813634.json、图片生成/文生图/KREA-2-EDIT-One-image-version-1.2_2080315514223681538.json、图片生成/文生图/双图编辑 ( Krea 2 Identity Edit v1.2_2079971231356506114.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `EmptySD3LatentImage`
- `GetImageSize`
- `KSampler`
- `Krea2EditGroundedEncode`
- `Krea2EditModelPatch`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 4/5 个有
- `ResizeImageMaskNode` —— 4/5 个有
- `Image Comparer (rgthree)` —— 3/5 个有
- `JjkText` —— 3/5 个有
- `PreviewImage` —— 2/5 个有
- `RH_Translator` —— 2/5 个有
- `ImageScaleBy` —— 1/5 个有
- `image_scale_pixel_v2` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 10 | 5 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 10，5 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（4/5 个样本）：Steps较低可能导致细节不足

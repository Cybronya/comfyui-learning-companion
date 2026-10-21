---
name: image_to_image_lora_sampler_unet_8
type: Image To Image
frequency: 6
level: strong
coverage: 0.7495
common_nodes: [CLIPLoader, EmptySD3LatentImage, KSampler, Krea2EditGroundedEncode, Krea2EditModelPatch, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/2102619986266251266.json, 图片生成/文生图/KREA-2-EDIT-One-image-version-1.2-two-image_2080340840479813634.json, 图片生成/文生图/KREA-2-EDIT-One-image-version-1.2_2080315514223681538.json, 图片生成/文生图/单图生成三视图完整工作流（模版一）消耗积分：KREA-2-EDIT版本_2088932692376248322.json, 图片生成/文生图/单图生成人物资产三视图完整工作流_2095809006400004097.json, 图片生成/文生图/双图编辑 ( Krea 2 Identity Edit v1.2_2079971231356506114.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_8

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/2102619986266251266.json、图片生成/文生图/KREA-2-EDIT-One-image-version-1.2-two-image_2080340840479813634.json、图片生成/文生图/KREA-2-EDIT-One-image-version-1.2_2080315514223681538.json、图片生成/文生图/单图生成三视图完整工作流（模版一）消耗积分：KREA-2-EDIT版本_2088932692376248322.json、图片生成/文生图/单图生成人物资产三视图完整工作流_2095809006400004097.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `EmptySD3LatentImage`
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
- `ResizeImageMaskNode` —— 5/6 个有
- `GetImageSize` —— 4/6 个有
- `PreviewImage` —— 3/6 个有
- `CR Text` —— 2/6 个有
- `ConditioningZeroOut` —— 2/6 个有
- `Image Comparer (rgthree)` —— 2/6 个有
- `ImageScaleBy` —— 2/6 个有
- `JjkText` —— 2/6 个有
- `Textbox` —— 2/6 个有
- `image_scale_pixel_v2` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 10 | 6 | 91% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 10，6 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（5/6 个样本）：Steps较低可能导致细节不足

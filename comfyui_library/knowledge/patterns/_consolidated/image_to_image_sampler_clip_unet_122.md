---
name: image_to_image_sampler_clip_unet_122
type: Image To Image
frequency: 5
level: weak
coverage: 0.8842
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/MOSS IMAGE 图生图（注意调：降噪 ）_2116868054356422657.json, 图片生成/图生图/MOSS-8步 图生图_2115934942751453185.json, 图片生成/图生图/MOSS-8步 洗图_2115940313247346690.json, 图片生成/图生图/图生图-krea2_2069933877975674882.json, 图片生成/图生图/洗图-krea2_2070082974246326274.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_122

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/MOSS IMAGE 图生图（注意调：降噪 ）_2116868054356422657.json、图片生成/图生图/MOSS-8步 图生图_2115934942751453185.json、图片生成/图生图/MOSS-8步 洗图_2115940313247346690.json、图片生成/图生图/图生图-krea2_2069933877975674882.json、图片生成/图生图/洗图-krea2_2070082974246326274.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 5 个 workflow 都包含：
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
- `ImageScaleToMaxDimension` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `AILab_QwenVL` —— 3/5 个有
- `PreviewAny` —— 3/5 个有
- `ConditioningZeroOut` —— 2/5 个有
- `Latent Noise Injection` —— 2/5 个有
- `LoraLoaderModelOnly` —— 2/5 个有
- `ImageScaleBy` —— 1/5 个有
- `ImageUpscaleWithModel` —— 1/5 个有
- `UpscaleModelLoader` —— 1/5 个有
- `easy imageConcat` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 25 | 5 | 40% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 5 | 54% |
| 采样算法 | euler | - | 5 | 80% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 0.7 | 0.3 - 1 | 5 | 64% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 25，5 个样本，取值分散，一致性仅 40%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，5 个样本
- 采样算法 最常用 euler，5 个样本，一致性 80%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 0.7，观测区间 0.3 - 1，5 个样本
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足

---
name: text_to_image_sampler_clip_unet_104
type: Text To Image
frequency: 4
level: weak
coverage: 0.91975
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Fast Groups Bypasser (rgthree), KSampler, KSamplerSelect, LoadImage, ModelSamplingAuraFlow, SamplerCustom, SaveImage, TextEncodeBooguEdit, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Boogu 文生图+单图编辑四合一工作流！_2067920112757334018.json, 图片生成/文生图/boogu单采+多图编辑_2069715605447598082.json, 图片生成/文生图/boogu图像模型两件套Base & Edit_2069786400983183362.json, 图片生成/文生图/boogu图像编辑_文生图_2071497005939118082.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_104

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Boogu 文生图+单图编辑四合一工作流！_2067920112757334018.json、图片生成/文生图/boogu单采+多图编辑_2069715605447598082.json、图片生成/文生图/boogu图像模型两件套Base & Edit_2069786400983183362.json、图片生成/文生图/boogu图像编辑_文生图_2071497005939118082.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SamplerCustom`
- `SaveImage`
- `TextEncodeBooguEdit`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `TTResolutionSelector` —— 3/4 个有
- `FluxKontextImageScale` —— 2/4 个有
- `GetImageSize+` —— 2/4 个有
- `Image Comparer (rgthree)` —— 2/4 个有
- `CR Prompt Text` —— 1/4 个有
- `DF_Get_image_size` —— 1/4 个有
- `ImageScaleToTotalPixels` —— 1/4 个有
- `Label (rgthree)` —— 1/4 个有
- `PreviewImage` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 728 - 1536 | 4 | 73% |
| 高度 | 1152 | 1024 - 1536 | 4 | 83% |
| 采样步数 | 4 | 4 - 40 | 4 | 0% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 4 | 26% |
| 采样算法 | euler | - | 4 | 50% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 0.35 - 1 | 4 | 66% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 728 - 1536，4 个样本
- 高度 中位数 1152，观测区间 1024 - 1536，4 个样本，取值集中（一致性 83%）
- 采样步数 中位数 4，观测区间 4 - 40，4 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，4 个样本，取值分散，一致性仅 26%
- 采样算法 最常用 euler，4 个样本，一致性 50%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 0.35 - 1，4 个样本
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足

---
name: image_to_image_upscale_sampler_clip_43
type: Image To Image
frequency: 2
level: weak
coverage: 0.8355
common_nodes: [CLIPLoader, CLIPTextEncode, Image Comparer (rgthree), KSampler, LoadImage, ModelSamplingAuraFlow, PreviewImage, RH_Captioner, SaveImage, UNETLoader, UltimateSDUpscale, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/千问图生图洗图放大工作流(真人变AI))_1953659875454844930.json, 图片生成/文生图/Z-Image（造相）【照片级真实】_1993840032675020801.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_clip_43

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/千问图生图洗图放大工作流(真人变AI))_1953659875454844930.json、图片生成/文生图/Z-Image（造相）【照片级真实】_1993840032675020801.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `RH_Captioner`
- `SaveImage`
- `UNETLoader`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere3` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `ImageConcatMulti` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `PrimitiveFloat` —— 1/2 个有
- `SDXLPromptStyler` —— 1/2 个有
- `ShowText` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 19.5 | - | 2 | 46% |
| Prompt 约束强度(CFG) | 2.5 | - | 2 | 40% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 19.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 46%
- Prompt 约束强度(CFG) 中位数 2.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 40%
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

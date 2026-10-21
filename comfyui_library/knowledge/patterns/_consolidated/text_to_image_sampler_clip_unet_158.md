---
name: text_to_image_sampler_clip_unet_158
type: Text To Image
frequency: 2
level: weak
coverage: 0.4895
common_nodes: [Anything Everywhere3, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, GetNode, KSampler, LoadImage, PreviewAny, PreviewImage, PrimitiveStringMultiline, ResizeImageMaskNode, SaveImage, Seed (rgthree), SetNode, TextGenerate, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea 2 图生图测试：一张图片，能否完整保留并提升细节？反推提示词 + 图生图_2074175626906529793.json, 图片生成/文生图/Krea2 多合一工作流_2074110855372959745.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_158

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Krea 2 图生图测试：一张图片，能否完整保留并提升细节？反推提示词 + 图生图_2074175626906529793.json、图片生成/文生图/Krea2 多合一工作流_2074110855372959745.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：49%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere3`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `GetNode`
- `KSampler`
- `LoadImage`
- `PreviewAny`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `ResizeImageMaskNode`
- `SaveImage`
- `Seed (rgthree)`
- `SetNode`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `ResolutionSelector` —— 1/2 个有
- `StringConcatenate` —— 1/2 个有
- `easy clearCacheAll` —— 1/2 个有
- `easy promptLine` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | ddim | - | 2 | 50% |
| 调度器 | kl_optimal | - | 2 | 50% |
| 重绘幅度 | 0.625 | - | 2 | 40% |
| 宽度 | 512 | - | 2 | 100% |
| 高度 | 512 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 ddim，2 个样本，一致性 50%
- 调度器 最常用 kl_optimal，2 个样本，一致性 50%
- 重绘幅度 中位数 0.625，样本不足，未给区间，2 个样本，取值分散，一致性仅 40%
- 宽度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（3/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

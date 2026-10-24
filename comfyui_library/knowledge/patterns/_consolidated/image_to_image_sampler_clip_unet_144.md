---
name: image_to_image_sampler_clip_unet_144
type: Image To Image
frequency: 3
level: strong
coverage: 0.778
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Florence2ModelLoader, Florence2Run, Image Comparer (rgthree), ImageScaleToMaxDimension, KSampler, LoadImage, ModelSamplingAuraFlow, PreviewTextNode, RepeatLatentBatch, SaveImage, SeedVR2Conditioning, SeedVR2PostProcessing, SeedVR2Preprocess, TextConcatenator, UNETLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAEEncodeTiled, VAELoader, easy ifElse]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/image2.5噪点色斑处理放大工作流_2093075912320446465.json, 图片生成/图生图/image2.5噪点色斑处理放大工作流_2105122148300967938.json, 图片生成/图生图/image2.5噪点色斑处理放大工作流_2105499479054049281.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_144

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/image2.5噪点色斑处理放大工作流_2093075912320446465.json、图片生成/图生图/image2.5噪点色斑处理放大工作流_2105122148300967938.json、图片生成/图生图/image2.5噪点色斑处理放大工作流_2105499479054049281.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Florence2ModelLoader`
- `Florence2Run`
- `Image Comparer (rgthree)`
- `ImageScaleToMaxDimension`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `PreviewTextNode`
- `RepeatLatentBatch`
- `SaveImage`
- `SeedVR2Conditioning`
- `SeedVR2PostProcessing`
- `SeedVR2Preprocess`
- `TextConcatenator`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAEEncodeTiled`
- `VAELoader`
- `easy ifElse`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 3 | 3 - 3 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | res_multistep | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 0.24 | 0.24 - 0.24 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 3，观测区间 3 - 3，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_multistep，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 0.24，观测区间 0.24 - 0.24，3 个样本，取值集中（一致性 100%）
- 高发问题（6/3 个样本）：Steps较低可能导致细节不足

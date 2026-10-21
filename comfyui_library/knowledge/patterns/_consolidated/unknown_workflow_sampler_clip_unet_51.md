---
name: unknown_workflow_sampler_clip_unet_51
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.7977
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [CR Aspect Ratio, CR Prompt Text, IRC Art Converter, IRC PNG Exporter, IRC Text Saver]
members: [图片生成/文生图/1954799878556704770.json, 图片生成/文生图/1955087487033118722.json, 图片生成/文生图/1955257152644550657.json, 图片生成/文生图/1955432929541459969.json, 图片生成/文生图/1955564286744543234.json, 图片生成/文生图/1958095012225495041.json, 图片生成/文生图/1962098134904147969.json, 图片生成/文生图/1962778802571096065.json, 图片生成/文生图/1962782328558862338.json, 图片生成/文生图/1963157852737212417.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_51

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/1954799878556704770.json、图片生成/文生图/1955087487033118722.json、图片生成/文生图/1955257152644550657.json、图片生成/文生图/1955432929541459969.json、图片生成/文生图/1955564286744543234.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 6/10 个有
- `CFGNorm` —— 5/10 个有
- `LoraLoaderModelOnly` —— 5/10 个有
- `SaveLatent` —— 4/10 个有
- `SeedVR2BlockSwap` —— 4/10 个有
- `CR Prompt Text` —— 3/10 个有
- `LoadImage` —— 3/10 个有
- `SeedVR2GGUF` —— 3/10 个有
- `easy showAnything` —— 3/10 个有
- `CR Aspect Ratio` —— 2/10 个有
- `ImagePadKJ` —— 2/10 个有
- `JjkText` —— 2/10 个有
- `QwenTemplateBuilder` —— 2/10 个有
- `IRC Art Converter` —— 1/10 个有
- `IRC PNG Exporter` —— 1/10 个有
- `IRC Text Saver` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 20 | 10 | 54% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 4 | 10 | 50% |
| 采样算法 | euler | - | 10 | 60% |
| 调度器 | simple | - | 10 | 40% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 20，10 个样本
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 4，10 个样本
- 采样算法 最常用 euler，10 个样本，一致性 60%
- 调度器 最常用 simple，10 个样本，一致性 40%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（17/10 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：CR Aspect Ratio、CR Prompt Text、IRC Art Converter、IRC PNG Exporter、IRC Text Saver

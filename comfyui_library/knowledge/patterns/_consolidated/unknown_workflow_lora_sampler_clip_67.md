---
name: unknown_workflow_lora_sampler_clip_67
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.84
common_nodes: [BetterFilmGrain, CLIPLoader, CLIPTextEncode, DeepTranslatorTextNode, DualCLIPLoader, EmptySD3LatentImage, EsesImageEffectBloom, FluxGuidance, ImageSharpen, KSampler, LoraLoaderModelOnly, ModelSamplingSD3, PreviewImage, SaveImage, Text Multiline, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: []
missing: [Text Multiline, easy cleanGpuUsed, Upscale Model Loader]
members: [图片生成/文生图/1944988238810636290.json, 图片生成/文生图/1946091501262958594.json, 图片生成/文生图/1946275529144328193.json, 图片生成/文生图/1946514636020543490.json, 图片生成/文生图/1946757510213562369.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_67

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/1944988238810636290.json、图片生成/文生图/1946091501262958594.json、图片生成/文生图/1946275529144328193.json、图片生成/文生图/1946514636020543490.json、图片生成/文生图/1946757510213562369.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 5 个 workflow 都包含：
- `BetterFilmGrain`
- `CLIPLoader`
- `CLIPTextEncode`
- `DeepTranslatorTextNode`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `EsesImageEffectBloom`
- `FluxGuidance`
- `ImageSharpen`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PreviewImage`
- `SaveImage`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `ImageConcanate` —— 4/5 个有
- `ImageScaleToMegapixels` —— 3/5 个有
- `Upscale Model Loader` —— 3/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 20 | 5 | 67% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | uni_pc | - | 5 | 80% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 0.25 | 0.2 - 1 | 5 | 25% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 20，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，5 个样本，一致性 80%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 0.25，观测区间 0.2 - 1，5 个样本，取值分散，一致性仅 25%
- 这些节点还没有知识卡，系统对它们的理解有限：Text Multiline、easy cleanGpuUsed、Upscale Model Loader

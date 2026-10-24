---
name: unknown_workflow_lora_sampler_clip_182
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.957
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, EsesImageEffectBloom, FluxGuidance, ImageScaleToTotalPixels, ImageSharpen, KSampler (Efficient), LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, PlaySound|pysssss, RH_Captioner, ReferenceLatent, SaveImage, SeedVR2, SeedVR2BlockSwap, UNETLoader, VAEEncode, VAELoader, easy ifElse]
problems: []
missing: []
members: [图片生成/图生图/去水印+洗图放大-FluxKontext+WAN2.2_1984582537911681026.json, 图片生成/图生图/去水印+洗图放大_2001265164164923393.json, 图片生成/图生图/去水印+洗图放大_2046048785104642049.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_182

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/去水印+洗图放大-FluxKontext+WAN2.2_1984582537911681026.json、图片生成/图生图/去水印+洗图放大_2001265164164923393.json、图片生成/图生图/去水印+洗图放大_2046048785104642049.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EsesImageEffectBloom`
- `FluxGuidance`
- `ImageScaleToTotalPixels`
- `ImageSharpen`
- `KSampler (Efficient)`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PlaySound|pysssss`
- `RH_Captioner`
- `ReferenceLatent`
- `SaveImage`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `UNETLoader`
- `VAEEncode`
- `VAELoader`
- `easy ifElse`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）

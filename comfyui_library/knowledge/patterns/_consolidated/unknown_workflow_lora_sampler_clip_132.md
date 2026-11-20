---
name: unknown_workflow_lora_sampler_clip_132
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.9688
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler (Efficient), LoadImage, LoraLoaderModelOnly, PathchSageAttentionKJ, ReferenceLatent, SaveImage, SeedVR2, SeedVR2BlockSwap, UNETLoader, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/反推提示词/46qushuiyinxitufangda_2050115183602876417.json, 图片生成/图生图/去水印+洗图放大-FluxKontext+WAN2.2_1984582537911681026.json, 图片生成/图生图/去水印+洗图放大_2001265164164923393.json, 图片生成/图生图/去水印+洗图放大_2046048785104642049.json, 平台全量/FluxKontext图片去水印+放大_2007343430602592257.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_132

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/反推提示词/46qushuiyinxitufangda_2050115183602876417.json、图片生成/图生图/去水印+洗图放大-FluxKontext+WAN2.2_1984582537911681026.json、图片生成/图生图/去水印+洗图放大_2001265164164923393.json、图片生成/图生图/去水印+洗图放大_2046048785104642049.json、平台全量/FluxKontext图片去水印+放大_2007343430602592257.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler (Efficient)`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `ReferenceLatent`
- `SaveImage`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `UNETLoader`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 4/5 个有
- `EsesImageEffectBloom` —— 4/5 个有
- `ImageScaleToTotalPixels` —— 4/5 个有
- `ImageSharpen` —— 4/5 个有
- `LayerUtility: PurgeVRAM V2` —— 4/5 个有
- `ModelSamplingSD3` —— 4/5 个有
- `PlaySound|pysssss` —— 4/5 个有
- `RH_Captioner` —— 4/5 个有
- `easy ifElse` —— 4/5 个有
- `PreviewImage` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）

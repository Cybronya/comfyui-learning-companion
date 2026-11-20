---
name: text_to_image_lora_sampler_clip_375
type: Text To Image
frequency: 5
level: strong
coverage: 0.8538
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DeepTranslatorTextNode, Display Any (rgthree), DualCLIPLoader, EmptyLatentImage, FluxGuidance, ImageResizeKJv2, KSampler, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux_Kontext多图融合（超强版）_1939540814261362690.json, 图片生成/图生图/kontext_多图组合_调节位置_多图融合_加速_ps_1939882468222930946.json, 图片生成/图生图/kontext双人合照_10秒极速优化版_1938748449276022786.json, 图片生成/图生图/kontext双人合照换背景_3图融合_15秒极速版_1938831480829497345.json, 图片生成/图生图/最强kontext双图融合工作流_1938480334402945026.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_375

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Flux_Kontext多图融合（超强版）_1939540814261362690.json、图片生成/图生图/kontext_多图组合_调节位置_多图融合_加速_ps_1939882468222930946.json、图片生成/图生图/kontext双人合照_10秒极速优化版_1938748449276022786.json、图片生成/图生图/kontext双人合照换背景_3图融合_15秒极速版_1938831480829497345.json、图片生成/图生图/最强kontext双图融合工作流_1938480334402945026.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DeepTranslatorTextNode`
- `Display Any (rgthree)`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `ImageResizeKJv2`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ACE_Expression_Eval` —— 4/5 个有
- `FluxResolutionNode` —— 4/5 个有
- `ImageConcanate` —— 4/5 个有
- `Int` —— 4/5 个有
- `LayerStyle: ColorOverlay V2` —— 4/5 个有
- `LayerUtility: CropByMask V2` —— 4/5 个有
- `MathExpression|pysssss` —— 4/5 个有
- `NunchakuFluxDiTLoader` —— 4/5 个有
- `easy imageRemBg` —— 4/5 个有
- `ApplyFBCacheOnModel` —— 3/5 个有
- `FlexLoraLoaderModelOnly` —— 3/5 个有
- `PreviewImage` —— 2/5 个有
- `Compositor3` —— 1/5 个有
- `CompositorConfig3` —— 1/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `LayerMask: BiRefNetUltraV2` —— 1/5 个有
- `LayerMask: LoadBiRefNetModelV2` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 760 | 760 - 1024 | 5 | 87% |
| 高度 | 1152 | 1024 - 1152 | 5 | 95% |
| 采样步数 | 20 | 12 - 20 | 5 | 83% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler_ancestral | - | 5 | 100% |
| 调度器 | sgm_uniform | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 760，观测区间 760 - 1024，5 个样本，取值集中（一致性 87%）
- 高度 中位数 1152，观测区间 1024 - 1152，5 个样本，取值集中（一致性 95%）
- 采样步数 中位数 20，观测区间 12 - 20，5 个样本，取值集中（一致性 83%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，5 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）

---
name: unknown_workflow_lora_sampler_unet_207
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.927667
common_nodes: [CFGNorm, CLIPLoader, CR Latent Input Switch, CR Text, ConditioningZeroOut, EmptySD3LatentImage, KOOK_ImageCompression, KOOK_SaveJPGImage, KSampler (Efficient), LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, ReferenceLatent, TextEncodeQwenImageEditPlus, UNETLoader, VAEEncode, VAELoader, easy getNode, easy setNode]
problems: []
missing: []
members: [图片生成/图生图/FireRed-Image-Edit-1.1   多图编辑_2032751050146451458.json, 图片生成/图生图/flux-2-klein-9b-fp8   EDIT   单修图 图像控制_2012434650270011394.json, 视频生成/图生视频/FireRed-Image-Edit-1.1   单图编辑_2032730903151120385.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_207

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/FireRed-Image-Edit-1.1   多图编辑_2032751050146451458.json、图片生成/图生图/flux-2-klein-9b-fp8   EDIT   单修图 图像控制_2012434650270011394.json、视频生成/图生视频/FireRed-Image-Edit-1.1   单图编辑_2032730903151120385.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CR Latent Input Switch`
- `CR Text`
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `KOOK_ImageCompression`
- `KOOK_SaveJPGImage`
- `KSampler (Efficient)`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `ReferenceLatent`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEEncode`
- `VAELoader`
- `easy getNode`
- `easy setNode`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 2/3 个有
- `ShowText|pysssss` —— 2/3 个有
- `CR Seed` —— 1/3 个有
- `CR Text Input Switch` —— 1/3 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/3 个有
- `ImageConcanate` —— 1/3 个有
- `ImageConcatMulti` —— 1/3 个有
- `ImageScaleToTotalPixels` —— 1/3 个有
- `PromptExpand` —— 1/3 个有
- `easy imageScaleDownToSize` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 3 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）

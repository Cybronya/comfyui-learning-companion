---
name: unknown_workflow_upscale_lora_sampler_117
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.742
common_nodes: [CFGNorm, CLIPLoader, CLIPTextEncode, CR Seed, CR Text, ConditioningZeroOut, EmptyFlux2LatentImage, GetNode, Image Comparer (rgthree), KOOK_ImageCompression, KOOK_SaveJPGImage, KSampler (Efficient), LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, ReferenceLatent, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, UNETLoader, VAEEncode, VAELoader, easy getNode, easy setNode]
problems: []
missing: []
members: [图片生成/图生图/一键运行：flux-2-klein  扩图 图像控制 修改工作流_2012724431151439874.json, 平台全量/一键运行：flux-2-klein-9b-fp8   产品修图高清放大工作流 拿来即用_2017816428337963009.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_117

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/一键运行：flux-2-klein  扩图 图像控制 修改工作流_2012724431151439874.json、平台全量/一键运行：flux-2-klein-9b-fp8   产品修图高清放大工作流 拿来即用_2017816428337963009.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：74%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Seed`
- `CR Text`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `GetNode`
- `Image Comparer (rgthree)`
- `KOOK_ImageCompression`
- `KOOK_SaveJPGImage`
- `KSampler (Efficient)`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `ReferenceLatent`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `UNETLoader`
- `VAEEncode`
- `VAELoader`
- `easy getNode`
- `easy setNode`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL` —— 1/2 个有
- `GetImage` —— 1/2 个有
- `GetImageSize+` —— 1/2 个有
- `ImagePadForOutpaint` —— 1/2 个有
- `InpaintModelConditioning` —— 1/2 个有
- `LayerFilter: HDREffects` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `SaveImage` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `StringFunction|pysssss` —— 1/2 个有
- `easy imageChooser` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

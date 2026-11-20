---
name: unknown_workflow_inpaint_lora_sampler_71
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.919333
common_nodes: [CLIPTextEncode, CLIPTextEncodeFlux, CLIPVisionEncode, CLIPVisionLoader, ConditioningZeroOut, ConstrainImage|pysssss, DetailerForEach, DifferentialDiffusion, DualCLIPLoader, GrowMaskWithBlur, Image Comparer (rgthree), InpaintModelConditioning, KSampler, LayerMask: SegmentAnythingUltra V2, LoadImage, LoraLoaderModelOnly, MaskToSEGS, SaveImage, StyleModelApply, StyleModelLoader, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [平台全量/一键更换背景 - F.1_1890048178039795713.json, 平台全量/迁移 - F.1_1900472478685372417.json, 平台全量/重磅更新__生成各种姿势的模特，保持外貌一致性不变_1899328460555468801.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_71

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/一键更换背景 - F.1_1890048178039795713.json、平台全量/迁移 - F.1_1900472478685372417.json、平台全量/重磅更新__生成各种姿势的模特，保持外貌一致性不变_1899328460555468801.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPTextEncodeFlux`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ConditioningZeroOut`
- `ConstrainImage|pysssss`
- `DetailerForEach`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `InpaintModelConditioning`
- `KSampler`
- `LayerMask: SegmentAnythingUltra V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskToSEGS`
- `SaveImage`
- `StyleModelApply`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `FluxGuidance` —— 2/3 个有
- `GetImageSize+` —— 2/3 个有
- `Image Filter Adjustments` —— 2/3 个有
- `ImageConcanate` —— 2/3 个有
- `ImageCrop+` —— 2/3 个有
- `ImageToMask` —— 2/3 个有
- `InpaintCrop` —— 2/3 个有
- `InpaintStitch` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `MaskToImage` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `preview_mask` —— 2/3 个有
- `CR Text` —— 1/3 个有
- `GroundingDinoModelLoader (segment anything)` —— 1/3 个有
- `GroundingDinoSAMSegment (segment anything)` —— 1/3 个有
- `Joy_caption_two` —— 1/3 个有
- `Joy_caption_two_load` —— 1/3 个有
- `Label (rgthree)` —— 1/3 个有
- `LoraLoader` —— 1/3 个有
- `MaskPreview+` —— 1/3 个有
- `SAMModelLoader (segment anything)` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有
- `Text Concatenate (JPS)` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.6 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |
| 采样步数 | 35 | 30 - 35 | 3 | 93% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 35，观测区间 30 - 35，3 个样本，取值集中（一致性 93%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）

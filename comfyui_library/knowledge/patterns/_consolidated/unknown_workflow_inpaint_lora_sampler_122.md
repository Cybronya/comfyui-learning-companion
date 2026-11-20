---
name: unknown_workflow_inpaint_lora_sampler_122
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8475
common_nodes: [BasicScheduler, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, ImageConcanate, ImageToMask, ImpactImageBatchToImageList, InpaintModelConditioning, InvertMask (segment anything), KSamplerSelect, LayerUtility: ColorImage V2, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, MaskToImage, PreviewImage, RepeatLatentBatch, SamplerCustom, SaveImage, StyleModelApply, StyleModelLoader, UNETLoader, VAEDecode, VAELoader, easy imageInsetCrop]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/一键换脸换衣换背景工作流V1.6（新增支持上传肖像照）_1897486132353912833.json, 平台全量/一键换脸换衣换背景工作流_1895797995805999105.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_122

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/一键换脸换衣换背景工作流V1.6（新增支持上传肖像照）_1897486132353912833.json、平台全量/一键换脸换衣换背景工作流_1895797995805999105.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImageConcanate`
- `ImageToMask`
- `ImpactImageBatchToImageList`
- `InpaintModelConditioning`
- `InvertMask (segment anything)`
- `KSamplerSelect`
- `LayerUtility: ColorImage V2`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskToImage`
- `PreviewImage`
- `RepeatLatentBatch`
- `SamplerCustom`
- `SaveImage`
- `StyleModelApply`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageInsetCrop`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 1/2 个有
- `DifferentialDiffusion` —— 1/2 个有
- `FaceAlignSingle` —— 1/2 个有
- `GrowMaskWithBlur` —— 1/2 个有
- `INPAINT_ExpandMask` —— 1/2 个有
- `ImageCompositeMasked` —— 1/2 个有
- `KSampler` —— 1/2 个有
- `Label (rgthree)` —— 1/2 个有
- `LayerMask: MaskGrow` —— 1/2 个有
- `LayerMask: SegformerB2ClothesUltra` —— 1/2 个有
- `LayerMask: SegmentAnythingUltra V2` —— 1/2 个有
- `Mask Fill Holes` —— 1/2 个有
- `MaskPreview+` —— 1/2 个有
- `ModelSamplingFlux` —— 1/2 个有
- `ReroutePrimitive|pysssss` —— 1/2 个有
- `String` —— 1/2 个有
- `SubtractMask` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有
- `easy int` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 1 | 100% |
| 采样算法 | euler | - | 1 | 100% |
| 调度器 | simple | - | 1 | 100% |
| 重绘幅度 | 0.5 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

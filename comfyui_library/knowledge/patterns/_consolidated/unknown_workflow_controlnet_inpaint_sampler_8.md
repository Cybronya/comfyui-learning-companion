---
name: unknown_workflow_controlnet_inpaint_sampler_8
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8665
common_nodes: [ApplyInstantID, CLIPTextEncode, CheckpointLoaderSimple, ColorMatch, ControlNetApplyAdvanced, ControlNetLoader, CropFace, DifferentialDiffusion, Fast Groups Bypasser (rgthree), ImageFromBatch, ImpactMakeImageBatch, ImpactSEGSToMaskBatch, ImpactSimpleDetectorSEGS, InpaintCrop, InpaintModelConditioning, InpaintStitch, InstantIDFaceAnalysis, InstantIDModelLoader, KSampler, LayerMask: MaskGrow, LoadImage, MaskFromBatch+, MaskToImage, PreviewImage, SAMLoader, SaveImage, UltralyticsDetectorProvider, VAEDecode, easy forLoopEnd, easy forLoopStart, easy imageCount]
problems: []
missing: []
members: [图片生成/图生图/单，多人换脸工作流_2059153660030050306.json, 图片生成/图生图/多人换脸_双人换脸_多人合照V3.0 (2)_1989714890313093121.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_inpaint_sampler_8

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/单，多人换脸工作流_2059153660030050306.json、图片生成/图生图/多人换脸_双人换脸_多人合照V3.0 (2)_1989714890313093121.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 2 个 workflow 都包含：
- `ApplyInstantID`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ColorMatch`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `CropFace`
- `DifferentialDiffusion`
- `Fast Groups Bypasser (rgthree)`
- `ImageFromBatch`
- `ImpactMakeImageBatch`
- `ImpactSEGSToMaskBatch`
- `ImpactSimpleDetectorSEGS`
- `InpaintCrop`
- `InpaintModelConditioning`
- `InpaintStitch`
- `InstantIDFaceAnalysis`
- `InstantIDModelLoader`
- `KSampler`
- `LayerMask: MaskGrow`
- `LoadImage`
- `MaskFromBatch+`
- `MaskToImage`
- `PreviewImage`
- `SAMLoader`
- `SaveImage`
- `UltralyticsDetectorProvider`
- `VAEDecode`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy imageCount`

**可变部分**（部分 workflow 才有）：
- `ApplyPulid` —— 1/2 个有
- `FaceAnalysisModels` —— 1/2 个有
- `FaceEmbedDistance` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `LoraLoader` —— 1/2 个有
- `PulidEvaClipLoader` —— 1/2 个有
- `PulidInsightFaceLoader` —— 1/2 个有
- `PulidModelLoader` —— 1/2 个有
- `ReActorFaceSwap` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.45 | - | 2 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |
| 采样步数 | 15 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1.75 | - | 2 | 86% |
| 采样算法 | euler_ancestral | - | 2 | 100% |
| 调度器 | sgm_uniform | - | 2 | 100% |
| 重绘幅度 | 0.5 | - | 2 | 80% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.45，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 15，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1.75，样本不足，未给区间，2 个样本，取值集中（一致性 86%）
- 采样算法 最常用 euler_ancestral，2 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，2 个样本，一致性 100%
- 重绘幅度 中位数 0.5，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

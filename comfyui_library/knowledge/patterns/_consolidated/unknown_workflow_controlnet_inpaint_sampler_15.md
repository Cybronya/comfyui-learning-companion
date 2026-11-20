---
name: unknown_workflow_controlnet_inpaint_sampler_15
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9085
common_nodes: [ApplyInstantID, CLIPTextEncode, CheckpointLoaderSimple, ColorMatch, ControlNetLoader, ImpactSimpleDetectorSEGS, InpaintCrop, InpaintModelConditioning, InpaintStitch, InstantIDFaceAnalysis, InstantIDModelLoader, KSampler, LoadImage, PreviewImage, SAMLoader, SaveImage, SegsToCombinedMask, UltralyticsDetectorProvider, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/InstantID 图像换脸工作流_1984454385600249858.json, 平台全量/单人换脸（简版）_1919291111574011905.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_inpaint_sampler_15

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/InstantID 图像换脸工作流_1984454385600249858.json、平台全量/单人换脸（简版）_1919291111574011905.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `ApplyInstantID`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ColorMatch`
- `ControlNetLoader`
- `ImpactSimpleDetectorSEGS`
- `InpaintCrop`
- `InpaintModelConditioning`
- `InpaintStitch`
- `InstantIDFaceAnalysis`
- `InstantIDModelLoader`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `SAMLoader`
- `SaveImage`
- `SegsToCombinedMask`
- `UltralyticsDetectorProvider`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `CR Simple Image Compare` —— 1/2 个有
- `CropFace` —— 1/2 个有
- `DifferentialDiffusion` —— 1/2 个有
- `GrowMaskWithBlur` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `MaskPreview+` —— 1/2 个有
- `MaskToImage` —— 1/2 个有
- `SEGSPreview` —— 1/2 个有
- `VAELoader` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 16.5 | - | 2 | 48% |
| Prompt 约束强度(CFG) | 1.25 | - | 2 | 80% |
| 采样算法 | euler_ancestral | - | 2 | 100% |
| 调度器 | sgm_uniform | - | 2 | 100% |
| 重绘幅度 | 0.835 | - | 2 | 80% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 16.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 48%
- Prompt 约束强度(CFG) 中位数 1.25，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- 采样算法 最常用 euler_ancestral，2 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，2 个样本，一致性 100%
- 重绘幅度 中位数 0.835，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

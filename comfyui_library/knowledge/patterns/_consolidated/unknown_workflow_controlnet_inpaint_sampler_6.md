---
name: unknown_workflow_controlnet_inpaint_sampler_6
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.822
common_nodes: [AIO_Preprocessor, ApplyInstantID, CLIPTextEncode, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, CropMask, GrowMask, ImageColorMatch+, ImageResize+, InpaintModelConditioning, InstantIDFaceAnalysis, InstantIDModelLoader, KSampler, LayerMask: MaskPreview, LayerUtility: CropBoxResolve, LayerUtility: CropByMask V2, LayerUtility: RestoreCropBox, LoadImage, MaskBlur+, PreviewImage, RepeatLatentBatch, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/图生图/图片-批量换脸_1972664683935277058.json, 图片生成/图生图/批量换脸，批量换装_2018385777666826242.json, 图片生成/图生图/高质量换脸工作流_1934950144754262017.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_inpaint_sampler_6

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/图片-批量换脸_1972664683935277058.json、图片生成/图生图/批量换脸，批量换装_2018385777666826242.json、图片生成/图生图/高质量换脸工作流_1934950144754262017.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 3 个 workflow 都包含：
- `AIO_Preprocessor`
- `ApplyInstantID`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `CropMask`
- `GrowMask`
- `ImageColorMatch+`
- `ImageResize+`
- `InpaintModelConditioning`
- `InstantIDFaceAnalysis`
- `InstantIDModelLoader`
- `KSampler`
- `LayerMask: MaskPreview`
- `LayerUtility: CropBoxResolve`
- `LayerUtility: CropByMask V2`
- `LayerUtility: RestoreCropBox`
- `LoadImage`
- `MaskBlur+`
- `PreviewImage`
- `RepeatLatentBatch`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `Bjornulf_ShowInt` —— 2/3 个有
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `LayerMask: PersonMaskUltra V2` —— 2/3 个有
- `LayerMask: SegmentAnythingUltra V2` —— 2/3 个有
- `RHBatchImages:` —— 2/3 个有
- `RHExtractImage` —— 2/3 个有
- `RHUploadZip` —— 2/3 个有
- `easy forLoopEnd` —— 2/3 个有
- `easy forLoopStart` —— 2/3 个有
- `easy imageCount` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `easy imageRemBg` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.45 | 0.45 - 0.45 | 3 | 100% |
| 采样步数 | 15 | 15 - 15 | 3 | 100% |
| Prompt 约束强度(CFG) | 1.5 | 1.5 - 1.5 | 3 | 100% |
| 采样算法 | euler_ancestral | - | 3 | 100% |
| 调度器 | sgm_uniform | - | 3 | 100% |
| 重绘幅度 | 0.6 | 0.6 - 0.6 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.45，观测区间 0.45 - 0.45，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 15，观测区间 15 - 15，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1.5，观测区间 1.5 - 1.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，3 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，3 个样本，一致性 100%
- 重绘幅度 中位数 0.6，观测区间 0.6 - 0.6，3 个样本，取值集中（一致性 100%）

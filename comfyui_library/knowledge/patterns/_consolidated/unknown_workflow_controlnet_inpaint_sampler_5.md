---
name: unknown_workflow_controlnet_inpaint_sampler_5
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.826
common_nodes: [AIO_Preprocessor, ApplyInstantID, CLIPTextEncode, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, CropMask, GrowMask, ImageColorMatch+, ImageResize+, InpaintModelConditioning, InstantIDFaceAnalysis, InstantIDModelLoader, KSampler, LayerMask: MaskPreview, LayerUtility: CropBoxResolve, LayerUtility: CropByMask V2, LayerUtility: RestoreCropBox, LoadImage, MaskBlur+, PreviewImage, RepeatLatentBatch, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/图生图/图片-批量换脸_1972664683935277058.json, 图片生成/图生图/批量换脸，批量换装_2018385777666826242.json, 图片生成/图生图/高质量换脸工作流_1934950144754262017.json, 数字人/数字人/换脸_1966685850157428738.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_inpaint_sampler_5

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/图片-批量换脸_1972664683935277058.json、图片生成/图生图/批量换脸，批量换装_2018385777666826242.json、图片生成/图生图/高质量换脸工作流_1934950144754262017.json、数字人/数字人/换脸_1966685850157428738.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 4 个 workflow 都包含：
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
- `Fast Groups Bypasser (rgthree)` —— 3/4 个有
- `LayerMask: SegmentAnythingUltra V2` —— 3/4 个有
- `Bjornulf_ShowInt` —— 2/4 个有
- `LayerMask: PersonMaskUltra V2` —— 2/4 个有
- `RHBatchImages:` —— 2/4 个有
- `RHExtractImage` —— 2/4 个有
- `RHUploadZip` —— 2/4 个有
- `easy forLoopEnd` —— 2/4 个有
- `easy forLoopStart` —— 2/4 个有
- `easy imageCount` —— 2/4 个有
- `easy showAnything` —— 2/4 个有
- `easy imageRemBg` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.45 | 0.45 - 0.45 | 4 | 100% |
| 采样步数 | 15 | 15 - 15 | 4 | 100% |
| Prompt 约束强度(CFG) | 1.5 | 1.5 - 1.5 | 4 | 100% |
| 采样算法 | euler_ancestral | - | 4 | 100% |
| 调度器 | sgm_uniform | - | 4 | 100% |
| 重绘幅度 | 0.6 | 0.6 - 0.6 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.45，观测区间 0.45 - 0.45，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 15，观测区间 15 - 15，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1.5，观测区间 1.5 - 1.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，4 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，4 个样本，一致性 100%
- 重绘幅度 中位数 0.6，观测区间 0.6 - 0.6，4 个样本，取值集中（一致性 100%）

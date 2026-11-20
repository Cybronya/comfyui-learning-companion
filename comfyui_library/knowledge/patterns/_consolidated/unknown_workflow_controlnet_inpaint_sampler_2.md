---
name: unknown_workflow_controlnet_inpaint_sampler_2
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.881778
common_nodes: [ApplyInstantID, CLIPTextEncode, CheckpointLoaderSimple, ControlNetLoader, CropMask, GrowMask, ImageResize+, InpaintModelConditioning, InstantIDFaceAnalysis, InstantIDModelLoader, KSampler, LayerMask: PersonMaskUltra V2, LayerUtility: CropBoxResolve, LayerUtility: CropByMask V2, LayerUtility: RestoreCropBox, LoadImage, MaskBlur+, PreviewImage, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/图生图/人像换脸_1900359783394979842.json, 图片生成/图生图/人像换脸_2039720218871734274.json, 图片生成/图生图/匹配脸型｜人像换脸｜一键生图_1922466832564027393.json, 图片生成/图生图/商用级精准换脸工作流_1918560729861914625.json, 图片生成/图生图/图片人像换脸_2052270289379176450.json, 图片生成/图生图/大厂专用换脸工作流_1918701460157038593.json, 图片生成/图生图/数字人_模特精准换脸工作流_2044685405022326785.json, 图片生成/图生图/极速换脸固定脸型（instantid）_1990667541708247041.json, 图片生成/图生图/极速换脸固定脸型（instantid）_2006714170363875329.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_inpaint_sampler_2

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/人像换脸_1900359783394979842.json、图片生成/图生图/人像换脸_2039720218871734274.json、图片生成/图生图/匹配脸型｜人像换脸｜一键生图_1922466832564027393.json、图片生成/图生图/商用级精准换脸工作流_1918560729861914625.json、图片生成/图生图/图片人像换脸_2052270289379176450.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 9 个 workflow 都包含：
- `ApplyInstantID`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetLoader`
- `CropMask`
- `GrowMask`
- `ImageResize+`
- `InpaintModelConditioning`
- `InstantIDFaceAnalysis`
- `InstantIDModelLoader`
- `KSampler`
- `LayerMask: PersonMaskUltra V2`
- `LayerUtility: CropBoxResolve`
- `LayerUtility: CropByMask V2`
- `LayerUtility: RestoreCropBox`
- `LoadImage`
- `MaskBlur+`
- `PreviewImage`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 7/9 个有
- `AIO_Preprocessor` —— 6/9 个有
- `ControlNetApplyAdvanced` —— 6/9 个有
- `ImageColorMatch+` —— 6/9 个有
- `LayerMask: MaskPreview` —— 5/9 个有
- `RepeatLatentBatch` —— 5/9 个有
- `ImageCompositeMasked` —— 4/9 个有
- `ImageSmartSharpen+` —— 4/9 个有
- `InvertMask` —— 4/9 个有
- `MaskPreview+` —— 4/9 个有
- `ColorMatch` —— 3/9 个有
- `FaceAnalysisModels` —— 3/9 个有
- `FaceBoundingBox` —— 3/9 个有
- `LayerUtility: ImageReel` —— 2/9 个有
- `LayerUtility: ImageReelComposit` —— 2/9 个有
- `PMRF` —— 2/9 个有
- `SUPIR_Upscale` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.45 | 0.45 - 0.45 | 6 | 100% |
| 采样步数 | 15 | 15 - 20 | 9 | 86% |
| Prompt 约束强度(CFG) | 1.5 | 1.5 - 2 | 9 | 86% |
| 采样算法 | euler_ancestral | - | 9 | 100% |
| 调度器 | sgm_uniform | - | 9 | 100% |
| 重绘幅度 | 0.6 | 0.5 - 1 | 9 | 69% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.45，观测区间 0.45 - 0.45，6 个样本，取值集中（一致性 100%）
- 采样步数 中位数 15，观测区间 15 - 20，9 个样本，取值集中（一致性 86%）
- Prompt 约束强度(CFG) 中位数 1.5，观测区间 1.5 - 2，9 个样本，取值集中（一致性 86%）
- 采样算法 最常用 euler_ancestral，9 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，9 个样本，一致性 100%
- 重绘幅度 中位数 0.6，观测区间 0.5 - 1，9 个样本

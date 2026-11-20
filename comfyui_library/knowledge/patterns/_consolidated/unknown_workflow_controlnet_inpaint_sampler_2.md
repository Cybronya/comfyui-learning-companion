---
name: unknown_workflow_controlnet_inpaint_sampler_2
type: Unknown Workflow
frequency: 16
level: moderate
coverage: 0.874812
common_nodes: [ApplyInstantID, CLIPTextEncode, CheckpointLoaderSimple, ControlNetLoader, CropMask, GrowMask, ImageResize+, InpaintModelConditioning, InstantIDFaceAnalysis, InstantIDModelLoader, KSampler, LayerMask: PersonMaskUltra V2, LayerUtility: CropBoxResolve, LayerUtility: CropByMask V2, LayerUtility: RestoreCropBox, LoadImage, MaskBlur+, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/图生图/人像换脸_1900359783394979842.json, 图片生成/图生图/人像换脸_2039720218871734274.json, 图片生成/图生图/匹配脸型｜人像换脸｜一键生图_1922466832564027393.json, 图片生成/图生图/商用级精准换脸工作流_1918560729861914625.json, 图片生成/图生图/图片人像换脸_2052270289379176450.json, 图片生成/图生图/大厂专用换脸工作流_1918701460157038593.json, 图片生成/图生图/数字人_模特精准换脸工作流_2044685405022326785.json, 图片生成/图生图/极速换脸固定脸型（instantid）_1990667541708247041.json, 图片生成/图生图/极速换脸固定脸型（instantid）_2006714170363875329.json, 平台全量/Instantid精准换脸工作流_1971811812297666562.json, 平台全量/Instantid精准换脸工作流_1985327454619320322.json, 平台全量/Instantid精准换脸工作流_2002987699717980161.json, 平台全量/instant id 换脸_1890368472273309698.json, 平台全量/工作流项目篇2-Instantid精准换脸工作流+放大节点_1976269061569028097.json, 平台全量/电商模特快速换 脸_2061004129140563969.json, 平台全量/空白工作流_1916036791374385154.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_inpaint_sampler_2

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/图生图/人像换脸_1900359783394979842.json、图片生成/图生图/人像换脸_2039720218871734274.json、图片生成/图生图/匹配脸型｜人像换脸｜一键生图_1922466832564027393.json、图片生成/图生图/商用级精准换脸工作流_1918560729861914625.json、图片生成/图生图/图片人像换脸_2052270289379176450.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 16 个 workflow 都包含：
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
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 15/16 个有
- `Image Comparer (rgthree)` —— 14/16 个有
- `RepeatLatentBatch` —— 11/16 个有
- `LayerMask: MaskPreview` —— 10/16 个有
- `ColorMatch` —— 9/16 个有
- `FaceAnalysisModels` —— 9/16 个有
- `FaceBoundingBox` —— 9/16 个有
- `AIO_Preprocessor` —— 8/16 个有
- `ControlNetApplyAdvanced` —— 8/16 个有
- `ImageColorMatch+` —— 7/16 个有
- `SUPIR_Upscale` —— 7/16 个有
- `ImageCompositeMasked` —— 5/16 个有
- `ImageSmartSharpen+` —— 5/16 个有
- `InvertMask` —— 5/16 个有
- `MaskPreview+` —— 5/16 个有
- `LayerUtility: ImageReel` —— 2/16 个有
- `LayerUtility: ImageReelComposit` —— 2/16 个有
- `PMRF` —— 2/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.45 | 0.45 - 0.45 | 8 | 100% |
| 采样步数 | 17.5 | 15 - 20 | 16 | 86% |
| Prompt 约束强度(CFG) | 1.75 | 1.5 - 2 | 16 | 86% |
| 采样算法 | euler_ancestral | - | 16 | 100% |
| 调度器 | sgm_uniform | - | 16 | 100% |
| 重绘幅度 | 0.55 | 0.5 - 1 | 16 | 67% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.45，观测区间 0.45 - 0.45，8 个样本，取值集中（一致性 100%）
- 采样步数 中位数 17.5，观测区间 15 - 20，16 个样本，取值集中（一致性 86%）
- Prompt 约束强度(CFG) 中位数 1.75，观测区间 1.5 - 2，16 个样本，取值集中（一致性 86%）
- 采样算法 最常用 euler_ancestral，16 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，16 个样本，一致性 100%
- 重绘幅度 中位数 0.55，观测区间 0.5 - 1，16 个样本

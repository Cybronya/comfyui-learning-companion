---
name: unknown_workflow_controlnet_inpaint_upscale
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.875417
common_nodes: [ApplyInstantID, BboxDetectorSEGS, CLIPTextEncode, CheckpointLoaderSimple, ControlNetLoader, Crop Face, DF_Image_scale_to_side, GrowMask, ImageComposite+, ImageCrop+, ImageResize+, ImageUpscaleWithModel, InpaintModelConditioning, InstantIDFaceAnalysis, InstantIDModelLoader, KSampler, Load RetinaFace, LoadImage, Mask Crop Region, MaskBlur+, PreviewImage, SAMDetectorCombined, SAMLoader, SaveImage, UltralyticsDetectorProvider, UpscaleModelLoader, VAEDecode]
problems: []
missing: []
members: [图片生成/图生图/Quick Face Swap_2062537685566312449.json, 图片生成/图生图/【CQ808】换脸-_2020057375142580226.json, 图片生成/图生图/一键换脸超高相似度换脸-InstantID_1909560735851315202.json, 图片生成/图生图/一键换脸超高相似度换脸-人像替换丨容貌替换丨面部迁移_1993840757727576065.json, 图片生成/图生图/模特换脸_lnstantiD_优化版_1953080359522136066.json, 平台全量/AI钢铁红刘_1826798272861360130.json, 平台全量/Flux-lnstantiD-换脸_1893568754796675073.json, 平台全量/一键换脸超高相似度换脸-InstantID 人像替换丨容貌替换丨面部迁移_1991668046943232001.json, 平台全量/快速换脸_1825849167305707522.json, 平台全量/快速换脸_1968941996016615425.json, 平台全量/换脸-黑神话悟空_1826927886225035265.json, 平台全量/跨风格换脸_1826784749456379905.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_inpaint_upscale

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/Quick Face Swap_2062537685566312449.json、图片生成/图生图/【CQ808】换脸-_2020057375142580226.json、图片生成/图生图/一键换脸超高相似度换脸-InstantID_1909560735851315202.json、图片生成/图生图/一键换脸超高相似度换脸-人像替换丨容貌替换丨面部迁移_1993840757727576065.json、图片生成/图生图/模特换脸_lnstantiD_优化版_1953080359522136066.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 12 个 workflow 都包含：
- `ApplyInstantID`
- `BboxDetectorSEGS`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetLoader`
- `Crop Face`
- `DF_Image_scale_to_side`
- `GrowMask`
- `ImageComposite+`
- `ImageCrop+`
- `ImageResize+`
- `ImageUpscaleWithModel`
- `InpaintModelConditioning`
- `InstantIDFaceAnalysis`
- `InstantIDModelLoader`
- `KSampler`
- `Load RetinaFace`
- `LoadImage`
- `Mask Crop Region`
- `MaskBlur+`
- `PreviewImage`
- `SAMDetectorCombined`
- `SAMLoader`
- `SaveImage`
- `UltralyticsDetectorProvider`
- `UpscaleModelLoader`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `MaskToImage` —— 10/12 个有
- `ApplyPulid` —— 8/12 个有
- `PulidEvaClipLoader` —— 8/12 个有
- `PulidModelLoader` —— 8/12 个有
- `Image Overlay` —— 2/12 个有
- `DapaoImageAspectRatioResizeNode` —— 1/12 个有
- `FaceDetailer` —— 1/12 个有
- `Image Comparer (rgthree)` —— 1/12 个有
- `LayerMask: MaskPreview` —— 1/12 个有
- `RepeatLatentBatch` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 10 | 12 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | euler_ancestral | - | 12 | 100% |
| 调度器 | sgm_uniform | - | 12 | 100% |
| 重绘幅度 | 0.5 | 0.5 - 0.5 | 12 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 10，12 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，12 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，12 个样本，一致性 100%
- 重绘幅度 中位数 0.5，观测区间 0.5 - 0.5，12 个样本，取值集中（一致性 100%）

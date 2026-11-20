---
name: unknown_workflow_controlnet_inpaint_upscale_2
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8574
common_nodes: [ApplyInstantID, BboxDetectorSEGS, CLIPTextEncode, CheckpointLoaderSimple, ControlNetLoader, Crop Face, DF_Image_scale_to_side, GrowMask, ImageComposite+, ImageCrop+, ImageResize+, ImageUpscaleWithModel, InpaintModelConditioning, InstantIDFaceAnalysis, InstantIDModelLoader, KSampler, Load RetinaFace, LoadImage, Mask Crop Region, MaskBlur+, PreviewImage, SAMDetectorCombined, SAMLoader, SaveImage, UltralyticsDetectorProvider, UpscaleModelLoader, VAEDecode]
problems: []
missing: []
members: [图片生成/图生图/Quick Face Swap_2062537685566312449.json, 图片生成/图生图/【CQ808】换脸-_2020057375142580226.json, 图片生成/图生图/一键换脸超高相似度换脸-InstantID_1909560735851315202.json, 图片生成/图生图/一键换脸超高相似度换脸-人像替换丨容貌替换丨面部迁移_1993840757727576065.json, 图片生成/图生图/模特换脸_lnstantiD_优化版_1953080359522136066.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_inpaint_upscale_2

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Quick Face Swap_2062537685566312449.json、图片生成/图生图/【CQ808】换脸-_2020057375142580226.json、图片生成/图生图/一键换脸超高相似度换脸-InstantID_1909560735851315202.json、图片生成/图生图/一键换脸超高相似度换脸-人像替换丨容貌替换丨面部迁移_1993840757727576065.json、图片生成/图生图/模特换脸_lnstantiD_优化版_1953080359522136066.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 5 个 workflow 都包含：
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
- `MaskToImage` —— 4/5 个有
- `ApplyPulid` —— 3/5 个有
- `PulidEvaClipLoader` —— 3/5 个有
- `PulidModelLoader` —— 3/5 个有
- `DapaoImageAspectRatioResizeNode` —— 1/5 个有
- `Image Overlay` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 10 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler_ancestral | - | 5 | 100% |
| 调度器 | sgm_uniform | - | 5 | 100% |
| 重绘幅度 | 0.5 | 0.5 - 0.5 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 10，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，5 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，5 个样本，一致性 100%
- 重绘幅度 中位数 0.5，观测区间 0.5 - 0.5，5 个样本，取值集中（一致性 100%）

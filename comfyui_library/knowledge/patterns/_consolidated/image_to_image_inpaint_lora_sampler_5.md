---
name: image_to_image_inpaint_lora_sampler_5
type: Image To Image
frequency: 4
level: strong
coverage: 0.86025
common_nodes: [ApplyPulidFlux, BboxDetectorSEGS, CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, GrowMaskWithBlur, Image Comparer (rgthree), ImageColorMatch+, ImageToMask, InpaintModelConditioning, JanusImageUnderstanding, JanusModelLoader, KSampler, LayerMask: MaskPreview, LayerMask: PersonMaskUltra V2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoader, MaskToImage, PreviewImage, PulidFluxEvaClipLoader, PulidFluxFaceDetector, PulidFluxInsightFaceLoader, PulidFluxModelLoader, PulidFluxOptions, SaveImage, SegsToCombinedMask, ShowText|pysssss, UNETLoader, UltralyticsDetectorProvider, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX+PULID 人物换脸进阶版工作流_2046978360336719874.json, 图片生成/图生图/FLUX+PULID_人物换脸进阶版_2064162963505901569.json, 图片生成/图生图/FLUX+PULID_人物换脸进阶版工作流_2063086878060007426.json, 图片生成/图生图/FLUX+PULID_人物换脸进阶版工作流_2063443764861030402.json]
source: knowledge_consolidation
---

# image_to_image_inpaint_lora_sampler_5

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/FLUX+PULID 人物换脸进阶版工作流_2046978360336719874.json、图片生成/图生图/FLUX+PULID_人物换脸进阶版_2064162963505901569.json、图片生成/图生图/FLUX+PULID_人物换脸进阶版工作流_2063086878060007426.json、图片生成/图生图/FLUX+PULID_人物换脸进阶版工作流_2063443764861030402.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 4 个 workflow 都包含：
- `ApplyPulidFlux`
- `BboxDetectorSEGS`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `ImageColorMatch+`
- `ImageToMask`
- `InpaintModelConditioning`
- `JanusImageUnderstanding`
- `JanusModelLoader`
- `KSampler`
- `LayerMask: MaskPreview`
- `LayerMask: PersonMaskUltra V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoader`
- `MaskToImage`
- `PreviewImage`
- `PulidFluxEvaClipLoader`
- `PulidFluxFaceDetector`
- `PulidFluxInsightFaceLoader`
- `PulidFluxModelLoader`
- `PulidFluxOptions`
- `SaveImage`
- `SegsToCombinedMask`
- `ShowText|pysssss`
- `UNETLoader`
- `UltralyticsDetectorProvider`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 0.7 | 0.7 - 0.7 | 4 | 100% |
| LoRA 模型强度 | 0.7 | 0.7 - 0.7 | 4 | 100% |
| LoRA 文本强度 | 0.7 | 0.7 - 0.7 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 0.7，观测区间 0.7 - 0.7，4 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.7，观测区间 0.7 - 0.7，4 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 0.7，观测区间 0.7 - 0.7，4 个样本，取值集中（一致性 100%）

---
name: text_to_image_inpaint_face_detailer_lora
type: Text To Image
frequency: 3
level: strong
coverage: 0.985
common_nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Text, ConditioningZeroOut, DifferentialDiffusion, DownloadAndLoadFlorence2Model, DualCLIPLoader, EmptyLatentImage, FaceDetailer, Florence2Run, FluxGuidance, GrowMaskWithBlur, ImageConcanate, ImageCrop+, ImageResize+, ImageToMask, InpaintCrop, InpaintModelConditioning, InpaintStitch, KSampler, LayerMask: LoadSegmentAnythingModels, LayerMask: SegmentAnythingUltra V3, LayerUtility: ColorImage, LayerUtility: CropByMask V2, LayerUtility: PurgeVRAM, LoadImage, LoraLoader, MaskToImage, ReduxAdvanced, SaveImage, StyleModelApply, StyleModelLoader, Text Concatenate, UNETLoader, UltralyticsDetectorProvider, VAEDecode, VAELoader, easy imageSize]
problems: []
missing: []
members: [图片生成/图生图/传输图片 产品试戴  多角度展示效果_2016164573182697473.json, 平台全量/帽子上身_1929823919572729858.json, 平台全量/帽子到模特多角度展示效果_1908433727792230401.json]
source: knowledge_consolidation
---

# text_to_image_inpaint_face_detailer_lora

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/传输图片 产品试戴  多角度展示效果_2016164573182697473.json、平台全量/帽子上身_1929823919572729858.json、平台全量/帽子到模特多角度展示效果_1908433727792230401.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Text`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `DownloadAndLoadFlorence2Model`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FaceDetailer`
- `Florence2Run`
- `FluxGuidance`
- `GrowMaskWithBlur`
- `ImageConcanate`
- `ImageCrop+`
- `ImageResize+`
- `ImageToMask`
- `InpaintCrop`
- `InpaintModelConditioning`
- `InpaintStitch`
- `KSampler`
- `LayerMask: LoadSegmentAnythingModels`
- `LayerMask: SegmentAnythingUltra V3`
- `LayerUtility: ColorImage`
- `LayerUtility: CropByMask V2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoader`
- `MaskToImage`
- `ReduxAdvanced`
- `SaveImage`
- `StyleModelApply`
- `StyleModelLoader`
- `Text Concatenate`
- `UNETLoader`
- `UltralyticsDetectorProvider`
- `VAEDecode`
- `VAELoader`
- `easy imageSize`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.5 | 0.5 - 0.5 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |
| 采样步数 | 28 | 28 - 28 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | normal | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 3 | 100% |
| 高度 | 1536 | 1536 - 1536 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.5，观测区间 0.5 - 0.5，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 28，观测区间 28 - 28，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 normal，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1536，观测区间 1536 - 1536，3 个样本，取值集中（一致性 100%）

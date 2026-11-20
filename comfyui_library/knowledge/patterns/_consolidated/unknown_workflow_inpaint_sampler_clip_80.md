---
name: unknown_workflow_inpaint_sampler_clip_80
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.623333
common_nodes: [APersonMaskGenerator, Any Switch (rgthree), CLIPTextEncode, CR Simple Image Compare, ConditioningZeroOut, DisplayAny, DualCLIPLoader, Fast Groups Bypasser (rgthree), FluxGuidance, Get Image Size, GetImageSize+, GetNode, GroundingDinoModelLoader (segment anything), GroundingDinoSAMSegment (segment anything), Image Comparer (rgthree), ImageToMask, InpaintCrop, InpaintModelConditioning, InpaintResize, InpaintStitch, KSampler, LayerMask: MaskGrow, LayerMask: PersonMaskUltra V2, LoadImage, MaskComposite, MaskToImage, SAMModelLoader (segment anything), SaveImage, SetNode, SimpleComparison+, SimpleCondition+, SimpleMath+, SimpleMathInt+, SimpleMathSlider+, SolidMask, StringFunction|pysssss, UNETLoader, VAEDecode, VAELoader, ttN text]
problems: []
missing: []
members: [图片生成/图生图/Flux磨皮-保留皮肤纹理真实感_1910203212941721602.json, 平台全量/Flux磨皮-保留皮肤纹理真实感_1904343717157703681.json, 平台全量/High-End Retouch with Flux Fill_1868907800964268033.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_80

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Flux磨皮-保留皮肤纹理真实感_1910203212941721602.json、平台全量/Flux磨皮-保留皮肤纹理真实感_1904343717157703681.json、平台全量/High-End Retouch with Flux Fill_1868907800964268033.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：62%

## 共有节点

全部 3 个 workflow 都包含：
- `APersonMaskGenerator`
- `Any Switch (rgthree)`
- `CLIPTextEncode`
- `CR Simple Image Compare`
- `ConditioningZeroOut`
- `DisplayAny`
- `DualCLIPLoader`
- `Fast Groups Bypasser (rgthree)`
- `FluxGuidance`
- `Get Image Size`
- `GetImageSize+`
- `GetNode`
- `GroundingDinoModelLoader (segment anything)`
- `GroundingDinoSAMSegment (segment anything)`
- `Image Comparer (rgthree)`
- `ImageToMask`
- `InpaintCrop`
- `InpaintModelConditioning`
- `InpaintResize`
- `InpaintStitch`
- `KSampler`
- `LayerMask: MaskGrow`
- `LayerMask: PersonMaskUltra V2`
- `LoadImage`
- `MaskComposite`
- `MaskToImage`
- `SAMModelLoader (segment anything)`
- `SaveImage`
- `SetNode`
- `SimpleComparison+`
- `SimpleCondition+`
- `SimpleMath+`
- `SimpleMathInt+`
- `SimpleMathSlider+`
- `SolidMask`
- `StringFunction|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `ttN text`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 2/3 个有
- `Bookmark (rgthree)` —— 1/3 个有
- `Fast Bypasser (rgthree)` —— 1/3 个有
- `Label (rgthree)` —— 1/3 个有
- `Lora Loader` —— 1/3 个有
- `MaskPreview+` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 1.01 | 1.01 - 1.01 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 0.4 | 0.4 - 0.4 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1.01，观测区间 1.01 - 1.01，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 0.4，观测区间 0.4 - 0.4，3 个样本，取值集中（一致性 100%）

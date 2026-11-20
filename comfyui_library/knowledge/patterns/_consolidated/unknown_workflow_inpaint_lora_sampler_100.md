---
name: unknown_workflow_inpaint_lora_sampler_100
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.816
common_nodes: [Anything Everywhere3, CLIPTextEncode, CLIPVisionLoader, CR Text, ConditioningZeroOut, DualCLIPLoader, Fast Groups Bypasser (rgthree), FluxGuidance, GrowMask, Image Comparer (rgthree), ImageAndMaskPreview, ImageCrop+, ImageMaskSwitch, ImageToMask, InpaintCrop, InpaintModelConditioning, InpaintResize, InpaintStitch, Int Literal, KSampler, LayerMask: SegformerB2ClothesUltra, LayerMask: SegmentAnythingUltra V2, LayerUtility: ColorPicker, LayerUtility: CropByMask V2, LayerUtility: ImageRemoveAlpha, LayerUtility: PurgeVRAM, LayerUtility: TextJoin, LoadAndResizeImage, LoadImage, LoraLoaderModelOnly, Mask Fill Holes, MaskPreview+, MaskToImage, PreviewImage, RH_LLMAPI_NODE, ReduxPromptStyler, SaveImage, ShowText|pysssss, StyleModelLoader, UNETLoader, VAEDecode, VAELoader, easy compare, easy makeImageForICLora]
problems: []
missing: []
members: [图片生成/图生图/换装工作流_1944673766569857026.json, 平台全量/Flux.1-Fill-OneRewar一键完美换装_1959869784093569026.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_100

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/换装工作流_1944673766569857026.json、平台全量/Flux.1-Fill-OneRewar一键完美换装_1959869784093569026.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere3`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CR Text`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `Fast Groups Bypasser (rgthree)`
- `FluxGuidance`
- `GrowMask`
- `Image Comparer (rgthree)`
- `ImageAndMaskPreview`
- `ImageCrop+`
- `ImageMaskSwitch`
- `ImageToMask`
- `InpaintCrop`
- `InpaintModelConditioning`
- `InpaintResize`
- `InpaintStitch`
- `Int Literal`
- `KSampler`
- `LayerMask: SegformerB2ClothesUltra`
- `LayerMask: SegmentAnythingUltra V2`
- `LayerUtility: ColorPicker`
- `LayerUtility: CropByMask V2`
- `LayerUtility: ImageRemoveAlpha`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: TextJoin`
- `LoadAndResizeImage`
- `LoadImage`
- `LoraLoaderModelOnly`
- `Mask Fill Holes`
- `MaskPreview+`
- `MaskToImage`
- `PreviewImage`
- `RH_LLMAPI_NODE`
- `ReduxPromptStyler`
- `SaveImage`
- `ShowText|pysssss`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy compare`
- `easy makeImageForICLora`

**可变部分**（部分 workflow 才有）：
- `easy bookmark` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 0.3 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 0.3，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

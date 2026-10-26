---
name: unknown_workflow_lora_sampler_unet_221
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.849333
common_nodes: [CFGGuider, CLIPLoader, ConditioningZeroOut, CropWithPadInfo_EditUtils, EditTextEncode_EditUtils, Flux2KleinConfigPreparer_EditUtils, Flux2KleinModelConfig_EditUtils, Flux2KleinOutputExtractor_EditUtils, Flux2Scheduler, Image Comparer (rgthree), KSamplerSelect, LoadImage, LoraLoaderModelOnly, PreviewImage, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/klein汽车图片车漆改色_2048755332972814337.json, 图片生成/图生图/一键去除水印高清极速版_2046154084654256130.json, 图片生成/图生图/单图强一致性编辑_2078743919415873537.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_221

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/klein汽车图片车漆改色_2048755332972814337.json、图片生成/图生图/一键去除水印高清极速版_2046154084654256130.json、图片生成/图生图/单图强一致性编辑_2078743919415873537.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `ConditioningZeroOut`
- `CropWithPadInfo_EditUtils`
- `EditTextEncode_EditUtils`
- `Flux2KleinConfigPreparer_EditUtils`
- `Flux2KleinModelConfig_EditUtils`
- `Flux2KleinOutputExtractor_EditUtils`
- `Flux2Scheduler`
- `Image Comparer (rgthree)`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AdaptiveLongestEdge_EditUtils` —— 2/3 个有
- `GetImageSize` —— 2/3 个有
- `PrimitiveInt` —— 2/3 个有
- `CR Value` —— 1/3 个有
- `GrowMask` —— 1/3 个有
- `ImpactConditionalBranch` —— 1/3 个有
- `InpaintCrop` —— 1/3 个有
- `InpaintStitch` —— 1/3 个有
- `Int` —— 1/3 个有
- `LayerMask: LoadSegmentAnythingModels` —— 1/3 个有
- `LayerMask: SegmentAnythingUltra V3` —— 1/3 个有
- `MaskPreview+` —— 1/3 个有
- `easy boolean` —— 1/3 个有
- `easy imageColorMatch` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

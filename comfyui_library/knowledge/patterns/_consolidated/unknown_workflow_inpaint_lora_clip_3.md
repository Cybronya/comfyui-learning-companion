---
name: unknown_workflow_inpaint_lora_clip_3
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8715
common_nodes: [BatchCount+, BboxDetectorCombined_v2, BlendInpaint, CLIPLoader, CLIPTextEncode, DetailerForEach, DownloadAndLoadFlorence2Model, Florence2Run, GrowMaskWithBlur, Image Comparer (rgthree), ImageAndMaskPreview, ImpactSEGSToMaskBatch, LayerUtility: CropByMask V2, LazySwitch1way, LoadImage, LoraLoaderModelOnly, Mask Fill Holes, MaskFromBatch+, MaskToSEGS, ModelSamplingSD3, PathchSageAttentionKJ, PreviewImage, SaveImage, String Literal, ToBinaryMask, UNETLoader, UltralyticsDetectorProvider, VAELoader, easy batchAnything, easy boolean, easy forLoopEnd, easy forLoopStart, easy imageSizeBySide, easy isMaskEmpty]
problems: []
missing: []
members: [图片生成/图生图/万物修复-工作流_1979758578909220866.json, 平台全量/修手工作流V2 可修万物_1975390312220766210.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_clip_3

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/万物修复-工作流_1979758578909220866.json、平台全量/修手工作流V2 可修万物_1975390312220766210.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 2 个 workflow 都包含：
- `BatchCount+`
- `BboxDetectorCombined_v2`
- `BlendInpaint`
- `CLIPLoader`
- `CLIPTextEncode`
- `DetailerForEach`
- `DownloadAndLoadFlorence2Model`
- `Florence2Run`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `ImageAndMaskPreview`
- `ImpactSEGSToMaskBatch`
- `LayerUtility: CropByMask V2`
- `LazySwitch1way`
- `LoadImage`
- `LoraLoaderModelOnly`
- `Mask Fill Holes`
- `MaskFromBatch+`
- `MaskToSEGS`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `SaveImage`
- `String Literal`
- `ToBinaryMask`
- `UNETLoader`
- `UltralyticsDetectorProvider`
- `VAELoader`
- `easy batchAnything`
- `easy boolean`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy imageSizeBySide`
- `easy isMaskEmpty`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere` —— 1/2 个有
- `Bjornulf_ShowInt` —— 1/2 个有
- `ImageToMask` —— 1/2 个有
- `MaskPreview+` —— 1/2 个有
- `MaskToImage` —— 1/2 个有
- `RHHiddenNodes` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

---
name: unknown_workflow_video_lora_sampler_706
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.5945
common_nodes: [Any Switch (rgthree), AutoCropFaces, BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, Fast Groups Bypasser (rgthree), Fast Muter (rgthree), GetImagesFromBatchIndexed, GetNode, GetVideoComponents, ImageConcatFromBatch, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, PreviewImage, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: [Fast Muter (rgthree), LayerUtility: SaveImagePlus]
members: [图片生成/图生图/2102282609287065601.json, 图片生成/图生图/Minimax h3 高一致性-人物四视图快速处理V2.0(PLUS)_2107343809830023169.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_706

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/2102282609287065601.json、图片生成/图生图/Minimax h3 高一致性-人物四视图快速处理V2.0(PLUS)_2107343809830023169.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：59%

## 共有节点

全部 2 个 workflow 都包含：
- `Any Switch (rgthree)`
- `AutoCropFaces`
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `Fast Groups Bypasser (rgthree)`
- `Fast Muter (rgthree)`
- `GetImagesFromBatchIndexed`
- `GetNode`
- `GetVideoComponents`
- `ImageConcatFromBatch`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `PreviewImage`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 1/2 个有
- `ImageConcatMulti` —— 1/2 个有
- `ImageScaleToTotalPixels` —— 1/2 个有
- `LayerUtility: SaveImagePlus` —— 1/2 个有
- `ResizeImageMaskNode` —— 1/2 个有
- `SaveImage` —— 1/2 个有
- `SaveImageAdvanced` —— 1/2 个有
- `SeedVR2LoadDiTModel` —— 1/2 个有
- `SeedVR2LoadVAEModel` —— 1/2 个有
- `SeedVR2VideoUpscaler` —— 1/2 个有
- `workflow>SeedVR放大节点` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：Fast Muter (rgthree)、LayerUtility: SaveImagePlus
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

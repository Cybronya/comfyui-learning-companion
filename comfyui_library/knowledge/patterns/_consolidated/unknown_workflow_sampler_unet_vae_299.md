---
name: unknown_workflow_sampler_unet_vae_299
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6785
common_nodes: [AILab_QwenVL, BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, GetImagesFromBatchIndexed, GetVideoComponents, HAIGC_SaveImagesToZip, ImageGrid, KSamplerSelect, MiniMaxH3ReferenceToVideo, MultiTextConcatenate, PreviewAny, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader, easy clearCacheAll]
problems: []
missing: []
members: [图片生成/图生图/h3 角色四视图设计-批量_2098362835725279234.json, 图片生成/图生图/h3 角色四视图设计_2094059970831675394.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_299

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/h3 角色四视图设计-批量_2098362835725279234.json、图片生成/图生图/h3 角色四视图设计_2094059970831675394.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：68%

## 共有节点

全部 2 个 workflow 都包含：
- `AILab_QwenVL`
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `GetImagesFromBatchIndexed`
- `GetVideoComponents`
- `HAIGC_SaveImagesToZip`
- `ImageGrid`
- `KSamplerSelect`
- `MiniMaxH3ReferenceToVideo`
- `MultiTextConcatenate`
- `PreviewAny`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy clearCacheAll`

**可变部分**（部分 workflow 才有）：
- `AutoCropFaces` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `ImageScaleBy` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `RHBatchImages:` —— 1/2 个有
- `RHExtractImage` —— 1/2 个有
- `RHUploadZip` —— 1/2 个有
- `VAEDecodeAudio` —— 1/2 个有
- `VHS_VideoCombine` —— 1/2 个有
- `ZML_PreviewImage` —— 1/2 个有
- `easy forLoopEnd` —— 1/2 个有
- `easy forLoopStart` —— 1/2 个有
- `easy imageCount` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

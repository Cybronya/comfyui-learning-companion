---
name: unknown_workflow_sampler_unet_vae_318
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.690333
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, GetImagesFromBatchIndexed, GetVideoComponents, ImageGrid, KSamplerSelect, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/h3 角色四视图设计-批量_2098362835725279234.json, 图片生成/图生图/h3 角色四视图设计_2094059970831675394.json, 平台全量/Minimax h3 高一致性-（人物四视图处理_2092452660359294978.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_318

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/h3 角色四视图设计-批量_2098362835725279234.json、图片生成/图生图/h3 角色四视图设计_2094059970831675394.json、平台全量/Minimax h3 高一致性-（人物四视图处理_2092452660359294978.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：69%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `GetImagesFromBatchIndexed`
- `GetVideoComponents`
- `ImageGrid`
- `KSamplerSelect`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL` —— 2/3 个有
- `AutoCropFaces` —— 2/3 个有
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `HAIGC_SaveImagesToZip` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `MultiTextConcatenate` —— 2/3 个有
- `PreviewAny` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `VAEDecodeAudio` —— 2/3 个有
- `VHS_VideoCombine` —— 2/3 个有
- `ZML_PreviewImage` —— 2/3 个有
- `easy clearCacheAll` —— 2/3 个有
- `ImageScaleBy` —— 1/3 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/3 个有
- `RHBatchImages:` —— 1/3 个有
- `RHExtractImage` —— 1/3 个有
- `RHUploadZip` —— 1/3 个有
- `easy forLoopEnd` —— 1/3 个有
- `easy forLoopStart` —— 1/3 个有
- `easy imageCount` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

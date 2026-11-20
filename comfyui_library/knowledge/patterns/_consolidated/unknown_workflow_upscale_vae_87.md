---
name: unknown_workflow_upscale_vae_87
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.702
common_nodes: [Bjornulf_ShowInt, PreviewImage, PrimitiveInt, RHBatchImages:, RHExtractImage, RHUploadZip, SaveImage, SeedVR2BlockSwap, SeedVR2ExtraArgs, SeedVR2GGUF, easy forLoopEnd, easy forLoopStart, easy imageCount, easy showAnything]
problems: []
missing: []
members: [平台全量/SeedVR-GGUF图像4K高清放大_1967554895995920385.json, 平台全量/SeedVR2.5图片批量高清放大_1991406880526454785.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_87

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/SeedVR-GGUF图像4K高清放大_1967554895995920385.json、平台全量/SeedVR2.5图片批量高清放大_1991406880526454785.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：70%

## 共有节点

全部 2 个 workflow 都包含：
- `Bjornulf_ShowInt`
- `PreviewImage`
- `PrimitiveInt`
- `RHBatchImages:`
- `RHExtractImage`
- `RHUploadZip`
- `SaveImage`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `SeedVR2GGUF`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy imageCount`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `SeedVR2LoadDiTModel` —— 1/2 个有
- `SeedVR2LoadVAEModel` —— 1/2 个有
- `SeedVR2VideoUpscaler` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有
- `easy imageSizeBySide` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

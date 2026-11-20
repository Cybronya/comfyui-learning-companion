---
name: unknown_workflow_upscale_vae_68
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.826
common_nodes: [Bjornulf_ShowInt, CompressImages, HYPIRImageRestoration, Image Comparer (rgthree), PreviewImage, RHBatchImages:, RHExtractImage, RHUploadZip, Ruyi_LoadModel, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, easy batchAnything, easy forLoopEnd, easy forLoopStart, easy imageCount, easy joinImageBatch, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/(zip)图片批量高清放大-seedvr2_1991826615334227970.json, 平台全量/444(zip)图片批量高清放大-seedvr2_2039609212464009218.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_68

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/(zip)图片批量高清放大-seedvr2_1991826615334227970.json、平台全量/444(zip)图片批量高清放大-seedvr2_2039609212464009218.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `Bjornulf_ShowInt`
- `CompressImages`
- `HYPIRImageRestoration`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `RHBatchImages:`
- `RHExtractImage`
- `RHUploadZip`
- `Ruyi_LoadModel`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `easy batchAnything`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy imageCount`
- `easy joinImageBatch`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `LoadImage` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

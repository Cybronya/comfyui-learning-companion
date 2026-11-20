---
name: unknown_workflow_upscale_vae_71
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8495
common_nodes: [GetImageSize, Image Comparer (rgthree), ImageFromBatch, ImageResize+, ImpactMinMax, Int, LoadImage, SaveImage, SimpleMath+, TTP_Image_Assy, TTP_Image_Tile_Batch, easy batchAnything, easy forLoopEnd, easy forLoopStart, easy imageCount, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/SeedVR2.5-最强分块高清放大（文字、图像统杀）_2016116788974587905.json, 平台全量/最强文字图像修复高清放大_1959437817124433922.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_71

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/SeedVR2.5-最强分块高清放大（文字、图像统杀）_2016116788974587905.json、平台全量/最强文字图像修复高清放大_1959437817124433922.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImageFromBatch`
- `ImageResize+`
- `ImpactMinMax`
- `Int`
- `LoadImage`
- `SaveImage`
- `SimpleMath+`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `easy batchAnything`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy imageCount`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `SeedVR2` —— 1/2 个有
- `SeedVR2LoadDiTModel` —— 1/2 个有
- `SeedVR2LoadVAEModel` —— 1/2 个有
- `SeedVR2VideoUpscaler` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

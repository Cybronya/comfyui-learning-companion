---
name: unknown_workflow_upscale_vae_51
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.776
common_nodes: [GetImageSize+, ImageCASharpening+, ImageResize+, ImageScaleBy, JjkText, LoadImage, RHLLMChatNode, RH_RhartImageG2ImageToImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, easy cleanGpuUsed, easy promptList, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/室内设计-辅助出图-最强全能图片Image2-8K高清图_2066460051233136641.json, 图片生成/图生图/室内设计生成分析图_2070787214996496385.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_51

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/室内设计-辅助出图-最强全能图片Image2-8K高清图_2066460051233136641.json、图片生成/图生图/室内设计生成分析图_2070787214996496385.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：78%

## 共有节点

全部 2 个 workflow 都包含：
- `GetImageSize+`
- `ImageCASharpening+`
- `ImageResize+`
- `ImageScaleBy`
- `JjkText`
- `LoadImage`
- `RHLLMChatNode`
- `RH_RhartImageG2ImageToImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `easy cleanGpuUsed`
- `easy promptList`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `PreviewAny` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

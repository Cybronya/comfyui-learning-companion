---
name: unknown_workflow_upscale_vae_85
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.913
common_nodes: [GetImageSize+, ImageResize+, ImageScaleBy, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, easy int]
problems: []
missing: []
members: [平台全量/4K放大_2062215192930504706.json, 平台全量/FlashVSR+SEEDVR2+TTP极速二亿像素放大_2063454131561521153.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_85

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/4K放大_2062215192930504706.json、平台全量/FlashVSR+SEEDVR2+TTP极速二亿像素放大_2063454131561521153.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `GetImageSize+`
- `ImageResize+`
- `ImageScaleBy`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `DapaoImageCompressionNode` —— 1/2 个有
- `FlashVSRNode` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `ImageCASharpening+` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `VRAMReserver` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有
- `忽略多组孤海` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

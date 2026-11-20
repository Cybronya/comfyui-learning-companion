---
name: unknown_workflow_upscale_vae_72
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6935
common_nodes: [Display Int (rgthree), Fast Groups Bypasser (rgthree), Image Comparer (rgthree), ImageCASharpening+, ImageResize+, ImpactInt, LayerFilter: GaussianBlur, LoadImage, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SimpleMath+, TTP_Image_Assy, TTP_Image_Tile_Batch, easy cleanGpuUsed, easy compare, easy ifElse, easy imageSizeByLongerSide, easy imageSizeBySide]
problems: []
missing: []
members: [图片生成/图生图/f10 SeedVR2 万物高清放大（自动计算分块数量优化）_2064631120456675329.json, 平台全量/SeedVR2 最强万物高清放大、不改细节（自动分块、降噪）_2001113157030604802.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_72

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/f10 SeedVR2 万物高清放大（自动计算分块数量优化）_2064631120456675329.json、平台全量/SeedVR2 最强万物高清放大、不改细节（自动分块、降噪）_2001113157030604802.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：69%

## 共有节点

全部 2 个 workflow 都包含：
- `Display Int (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `ImageCASharpening+`
- `ImageResize+`
- `ImpactInt`
- `LayerFilter: GaussianBlur`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SimpleMath+`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `easy cleanGpuUsed`
- `easy compare`
- `easy ifElse`
- `easy imageSizeByLongerSide`
- `easy imageSizeBySide`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `easy getNode` —— 1/2 个有
- `easy setNode` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

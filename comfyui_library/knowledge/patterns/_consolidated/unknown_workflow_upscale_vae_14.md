---
name: unknown_workflow_upscale_vae_14
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.82475
common_nodes: [Image Comparer (rgthree), ImageResize+, ImageScaleBy, LayerUtility: PurgeVRAM, LoadImage, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, easy imageSize]
problems: []
missing: []
members: [图片生成/图生图/8K高清放大  细节增强 极速修复 商业级大片  SeedVR2.5+TTP_2069588469764149250.json, 图片生成/图生图/TTP+seedVR2超分放大_2095679773157707777.json, 图片生成/图生图/TTP+seedVR2超分放大_2095690777207861249.json, 图片生成/图生图/TTP+seedVR2超分放大_2095743798902083585.json, 图片生成/图生图/亿万级像素_2086854199047970818.json, 图片生成/图生图/强大版 图片放大+FlashVSR+V1.1+SeedVR2_2062709441811800066.json, 图片生成/图生图/本地版_强大8K媲美商业级图片放大_FlashVSR_V1.1+SeedVR2.5_2096885620097507329.json, 图片生成/图生图/本地版_强大8K媲美商业级图片放大_FlashVSR_V1.1+SeedVR2.5_2097224470044954625.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_14

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/8K高清放大  细节增强 极速修复 商业级大片  SeedVR2.5+TTP_2069588469764149250.json、图片生成/图生图/TTP+seedVR2超分放大_2095679773157707777.json、图片生成/图生图/TTP+seedVR2超分放大_2095690777207861249.json、图片生成/图生图/TTP+seedVR2超分放大_2095743798902083585.json、图片生成/图生图/亿万级像素_2086854199047970818.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 8 个 workflow 都包含：
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImageScaleBy`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `TTP_Image_Tile_Batch` —— 5/8 个有
- `TTP_Tile_image_size` —— 5/8 个有
- `FlashVSRNode` —— 4/8 个有
- `ImageCASharpening+` —— 4/8 个有
- `ImpactFloat` —— 4/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/8 个有
- `easy int` —— 4/8 个有
- `RHHiddenNodes` —— 3/8 个有
- `VRAMReserver` —— 3/8 个有
- `easy cleanGpuUsed` —— 3/8 个有
- `easy showAnything` —— 3/8 个有
- `LayerUtility: ImageScaleRestore` —— 1/8 个有
- `LayerUtility: NumberCalculatorV2` —— 1/8 个有
- `LayerUtility: PurgeVRAM V2` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

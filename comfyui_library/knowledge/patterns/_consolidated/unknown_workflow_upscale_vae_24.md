---
name: unknown_workflow_upscale_vae_24
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.882
common_nodes: [GetImageSize+, Image Comparer (rgthree), ImageResize+, ImageScaleBy, LoadImage, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, easy imageScaleDownBy]
problems: []
missing: []
members: [图片生成/反推提示词/分块_扣图_反推SeedVR2常用工具集搭建好的含模型_2010003083014705154.json, 图片生成/图生图/SeedVR2模糊+变高清v2+支持4k8K出图_2044796576966643714.json, 图片生成/图生图/SeedVR2模糊变高清支持4k8K出图_2054196306217840642.json, 图片生成/图生图/SeedVR2模糊变高清支持4k8K出图_2054368025943519234.json, 图片生成/图生图/SeedVR2模糊变高清支持4k8K出图_2054411504459501570.json, 图片生成/图生图/模糊+变高清v2 支持4k_8K出图_2015651335382769666.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_24

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/反推提示词/分块_扣图_反推SeedVR2常用工具集搭建好的含模型_2010003083014705154.json、图片生成/图生图/SeedVR2模糊+变高清v2+支持4k8K出图_2044796576966643714.json、图片生成/图生图/SeedVR2模糊变高清支持4k8K出图_2054196306217840642.json、图片生成/图生图/SeedVR2模糊变高清支持4k8K出图_2054368025943519234.json、图片生成/图生图/SeedVR2模糊变高清支持4k8K出图_2054411504459501570.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 6 个 workflow 都包含：
- `GetImageSize+`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImageScaleBy`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `easy imageScaleDownBy`

**可变部分**（部分 workflow 才有）：
- `Float` —— 5/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/6 个有
- `easy cleanGpuUsed` —— 5/6 个有
- `easy clearCacheAll` —— 5/6 个有
- `Qwen3_VQA` —— 1/6 个有
- `RMBG` —— 1/6 个有
- `ShowText|pysssss` —— 1/6 个有
- `VHS_LoadVideo` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

---
name: unknown_workflow_upscale_vae_10
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.812462
common_nodes: [GetImageSize+, Image Comparer (rgthree), ImageResize+, ImageScaleBy, LoadImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size]
problems: []
missing: []
members: [图片生成/图生图/SeedVR2模糊+变高清v2+支持4k8K出图_2044796576966643714.json, 图片生成/图生图/SeedVR2模糊变高清支持4k8K出图_2054196306217840642.json, 图片生成/图生图/SeedVR2模糊变高清支持4k8K出图_2054368025943519234.json, 图片生成/图生图/SeedVR2模糊变高清支持4k8K出图_2054411504459501570.json, 图片生成/图生图/⭐️⭐️⭐️⭐️⭐️——TTP+seed VR2放大（亿级像素）_2008476095489777666.json, 图片生成/图生图/一亿像素极速放大【seedvr2分块放大】_1993128037634031617.json, 图片生成/图生图/图像8K放大-不变形_2004662548261728258.json, 图片生成/图生图/图片高清放大_SeedVR2放大_2077948514235142145.json, 图片生成/图生图/无损8k放大_2095771047361605633.json, 图片生成/图生图/无损8k放大_2096064513807306754.json, 图片生成/图生图/星绘-超清SeedVR2+无损耗压缩_2015623404509990914.json, 图片生成/图生图/模糊+变高清v2 支持4k_8K出图_2015651335382769666.json, 图片生成/图生图/（超好用！）SeedVR2+TTP一亿像素极限放大+0损耗压缩_2004539129138475009.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_10

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/SeedVR2模糊+变高清v2+支持4k8K出图_2044796576966643714.json、图片生成/图生图/SeedVR2模糊变高清支持4k8K出图_2054196306217840642.json、图片生成/图生图/SeedVR2模糊变高清支持4k8K出图_2054368025943519234.json、图片生成/图生图/SeedVR2模糊变高清支持4k8K出图_2054411504459501570.json、图片生成/图生图/⭐️⭐️⭐️⭐️⭐️——TTP+seed VR2放大（亿级像素）_2008476095489777666.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 13 个 workflow 都包含：
- `GetImageSize+`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImageScaleBy`
- `LoadImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/13 个有
- `PreviewImage` —— 7/13 个有
- `Float` —— 6/13 个有
- `KOOK_ImageCompression` —— 5/13 个有
- `easy cleanGpuUsed` —— 5/13 个有
- `easy clearCacheAll` —— 5/13 个有
- `easy imageScaleDownBy` —— 5/13 个有
- `easy showAnything` —— 5/13 个有
- `Fast Groups Bypasser (rgthree)` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

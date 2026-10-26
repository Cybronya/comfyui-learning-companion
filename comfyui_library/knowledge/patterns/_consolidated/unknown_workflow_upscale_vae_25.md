---
name: unknown_workflow_upscale_vae_25
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.739333
common_nodes: [LoadImage, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler]
problems: []
missing: []
members: [图片生成/图生图/-全能图片V2 图像编辑_1991491723134246914.json, 图片生成/图生图/007.其他-功能风格004.SeedVR2 高清图片修复_2035402510206242818.json, 图片生成/图生图/007.其他-功能风格005.批量SeedVR2 高清图片修复_2035403955248832513.json, 图片生成/图生图/SeedVR-2高清修复_2077567322830757890.json, 图片生成/图生图/SeedVR-2高清修复_2077670806905253889.json, 图片生成/图生图/SeedVR2图像4K放大_2089291110207279106.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_25

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/-全能图片V2 图像编辑_1991491723134246914.json、图片生成/图生图/007.其他-功能风格004.SeedVR2 高清图片修复_2035402510206242818.json、图片生成/图生图/007.其他-功能风格005.批量SeedVR2 高清图片修复_2035403955248832513.json、图片生成/图生图/SeedVR-2高清修复_2077567322830757890.json、图片生成/图生图/SeedVR-2高清修复_2077670806905253889.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：74%

## 共有节点

全部 6 个 workflow 都包含：
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 5/6 个有
- `ImageScaleBy` —— 3/6 个有
- `easy imageScaleDownToSize` —— 2/6 个有
- `RB_LoadImagesFromDir` —— 1/6 个有
- `RH_Nano_Banana2_Image2Image` —— 1/6 个有
- `VOSR2ModelLoader` —— 1/6 个有
- `VOSR2Upscale` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

---
name: unknown_workflow_upscale_vae_8
type: Unknown Workflow
frequency: 16
level: moderate
coverage: 0.772938
common_nodes: [LoadImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler]
problems: []
missing: []
members: [图片生成/图生图/007.其他-功能风格006.图像4K高清放大_2035404694134202370.json, 图片生成/图生图/251207-07.图像4K高清放大_1997726954667356161.json, 图片生成/图生图/2SeedVR2图像4K放大_1996540812534104065.json, 图片生成/图生图/4K高清放大_1915284920053202946.json, 图片生成/图生图/70.tonnie-SeedVR2.5高清放大_2010320101618229250.json, 图片生成/图生图/SEEDVR2放大 图像放大到2K  接入SD-PPP实现 SEEDVR2.5放大_2075057559576338434.json, 图片生成/图生图/SeedVR-2高清修复_2077567322830757890.json, 图片生成/图生图/SeedVR-2高清修复_2077670806905253889.json, 图片生成/图生图/SeedVR2 高清放大_2058824859437850625.json, 图片生成/图生图/SeedVR2 高清放大_2066866184934481922.json, 图片生成/图生图/SeedVR2 高清放大_2094591496115806210.json, 图片生成/图生图/SeedVR2.5_4K_图像4K高清放大_1997923965844750337.json, 图片生成/图生图/SeedVR2.5_图像4K高清放大_1997976745368281090.json, 图片生成/图生图/图像4K高清放大：SeedVR2.5_4K_image_upscale_1997861575845457921.json, 平台全量/【SeedVR2.5】图像4K高清放大_2000154178695593986.json, 平台全量/高清修复_2047861801844482050.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_8

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/图生图/007.其他-功能风格006.图像4K高清放大_2035404694134202370.json、图片生成/图生图/251207-07.图像4K高清放大_1997726954667356161.json、图片生成/图生图/2SeedVR2图像4K放大_1996540812534104065.json、图片生成/图生图/4K高清放大_1915284920053202946.json、图片生成/图生图/70.tonnie-SeedVR2.5高清放大_2010320101618229250.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 16 个 workflow 都包含：
- `LoadImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 11/16 个有
- `PreviewImage` —— 10/16 个有
- `JoinImageWithAlpha` —— 6/16 个有
- `ImageScaleBy` —— 4/16 个有
- `ImageScaleRestore_UTK` —— 4/16 个有
- `easy int` —— 4/16 个有
- `easy imageScaleDownToSize` —— 3/16 个有
- `Label (rgthree)` —— 1/16 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

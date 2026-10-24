---
name: unknown_workflow_upscale_vae_31
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.77775
common_nodes: [Image Comparer (rgthree), ImageScaleToTotalPixels, LoadImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler]
problems: []
missing: []
members: [图片生成/图生图/B5、SeedVR2 V2 + 放大模型  —— 和风整理_2008398304526209026.json, 图片生成/图生图/SeedVR2-高清放大_2057666509887074306.json, 图片生成/图生图/SeedVR2高清放大工作流_1991362449412829185.json, 图片生成/图生图/图像无损高清放大4K工作流_2050512834345349121.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_31

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/B5、SeedVR2 V2 + 放大模型  —— 和风整理_2008398304526209026.json、图片生成/图生图/SeedVR2-高清放大_2057666509887074306.json、图片生成/图生图/SeedVR2高清放大工作流_1991362449412829185.json、图片生成/图生图/图像无损高清放大4K工作流_2050512834345349121.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 4 个 workflow 都包含：
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 2/4 个有
- `ImageUpscaleWithModel` —— 2/4 个有
- `UpscaleModelLoader` —— 2/4 个有
- `easy int` —— 2/4 个有
- `ColorMatch` —— 1/4 个有
- `Int` —— 1/4 个有
- `PreviewImage` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

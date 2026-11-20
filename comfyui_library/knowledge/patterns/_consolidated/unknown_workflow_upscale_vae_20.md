---
name: unknown_workflow_upscale_vae_20
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.892286
common_nodes: [LoadImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler]
problems: []
missing: []
members: [图片生成/图生图/SeedVR2-图片放大-高清直出_2063278464265965569.json, 图片生成/图生图/SeedVR2.5.10 Q8图像高清放大修复极速版_1996047712917372930.json, 图片生成/图生图/SeedVR2.5.10 Q8图像高清放大修复极速版_2080511002810085377.json, 图片生成/图生图/SeedVR2VideoUpscaler角色定妆照-高清细节重建+全节点注释_2042469777528066049.json, 图片生成/图生图/seedvr2高清放大-标准版-（必收藏）_2051678904477331457.json, 图片生成/图生图/seedvr2高清放大_标准版_（必收藏）_2051853967776337921.json, 图片生成/图生图/视频放大超清修复_2029498990739333122.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_20

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/SeedVR2-图片放大-高清直出_2063278464265965569.json、图片生成/图生图/SeedVR2.5.10 Q8图像高清放大修复极速版_1996047712917372930.json、图片生成/图生图/SeedVR2.5.10 Q8图像高清放大修复极速版_2080511002810085377.json、图片生成/图生图/SeedVR2VideoUpscaler角色定妆照-高清细节重建+全节点注释_2042469777528066049.json、图片生成/图生图/seedvr2高清放大-标准版-（必收藏）_2051678904477331457.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 7 个 workflow 都包含：
- `LoadImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`

**可变部分**（部分 workflow 才有）：
- `Int` —— 5/7 个有
- `ImageScaleToTotalPixels` —— 3/7 个有
- `MathExpression|pysssss` —— 2/7 个有
- `PreviewImage` —— 2/7 个有
- `Label (rgthree)` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

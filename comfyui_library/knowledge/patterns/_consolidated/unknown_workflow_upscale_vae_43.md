---
name: unknown_workflow_upscale_vae_43
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.775
common_nodes: [Image Comparer (rgthree), LoadImage, PrimitiveFloat, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SimpleMath+]
problems: []
missing: []
members: [图片生成/图生图/SeedVR2 高清修复放大_2112095231582760962.json, 图片生成/图生图/SeedVR2.5图片高清放大_2000567352251084802.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_43

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/SeedVR2 高清修复放大_2112095231582760962.json、图片生成/图生图/SeedVR2.5图片高清放大_2000567352251084802.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：78%

## 共有节点

全部 2 个 workflow 都包含：
- `Image Comparer (rgthree)`
- `LoadImage`
- `PrimitiveFloat`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SimpleMath+`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 1/2 个有
- `ImpactCompare` —— 1/2 个有
- `LayerUtility: If ` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有
- `easy imageSizeBySide` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

---
name: unknown_workflow_upscale_vae_59
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.834
common_nodes: [Image Comparer (rgthree), LoadImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, easy cleanGpuUsed, easy clearCacheAll, easy int]
problems: []
missing: []
members: [图片生成/图生图/表情迁移工作流（AdvancedLivePortrait+seedvr2）_2059644545025007617.json, 数字人/数字人/YJ-APP-SeedVR2.5高清放大_2038204911585857538.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_59

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/表情迁移工作流（AdvancedLivePortrait+seedvr2）_2059644545025007617.json、数字人/数字人/YJ-APP-SeedVR2.5高清放大_2038204911585857538.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `Image Comparer (rgthree)`
- `LoadImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `ExpressionEditor` —— 1/2 个有
- `ImageResize+` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `ResizeImagesByLongerEdge` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

---
name: unknown_workflow_upscale_vae_52
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.8
common_nodes: [Image Comparer (rgthree), LoadImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, easy cleanGpuUsed, easy clearCacheAll, easy int]
problems: []
missing: []
members: [图片生成/图生图/表情迁移工作流（AdvancedLivePortrait+seedvr2）_2059644545025007617.json, 平台全量/SeedVR2.5最新版高清放大工作流_2093678835450601474.json, 平台全量/SeedVR2.5最新版高清放大工作流_2120502993173958658.json, 平台全量/SeedVR2.5高清放大工作流 V1.0_2030856936375193601.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_52

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/表情迁移工作流（AdvancedLivePortrait+seedvr2）_2059644545025007617.json、平台全量/SeedVR2.5最新版高清放大工作流_2093678835450601474.json、平台全量/SeedVR2.5最新版高清放大工作流_2120502993173958658.json、平台全量/SeedVR2.5高清放大工作流 V1.0_2030856936375193601.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 4 个 workflow 都包含：
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
- `PreviewImage` —— 2/4 个有
- `ResizeImagesByLongerEdge` —— 2/4 个有
- `ExpressionEditor` —— 1/4 个有
- `ImageResize+` —— 1/4 个有
- `ImageScaleToTotalPixels` —— 1/4 个有
- `JoinImageWithAlpha` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

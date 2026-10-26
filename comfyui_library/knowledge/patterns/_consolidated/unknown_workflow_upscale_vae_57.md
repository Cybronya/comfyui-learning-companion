---
name: unknown_workflow_upscale_vae_57
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9
common_nodes: [LayerUtility: PurgeVRAM V2, LoadImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, easy int]
problems: []
missing: []
members: [图片生成/图生图/电商水彩画类型专用_放大5900（T恤定制 300 DPI）_2078689075812454402.json, 图片生成/图生图/细节爆炸！让你的图片从“能看”到“震撼”！双重无损高清放大SeedVR2.5_2062500413340995585.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_57

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/电商水彩画类型专用_放大5900（T恤定制 300 DPI）_2078689075812454402.json、图片生成/图生图/细节爆炸！让你的图片从“能看”到“震撼”！双重无损高清放大SeedVR2.5_2062500413340995585.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

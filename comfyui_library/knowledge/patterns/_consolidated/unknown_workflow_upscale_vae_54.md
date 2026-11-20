---
name: unknown_workflow_upscale_vae_54
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.9335
common_nodes: [CreateVideo, GetVideoComponents, LoadVideo, SaveVideo, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2TorchCompileSettings, SeedVR2VideoUpscaler]
problems: []
missing: []
members: [平台全量/SeedVR2-Video_2077272747109081089.json, 平台全量/SeedVR2-Video_2120494825874214913.json, 平台全量/SeedVR2无损高清放大，支持4倍放大_2029397196180824065.json, 平台全量/SeedVR2无损高清放大，支持4倍放大_2064610668040511490.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_54

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/SeedVR2-Video_2077272747109081089.json、平台全量/SeedVR2-Video_2120494825874214913.json、平台全量/SeedVR2无损高清放大，支持4倍放大_2029397196180824065.json、平台全量/SeedVR2无损高清放大，支持4倍放大_2064610668040511490.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 4 个 workflow 都包含：
- `CreateVideo`
- `GetVideoComponents`
- `LoadVideo`
- `SaveVideo`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2TorchCompileSettings`
- `SeedVR2VideoUpscaler`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 2/4 个有
- `ImageScaleToTotalPixels` —— 2/4 个有
- `LoadImage` —— 2/4 个有
- `SaveImage` —— 2/4 个有
- `easy int` —— 2/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

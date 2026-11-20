---
name: unknown_workflow_upscale_vae_42
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9302
common_nodes: [CreateVideo, GetVideoComponents, LoadVideo, SaveVideo, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler]
problems: []
missing: []
members: [平台全量/SeedVR2视频放大_1996539516238307329.json, 平台全量/Seedvr2视频放大工作流_2086761854814216194.json, 平台全量/Y-SeedVR2视频高清放大_2003014350837301249.json, 平台全量/【阡陌】SeedVR 2.5 视频超高清放大工作流_2013232523886731266.json, 平台全量/视频高清放大_2040254439273009154.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_42

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/SeedVR2视频放大_1996539516238307329.json、平台全量/Seedvr2视频放大工作流_2086761854814216194.json、平台全量/Y-SeedVR2视频高清放大_2003014350837301249.json、平台全量/【阡陌】SeedVR 2.5 视频超高清放大工作流_2013232523886731266.json、平台全量/视频高清放大_2040254439273009154.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 5 个 workflow 都包含：
- `CreateVideo`
- `GetVideoComponents`
- `LoadVideo`
- `SaveVideo`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`

**可变部分**（部分 workflow 才有）：
- `JoinImageWithAlpha` —— 2/5 个有
- `SeedVR2TorchCompileSettings` —— 2/5 个有
- `LoadImage` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

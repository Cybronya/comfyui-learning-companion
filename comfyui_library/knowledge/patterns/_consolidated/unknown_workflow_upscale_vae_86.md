---
name: unknown_workflow_upscale_vae_86
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9
common_nodes: [CreateVideo, SaveVideo, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, VHS_LoadVideo, VHS_VideoInfo, easy int]
problems: []
missing: []
members: [平台全量/4K超清视频放大修复-SeedVR2_HD_2095883965432422401.json, 平台全量/SeedVR2 4K电影级视频超分放大｜画质救星_2096074942797406210.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_86

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/4K超清视频放大修复-SeedVR2_HD_2095883965432422401.json、平台全量/SeedVR2 4K电影级视频超分放大｜画质救星_2096074942797406210.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `CreateVideo`
- `SaveVideo`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `VHS_LoadVideo`
- `VHS_VideoInfo`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

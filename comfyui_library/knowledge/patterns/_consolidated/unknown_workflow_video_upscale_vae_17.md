---
name: unknown_workflow_video_upscale_vae_17
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8635
common_nodes: [Fast Groups Bypasser (rgthree), LayerUtility: PurgeVRAM, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, easy imageSize, easy int]
problems: []
missing: []
members: [平台全量/常用：视频超分放大_SeedVR2 _ FlashVSR_2055912717944401922.json, 平台全量/视频超分放大_SeedVR2 _ FlashVSR_1999548092301144065.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_vae_17

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/常用：视频超分放大_SeedVR2 _ FlashVSR_2055912717944401922.json、平台全量/视频超分放大_SeedVR2 _ FlashVSR_1999548092301144065.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `Fast Groups Bypasser (rgthree)`
- `LayerUtility: PurgeVRAM`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `easy imageSize`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `FlashVSRNode` —— 1/2 个有
- `LayerUtility: PurgeVRAM V2` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

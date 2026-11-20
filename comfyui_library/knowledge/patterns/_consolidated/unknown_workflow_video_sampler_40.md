---
name: unknown_workflow_video_sampler_40
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.77475
common_nodes: [Fast Groups Bypasser (rgthree), FlashVSRNode, FlashVSR_SM_KSampler, FlashVSR_SM_Model, ImageConcatMulti, ImageScaleToTotalPixels, JWInteger, LayerUtility: PurgeVRAM V2, Reroute (rgthree), VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo]
problems: []
missing: []
members: [平台全量/FlashVSR ThePAI电商视频超分高清修复 video super resolution_2009210646763675649.json, 平台全量/FlashVSR视频超分高清修复 安静自用版_2001682455654461442.json, 平台全量/极速低显存 视频分辨率修复_1999374132347273218.json, 视频生成/图生视频/FlashVSR视频超分高清修复【Ultra-Fast】_1996999051935694849.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_40

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/FlashVSR ThePAI电商视频超分高清修复 video super resolution_2009210646763675649.json、平台全量/FlashVSR视频超分高清修复 安静自用版_2001682455654461442.json、平台全量/极速低显存 视频分辨率修复_1999374132347273218.json、视频生成/图生视频/FlashVSR视频超分高清修复【Ultra-Fast】_1996999051935694849.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 4 个 workflow 都包含：
- `Fast Groups Bypasser (rgthree)`
- `FlashVSRNode`
- `FlashVSR_SM_KSampler`
- `FlashVSR_SM_Model`
- `ImageConcatMulti`
- `ImageScaleToTotalPixels`
- `JWInteger`
- `LayerUtility: PurgeVRAM V2`
- `Reroute (rgthree)`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 1.35572e+09 | 1.73646e+08 - 1.81398e+09 | 4 | 43% |
| Prompt 约束强度(CFG) | randomize | - | 4 | 100% |
| 采样算法 | 2 | 2 - 2 | 4 | 100% |
| 调度器 | 3.5 | 3.5 - 3.5 | 4 | 100% |
| 重绘幅度 | 11 | 11 - 11 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 1.35572e+09，观测区间 1.73646e+08 - 1.81398e+09，4 个样本，取值分散，一致性仅 43%
- Prompt 约束强度(CFG) 最常用 randomize，4 个样本，一致性 100%
- 采样算法 中位数 2，观测区间 2 - 2，4 个样本，取值集中（一致性 100%）
- 调度器 中位数 3.5，观测区间 3.5 - 3.5，4 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 11，观测区间 11 - 11，4 个样本，取值集中（一致性 100%）
- 风险：采样步数 观测到 1.81398e+09，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
- 风险：重绘幅度 观测到 11，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）

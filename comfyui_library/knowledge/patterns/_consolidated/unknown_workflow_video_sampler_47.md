---
name: unknown_workflow_video_sampler_47
type: Unknown Workflow
frequency: 3
level: strong
coverage: 1
common_nodes: [FlashVSR_SM_KSampler, FlashVSR_SM_Model, LayerUtility: ImageScaleByAspectRatio V2, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, easy int]
problems: []
missing: []
members: [平台全量/FlashVSR视频超分工作流_2080283446794088449.json, 平台全量/快速视频放大_2087542111943090178.json, 平台全量/视频超分放大-FlashVSR 工作流_2071153346395860994.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_47

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/FlashVSR视频超分工作流_2080283446794088449.json、平台全量/快速视频放大_2087542111943090178.json、平台全量/视频超分放大-FlashVSR 工作流_2071153346395860994.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 3 个 workflow 都包含：
- `FlashVSR_SM_KSampler`
- `FlashVSR_SM_Model`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `ImageFromBatch` —— 2/3 个有
- `easy mathInt` —— 2/3 个有
- `GetImageSize` —— 1/3 个有
- `ImageBatch` —— 1/3 个有
- `RepeatImageBatch` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 1.17211e+09 | 7.59213e+08 - 1.17211e+09 | 3 | 81% |
| Prompt 约束强度(CFG) | fixed | - | 3 | 100% |
| 采样算法 | 2 | 1 - 2 | 3 | 72% |
| 调度器 | 3.5 | 3.5 - 3.5 | 3 | 100% |
| 重绘幅度 | 11 | 11 - 11 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 1.17211e+09，观测区间 7.59213e+08 - 1.17211e+09，3 个样本，取值集中（一致性 81%）
- Prompt 约束强度(CFG) 最常用 fixed，3 个样本，一致性 100%
- 采样算法 中位数 2，观测区间 1 - 2，3 个样本
- 调度器 中位数 3.5，观测区间 3.5 - 3.5，3 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 11，观测区间 11 - 11，3 个样本，取值集中（一致性 100%）
- 风险：采样步数 观测到 1.17211e+09，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
- 风险：重绘幅度 观测到 11，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）

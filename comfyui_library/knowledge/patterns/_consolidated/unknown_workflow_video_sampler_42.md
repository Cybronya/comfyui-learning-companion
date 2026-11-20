---
name: unknown_workflow_video_sampler_42
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.97225
common_nodes: [FlashVSR_SM_KSampler, FlashVSR_SM_Model, LayerUtility: ImageScaleByAspectRatio V2, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded]
problems: []
missing: []
members: [平台全量/修复+补帧-个人用_2004576209289834497.json, 平台全量/全能视频S视频提升清晰度_1998563887043739650.json, 平台全量/全能视频S视频提升清晰度_2005809626346127362.json, 平台全量/全能视频S高清修复_1982083939735093249.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_42

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/修复+补帧-个人用_2004576209289834497.json、平台全量/全能视频S视频提升清晰度_1998563887043739650.json、平台全量/全能视频S视频提升清晰度_2005809626346127362.json、平台全量/全能视频S高清修复_1982083939735093249.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 4 个 workflow 都包含：
- `FlashVSR_SM_KSampler`
- `FlashVSR_SM_Model`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`

**可变部分**（部分 workflow 才有）：
- `GetImageRangeFromBatch` —— 1/4 个有
- `Image Comparer (rgthree)` —— 1/4 个有
- `ImageGaussianBlur` —— 1/4 个有
- `RIFE VFI` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 3.73819e+08 | 4.50549e+07 - 1.31132e+09 | 4 | 10% |
| Prompt 约束强度(CFG) | randomize | - | 4 | 100% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | 3.5 | 3.5 - 3.5 | 4 | 100% |
| 重绘幅度 | 11 | 11 - 11 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 3.73819e+08，观测区间 4.50549e+07 - 1.31132e+09，4 个样本，取值分散，一致性仅 10%
- Prompt 约束强度(CFG) 最常用 randomize，4 个样本，一致性 100%
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 中位数 3.5，观测区间 3.5 - 3.5，4 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 11，观测区间 11 - 11，4 个样本，取值集中（一致性 100%）
- 风险：采样步数 观测到 1.31132e+09，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
- 风险：重绘幅度 观测到 11，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）

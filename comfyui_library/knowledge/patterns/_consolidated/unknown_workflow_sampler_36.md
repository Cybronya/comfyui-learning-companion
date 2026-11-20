---
name: unknown_workflow_sampler_36
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 1
common_nodes: [CreateVideo, FlashVSR_SM_KSampler, FlashVSR_SM_Model, GetVideoComponents, LoadVideo, SaveVideo]
problems: []
missing: []
members: [平台全量/FlashVSR满血版工作流横屏版_1983501218616123393.json, 平台全量/FlashVSR满血版工作流，一键把模糊视频变高清_1981973629233709057.json, 平台全量/视频2倍修复_2017198046089580545.json, 平台全量/视频2倍修复_2017242484832735233.json, 视频生成/图生视频/视频高清工作流_1992846680425033730.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_36

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/FlashVSR满血版工作流横屏版_1983501218616123393.json、平台全量/FlashVSR满血版工作流，一键把模糊视频变高清_1981973629233709057.json、平台全量/视频2倍修复_2017198046089580545.json、平台全量/视频2倍修复_2017242484832735233.json、视频生成/图生视频/视频高清工作流_1992846680425033730.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 5 个 workflow 都包含：
- `CreateVideo`
- `FlashVSR_SM_KSampler`
- `FlashVSR_SM_Model`
- `GetVideoComponents`
- `LoadVideo`
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `DF_Get_image_size` —— 2/5 个有
- `DF_Image_scale_to_side` —— 2/5 个有
- `Label (rgthree)` —— 2/5 个有
- `easy cleanGpuUsed` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 1.49834e+09 | 666 - 1.86602e+09 | 5 | 18% |
| Prompt 约束强度(CFG) | fixed | - | 5 | 80% |
| 采样算法 | 1 | 1 - 2 | 5 | 67% |
| 调度器 | 3.5 | 3.5 - 3.5 | 5 | 100% |
| 重绘幅度 | 7 | 7 - 11 | 5 | 77% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 1.49834e+09，观测区间 666 - 1.86602e+09，5 个样本，取值分散，一致性仅 18%
- Prompt 约束强度(CFG) 最常用 fixed，5 个样本，一致性 80%
- 采样算法 中位数 1，观测区间 1 - 2，5 个样本
- 调度器 中位数 3.5，观测区间 3.5 - 3.5，5 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 7，观测区间 7 - 11，5 个样本
- 风险：采样步数 观测到 1.86602e+09，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
- 风险：重绘幅度 观测到 11，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）

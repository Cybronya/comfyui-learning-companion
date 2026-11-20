---
name: unknown_workflow_video_sampler_70
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.932
common_nodes: [FlashVSR_SM_KSampler, FlashVSR_SM_Model, Label (rgthree), VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo]
problems: []
missing: []
members: [平台全量/FlashVSR视频超分高质量工作流(推荐)_1981035696435642369.json, 平台全量/FlsahVSR超分高清放大工作流快速版_1980919129639178241.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_70

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/FlashVSR视频超分高质量工作流(推荐)_1981035696435642369.json、平台全量/FlsahVSR超分高清放大工作流快速版_1980919129639178241.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `FlashVSR_SM_KSampler`
- `FlashVSR_SM_Model`
- `Label (rgthree)`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`

**可变部分**（部分 workflow 才有）：
- `FlashVSRNode` —— 1/2 个有
- `GetImageSize+` —— 1/2 个有
- `ImageConcatMulti` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9.33011e+08 | - | 2 | 0% |
| Prompt 约束强度(CFG) | 0 | - | 1 | 100% |
| 采样算法 | 2 | - | 1 | 100% |
| 调度器 | 3.75 | - | 2 | 93% |
| 重绘幅度 | 7.25 | - | 2 | 48% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 9.33011e+08，样本不足，未给区间，2 个样本，取值分散，一致性仅 0%
- 调度器 中位数 3.75，样本不足，未给区间，2 个样本，取值集中（一致性 93%）
- 重绘幅度 中位数 7.25，样本不足，未给区间，2 个样本，取值分散，一致性仅 48%
- 风险：采样步数 观测到 1.86602e+09，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
- 风险：Prompt 约束强度(CFG) 观测到 0，低于常用下限 1（CFG 过低可能导致 Prompt 约束不足、结果偏离描述）
- 风险：重绘幅度 观测到 11，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

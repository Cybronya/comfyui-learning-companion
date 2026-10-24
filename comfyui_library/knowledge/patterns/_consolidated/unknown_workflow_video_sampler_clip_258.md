---
name: unknown_workflow_video_sampler_clip_258
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.923
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, KSampler (Efficient), LoadImage, ModelSamplingSD3, Seed Everywhere, VHS_VideoCombine, WanVaceToVideo, WanVideoVACEStartToEndFrame, easy imageScaleDownToSize]
problems: []
missing: []
members: [视频生成/图生视频/一键运行：Wan2.2 WAN2.2-14B-Rapid-AlO Mega V7 图生视频_1977560592129118209.json, 视频生成/图生视频/首尾帧 Wan2.2 WAN2.2-14B-Rapid-AlO Mega V7_1977916445906665474.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_258

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/一键运行：Wan2.2 WAN2.2-14B-Rapid-AlO Mega V7 图生视频_1977560592129118209.json、视频生成/图生视频/首尾帧 Wan2.2 WAN2.2-14B-Rapid-AlO Mega V7_1977916445906665474.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `KSampler (Efficient)`
- `LoadImage`
- `ModelSamplingSD3`
- `Seed Everywhere`
- `VHS_VideoCombine`
- `WanVaceToVideo`
- `WanVideoVACEStartToEndFrame`
- `easy imageScaleDownToSize`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | sa_solver | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 sa_solver，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

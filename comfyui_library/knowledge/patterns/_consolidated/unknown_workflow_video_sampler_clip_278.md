---
name: unknown_workflow_video_sampler_clip_278
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.787
common_nodes: [CLIPTextEncode, EmptyHunyuanLatentVideo, Int, KSampler, LoadImage, MathExpression|pysssss, ModelSamplingSD3, Primitive integer [Crystools], PrimitiveStringMultiline, RH_LLMAPI_NODE, ShowText|pysssss, VAEDecode, VHS_VideoCombine, easy textSwitch]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/Wan2.2-AIO文生和图生视频【自动优化提示词】_1951496649069768705.json, 视频生成/文生视频/【AIO-V10大一统】文生视频-Wan2.2_1962869476662415362.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_278

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/Wan2.2-AIO文生和图生视频【自动优化提示词】_1951496649069768705.json、视频生成/文生视频/【AIO-V10大一统】文生视频-Wan2.2_1962869476662415362.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：79%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `Int`
- `KSampler`
- `LoadImage`
- `MathExpression|pysssss`
- `ModelSamplingSD3`
- `Primitive integer [Crystools]`
- `PrimitiveStringMultiline`
- `RH_LLMAPI_NODE`
- `ShowText|pysssss`
- `VAEDecode`
- `VHS_VideoCombine`
- `easy textSwitch`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 1/2 个有
- `CR Text` —— 1/2 个有
- `CheckpointLoaderSimple` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有
- `UNETLoader` —— 1/2 个有
- `VAELoader` —— 1/2 个有
- `WanImageToVideo` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | sa_solver | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 sa_solver，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（3/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

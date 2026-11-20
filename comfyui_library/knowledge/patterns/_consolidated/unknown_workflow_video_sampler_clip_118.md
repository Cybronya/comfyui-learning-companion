---
name: unknown_workflow_video_sampler_clip_118
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.887667
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, KSamplerAdvanced, ModelSamplingSD3, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/WAN2.2 文生视频、图生视频工作流_1949440813809467394.json, 视频生成/文生视频/WAN2.2 文生视频、图生视频工作流_2018552915408982018.json, 视频生成/文生视频/WAN2.2 文生视频、图生视频工作流_2042210649249423362.json, 视频生成/文生视频/WAN2.2 文生视频女孩穿梭_1950186717304242177.json, 视频生成/文生视频/Wan2.2 14B+Teacache+Sage文生视频加速版工作流_1949879786422362114.json, 视频生成/文生视频/Wan2.2 14B-文生视频_1949911446906912770.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_118

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/文生视频/WAN2.2 文生视频、图生视频工作流_1949440813809467394.json、视频生成/文生视频/WAN2.2 文生视频、图生视频工作流_2018552915408982018.json、视频生成/文生视频/WAN2.2 文生视频、图生视频工作流_2042210649249423362.json、视频生成/文生视频/WAN2.2 文生视频女孩穿梭_1950186717304242177.json、视频生成/文生视频/Wan2.2 14B+Teacache+Sage文生视频加速版工作流_1949879786422362114.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `KSamplerAdvanced`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 4/6 个有
- `WanImageToVideo` —— 4/6 个有
- `ModelPatchTorchSettings` —— 3/6 个有
- `JWInteger` —— 2/6 个有
- `LoadVideo` —— 2/6 个有
- `TeaCache` —— 2/6 个有
- `JjkText` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 6 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 20 | 6 | 53% |
| 采样算法 | 3.5 | 3.5 - 3.5 | 6 | 100% |
| 调度器 | euler | - | 6 | 100% |
| 重绘幅度 | simple | - | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，6 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 20，6 个样本
- 采样算法 中位数 3.5，观测区间 3.5 - 3.5，6 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，6 个样本，一致性 100%
- 重绘幅度 最常用 simple，6 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））

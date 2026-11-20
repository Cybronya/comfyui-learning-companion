---
name: unknown_workflow_video_sampler_clip_187
type: Unknown Workflow
frequency: 3
level: weak
coverage: 0.979333
common_nodes: [CLIPLoader, CLIPTextEncode, ImageResizeKJ, KSampler, ModelSamplingSD3, PatchModelPatcherOrder, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAEEncodeTiled, VAELoader, VHS_LoadVideo, VHS_VideoCombine]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/03-03-01-WAN2.1_视频转绘-t2v-原生_1989235234329726978.json, 平台全量/wan2.1 视频生视频 二创工作流_1897650288189198337.json, 平台全量/wan2.1+视频生视频+二创工作流_2048641795487178754.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_187

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/03-03-01-WAN2.1_视频转绘-t2v-原生_1989235234329726978.json、平台全量/wan2.1 视频生视频 二创工作流_1897650288189198337.json、平台全量/wan2.1+视频生视频+二创工作流_2048641795487178754.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：98%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ImageResizeKJ`
- `KSampler`
- `ModelSamplingSD3`
- `PatchModelPatcherOrder`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAEEncodeTiled`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 6 - 30 | 3 | 49% |
| Prompt 约束强度(CFG) | 6 | 1 - 6 | 3 | 46% |
| 采样算法 | uni_pc | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 0.75 | 0.5 - 0.75 | 3 | 82% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 30，观测区间 6 - 30，3 个样本，取值分散，一致性仅 49%
- Prompt 约束强度(CFG) 中位数 6，观测区间 1 - 6，3 个样本，取值分散，一致性仅 46%
- 采样算法 最常用 uni_pc，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 0.75，观测区间 0.5 - 0.75，3 个样本，取值集中（一致性 82%）

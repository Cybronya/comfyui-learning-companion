---
name: unknown_workflow_sampler_clip_checkpoint_41
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8345
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptySD3LatentImage, KSampler, PreviewImage, SaveImage, TripleCLIPLoader, VAEDecode]
problems: []
missing: []
members: [平台全量/SD3 + Portrait Master Workflow_1869251291842256897.json, 视频生成/图生视频/SD3.5文生图官方工作流FP8_1930207326282878978.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_checkpoint_41

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/SD3 + Portrait Master Workflow_1869251291842256897.json、视频生成/图生视频/SD3.5文生图官方工作流FP8_1930207326282878978.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptySD3LatentImage`
- `KSampler`
- `PreviewImage`
- `SaveImage`
- `TripleCLIPLoader`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 1/2 个有
- `DualCLIPLoader` —— 1/2 个有
- `PortraitMaster` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 5.45 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | sgm_uniform | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 5.45，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

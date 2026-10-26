---
name: unknown_workflow_sampler_clip_checkpoint_19
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8212
common_nodes: [CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, DualCLIPLoader, EmptySD3LatentImage, KSampler, SaveImage, TripleCLIPLoader, VAEDecode]
problems: []
missing: []
members: [图片生成/文生图/sd3.5_Large 模型的基础工作流_1891736065517203458.json, 图片生成/文生图/sd3.5_large 满血版 官方文生图示例_1848750522676416513.json, 图片生成/文生图/sd3.5_large 生成双人合照_1848787187654594562.json, 图片生成/文生图/sd3.5_medium_1852341200979206145.json, 视频生成/图生视频/SD3.5文生图官方工作流FP8_1930207326282878978.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_checkpoint_19

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/sd3.5_Large 模型的基础工作流_1891736065517203458.json、图片生成/文生图/sd3.5_large 满血版 官方文生图示例_1848750522676416513.json、图片生成/文生图/sd3.5_large 生成双人合照_1848787187654594562.json、图片生成/文生图/sd3.5_medium_1852341200979206145.json、视频生成/图生视频/SD3.5文生图官方工作流FP8_1930207326282878978.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `TripleCLIPLoader`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `SeargePromptText` —— 3/5 个有
- `PreviewImage` —— 1/5 个有
- `RH_Prompter` —— 1/5 个有
- `ShowText|pysssss` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 5 | 83% |
| Prompt 约束强度(CFG) | 5.45 | 5.45 - 5.45 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | sgm_uniform | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，5 个样本，取值集中（一致性 83%）
- Prompt 约束强度(CFG) 中位数 5.45，观测区间 5.45 - 5.45，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）

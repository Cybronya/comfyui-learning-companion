---
name: unknown_workflow_sampler_clip_checkpoint_8
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.839286
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptySD3LatentImage, KSampler, SaveImage, TripleCLIPLoader, VAEDecode]
problems: []
missing: []
members: [图片生成/文生图/1930199196047982593.json, 图片生成/文生图/1955937848417550338.json, 图片生成/文生图/sd3.5_Large 模型的基础工作流_1891736065517203458.json, 图片生成/文生图/sd3.5_large 满血版 官方文生图示例_1848750522676416513.json, 图片生成/文生图/sd3.5_large 生成双人合照_1848787187654594562.json, 图片生成/文生图/sd3.5_medium_1852341200979206145.json, 视频生成/图生视频/1930207326282878978.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_checkpoint_8

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/1930199196047982593.json、图片生成/文生图/1955937848417550338.json、图片生成/文生图/sd3.5_Large 模型的基础工作流_1891736065517203458.json、图片生成/文生图/sd3.5_large 满血版 官方文生图示例_1848750522676416513.json、图片生成/文生图/sd3.5_large 生成双人合照_1848787187654594562.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `TripleCLIPLoader`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 6/7 个有
- `DualCLIPLoader` —— 6/7 个有
- `SeargePromptText` —— 3/7 个有
- `PreviewImage` —— 2/7 个有
- `RH_Prompter` —— 1/7 个有
- `ShowText|pysssss` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 7 | 81% |
| Prompt 约束强度(CFG) | 5.45 | 5.45 - 5.45 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | sgm_uniform | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，7 个样本，取值集中（一致性 81%）
- Prompt 约束强度(CFG) 中位数 5.45，观测区间 5.45 - 5.45，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）

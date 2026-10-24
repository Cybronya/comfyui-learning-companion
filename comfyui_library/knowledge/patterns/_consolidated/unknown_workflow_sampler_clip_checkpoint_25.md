---
name: unknown_workflow_sampler_clip_checkpoint_25
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.79975
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptySD3LatentImage, KSampler, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/文生图/Netayume Lumina 动漫文生图_2078655787282554882.json, 图片生成/文生图/SD 3.5 官方工作流（教学用）_1955937848417550338.json, 图片生成/文生图/image_netayume_lumina_t2i_2059957968740900865.json, 图片生成/文生图/【遇见AI】sd3_medium_basic文生图_2039206201413607426.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_checkpoint_25

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Netayume Lumina 动漫文生图_2078655787282554882.json、图片生成/文生图/SD 3.5 官方工作流（教学用）_1955937848417550338.json、图片生成/文生图/image_netayume_lumina_t2i_2059957968740900865.json、图片生成/文生图/【遇见AI】sd3_medium_basic文生图_2039206201413607426.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 2/4 个有
- `PrimitiveStringMultiline` —— 2/4 个有
- `StringConcatenate` —— 2/4 个有
- `TripleCLIPLoader` —— 2/4 个有
- `ModelSamplingSD3` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 29 | 20 - 30 | 4 | 85% |
| Prompt 约束强度(CFG) | 4.25 | 4 - 5.45 | 4 | 87% |
| 采样算法 | res_multistep | - | 4 | 50% |
| 调度器 | simple | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 29，观测区间 20 - 30，4 个样本，取值集中（一致性 85%）
- Prompt 约束强度(CFG) 中位数 4.25，观测区间 4 - 5.45，4 个样本，取值集中（一致性 87%）
- 采样算法 最常用 res_multistep，4 个样本，一致性 50%
- 调度器 最常用 simple，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）

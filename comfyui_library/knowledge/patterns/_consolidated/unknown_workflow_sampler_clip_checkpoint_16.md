---
name: unknown_workflow_sampler_clip_checkpoint_16
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.74975
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptySD3LatentImage, KSampler, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/文生图/1955937848417550338.json, 图片生成/文生图/Lumina Image 2.0 官方工作流_1894345126246809602.json, 图片生成/文生图/Netayume Lumina 动漫文生图_2078655787282554882.json, 图片生成/文生图/image_netayume_lumina_t2i_2059957968740900865.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_checkpoint_16

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/1955937848417550338.json、图片生成/文生图/Lumina Image 2.0 官方工作流_1894345126246809602.json、图片生成/文生图/Netayume Lumina 动漫文生图_2078655787282554882.json、图片生成/文生图/image_netayume_lumina_t2i_2059957968740900865.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 3/4 个有
- `PrimitiveStringMultiline` —— 2/4 个有
- `StringConcatenate` —— 2/4 个有
- `TripleCLIPLoader` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 27.5 | 20 - 30 | 4 | 84% |
| Prompt 约束强度(CFG) | 4 | 4 - 5.45 | 4 | 86% |
| 采样算法 | res_multistep | - | 4 | 75% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 27.5，观测区间 20 - 30，4 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 5.45，4 个样本，取值集中（一致性 86%）
- 采样算法 最常用 res_multistep，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）

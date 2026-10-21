---
name: unknown_workflow_sampler_clip_vae_35
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.863333
common_nodes: [CLIPTextEncodeFlux, EmptyLatentImage, KSampler, PreviewImage, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [CR Text Concatenate]
members: [图片生成/文生图/1930149940532559873.json, 图片生成/文生图/1937011516359217154.json, 图片生成/文生图/FLUx-gguf_1830883788774666242.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_35

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1930149940532559873.json、图片生成/文生图/1937011516359217154.json、图片生成/文生图/FLUx-gguf_1830883788774666242.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncodeFlux`
- `EmptyLatentImage`
- `KSampler`
- `PreviewImage`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 2/3 个有
- `DualCLIPLoader` —— 2/3 个有
- `DualCLIPLoaderGGUF` —— 2/3 个有
- `UnetLoaderGGUF` —— 2/3 个有
- `CR Text Concatenate` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `Text` —— 1/3 个有
- `UNETLoader` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 4 - 20 | 3 | 49% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | normal | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 896 | 768 - 1024 | 3 | 88% |
| 高度 | 1024 | 1024 - 1152 | 3 | 94% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 4 - 20，3 个样本，取值分散，一致性仅 49%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 normal，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 896，观测区间 768 - 1024，3 个样本，取值集中（一致性 88%）
- 高度 中位数 1024，观测区间 1024 - 1152，3 个样本，取值集中（一致性 94%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text Concatenate

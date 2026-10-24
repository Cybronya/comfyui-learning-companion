---
name: unknown_workflow_sampler_clip_vae_38
type: Unknown Workflow
frequency: 6
level: weak
coverage: 0.918
common_nodes: [CLIPTextEncode, KSampler, SaveImage, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/04.WAN2.2-文生图-nf_1991131479682166785.json, 图片生成/文生图/09.Wan2.2文生图_1993297565200351233.json, 图片生成/文生图/Qwen-image-GGUF 海报设计_2013882015992520706.json, 图片生成/文生图/hunyuan-image gguf 8步加速版_1966037699108966402.json, 图片生成/文生图/qwen-image gguf 加速版_1955880153337483265.json, 图片生成/文生图/sim▷Qwen中秋节海报特辑_1972281991481782274.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_38

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/04.WAN2.2-文生图-nf_1991131479682166785.json、图片生成/文生图/09.Wan2.2文生图_1993297565200351233.json、图片生成/文生图/Qwen-image-GGUF 海报设计_2013882015992520706.json、图片生成/文生图/hunyuan-image gguf 8步加速版_1966037699108966402.json、图片生成/文生图/qwen-image gguf 加速版_1955880153337483265.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `KSampler`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 5/6 个有
- `EmptyHunyuanLatentVideo` —— 5/6 个有
- `UnetLoaderGGUF` —— 5/6 个有
- `VAELoader` —— 5/6 个有
- `LoraLoaderModelOnly` —— 4/6 个有
- `ModelSamplingAuraFlow` —— 3/6 个有
- `ModelSamplingSD3` —— 3/6 个有
- `LayerUtility: PurgeVRAM` —— 2/6 个有
- `CheckpointLoaderSimple` —— 1/6 个有
- `EmptyHunyuanImageLatent` —— 1/6 个有
- `LoadImage` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 20 | 6 | 38% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 6 | 36% |
| 采样算法 | euler | - | 6 | 83% |
| 调度器 | simple | - | 6 | 67% |
| 重绘幅度 | 1 | 0.5 - 1 | 6 | 80% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 20，6 个样本，取值分散，一致性仅 38%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，6 个样本，取值分散，一致性仅 36%
- 采样算法 最常用 euler，6 个样本，一致性 83%
- 调度器 最常用 simple，6 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 0.5 - 1，6 个样本
- 高发问题（5/6 个样本）：Steps较低可能导致细节不足

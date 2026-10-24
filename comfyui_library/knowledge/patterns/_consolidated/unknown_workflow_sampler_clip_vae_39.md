---
name: unknown_workflow_sampler_clip_vae_39
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 1
common_nodes: [CLIPTextEncode, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/06.Z-Image-T-Lora文生图-NF_1996576652488491010.json, 图片生成/文生图/Qwen-image gguf版_1953699331356459009.json, 图片生成/文生图/Z Image 小强模型极速出图_1993947409080401922.json, 图片生成/文生图/Z-Image 文生图_2016054204908965889.json, 图片生成/文生图/Z-Image 最强文生图，30秒出图，超高性价比_2011687215461572609.json, 图片生成/文生图/Z-Image 最强文生图，30秒出图，超高性价比_2025784515674775553.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_39

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/06.Z-Image-T-Lora文生图-NF_1996576652488491010.json、图片生成/文生图/Qwen-image gguf版_1953699331356459009.json、图片生成/文生图/Z Image 小强模型极速出图_1993947409080401922.json、图片生成/文生图/Z-Image 文生图_2016054204908965889.json、图片生成/文生图/Z-Image 最强文生图，30秒出图，超高性价比_2011687215461572609.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 5/6 个有
- `PathchSageAttentionKJ` —— 5/6 个有
- `SaveImage` —— 5/6 个有
- `Text` —— 4/6 个有
- `UNETLoader` —— 4/6 个有
- `Int` —— 2/6 个有
- `UnetLoaderGGUF` —— 2/6 个有
- `ClipLoaderGGUF` —— 1/6 个有
- `CompressImages` —— 1/6 个有
- `Lora Loader Stack (rgthree)` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 9 - 20 | 6 | 63% |
| Prompt 约束强度(CFG) | 1 | 1 - 2 | 6 | 68% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 9 - 20，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2，6 个样本
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（4/6 个样本）：Steps较低可能导致细节不足

---
name: unknown_workflow_sampler_unet_vae_95
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.928
common_nodes: [CLIPLoader, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/z-image-turbo动漫图片生成_2067966937392574466.json, 图片生成/文生图/千问-qwen2512-image-文生图工作流_2008014250991685634.json, 图片生成/文生图/千问大模型Z_Image 文生图大模型（目前最真实）_1994767919693410305.json, 图片生成/文生图/千问工作流_2083184424287563777.json, 图片生成/文生图/千问文生图快速中文直出2512_2027699940423639041.json, 图片生成/文生图/千问文生图最新版工作流_2000925762351923202.json, 图片生成/文生图/原生z-image-turbo_2003323871308677121.json, 图片生成/文生图/唯一讲述着专用Z-image造像_2000531408500162562.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_95

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/z-image-turbo动漫图片生成_2067966937392574466.json、图片生成/文生图/千问-qwen2512-image-文生图工作流_2008014250991685634.json、图片生成/文生图/千问大模型Z_Image 文生图大模型（目前最真实）_1994767919693410305.json、图片生成/文生图/千问工作流_2083184424287563777.json、图片生成/文生图/千问文生图快速中文直出2512_2027699940423639041.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 7/8 个有
- `EmptySD3LatentImage` —— 7/8 个有
- `ModelSamplingAuraFlow` —— 6/8 个有
- `LoraLoaderModelOnly` —— 2/8 个有
- `CLIPTextEncodeBREAK` —— 1/8 个有
- `EmptyLatentImage` —— 1/8 个有
- `LoraLoader` —— 1/8 个有
- `Text Multiline` —— 1/8 个有
- `easy promptConcat` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 8 - 20 | 8 | 61% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 8 | 33% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 1024 | - | 1 | 100% |
| 高度 | 1024 | - | 1 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 8 - 20，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，8 个样本，取值分散，一致性仅 33%
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（6/8 个样本）：Steps较低可能导致细节不足

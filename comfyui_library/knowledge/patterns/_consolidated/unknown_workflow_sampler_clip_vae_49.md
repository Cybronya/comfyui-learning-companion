---
name: unknown_workflow_sampler_clip_vae_49
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.9452
common_nodes: [AILab_QwenVL, CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, Text Concatenate, Text Multiline, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/qwen千问文生图_1988181167390244866.json, 图片生成/文生图/qwen千问文生图_1988450428977373186.json, 图片生成/文生图/一次生成三种模型的海报_1998634326935920641.json, 图片生成/文生图/万能懒人海报设计_2077383233066590209.json, 图片生成/文生图/初芒-_2013994857626345474.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_49

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/qwen千问文生图_1988181167390244866.json、图片生成/文生图/qwen千问文生图_1988450428977373186.json、图片生成/文生图/一次生成三种模型的海报_1998634326935920641.json、图片生成/文生图/万能懒人海报设计_2077383233066590209.json、图片生成/文生图/初芒-_2013994857626345474.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 5 个 workflow 都包含：
- `AILab_QwenVL`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `Text Concatenate`
- `Text Multiline`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 3/5 个有
- `PreviewAny` —— 3/5 个有
- `UNETLoader` —— 3/5 个有
- `Fast Groups Bypasser (rgthree)` —— 2/5 个有
- `Int` —— 2/5 个有
- `UnetLoaderGGUF` —— 2/5 个有
- `Image Batch` —— 1/5 个有
- `LayerUtility: PurgeVRAM V2` —— 1/5 个有
- `easy showAnything` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 4 - 10 | 5 | 61% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 4 - 10，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）

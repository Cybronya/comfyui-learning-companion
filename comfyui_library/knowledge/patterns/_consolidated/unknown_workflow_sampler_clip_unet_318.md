---
name: unknown_workflow_sampler_clip_unet_318
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.94125
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/一字马-300张Lora-洗图工作流_1994669431991246850.json, 图片生成/文生图/千问真实幻想V2文生图_1987923112853442561.json, 图片生成/文生图/反推词image图生图洗图_2043516005657350145.json, 图片生成/文生图/极致真实的人像质感(Qwen Image 文生图）_1984498747142979586.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_318

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/一字马-300张Lora-洗图工作流_1994669431991246850.json、图片生成/文生图/千问真实幻想V2文生图_1987923112853442561.json、图片生成/文生图/反推词image图生图洗图_2043516005657350145.json、图片生成/文生图/极致真实的人像质感(Qwen Image 文生图）_1984498747142979586.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `ShowText|pysssss` —— 3/4 个有
- `CR Text` —— 2/4 个有
- `Text Multiline` —— 2/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `GetImageSize+` —— 1/4 个有
- `Seed Generator` —— 1/4 个有
- `Text Concatenate` —— 1/4 个有
- `workflow>横屏` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 19 | 8 - 30 | 4 | 42% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 4 | 4 | 40% |
| 采样算法 | euler_ancestral | - | 4 | 50% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 19，观测区间 8 - 30，4 个样本，取值分散，一致性仅 42%
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 4，4 个样本，取值分散，一致性仅 40%
- 采样算法 最常用 euler_ancestral，4 个样本，一致性 50%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（3/4 个样本）：Steps较低可能导致细节不足

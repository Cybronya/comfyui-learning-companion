---
name: unknown_workflow_sampler_clip_unet_41
type: Unknown Workflow
frequency: 18
level: weak
coverage: 0.941722
common_nodes: [CLIPTextEncode, EmptySD3LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/文生图  MOSS文生图  2K极速版_2116878349103616002.json, 图片生成/文生图/文生图  Z-image  zimage  超真实 去除AI味_2042796990563622914.json, 图片生成/文生图/文生图 Z-image  zimage 超真实_2042852589439553537.json, 图片生成/文生图/文生图 硕阳_2016782171092029441.json, 图片生成/文生图/文生图 阿里 Z-image  超真实 去除AI味_2041885856356638722.json, 图片生成/文生图/文生图 阿里 Z-image  超真实 去除AI味_2042157391986298882.json, 图片生成/文生图/文生图(人像)_2006960061226164225.json, 图片生成/文生图/文生图+LoRA_2014558730028851201.json, 图片生成/文生图/文生图+写实光影LORA+Engineer大师模式_2029093017558196225.json, 图片生成/文生图/文生图-Q版森林_2087797265531498498.json, 图片生成/文生图/文生图-古瓷碗里的微景观_2114540826620678146.json, 图片生成/文生图/文生图-古瓷碗里的微景观_2115286569815986177.json, 图片生成/文生图/文生图-微景观-迷你朋克工坊_2084933542248804354.json, 图片生成/文生图/文生图-微景观桃园_2088147505304395778.json, 图片生成/文生图/文生图-微景观草莓园_2085177631280029697.json, 图片生成/文生图/文生图-手机里的微景观_2084940722343600130.json, 图片生成/文生图/文生图，中英文都可以，我自己用，出图快 且准确 质量高_2026835950390747137.json, 图片生成/文生图/本地专用 Z-Image 文生图_2005279973143445506.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_41

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（图片生成/文生图/文生图  MOSS文生图  2K极速版_2116878349103616002.json、图片生成/文生图/文生图  Z-image  zimage  超真实 去除AI味_2042796990563622914.json、图片生成/文生图/文生图 Z-image  zimage 超真实_2042852589439553537.json、图片生成/文生图/文生图 硕阳_2016782171092029441.json、图片生成/文生图/文生图 阿里 Z-image  超真实 去除AI味_2041885856356638722.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 18 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 17/18 个有
- `ModelSamplingAuraFlow` —— 17/18 个有
- `LoraLoaderModelOnly` —— 13/18 个有
- `ConditioningZeroOut` —— 11/18 个有
- `CR Text` —— 2/18 个有
- `CLIPLoaderGGUF` —— 1/18 个有
- `ConditioningCombine` —— 1/18 个有
- `ConditioningSetTimestepRange` —— 1/18 个有
- `DuckHideNode` —— 1/18 个有
- `PreviewImage` —— 1/18 个有
- `easy bookmark` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8.5 | 4 - 50 | 18 | 5% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 18 | 43% |
| 采样算法 | euler | - | 18 | 61% |
| 调度器 | simple | - | 18 | 94% |
| 重绘幅度 | 1 | 1 - 1 | 18 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/18 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8.5，观测区间 4 - 50，18 个样本，取值分散，一致性仅 5%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，18 个样本，取值分散，一致性仅 43%
- 采样算法 最常用 euler，18 个样本，一致性 61%
- 调度器 最常用 simple，18 个样本，一致性 94%
- 重绘幅度 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 高发问题（11/18 个样本）：Steps较低可能导致细节不足

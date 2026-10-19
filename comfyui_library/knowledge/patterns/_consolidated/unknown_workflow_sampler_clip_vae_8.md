---
name: unknown_workflow_sampler_clip_vae_8
type: Unknown Workflow
frequency: 7
level: weak
coverage: 0.810143
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, ModelSamplingAuraFlow, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [easy clearCacheAll, CR SDXL Aspect Ratio]
members: [图片生成/文生图/1966414867236368386.json, 图片生成/文生图/1966426602882183170.json, 图片生成/文生图/1966447914094637058.json, 图片生成/文生图/1966547887809343490.json, 图片生成/文生图/1967367971867910145.json, 图片生成/文生图/1967372243183525890.json, 图片生成/文生图/1968001076735651842.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_8

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/1966414867236368386.json、图片生成/文生图/1966426602882183170.json、图片生成/文生图/1966447914094637058.json、图片生成/文生图/1966547887809343490.json、图片生成/文生图/1967367971867910145.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：81%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 6/7 个有
- `CFGNorm` —— 5/7 个有
- `JjkText` —— 5/7 个有
- `LoadImage` —— 5/7 个有
- `NunchakuQwenImageDiTLoader` —— 4/7 个有
- `LoraLoaderModelOnly` —— 3/7 个有
- `UNETLoader` —— 3/7 个有
- `CR SDXL Aspect Ratio` —— 1/7 个有
- `ConditioningZeroOut` —— 1/7 个有
- `TextCombinerTwo` —— 1/7 个有
- `easy clearCacheAll` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 30 | 7 | 19% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 7 | 36% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | normal | - | 7 | 57% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 30，7 个样本，取值分散，一致性仅 19%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，7 个样本，取值分散，一致性仅 36%
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 normal，7 个样本，一致性 57%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（5/7 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：easy clearCacheAll、CR SDXL Aspect Ratio

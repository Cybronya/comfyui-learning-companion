---
name: unknown_workflow_sampler_clip_vae_7
type: Unknown Workflow
frequency: 12
level: weak
coverage: 0.815833
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [easy clearCacheAll, CR Text]
members: [图片生成/文生图/1965259047710674945.json, 图片生成/文生图/1966409848168624130.json, 图片生成/文生图/1966414867236368386.json, 图片生成/文生图/1966426602882183170.json, 图片生成/文生图/1966447914094637058.json, 图片生成/文生图/1966547887809343490.json, 图片生成/文生图/1967367971867910145.json, 图片生成/文生图/1967372243183525890.json, 图片生成/文生图/1970739735536824321.json, 图片生成/文生图/1987923112853442561.json, 图片生成/文生图/1988091761648115713.json, 图片生成/文生图/FireRed-Image-Edit 1.1 参考人物生图工作流+全节点注释_2055176231376695297.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_7

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/1965259047710674945.json、图片生成/文生图/1966409848168624130.json、图片生成/文生图/1966414867236368386.json、图片生成/文生图/1966426602882183170.json、图片生成/文生图/1966447914094637058.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 8/12 个有
- `LoadImage` —— 8/12 个有
- `LoraLoaderModelOnly` —— 6/12 个有
- `NunchakuQwenImageDiTLoader` —— 6/12 个有
- `UNETLoader` —— 6/12 个有
- `JjkText` —— 5/12 个有
- `CR Text` —— 3/12 个有
- `PrimitiveInt` —— 2/12 个有
- `GetImageSize` —— 1/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/12 个有
- `Text` —— 1/12 个有
- `TextEncodeQwenImageEditPlus` —— 1/12 个有
- `easy clearCacheAll` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 30 | 12 | 30% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 12 | 42% |
| 采样算法 | euler | - | 12 | 92% |
| 调度器 | normal | - | 12 | 42% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 30，12 个样本，取值分散，一致性仅 30%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，12 个样本，取值分散，一致性仅 42%
- 采样算法 最常用 euler，12 个样本，一致性 92%
- 调度器 最常用 normal，12 个样本，一致性 42%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 高发问题（11/12 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：easy clearCacheAll、CR Text

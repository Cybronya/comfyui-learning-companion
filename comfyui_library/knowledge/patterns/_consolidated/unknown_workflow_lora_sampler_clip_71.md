---
name: unknown_workflow_lora_sampler_clip_71
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.796333
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [LayerUtility: JoyCaptionBeta1, LayerUtility: LoadJoyCaptionBeta1Model, LayerUtility: JoyCaptionBeta1ExtraOptions, LayerUtility: ImageScaleByAspectRatio V2, Text Multiline]
members: [图片生成/文生图/1950055564211568642.json, 图片生成/文生图/1952963427289468930.json, 图片生成/文生图/1984498747142979586.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_71

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1950055564211568642.json、图片生成/文生图/1952963427289468930.json、图片生成/文生图/1984498747142979586.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 2/3 个有
- `LayerUtility: JoyCaptionBeta1` —— 2/3 个有
- `LayerUtility: LoadJoyCaptionBeta1Model` —— 2/3 个有
- `ModelSamplingAuraFlow` —— 2/3 个有
- `ShowText|pysssss` —— 2/3 个有
- `AILab_QwenVL` —— 1/3 个有
- `EmptyHunyuanLatentVideo` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `LayerUtility: JoyCaptionBeta1ExtraOptions` —— 1/3 个有
- `ShowText` —— 1/3 个有
- `Text Multiline` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 8 - 30 | 3 | 54% |
| Prompt 约束强度(CFG) | 4 | 1 - 4 | 3 | 53% |
| 采样算法 | res_2s | - | 3 | 33% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 30，观测区间 8 - 30，3 个样本
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 4，3 个样本
- 采样算法 最常用 res_2s，3 个样本，一致性 33%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: JoyCaptionBeta1、LayerUtility: LoadJoyCaptionBeta1Model、LayerUtility: JoyCaptionBeta1ExtraOptions、LayerUtility: ImageScaleByAspectRatio V2、Text Multiline

---
name: unknown_workflow_sampler_clip_vae_6
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.574143
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, Text Multiline, VAEDecode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: [LayerUtility: ImageScaleByAspectRatio V2, Text Multiline, CR Text Replace, LayerUtility: JoyCaptionBeta1, LayerUtility: JoyCaptionBeta1ExtraOptions, LayerUtility: LoadJoyCaptionBeta1Model]
members: [图片生成/文生图/1953067660055613442.json, 图片生成/文生图/1955892796286795777.json, 图片生成/文生图/1970152346649063426.json, 图片生成/文生图/1970162502074068993.json, 图片生成/文生图/1972314392975110146.json, 图片生成/文生图/1973238135855386626.json, 图片生成/文生图/1984091087096741890.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_6

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/1953067660055613442.json、图片生成/文生图/1955892796286795777.json、图片生成/文生图/1970152346649063426.json、图片生成/文生图/1970162502074068993.json、图片生成/文生图/1972314392975110146.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：57%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `Text Multiline`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ImpactSwitch` —— 6/7 个有
- `Int` —— 6/7 个有
- `LoadImage` —— 6/7 个有
- `PrimitiveBoolean` —— 6/7 个有
- `UNETLoader` —— 6/7 个有
- `easy ifElse` —— 6/7 个有
- `CR Text Replace` —— 5/7 个有
- `FluxResolutionNode` —— 5/7 个有
- `RH_Captioner` —— 5/7 个有
- `Fast Groups Bypasser (rgthree)` —— 4/7 个有
- `PreviewImage` —— 3/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/7 个有
- `LayerUtility: JoyCaptionBeta1` —— 1/7 个有
- `LayerUtility: JoyCaptionBeta1ExtraOptions` —— 1/7 个有
- `LayerUtility: LoadJoyCaptionBeta1Model` —— 1/7 个有
- `NunchakuQwenImageDiTLoader` —— 1/7 个有
- `Prompt_Text` —— 1/7 个有
- `ShowText|pysssss` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 20 | 7 | 77% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 2.5 | 7 | 77% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，7 个样本
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 2.5，7 个样本
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2、Text Multiline、CR Text Replace、LayerUtility: JoyCaptionBeta1、LayerUtility: JoyCaptionBeta1ExtraOptions

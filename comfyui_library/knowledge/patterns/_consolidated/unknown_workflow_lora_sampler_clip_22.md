---
name: unknown_workflow_lora_sampler_clip_22
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.70075
common_nodes: [CLIPLoader, CLIPTextEncode, CR SDXL Aspect Ratio, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [Text Concatenate, CR SDXL Aspect Ratio, Text Multiline, LayerUtility: JoyCaptionBeta1, LayerUtility: LoadJoyCaptionBeta1Model]
members: [图片生成/文生图/1955343006078418945.json, 图片生成/文生图/1955523693487296514.json, 图片生成/文生图/1959596933876756481.json, 图片生成/文生图/1959992517599113217.json, 图片生成/文生图/1961096208251076609.json, 图片生成/文生图/1961577874413260802.json, 图片生成/文生图/1961717444916264961.json, 图片生成/文生图/1969006640156581890.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_22

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/1955343006078418945.json、图片生成/文生图/1955523693487296514.json、图片生成/文生图/1959596933876756481.json、图片生成/文生图/1959992517599113217.json、图片生成/文生图/1961096208251076609.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：70%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR SDXL Aspect Ratio`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 7/8 个有
- `PrimitiveString` —— 7/8 个有
- `Text Concatenate` —— 7/8 个有
- `easy showAnything` —— 7/8 个有
- `RH_Captioner` —— 6/8 个有
- `PreviewImage` —— 3/8 个有
- `CFGNorm` —— 2/8 个有
- `GetImageSize` —— 1/8 个有
- `LayerUtility: JoyCaptionBeta1` —— 1/8 个有
- `LayerUtility: LoadJoyCaptionBeta1Model` —— 1/8 个有
- `ShowText|pysssss` —— 1/8 个有
- `Text Multiline` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 8 - 30 | 8 | 68% |
| Prompt 约束强度(CFG) | 3.25 | 1 - 4 | 8 | 66% |
| 采样算法 | euler | - | 8 | 88% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 25，观测区间 8 - 30，8 个样本
- Prompt 约束强度(CFG) 中位数 3.25，观测区间 1 - 4，8 个样本
- 采样算法 最常用 euler，8 个样本，一致性 88%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：Text Concatenate、CR SDXL Aspect Ratio、Text Multiline、LayerUtility: JoyCaptionBeta1、LayerUtility: LoadJoyCaptionBeta1Model

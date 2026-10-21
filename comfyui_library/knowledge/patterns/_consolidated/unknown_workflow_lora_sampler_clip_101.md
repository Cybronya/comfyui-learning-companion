---
name: unknown_workflow_lora_sampler_clip_101
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.672667
common_nodes: [CLIPTextEncode, CR SDXL Aspect Ratio, EmptySD3LatentImage, Fast Groups Bypasser (rgthree), KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, QuadrupleCLIPLoader, RH_Captioner, SaveImage, Text Concatenate, Text Multiline, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [LayerUtility: JoyCaptionBeta1, LayerUtility: JoyCaptionBeta1ExtraOptions, LayerUtility: LoadJoyCaptionBeta1Model, Text Concatenate, Text Multiline, CR SDXL Aspect Ratio]
members: [图片生成/文生图/1912548267165712385.json, 图片生成/文生图/1916785448868581378.json, 图片生成/文生图/1917590380785897473.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_101

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1912548267165712385.json、图片生成/文生图/1916785448868581378.json、图片生成/文生图/1917590380785897473.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：67%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CR SDXL Aspect Ratio`
- `EmptySD3LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `QuadrupleCLIPLoader`
- `RH_Captioner`
- `SaveImage`
- `Text Concatenate`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JjkShowText` —— 2/3 个有
- `TeaCache` —— 2/3 个有
- `LayerUtility: JoyCaptionBeta1` —— 1/3 个有
- `LayerUtility: JoyCaptionBeta1ExtraOptions` —— 1/3 个有
- `LayerUtility: LoadJoyCaptionBeta1Model` —— 1/3 个有
- `UnetLoaderGGUF` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 50 | 28 - 50 | 3 | 76% |
| Prompt 约束强度(CFG) | 5 | 1 - 5 | 3 | 49% |
| 采样算法 | uni_pc | - | 3 | 67% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 50，观测区间 28 - 50，3 个样本
- Prompt 约束强度(CFG) 中位数 5，观测区间 1 - 5，3 个样本，取值分散，一致性仅 49%
- 采样算法 最常用 uni_pc，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: JoyCaptionBeta1、LayerUtility: JoyCaptionBeta1ExtraOptions、LayerUtility: LoadJoyCaptionBeta1Model、Text Concatenate、Text Multiline

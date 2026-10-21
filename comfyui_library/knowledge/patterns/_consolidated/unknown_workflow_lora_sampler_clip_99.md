---
name: unknown_workflow_lora_sampler_clip_99
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.584667
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncodeFlux, CR SDXL Aspect Ratio, DualCLIPLoader, EmptyLatentImage, Fast Groups Bypasser (rgthree), KSamplerSelect, LoadImage, LoraLoader, LyingSigmaSampler, RandomNoise, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, StringFunction|pysssss, Text Concatenate (JPS), UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [StringFunction|pysssss, Text Concatenate (JPS), easy imageScaleDownBy, CR SDXL Aspect Ratio, easy stylesSelector, LayerUtility: JoyCaptionBeta1, LayerUtility: JoyCaptionBeta1ExtraOptions, LayerUtility: LoadJoyCaptionBeta1Model]
members: [图片生成/文生图/1902223229052985346.json, 图片生成/文生图/1922306279304286210.json, 图片生成/文生图/1928392034858745858.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_99

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1902223229052985346.json、图片生成/文生图/1922306279304286210.json、图片生成/文生图/1928392034858745858.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：58%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncodeFlux`
- `CR SDXL Aspect Ratio`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoader`
- `LyingSigmaSampler`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `ShowText|pysssss`
- `StringFunction|pysssss`
- `Text Concatenate (JPS)`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ApplyFBCacheOnModel` —— 1/3 个有
- `JJC_JoyCaption` —— 1/3 个有
- `JJC_JoyCaption_Custom` —— 1/3 个有
- `Joy_caption` —— 1/3 个有
- `Joy_caption_load` —— 1/3 个有
- `LayerUtility: JoyCaptionBeta1` —— 1/3 个有
- `LayerUtility: JoyCaptionBeta1ExtraOptions` —— 1/3 个有
- `LayerUtility: LoadJoyCaptionBeta1Model` —— 1/3 个有
- `RH_Translator` —— 1/3 个有
- `easy imageScaleDownBy` —— 1/3 个有
- `easy stylesSelector` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 800 | 800 - 800 | 3 | 100% |
| 高度 | 1024 | 1024 - 1024 | 3 | 100% |
| LoRA 模型强度 | 0.8 | 0.4 - 4 | 3 | 7% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 800，观测区间 800 - 800，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.8，观测区间 0.4 - 4，3 个样本，取值分散，一致性仅 7%
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：StringFunction|pysssss、Text Concatenate (JPS)、easy imageScaleDownBy、CR SDXL Aspect Ratio、easy stylesSelector

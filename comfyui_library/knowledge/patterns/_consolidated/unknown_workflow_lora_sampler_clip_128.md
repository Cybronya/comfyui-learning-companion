---
name: unknown_workflow_lora_sampler_clip_128
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.73325
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncodeFlux, CR SDXL Aspect Ratio, DualCLIPLoader, EmptyLatentImage, Fast Groups Bypasser (rgthree), KSamplerSelect, LoadImage, LoraLoader, LyingSigmaSampler, RandomNoise, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, StringFunction|pysssss, Text Concatenate (JPS), UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux万物精灵-自然造物_1904844822627143681.json, 图片生成/文生图/Flux万物精灵-自然造物_1902223229052985346.json, 图片生成/文生图/Joy Beta1继Joy2新一代打标神器_1922306279304286210.json, 图片生成/文生图/最强joy3-Joy Beta1开源打标反推神器_1928392034858745858.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_128

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Flux万物精灵-自然造物_1904844822627143681.json、图片生成/文生图/Flux万物精灵-自然造物_1902223229052985346.json、图片生成/文生图/Joy Beta1继Joy2新一代打标神器_1922306279304286210.json、图片生成/文生图/最强joy3-Joy Beta1开源打标反推神器_1928392034858745858.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：73%

## 共有节点

全部 4 个 workflow 都包含：
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
- `ApplyFBCacheOnModel` —— 2/4 个有
- `Joy_caption` —— 2/4 个有
- `Joy_caption_load` —— 2/4 个有
- `easy imageScaleDownBy` —— 2/4 个有
- `easy stylesSelector` —— 2/4 个有
- `JJC_JoyCaption` —— 1/4 个有
- `JJC_JoyCaption_Custom` —— 1/4 个有
- `LayerUtility: JoyCaptionBeta1` —— 1/4 个有
- `LayerUtility: JoyCaptionBeta1ExtraOptions` —— 1/4 个有
- `LayerUtility: LoadJoyCaptionBeta1Model` —— 1/4 个有
- `RH_Translator` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 800 | 800 - 800 | 4 | 100% |
| 高度 | 1024 | 1024 - 1024 | 4 | 100% |
| LoRA 模型强度 | 2.4 | 0.4 - 4 | 4 | 26% |
| LoRA 文本强度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 800，观测区间 800 - 800，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 2.4，观测区间 0.4 - 4，4 个样本，取值分散，一致性仅 26%
- LoRA 文本强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）

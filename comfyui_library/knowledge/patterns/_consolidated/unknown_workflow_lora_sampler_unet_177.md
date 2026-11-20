---
name: unknown_workflow_lora_sampler_unet_177
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.7775
common_nodes: [ACE_TextConcatenate, CFGNorm, CLIPLoader, CR Overlay Text, CR Text, ConditioningZeroOut, GODMT_ListSlice, ImageConcatFromBatch, ImageFromBatch, ImageListToImageBatch, ImpactImageBatchToImageList, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewAny, PreviewImage, RH_LLMAPI_NODE, RH_Translator, ReplaceText, SDVM Image List Repeat, SaveImage, String Literal, Text, TextEncodeQwenImageEditPlusAdvance_lrzjason, TextListSplit, UNETLoader, VAEDecode, VAELoader, easy promptList, easy showAnything, ttN text7BOX_concat]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Image-Edit 2509：全自动三宫格写真，超越豆包即梦！美学升级！_1982657867910127617.json, 图片生成/图生图/Qwen-image-edit2511多模式新年写真三宫格_2075868586941444097.json, 图片生成/图生图/Qwen-image-edit2511多模式新年写真三宫格三款风格，一键承包你的全网新年炫图嗨起来！_2013064442698797058.json, 图片生成/图生图/Qwen-image-edit2511：多模式新年写真三宫格，三款风格，一键承包你的全网新年！_2005908714278318082.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_177

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen-Image-Edit 2509：全自动三宫格写真，超越豆包即梦！美学升级！_1982657867910127617.json、图片生成/图生图/Qwen-image-edit2511多模式新年写真三宫格_2075868586941444097.json、图片生成/图生图/Qwen-image-edit2511多模式新年写真三宫格三款风格，一键承包你的全网新年炫图嗨起来！_2013064442698797058.json、图片生成/图生图/Qwen-image-edit2511：多模式新年写真三宫格，三款风格，一键承包你的全网新年！_2005908714278318082.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 4 个 workflow 都包含：
- `ACE_TextConcatenate`
- `CFGNorm`
- `CLIPLoader`
- `CR Overlay Text`
- `CR Text`
- `ConditioningZeroOut`
- `GODMT_ListSlice`
- `ImageConcatFromBatch`
- `ImageFromBatch`
- `ImageListToImageBatch`
- `ImpactImageBatchToImageList`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewAny`
- `PreviewImage`
- `RH_LLMAPI_NODE`
- `RH_Translator`
- `ReplaceText`
- `SDVM Image List Repeat`
- `SaveImage`
- `String Literal`
- `Text`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `TextListSplit`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy promptList`
- `easy showAnything`
- `ttN text7BOX_concat`

**可变部分**（部分 workflow 才有）：
- `ImpactSwitch` —— 3/4 个有
- `TextEncodeQwenImageEditPlus` —— 3/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 8 | 4 | 87% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler_ancestral | - | 4 | 75% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 8，4 个样本，取值集中（一致性 87%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，4 个样本，一致性 75%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足

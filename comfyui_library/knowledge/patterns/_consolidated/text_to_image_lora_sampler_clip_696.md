---
name: text_to_image_lora_sampler_clip_696
type: Text To Image
frequency: 2
level: weak
coverage: 0.5775
common_nodes: [Any Switch (rgthree), CLIPTextEncode, CR Text, CheckpointLoaderSimple, ComfySwitchNode, ConditioningZeroOut, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetNode, INTConstant, JDCN_StringToList, KSampler, LayerColor: Brightness & Contrast, LayerFilter: AddGrain, LoadImage, LoraLoaderModelOnly, PathchSageAttentionKJ, PrimitiveBoolean, ProcessString, SaveImage, SetNode, StringConcatenate, VAEDecode, ZFImageReferenceAnalyzer, ZFLazyPromptSwitch, ZFPromptDirector, ZFPromptDirectorLocalLLM, ZFPromptDirectorMultiTextSelector, ZFPromptValidator, ZFReferenceCreativeAdapter, ZFTextListMemory, easy seed, easy showAnything, llama_cpp_model_loader, llama_cpp_parameters]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/提示词导演台_2083560457750794241.json, 图片生成/文生图/提示词导演台分镜出图，文生图创意设定一步到位_2110784213380329473.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_696

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/提示词导演台_2083560457750794241.json、图片生成/文生图/提示词导演台分镜出图，文生图创意设定一步到位_2110784213380329473.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：58%

## 共有节点

全部 2 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CLIPTextEncode`
- `CR Text`
- `CheckpointLoaderSimple`
- `ComfySwitchNode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `INTConstant`
- `JDCN_StringToList`
- `KSampler`
- `LayerColor: Brightness & Contrast`
- `LayerFilter: AddGrain`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `PrimitiveBoolean`
- `ProcessString`
- `SaveImage`
- `SetNode`
- `StringConcatenate`
- `VAEDecode`
- `ZFImageReferenceAnalyzer`
- `ZFLazyPromptSwitch`
- `ZFPromptDirector`
- `ZFPromptDirectorLocalLLM`
- `ZFPromptDirectorMultiTextSelector`
- `ZFPromptValidator`
- `ZFReferenceCreativeAdapter`
- `ZFTextListMemory`
- `easy seed`
- `easy showAnything`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `UNETLoader` —— 1/2 个有
- `VAELoader` —— 1/2 个有
- `solarL_SaveImagesToZip` —— 1/2 个有
- `孤海注释` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 552 | - | 2 | 14% |
| 高度 | 552 | - | 2 | 14% |
| 采样步数 | 6 | - | 2 | 67% |
| Prompt 约束强度(CFG) | 2.75 | - | 2 | 36% |
| 采样算法 | euler | - | 2 | 50% |
| 调度器 | simple | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 552，样本不足，未给区间，2 个样本，取值分散，一致性仅 14%
- 高度 中位数 552，样本不足，未给区间，2 个样本，取值分散，一致性仅 14%
- 采样步数 中位数 6，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 2.75，样本不足，未给区间，2 个样本，取值分散，一致性仅 36%
- 采样算法 最常用 euler，2 个样本，一致性 50%
- 调度器 最常用 simple，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（3/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

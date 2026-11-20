---
name: unknown_workflow_lora_sampler_unet_228
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.83
common_nodes: [CM_IntToNumber, Int, LayerUtility: PurgeVRAM V2, LoadImage, Number to Text, PlaySound|pysssss, PreviewImage, ProcessString, RandomInt, ReplaceString, ReplaceText, SaveImage, Text, TextConcatenate_UTK, TextSplitJoinByDelimiter, easy batchAnything, easy forLoopEnd, easy forLoopStart, easy indexAnything, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/动漫人物 gemma4+image全自动批量出图_2052999135049076738.json, 图片生成/图生图/超现实风格图像_2053336006258114562.json, 图片生成/图生图/魔幻风格批量生成_2053376032887058434.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_228

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/动漫人物 gemma4+image全自动批量出图_2052999135049076738.json、图片生成/图生图/超现实风格图像_2053336006258114562.json、图片生成/图生图/魔幻风格批量生成_2053376032887058434.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 3 个 workflow 都包含：
- `CM_IntToNumber`
- `Int`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `Number to Text`
- `PlaySound|pysssss`
- `PreviewImage`
- `ProcessString`
- `RandomInt`
- `ReplaceString`
- `ReplaceText`
- `SaveImage`
- `Text`
- `TextConcatenate_UTK`
- `TextSplitJoinByDelimiter`
- `easy batchAnything`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy indexAnything`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 2/3 个有
- `ConditioningZeroOut` —— 2/3 个有
- `EmptyLatentImage` —— 2/3 个有
- `Flux2KleinEditTextEncode_EditUtils` —— 2/3 个有
- `FluxResolutionNode` —— 2/3 个有
- `KSampler` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `UNETLoader` —— 2/3 个有
- `VAEDecode` —— 2/3 个有
- `VAELoader` —— 2/3 个有
- `llama_cpp_instruct_adv` —— 2/3 个有
- `llama_cpp_model_loader` —— 2/3 个有
- `llama_cpp_parameters` —— 2/3 个有
- `RHLLMChatNode` —— 1/3 个有
- `RH_GPT_Image15` —— 1/3 个有
- `RH_RhartImageG2OfficialImageToImage` —— 1/3 个有
- `Switch` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 512 | - | 2 | 100% |
| 高度 | 512 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足

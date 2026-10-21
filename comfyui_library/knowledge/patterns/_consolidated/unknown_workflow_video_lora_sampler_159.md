---
name: unknown_workflow_video_lora_sampler_159
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.809273
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, ConditioningZeroOut, EmptyLatentImage, EnhancedLoadDiffusionModel, FluxKontextMultiReferenceLatentMethod, KSampler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, PreviewImage, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, Split String by Commas, StringReplace, Text, TextConcatenate_UTK, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, easy MiniMaxH3ReferenceToVideoBridge, easy indexAnything, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MInimaxH3+Qwen+Gemma4全开源多参视频T1_2085991085813362690.json, 视频生成/图生视频/MInimaxH3+Qwen+Gemma4全开源多参视频T2_2085995902447210498.json, 视频生成/图生视频/MInimaxH3+Qwen+Gemma4全开源多参视频T3_2086341408956436482.json, 视频生成/图生视频/MInimaxH3+Qwen+Gemma4全开源多参视频T4_2086352524814151681.json, 视频生成/图生视频/MInimaxH3+Qwen+Gemma4全开源多参视频_2086338325744541698.json, 视频生成/图生视频/MInimaxH3+Qwen+Gemma4全开源多参视频八步加速_2087754291292491778.json, 视频生成/图生视频/MInimaxH3+Qwen+Gemma4全开源多参视频八步加速_2100066036602200066.json, 视频生成/图生视频/MInimaxH3+Qwen+Gemma4全开源多参视频八步加速_2100143918137561090.json, 视频生成/图生视频/MInimaxH3+Qwen+Gemma4全开源多参视频八步加速_2101302827879583746.json, 视频生成/图生视频/MInimaxH3电商人物广告_2086335748348923905.json, 视频生成/图生视频/高清弹吉他·的小女孩_2090255545633693697.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_159

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/MInimaxH3+Qwen+Gemma4全开源多参视频T1_2085991085813362690.json、视频生成/图生视频/MInimaxH3+Qwen+Gemma4全开源多参视频T2_2085995902447210498.json、视频生成/图生视频/MInimaxH3+Qwen+Gemma4全开源多参视频T3_2086341408956436482.json、视频生成/图生视频/MInimaxH3+Qwen+Gemma4全开源多参视频T4_2086352524814151681.json、视频生成/图生视频/MInimaxH3+Qwen+Gemma4全开源多参视频_2086338325744541698.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `EnhancedLoadDiffusionModel`
- `FluxKontextMultiReferenceLatentMethod`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PreviewImage`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `Split String by Commas`
- `StringReplace`
- `Text`
- `TextConcatenate_UTK`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `easy MiniMaxH3ReferenceToVideoBridge`
- `easy indexAnything`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `easy cleanGpuUsed` —— 10/11 个有
- `RHHiddenNodes` —— 9/11 个有
- `MiniMaxH3BlockCacheT8` —— 6/11 个有
- `JDCN_StringToList` —— 3/11 个有
- `ImageConcatMulti` —— 2/11 个有
- `ImageConcatenate_UTK` —— 2/11 个有
- `RH_Captioner` —— 2/11 个有
- `EmptyImage` —— 1/11 个有
- `ImageScaleToTotalPixels` —— 1/11 个有
- `Int` —— 1/11 个有
- `LayerUtility: PurgeVRAM V2` —— 1/11 个有
- `RandomInt` —— 1/11 个有
- `easy batchAnything` —— 1/11 个有
- `easy forLoopEnd` —— 1/11 个有
- `easy forLoopStart` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 11 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| 宽度 | 1280 | 1280 - 1280 | 11 | 100% |
| 高度 | 720 | 720 - 720 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 21/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 宽度 中位数 1280，观测区间 1280 - 1280，11 个样本，取值集中（一致性 100%）
- 高度 中位数 720，观测区间 720 - 720，11 个样本，取值集中（一致性 100%）
- 高发问题（21/11 个样本）：Steps较低可能导致细节不足

---
name: text_to_image_lora_sampler_clip_594
type: Text To Image
frequency: 2
level: weak
coverage: 0.586
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Fast Groups Muter (rgthree), Florence2ModelLoader, Florence2Run, Int, JanusImageUnderstanding, JanusModelLoader, Joy_caption_two_advanced, Joy_caption_two_load, Joy_extra_options, KSampler, LayerUtility: JoyCaptionBeta1, LayerUtility: JoyCaptionBeta1ExtraOptions, LayerUtility: LoadJoyCaptionBeta1Model, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewAny, PrimitiveStringMultiline, Qwen3_VQA, RH_LLMAPI_NODE, RH_LLMAPI_Pro_Node, RH_Translator, SaveImage, ShowText|pysssss, UNETLoader, VAEDecode, VAELoader, WD14Tagger|pysssss, easy saveText, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/提示词反推多方案集合（附使用场景介绍及性能分析）（2026.4.9更新）_1978072449780699138.json, 图片生成/文生图/Qwen 3.5_DeepSeek_JoyCaption_提示词反推多方案集合  Z-image b_2031980126619049986.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_594

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/反推提示词/提示词反推多方案集合（附使用场景介绍及性能分析）（2026.4.9更新）_1978072449780699138.json、图片生成/文生图/Qwen 3.5_DeepSeek_JoyCaption_提示词反推多方案集合  Z-image b_2031980126619049986.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：59%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Fast Groups Muter (rgthree)`
- `Florence2ModelLoader`
- `Florence2Run`
- `Int`
- `JanusImageUnderstanding`
- `JanusModelLoader`
- `Joy_caption_two_advanced`
- `Joy_caption_two_load`
- `Joy_extra_options`
- `KSampler`
- `LayerUtility: JoyCaptionBeta1`
- `LayerUtility: JoyCaptionBeta1ExtraOptions`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewAny`
- `PrimitiveStringMultiline`
- `Qwen3_VQA`
- `RH_LLMAPI_NODE`
- `RH_LLMAPI_Pro_Node`
- `RH_Translator`
- `SaveImage`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `WD14Tagger|pysssss`
- `easy saveText`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `JoyAI_Image_SM_Clip` —— 1/2 个有
- `JoyAI_Image_Understand` —— 1/2 个有
- `RH_Captioner` —— 1/2 个有
- `RH_Captioner_Pro` —— 1/2 个有
- `ShellAgentPluginOutputText` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1280 | - | 2 | 100% |
| 高度 | 1920 | - | 2 | 100% |
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | lcm | - | 2 | 50% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1280，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1920，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 lcm，2 个样本，一致性 50%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

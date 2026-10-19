---
name: unknown_workflow_lora_sampler_clip_60
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.7165
common_nodes: [BasicScheduler, BerniniPromptEnhancer, CFGGuider, CLIPLoader, CLIPTextEncode, CR Text, CR Text Concatenate, ConditioningZeroOut, CreateVideo, Display Any (rgthree), DualCLIPLoader, GetNode, GetVideoComponents, ImageScaleToMaxDimension, ImpactSwitch, JWInteger, KSamplerAdvanced, KSamplerSelect, LTXVAudioVAEDecode, LTXVAudioVideoMask, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, ManualSigmas, MathExpression|pysssss, ModelPatchMemoryCleaner, PathchSageAttentionKJ, PrimitiveInt, RH_LLMAPI_NODE, RH_LLMAPI_Pro_Node, RandomNoise, SamplerCustomAdvanced, SaveVideo, SetNode, StringReplace, Text, UNETLoader, VAEDecode, VAEDecodeTiled, VAEEncodeTiled, VAELoader, VAELoaderKJ, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/2064635596194271233.json, 视频生成/图生视频/2065001018898870274.json, 视频生成/图生视频/2073281054196383744.json, 视频生成/图生视频/2076389088697085954.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_60

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/2064635596194271233.json、视频生成/图生视频/2065001018898870274.json、视频生成/图生视频/2073281054196383744.json、视频生成/图生视频/2076389088697085954.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：72%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicScheduler`
- `BerniniPromptEnhancer`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `CR Text Concatenate`
- `ConditioningZeroOut`
- `CreateVideo`
- `Display Any (rgthree)`
- `DualCLIPLoader`
- `GetNode`
- `GetVideoComponents`
- `ImageScaleToMaxDimension`
- `ImpactSwitch`
- `JWInteger`
- `KSamplerAdvanced`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVAudioVideoMask`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MathExpression|pysssss`
- `ModelPatchMemoryCleaner`
- `PathchSageAttentionKJ`
- `PrimitiveInt`
- `RH_LLMAPI_NODE`
- `RH_LLMAPI_Pro_Node`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `SetNode`
- `StringReplace`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncodeTiled`
- `VAELoader`
- `VAELoaderKJ`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `BerniniConditioningReferenceSlots` —— 3/4 个有
- `FrameInterpolate` —— 3/4 个有
- `FrameInterpolationModelLoader` —— 3/4 个有
- `HAIGC_VideoLastFrame` —— 3/4 个有
- `RTXVideoSuperResolution` —— 3/4 个有
- `SaveImage` —— 3/4 个有
- `Fast Groups Muter (rgthree)` —— 2/4 个有
- `BatchImagesNode` —— 1/4 个有
- `BerniniConditioning` —— 1/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/4 个有
- `PreviewImage` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 258 | 129 - 258 | 4 | 75% |
| 高度 | 30 | 24 - 30 | 4 | 91% |
| 采样步数 | randomize | - | 4 | 100% |
| Prompt 约束强度(CFG) | 7 | 4 - 10 | 4 | 57% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | euler | - | 4 | 100% |
| 重绘幅度 | simple | - | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 258，观测区间 129 - 258，4 个样本
- 高度 中位数 30，观测区间 24 - 30，4 个样本，取值集中（一致性 91%）
- 采样步数 最常用 randomize，4 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 7，观测区间 4 - 10，4 个样本
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，4 个样本，一致性 100%
- 重绘幅度 最常用 simple，4 个样本，一致性 100%

---
name: text_to_image_video_lora_sampler_205
type: Text To Image
frequency: 2
level: weak
coverage: 0.829
common_nodes: [BasicGuider, BasicScheduler, CFGGuider, CLIPLoader, CLIPSetLastLayer, CLIPTextEncode, CR Split String, CR Text, CheckpointLoaderSimple, ConditioningZeroOut, DualCLIPLoader, EmptyAceStepLatentAudio, EmptyLatentAudio, EmptyLatentImage, Evaluate Integers, GetNode, Int, JWInteger, JjkShowText, KSampler, KSamplerSelect, LatentApplyOperationCFG, LatentOperationTonemapReinhard, LayerUtility: ImageScaleByAspectRatio V2, LoadWanVideoT5TextEncoder, LoraLoader, MathExpression|pysssss, ModelSamplingSD3, PreviewAudio, RH_Captioner, RH_LLMAPI_NODE, RH_Translator, RandomNoise, SamplerCustomAdvanced, SaveImage, SetNode, ShowText, StringFunction|pysssss, Text Concatenate (JPS), TextBox, TextEncodeAceStepAudio, TextInput_, TextSplitByDelimiter, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_MergeImages, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVACEStartToEndFrame, WanVideoVAELoader, easy cleanGpuUsed, easy imageSplitGrid, easy imagesSplitImage, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/1934491272000466945.json, 视频生成/图生视频/1934800531288465410.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_205

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1934491272000466945.json、视频生成/图生视频/1934800531288465410.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CFGGuider`
- `CLIPLoader`
- `CLIPSetLastLayer`
- `CLIPTextEncode`
- `CR Split String`
- `CR Text`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyAceStepLatentAudio`
- `EmptyLatentAudio`
- `EmptyLatentImage`
- `Evaluate Integers`
- `GetNode`
- `Int`
- `JWInteger`
- `JjkShowText`
- `KSampler`
- `KSamplerSelect`
- `LatentApplyOperationCFG`
- `LatentOperationTonemapReinhard`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadWanVideoT5TextEncoder`
- `LoraLoader`
- `MathExpression|pysssss`
- `ModelSamplingSD3`
- `PreviewAudio`
- `RH_Captioner`
- `RH_LLMAPI_NODE`
- `RH_Translator`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
- `ShowText`
- `StringFunction|pysssss`
- `Text Concatenate (JPS)`
- `TextBox`
- `TextEncodeAceStepAudio`
- `TextInput_`
- `TextSplitByDelimiter`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_MergeImages`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVACEStartToEndFrame`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy imageSplitGrid`
- `easy imagesSplitImage`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ColorMatch` —— 1/2 个有
- `Primitive integer [Crystools]` —— 1/2 个有
- `WanVideoLoraSelect` —— 1/2 个有
- `WanVideoMagCache` —— 1/2 个有
- `WanVideoSLG` —— 1/2 个有
- `WanVideoVACEModelSelect` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 40 | - | 2 | 100% |
| 高度 | 1 | - | 2 | 100% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| 采样步数 | 50 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 5 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 40，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 50，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

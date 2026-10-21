---
name: text_to_image_video_lora_sampler_57
type: Text To Image
frequency: 12
level: moderate
coverage: 0.844
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLTXVLatentVideo, EmptyLatentImage, EnhancedLoadDiffusionModel, FluxKontextMultiReferenceLatentMethod, INTConstant, Int, KSampler, KSamplerSelect, LTXAVTextEncoderLoader, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LayerUtility: PurgeVRAM V2, LiconMSR, LoadImage, LoraLoaderModelOnly, LowVRAMCheckpointLoader, ManualSigmas, PreviewImage, RandomInt, RandomNoise, SamplerCustomAdvanced, Text, TextEncodeQwenImageEditPlus, VAEDecode, VAELoader, VHS_VideoCombine, easy batchAnything, easy forLoopEnd, easy forLoopStart, easy indexAnything, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/2072609363512094721.json, 视频生成/图生视频/2072967530607632385.json, 视频生成/图生视频/2074307864331636737.json, 视频生成/图生视频/2074307850519797761.json, 视频生成/图生视频/2074345334553268226.json, 视频生成/图生视频/2074181237513744385.json, 视频生成/图生视频/2074184483884064769.json, 视频生成/图生视频/2074365914375614466.json, 视频生成/图生视频/2072600045387599874.json, 视频生成/图生视频/2074366376860545025.json, 视频生成/图生视频/2079795396607565825.json, 视频生成/图生视频/2079483993136918530.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_57

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/2072609363512094721.json、视频生成/图生视频/2072967530607632385.json、视频生成/图生视频/2074307864331636737.json、视频生成/图生视频/2074307850519797761.json、视频生成/图生视频/2074345334553268226.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 12 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLTXVLatentVideo`
- `EmptyLatentImage`
- `EnhancedLoadDiffusionModel`
- `FluxKontextMultiReferenceLatentMethod`
- `INTConstant`
- `Int`
- `KSampler`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXAddVideoICLoRAGuide`
- `LTXICLoRALoaderModelOnly`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVSeparateAVLatent`
- `LayerUtility: PurgeVRAM V2`
- `LiconMSR`
- `LoadImage`
- `LoraLoaderModelOnly`
- `LowVRAMCheckpointLoader`
- `ManualSigmas`
- `PreviewImage`
- `RandomInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `Text`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy batchAnything`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy indexAnything`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `TextConcatenate_UTK` —— 9/12 个有
- `RH_Captioner` —— 8/12 个有
- `Split String by Commas` —— 8/12 个有
- `StringReplace` —— 8/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/12 个有
- `ImageConcatenate_UTK` —— 6/12 个有
- `ImageScaleToTotalPixels` —— 4/12 个有
- `RHHiddenNodes` —— 4/12 个有
- `SetNode` —— 4/12 个有
- `CR Float To Integer` —— 2/12 个有
- `CR Prompt Text` —— 2/12 个有
- `FloatConstant` —— 2/12 个有
- `LTX2_NAG` —— 2/12 个有
- `PromptRelayEncode` —— 2/12 个有
- `SimpleMath+` —— 2/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1280 | 241 - 1280 | 12 | 65% |
| 高度 | 720 | 50 - 720 | 12 | 59% |
| 采样步数 | 8 | 8 - 8 | 12 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | euler | - | 12 | 100% |
| 调度器 | simple | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1280，观测区间 241 - 1280，12 个样本
- 高度 中位数 720，观测区间 50 - 720，12 个样本
- 采样步数 中位数 8，观测区间 8 - 8，12 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，12 个样本，一致性 100%
- 调度器 最常用 simple，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 高发问题（12/12 个样本）：Steps较低可能导致细节不足

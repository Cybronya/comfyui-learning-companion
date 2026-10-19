---
name: unknown_workflow_video_lora_sampler_606
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.881667
common_nodes: [BasicScheduler, CLIPTextEncode, ComfySwitchNode, DualCLIPLoader, EmptyLTXVLatentVideo, Float, KSamplerSelect, LTX2SamplingPreviewOverride, LTX2_NAG, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LiconMSR, LoadAudioUI, LoadImage, PrimitiveBoolean, SamplerCustom, SetLatentNoiseMask, SimpleMath+, SolidMask, UNETLoader, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine, VisualizeSigmasKJ]
problems: []
missing: []
members: [视频生成/图生视频/2071508676480950273.json, 视频生成/图生视频/LTX2.3-MSR  Multi-Image Reference（custom audio)_2087391136162865154.json, 视频生成/图生视频/2069271166765854721.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_606

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/2071508676480950273.json、视频生成/图生视频/LTX2.3-MSR  Multi-Image Reference（custom audio)_2087391136162865154.json、视频生成/图生视频/2069271166765854721.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicScheduler`
- `CLIPTextEncode`
- `ComfySwitchNode`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `Float`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `LTXAddVideoICLoRAGuide`
- `LTXICLoRALoaderModelOnly`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVSeparateAVLatent`
- `LiconMSR`
- `LoadAudioUI`
- `LoadImage`
- `PrimitiveBoolean`
- `SamplerCustom`
- `SetLatentNoiseMask`
- `SimpleMath+`
- `SolidMask`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `VisualizeSigmasKJ`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 2/3 个有
- `Dapao_LlamaCaption` —— 2/3 个有
- `Dapao_LlamaCaptionOptions` —— 2/3 个有
- `INTConstant` —— 2/3 个有
- `RegexReplace` —— 2/3 个有
- `easy cleanGpuUsed` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `Int` —— 1/3 个有
- `JjkText` —— 1/3 个有
- `Label (rgthree)` —— 1/3 个有
- `LoadAudio` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `MultiTextConcatenate` —— 1/3 个有
- `PrimitiveStringMultiline` —— 1/3 个有
- `RH_Utils` —— 1/3 个有
- `SetNode` —— 1/3 个有
- `SimpleMathBoolean+` —— 1/3 个有
- `ttN concat` —— 1/3 个有
- `孤海注释` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 241 | 241 - 241 | 3 | 100% |
| 高度 | 50 | 24 - 50 | 3 | 70% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 241，观测区间 241 - 241，3 个样本，取值集中（一致性 100%）
- 高度 中位数 50，观测区间 24 - 50，3 个样本

---
name: unknown_workflow_video_lora_sampler_522
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.8835
common_nodes: [BasicScheduler, CLIPTextEncode, ComfySwitchNode, DualCLIPLoader, EmptyLTXVLatentVideo, Float, KSamplerSelect, LTX2SamplingPreviewOverride, LTX2_NAG, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LiconMSR, LoadAudioUI, LoadImage, PrimitiveBoolean, SamplerCustom, SetLatentNoiseMask, SimpleMath+, SolidMask, UNETLoader, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine, VisualizeSigmasKJ]
problems: []
missing: []
members: [图片生成/图生图/LTX2.3 MSR全能参考慢剧+自定义音频_2069955656362315777.json, 视频生成/图生视频/LTX2.3 MSR全能参考慢剧+自定义音频_2071508676480950273.json, 视频生成/图生视频/LTX2.3-MSR  Multi-Image Reference（custom audio)_2087391136162865154.json, 视频生成/图生视频/LTX2.3-MSR全能参考升级-支持自定义音频-自动提示词版-高帧率-高动态-去字幕_2069271166765854721.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_522

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/LTX2.3 MSR全能参考慢剧+自定义音频_2069955656362315777.json、视频生成/图生视频/LTX2.3 MSR全能参考慢剧+自定义音频_2071508676480950273.json、视频生成/图生视频/LTX2.3-MSR  Multi-Image Reference（custom audio)_2087391136162865154.json、视频生成/图生视频/LTX2.3-MSR全能参考升级-支持自定义音频-自动提示词版-高帧率-高动态-去字幕_2069271166765854721.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 4 个 workflow 都包含：
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
- `CR Prompt Text` —— 2/4 个有
- `Dapao_LlamaCaption` —— 2/4 个有
- `Dapao_LlamaCaptionOptions` —— 2/4 个有
- `INTConstant` —— 2/4 个有
- `PrimitiveStringMultiline` —— 2/4 个有
- `RegexReplace` —— 2/4 个有
- `SimpleMathBoolean+` —— 2/4 个有
- `easy cleanGpuUsed` —— 2/4 个有
- `easy showAnything` —— 2/4 个有
- `Int` —— 1/4 个有
- `JjkText` —— 1/4 个有
- `Label (rgthree)` —— 1/4 个有
- `LoadAudio` —— 1/4 个有
- `LoraLoaderModelOnly` —— 1/4 个有
- `MultiTextConcatenate` —— 1/4 个有
- `RH_Utils` —— 1/4 个有
- `SetNode` —— 1/4 个有
- `SizeSelector` —— 1/4 个有
- `ttN concat` —— 1/4 个有
- `孤海注释` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 241 | 241 - 241 | 4 | 100% |
| 高度 | 37 | 24 - 50 | 4 | 65% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 241，观测区间 241 - 241，4 个样本，取值集中（一致性 100%）
- 高度 中位数 37，观测区间 24 - 50，4 个样本

---
key: 视频生成/图生视频/LTX2.3-MSR全能参考升级-支持自定义音频-自动提示词版-高帧率-高动态-去字幕_2069271166765854721.json
name: LTX2.3-MSR全能参考升级-支持自定义音频-自动提示词版-高帧率-高动态-去字幕_2069271166765854721.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3-MSR全能参考升级-支持自定义音频-自动提示词版-高帧率-高动态-去字幕_2069271166765854721.json
hash: 2ed9f3356b1f1f2e
coverage: 0.819672
learned_at: 2026-10-15 22:40:27
nodes: [KSamplerSelect, LTX2SamplingPreviewOverride, VisualizeSigmasKJ, CLIPTextEncode, LTXAddVideoICLoRAGuide, LTX2_NAG, LTXVConditioning, EmptyLTXVLatentVideo, LTXVConcatAVLatent, LTXVEmptyLatentAudio, BasicScheduler, VHS_VideoCombine, ComfySwitchNode, Reroute, MultiTextConcatenate, RegexReplace, SimpleMath+, SimpleMath+, LiconMSR, INTConstant, INTConstant, Float, LTXVAudioVAEEncode, SolidMask, SimpleMath+, CLIPTextEncode, easy cleanGpuUsed, SamplerCustom, LTXVCropGuides, LTXVSeparateAVLatent, VAEDecodeTiled, ComfySwitchNode, LTXVAudioVAEDecode, VHS_VideoCombine, VHS_VideoCombine, PrimitiveBoolean, UNETLoader, LTXICLoRALoaderModelOnly, DualCLIPLoader, SetLatentNoiseMask, VAELoaderKJ, VAELoaderKJ, INTConstant, SetNode, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoadImage, LoadImage, LoadImage, JjkText, CR Prompt Text, LoadAudioUI, 孤海注释, 孤海注释, 孤海注释, 孤海注释, easy showAnything, CR Prompt Text, Dapao_LlamaCaptionOptions, Dapao_LlamaCaption]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 50, "width": 241}
---

# 视频生成/图生视频/LTX2.3-MSR全能参考升级-支持自定义音频-自动提示词版-高帧率-高动态-去字幕_2069271166765854721.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2069271166765854721.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Other

**节点**（61 个）：
- `KSamplerSelect` ★核心
- `LTX2SamplingPreviewOverride`
- `VisualizeSigmasKJ`
- `CLIPTextEncode` ★核心
- `LTXAddVideoICLoRAGuide`
- `LTX2_NAG`
- `LTXVConditioning`
- `EmptyLTXVLatentVideo`
- `LTXVConcatAVLatent`
- `LTXVEmptyLatentAudio` ★核心
- `BasicScheduler`
- `VHS_VideoCombine`
- `ComfySwitchNode`
- `Reroute`
- `MultiTextConcatenate`
- `RegexReplace`
- `SimpleMath+`
- `SimpleMath+`
- `LiconMSR`
- `INTConstant`
- `INTConstant`
- `Float`
- `LTXVAudioVAEEncode` ★核心
- `SolidMask`
- `SimpleMath+`
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `SamplerCustom` ★核心
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `ComfySwitchNode`
- `LTXVAudioVAEDecode` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `PrimitiveBoolean`
- `UNETLoader` ★核心
- `LTXICLoRALoaderModelOnly` ★核心
- `DualCLIPLoader`
- `SetLatentNoiseMask`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `INTConstant`
- `SetNode`
- `JjkText`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `JjkText`
- `CR Prompt Text`
- `LoadAudioUI`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `easy showAnything`
- `CR Prompt Text`
- `Dapao_LlamaCaptionOptions`
- `Dapao_LlamaCaption`

## 关键参数

- `width` = `241`
- `height` = `50`
- `batch_size` = `1`

## 知识

覆盖率 **82%**（50/61）

**有卡**：`KSamplerSelect`、`LTX2SamplingPreviewOverride`、`VisualizeSigmasKJ`、`CLIPTextEncode`、`LTXAddVideoICLoRAGuide`、`LTX2_NAG`、`LTXVConditioning`、`EmptyLTXVLatentVideo`、`LTXVConcatAVLatent`、`LTXVEmptyLatentAudio`、`BasicScheduler`、`VHS_VideoCombine`、`MultiTextConcatenate`、`RegexReplace`、`SimpleMath+`、`LiconMSR`、`INTConstant`、`Float`、`LTXVAudioVAEEncode`、`SolidMask`、`easy cleanGpuUsed`、`SamplerCustom`、`LTXVCropGuides`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`PrimitiveBoolean`、`UNETLoader`、`LTXICLoRALoaderModelOnly`、`DualCLIPLoader`、`SetLatentNoiseMask`、`VAELoaderKJ`、`LoraLoaderModelOnly`、`LoadImage`、`CR Prompt Text`、`LoadAudioUI`、`Dapao_LlamaCaptionOptions`、`Dapao_LlamaCaption`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom、LTXVConcatAVLatent、LTXVSeparateAVLatent

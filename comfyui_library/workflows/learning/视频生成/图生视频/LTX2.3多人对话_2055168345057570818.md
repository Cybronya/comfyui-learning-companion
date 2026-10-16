---
key: 视频生成/图生视频/LTX2.3多人对话_2055168345057570818.json
name: LTX2.3多人对话_2055168345057570818.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2055168345057570818.json
hash: 012b62e6f9203e62
coverage: 0.906977
learned_at: 2026-10-15 22:37:55
nodes: [VAELoaderKJ, ImageResizeKJv2, Switch image [Crystools], EmptyImage, easy isNone, SimpleMath+, INTConstant, CM_BoolToInt, UNETLoader, DualCLIPLoader, easy showAnything, PathchSageAttentionKJ, LTXVSeparateAVLatent, EmptyLTXVLatentVideo, LTXVChunkFeedForward, LTXVConditioning, ManualSigmas, KSamplerSelect, LTXVConcatAVLatent, PreviewImage, BasicScheduler, VisualizeSigmasKJ, SamplerCustom, VAELoaderKJ, SimpleMath+, SimpleMath+, LTXVImgToVideoInplaceKJ, VAEDecodeTiled, LTXVAudioVAEDecode, LTX2_NAG, LTX2SamplingPreviewOverride, LTXVEmptyLatentAudio, Lora Loader Stack (rgthree), LoadImage, PreviewImage, VHS_VideoCombine, INTConstant, INTConstant, CLIPTextEncode, CLIPTextEncode, PreviewImage, INTConstant, INTConstant]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 361}
---

# 视频生成/图生视频/LTX2.3多人对话_2055168345057570818.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2055168345057570818.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（43 个）：
- `VAELoaderKJ`
- `ImageResizeKJv2`
- `Switch image [Crystools]`
- `EmptyImage`
- `easy isNone`
- `SimpleMath+`
- `INTConstant`
- `CM_BoolToInt`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `easy showAnything`
- `PathchSageAttentionKJ`
- `LTXVSeparateAVLatent`
- `EmptyLTXVLatentVideo`
- `LTXVChunkFeedForward`
- `LTXVConditioning`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `PreviewImage`
- `BasicScheduler`
- `VisualizeSigmasKJ`
- `SamplerCustom` ★核心
- `VAELoaderKJ`
- `SimpleMath+`
- `SimpleMath+`
- `LTXVImgToVideoInplaceKJ`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTX2_NAG`
- `LTX2SamplingPreviewOverride`
- `LTXVEmptyLatentAudio` ★核心
- `Lora Loader Stack (rgthree)`
- `LoadImage`
- `PreviewImage`
- `VHS_VideoCombine`
- `INTConstant`
- `INTConstant`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `INTConstant`
- `INTConstant`

## 关键参数

- `width` = `361`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **91%**（39/43）

**有卡**：`VAELoaderKJ`、`ImageResizeKJv2`、`Switch image [Crystools]`、`EmptyImage`、`easy isNone`、`SimpleMath+`、`INTConstant`、`CM_BoolToInt`、`UNETLoader`、`DualCLIPLoader`、`PathchSageAttentionKJ`、`LTXVSeparateAVLatent`、`EmptyLTXVLatentVideo`、`LTXVChunkFeedForward`、`LTXVConditioning`、`ManualSigmas`、`KSamplerSelect`、`LTXVConcatAVLatent`、`BasicScheduler`、`VisualizeSigmasKJ`、`SamplerCustom`、`LTXVImgToVideoInplaceKJ`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`LTX2_NAG`、`LTX2SamplingPreviewOverride`、`LTXVEmptyLatentAudio`、`Lora Loader Stack (rgthree)`、`LoadImage`、`VHS_VideoCombine`、`CLIPTextEncode`

**用到的条目**：CLIPTextEncode、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom、LTXVConcatAVLatent、LTXVSeparateAVLatent、VAEDecodeTiled

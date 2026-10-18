---
key: 视频生成/图生视频/LTX2.3多人对话_2056562094497161218.json
name: LTX2.3多人对话_2056562094497161218.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3多人对话_2056562094497161218.json
hash: 76e811d3f0d886e1
coverage: 0.948718
learned_at: 2026-10-15 22:38:04
nodes: [VAELoaderKJ, Switch image [Crystools], EmptyImage, easy isNone, SimpleMath+, INTConstant, CM_BoolToInt, UNETLoader, DualCLIPLoader, easy showAnything, PathchSageAttentionKJ, LTXVSeparateAVLatent, EmptyLTXVLatentVideo, LTXVChunkFeedForward, LTXVConditioning, ManualSigmas, KSamplerSelect, LTXVConcatAVLatent, SamplerCustom, VAELoaderKJ, SimpleMath+, VAEDecodeTiled, LTXVAudioVAEDecode, LTX2_NAG, LTX2SamplingPreviewOverride, LTXVEmptyLatentAudio, Lora Loader Stack (rgthree), PreviewImage, VHS_VideoCombine, CLIPTextEncode, INTConstant, CLIPTextEncode, LTXVImgToVideoInplaceKJ, INTConstant, INTConstant, INTConstant, SimpleMath+, ImageResizeKJv2, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 361}
---

# 视频生成/图生视频/LTX2.3多人对话_2056562094497161218.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2056562094497161218.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（39 个）：
- `VAELoaderKJ`
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
- `SamplerCustom` ★核心
- `VAELoaderKJ`
- `SimpleMath+`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTX2_NAG`
- `LTX2SamplingPreviewOverride`
- `LTXVEmptyLatentAudio` ★核心
- `Lora Loader Stack (rgthree)`
- `PreviewImage`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `INTConstant`
- `CLIPTextEncode` ★核心
- `LTXVImgToVideoInplaceKJ`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `SimpleMath+`
- `ImageResizeKJv2`
- `LoadImage`

## 关键参数

- `width` = `361`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **95%**（37/39）

**有卡**：`VAELoaderKJ`、`Switch image [Crystools]`、`EmptyImage`、`easy isNone`、`SimpleMath+`、`INTConstant`、`CM_BoolToInt`、`UNETLoader`、`DualCLIPLoader`、`PathchSageAttentionKJ`、`LTXVSeparateAVLatent`、`EmptyLTXVLatentVideo`、`LTXVChunkFeedForward`、`LTXVConditioning`、`ManualSigmas`、`KSamplerSelect`、`LTXVConcatAVLatent`、`SamplerCustom`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`LTX2_NAG`、`LTX2SamplingPreviewOverride`、`LTXVEmptyLatentAudio`、`Lora Loader Stack (rgthree)`、`VHS_VideoCombine`、`CLIPTextEncode`、`LTXVImgToVideoInplaceKJ`、`ImageResizeKJv2`、`LoadImage`

**用到的条目**：CLIPTextEncode、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom、LTXVConcatAVLatent、LTXVSeparateAVLatent、VAEDecodeTiled

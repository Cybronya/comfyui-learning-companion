---
key: 平台全量/LTX-2.3-outpaint-视频外扩-效果惊艳_2050409773828452353.json
name: LTX-2.3-outpaint-视频外扩-效果惊艳_2050409773828452353
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/LTX-2.3-outpaint-视频外扩-效果惊艳_2050409773828452353.json
hash: 4c9e29cc4d92b4aa
coverage: 1
learned_at: 2026-11-14 00:37:04
nodes: [EmptyLTXVLatentVideo, LTXVImgToVideoConditionOnly, LTXVPreprocess, CFGGuider, KSamplerSelect, RandomNoise, LTXVSeparateAVLatent, PrimitiveBoolean, DualCLIPLoader, ResizeImageMaskNode, LTXVAudioVAEDecode, LoadImage, LTXICLoRALoaderModelOnly, UNETLoader, VAELoaderKJ, VAELoaderKJ, CLIPTextEncode, LTXVConditioning, CLIPTextEncode, LTXAddVideoICLoRAGuide, LTXVConcatAVLatent, GetVideoComponents, CustomAddLabel, LTXVCropGuides, ManualSigmas, SamplerCustomAdvanced, TTResolutionSelector, VHS_LoadVideo, SaveVideo, VHS_VideoCombine, GetImageSize, VAEDecodeTiled, CreateVideo, ImageResizeKJv2, VHS_VideoInfo, SimpleMath+, LTXVEmptyLatentAudio, Int, Text, SimpleMath+, Int]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 平台全量/LTX-2.3-outpaint-视频外扩-效果惊艳_2050409773828452353.json

> 来源文件 `comfyui_library/workflows/平台全量/LTX-2.3-outpaint-视频外扩-效果惊艳_2050409773828452353.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（41 个）：
- `EmptyLTXVLatentVideo`
- `LTXVImgToVideoConditionOnly`
- `LTXVPreprocess`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `PrimitiveBoolean`
- `DualCLIPLoader`
- `ResizeImageMaskNode`
- `LTXVAudioVAEDecode` ★核心
- `LoadImage`
- `LTXICLoRALoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `VAELoaderKJ`
- `VAELoaderKJ`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `LTXAddVideoICLoRAGuide`
- `LTXVConcatAVLatent`
- `GetVideoComponents`
- `CustomAddLabel`
- `LTXVCropGuides`
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `TTResolutionSelector`
- `VHS_LoadVideo`
- `SaveVideo`
- `VHS_VideoCombine`
- `GetImageSize`
- `VAEDecodeTiled` ★核心
- `CreateVideo`
- `ImageResizeKJv2`
- `VHS_VideoInfo`
- `SimpleMath+`
- `LTXVEmptyLatentAudio` ★核心
- `Int`
- `Text`
- `SimpleMath+`
- `Int`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **100%**（41/41）

**有卡**：`EmptyLTXVLatentVideo`、`LTXVImgToVideoConditionOnly`、`LTXVPreprocess`、`CFGGuider`、`KSamplerSelect`、`RandomNoise`、`LTXVSeparateAVLatent`、`PrimitiveBoolean`、`DualCLIPLoader`、`ResizeImageMaskNode`、`LTXVAudioVAEDecode`、`LoadImage`、`LTXICLoRALoaderModelOnly`、`UNETLoader`、`VAELoaderKJ`、`CLIPTextEncode`、`LTXVConditioning`、`LTXAddVideoICLoRAGuide`、`LTXVConcatAVLatent`、`GetVideoComponents`、`CustomAddLabel`、`LTXVCropGuides`、`ManualSigmas`、`SamplerCustomAdvanced`、`TTResolutionSelector`、`VHS_LoadVideo`、`SaveVideo`、`VHS_VideoCombine`、`GetImageSize`、`VAEDecodeTiled`、`CreateVideo`、`ImageResizeKJv2`、`VHS_VideoInfo`、`SimpleMath+`、`LTXVEmptyLatentAudio`、`Int`、`Text`

**用到的条目**：CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、EmptyLTXVLatentVideo、LTXVAudioVAEDecode

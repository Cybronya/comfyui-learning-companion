---
key: 视频生成/图生视频/LTX-2.3_ICLoRA_cameraman_v2-镜头迁移_2074096652201320450.json
name: LTX-2.3_ICLoRA_cameraman_v2-镜头迁移_2074096652201320450.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX-2.3_ICLoRA_cameraman_v2-镜头迁移_2074096652201320450.json
hash: 985e8d3f6f790187
coverage: 0.690909
learned_at: 2026-10-15 22:41:12
nodes: [CFGGuider, KSamplerSelect, RandomNoise, SetNode, SetNode, SetNode, SetNode, SetNode, LTXVSeparateAVLatent, LTXVCropGuides, SetNode, LTXVConcatAVLatent, ManualSigmas, SetNode, SetNode, SetNode, SetNode, LTXVConditioning, CLIPTextEncode, SetNode, GetNode, SimpleMath+, SetNode, VAELoaderKJ, DualCLIPLoader, LatentUpscaleModelLoader, INTConstant, INTConstant, ImageResizeKJv2, SamplerCustomAdvanced, VAELoaderKJ, SetNode, PrimitiveBoolean, VHS_VideoInfo, SetNode, LTXVEmptyLatentAudio, ImageResizeKJv2, GetImageSize, SimpleMath+, SimpleMath+, EmptyLTXVLatentVideo, LTXVPreprocess, UNETLoader, LTXVImgToVideoConditionOnly, LTXAddVideoICLoRAGuide, LoadImage, VHS_LoadVideo, GetNode, GetNode, VHS_VideoCombine, VAEDecodeTiled, LTXVAudioVAEDecode, VHS_VideoCombine, CLIPTextEncode, LTXICLoRALoaderModelOnly]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX-2.3_ICLoRA_cameraman_v2-镜头迁移_2074096652201320450.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2074096652201320450.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（55 个）：
- `CFGGuider`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `SetNode`
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `SetNode`
- `GetNode`
- `SimpleMath+`
- `SetNode`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `LatentUpscaleModelLoader`
- `INTConstant`
- `INTConstant`
- `ImageResizeKJv2`
- `SamplerCustomAdvanced` ★核心
- `VAELoaderKJ`
- `SetNode`
- `PrimitiveBoolean`
- `VHS_VideoInfo`
- `SetNode`
- `LTXVEmptyLatentAudio` ★核心
- `ImageResizeKJv2`
- `GetImageSize`
- `SimpleMath+`
- `SimpleMath+`
- `EmptyLTXVLatentVideo`
- `LTXVPreprocess`
- `UNETLoader` ★核心
- `LTXVImgToVideoConditionOnly`
- `LTXAddVideoICLoRAGuide`
- `LoadImage`
- `VHS_LoadVideo`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `LTXICLoRALoaderModelOnly` ★核心

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **69%**（38/55）

**有卡**：`CFGGuider`、`KSamplerSelect`、`RandomNoise`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`LTXVConcatAVLatent`、`ManualSigmas`、`LTXVConditioning`、`CLIPTextEncode`、`SimpleMath+`、`VAELoaderKJ`、`DualCLIPLoader`、`LatentUpscaleModelLoader`、`INTConstant`、`ImageResizeKJv2`、`SamplerCustomAdvanced`、`PrimitiveBoolean`、`VHS_VideoInfo`、`LTXVEmptyLatentAudio`、`GetImageSize`、`EmptyLTXVLatentVideo`、`LTXVPreprocess`、`UNETLoader`、`LTXVImgToVideoConditionOnly`、`LTXAddVideoICLoRAGuide`、`LoadImage`、`VHS_LoadVideo`、`VHS_VideoCombine`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`LTXICLoRALoaderModelOnly`

**用到的条目**：CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent、LTXVSeparateAVLatent

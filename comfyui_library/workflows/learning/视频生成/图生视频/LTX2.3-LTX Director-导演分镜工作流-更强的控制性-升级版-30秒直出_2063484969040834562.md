---
key: 视频生成/图生视频/LTX2.3-LTX Director-导演分镜工作流-更强的控制性-升级版-30秒直出_2063484969040834562.json
name: LTX2.3-LTX Director-导演分镜工作流-更强的控制性-升级版-30秒直出_2063484969040834562.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3-LTX Director-导演分镜工作流-更强的控制性-升级版-30秒直出_2063484969040834562.json
hash: 0a031ebcf01c17b6
coverage: 0.813953
learned_at: 2026-10-15 22:39:13
nodes: [ImageScaleToTotalPixels, SeedVR2BlockSwap, SeedVR2ExtraArgs, SaveImage, SeedVR2, Fast Groups Bypasser (rgthree), KSamplerSelect, LTXVConditioning, CLIPTextEncode, CheckpointLoaderSimple, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, DualCLIPLoader, VAELoaderKJ, VAELoaderKJ, LTX2SamplingPreviewOverride, VisualizeSigmasKJ, BasicScheduler, LTXVConcatAVLatent, LTX2_NAG, SamplerCustom, LTXVSeparateAVLatent, LTXVCropGuides, VAEDecodeTiled, CreateVideo, GetVideoComponents, LTXVAudioVAEDecode, VHS_VideoCombine, LoadImage, GuHaiAutoImageSplit, PreviewImage, Fast Groups Bypasser (rgthree), VHS_VideoCombine, MarkdownNote, LTXDirectorGuide, YusuLTXDirector, 孤海注释, 孤海注释, 孤海注释, 孤海注释]
patterns: []
missing: []
parameters: {"checkpoint": "ltx-2.3-22b-dev-fp8.safetensors"}
---

# 视频生成/图生视频/LTX2.3-LTX Director-导演分镜工作流-更强的控制性-升级版-30秒直出_2063484969040834562.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2063484969040834562.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（43 个）：
- `ImageScaleToTotalPixels`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `SaveImage`
- `SeedVR2`
- `Fast Groups Bypasser (rgthree)`
- `KSamplerSelect` ★核心
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `DualCLIPLoader`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `LTX2SamplingPreviewOverride`
- `VisualizeSigmasKJ`
- `BasicScheduler`
- `LTXVConcatAVLatent`
- `LTX2_NAG`
- `SamplerCustom` ★核心
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `VAEDecodeTiled` ★核心
- `CreateVideo`
- `GetVideoComponents`
- `LTXVAudioVAEDecode` ★核心
- `VHS_VideoCombine`
- `LoadImage`
- `GuHaiAutoImageSplit`
- `PreviewImage`
- `Fast Groups Bypasser (rgthree)`
- `VHS_VideoCombine`
- `MarkdownNote`
- `LTXDirectorGuide`
- `YusuLTXDirector`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `孤海注释`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **81%**（35/43）

**有卡**：`ImageScaleToTotalPixels`、`SeedVR2BlockSwap`、`SeedVR2ExtraArgs`、`SaveImage`、`SeedVR2`、`KSamplerSelect`、`LTXVConditioning`、`CLIPTextEncode`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`DualCLIPLoader`、`VAELoaderKJ`、`LTX2SamplingPreviewOverride`、`VisualizeSigmasKJ`、`BasicScheduler`、`LTXVConcatAVLatent`、`LTX2_NAG`、`SamplerCustom`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`VAEDecodeTiled`、`CreateVideo`、`GetVideoComponents`、`LTXVAudioVAEDecode`、`VHS_VideoCombine`、`LoadImage`、`GuHaiAutoImageSplit`、`LTXDirectorGuide`、`YusuLTXDirector`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、KSamplerSelect、SeedVR2、SeedVR2BlockSwap、SeedVR2ExtraArgs

---
key: 视频生成/图生视频/全能Pro+多角度自由切换+首尾帧出图完美切换 一键出片 V1.0_2011468518830641154.json
name: 全能Pro+多角度自由切换+首尾帧出图完美切换 一键出片 V1.0_2011468518830641154.json
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/全能Pro+多角度自由切换+首尾帧出图完美切换 一键出片 V1.0_2011468518830641154.json
hash: 305cf8fbb8083da6
coverage: 0.736111
learned_at: 2026-10-15 22:34:23
nodes: [ModelSamplingSD3, ModelSamplingSD3, ModelPatchTorchSettings, ModelPatchTorchSettings, PathchSageAttentionKJ, PathchSageAttentionKJ, SetNode, VAELoader, SetNode, ImageResizeKJ, LayerUtility: ImageScaleByAspectRatio V2, ImpactInt, CLIPVisionLoader, CLIPVisionEncode, CLIPVisionEncode, CLIPTextEncode, CLIPTextEncode, MathExpression|pysssss, GetNode, WanMoeKSampler, easy getNode, RIFE VFI, easy getNode, easy setNode, VAEDecode, Mute / Bypass Repeater (rgthree), Fast Bypasser (rgthree), FluxKontextMultiReferenceLatentMethod, FluxKontextMultiReferenceLatentMethod, CFGNorm, TextEncodeQwenImageEditPlus, Note, VAELoader, CLIPLoader, UNETLoader, TextEncodeQwenImageEditPlus, KSampler, ModelSamplingAuraFlow, VAEEncode, VAEDecode, GetNode, WanFirstLastFrameToVideo, GetNode, GetNode, GetNode, SetNode, GetNode, SetNode, SetNode, GetNode, GetNode, FluxKontextImageScale, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, PreviewImage, Reroute, SetNode, SetNode, CLIPLoader, VHS_VideoCombine, VHS_VideoCombine, ImpactInt, easy showAnything, UNETLoader, QwenMultiangleCameraNode, RH_Nano_Banana2_Image2Image, LoadImage, RH_Captioner_Pro, UNETLoader]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 213472552666429, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/全能Pro+多角度自由切换+首尾帧出图完美切换 一键出片 V1.0_2011468518830641154.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2011468518830641154.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（72 个）：
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `SetNode`
- `VAELoader`
- `SetNode`
- `ImageResizeKJ`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImpactInt`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `MathExpression|pysssss`
- `GetNode`
- `WanMoeKSampler` ★核心
- `easy getNode`
- `RIFE VFI`
- `easy getNode`
- `easy setNode`
- `VAEDecode` ★核心
- `Mute / Bypass Repeater (rgthree)`
- `Fast Bypasser (rgthree)`
- `FluxKontextMultiReferenceLatentMethod`
- `FluxKontextMultiReferenceLatentMethod`
- `CFGNorm`
- `TextEncodeQwenImageEditPlus`
- `Note`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `TextEncodeQwenImageEditPlus`
- `KSampler` ★核心
- `ModelSamplingAuraFlow`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `GetNode`
- `WanFirstLastFrameToVideo`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `FluxKontextImageScale`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PreviewImage`
- `Reroute`
- `SetNode`
- `SetNode`
- `CLIPLoader`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ImpactInt`
- `easy showAnything`
- `UNETLoader` ★核心
- `QwenMultiangleCameraNode`
- `RH_Nano_Banana2_Image2Image`
- `LoadImage`
- `RH_Captioner_Pro`
- `UNETLoader` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `213472552666429`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **74%**（53/72）

**有卡**：`ModelSamplingSD3`、`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`VAELoader`、`ImageResizeKJ`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImpactInt`、`CLIPVisionLoader`、`CLIPVisionEncode`、`CLIPTextEncode`、`MathExpression|pysssss`、`WanMoeKSampler`、`easy getNode`、`RIFE VFI`、`easy setNode`、`VAEDecode`、`Mute / Bypass Repeater (rgthree)`、`Fast Bypasser (rgthree)`、`FluxKontextMultiReferenceLatentMethod`、`CFGNorm`、`TextEncodeQwenImageEditPlus`、`CLIPLoader`、`UNETLoader`、`KSampler`、`ModelSamplingAuraFlow`、`VAEEncode`、`WanFirstLastFrameToVideo`、`FluxKontextImageScale`、`LoraLoaderModelOnly`、`VHS_VideoCombine`、`QwenMultiangleCameraNode`、`RH_Nano_Banana2_Image2Image`、`LoadImage`、`RH_Captioner_Pro`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

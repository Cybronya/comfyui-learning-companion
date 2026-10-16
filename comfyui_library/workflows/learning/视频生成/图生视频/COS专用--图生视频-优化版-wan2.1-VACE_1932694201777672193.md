---
key: 视频生成/图生视频/COS专用--图生视频-优化版-wan2.1-VACE_1932694201777672193.json
name: COS专用--图生视频-优化版-wan2.1-VACE_1932694201777672193.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1932694201777672193.json
hash: b9681d6ea9f1b92d
coverage: 0.828571
learned_at: 2026-10-15 22:30:12
nodes: [WanVideoTeaCache, LoadWanVideoT5TextEncoder, WanVideoEnhanceAVideo, MathExpression|pysssss, MathExpression|pysssss, Reroute, WanVideoBlockSwap, WanVideoModelLoader, WanVideoTextEncode, Int, InversionDemoLazyIndexSwitch, InversionDemoLazyIndexSwitch, MathExpression|pysssss, Int, Int, MMAudioFeatureUtilsLoader, CLIPTextEncode, CLIPTextEncode, Evaluate Integers, CheckpointLoaderSimple, CLIPLoader, EmptyLatentAudio, VAEDecodeAudio, KSampler, MMAudioModelLoader, RH_Captioner, PreviewAudio, MathExpression|pysssss, WanVideoVACEModelSelect, WanVideoSLG, WanVideoExperimentalArgs, ImageResize+, easy showAnything, MMAudioSampler, PreviewAudio, AudioCombine, SaveAudio, RH_Captioner, RH_Captioner, easy showAnything, RH_Translator, easy showAnything, VHS_VideoCombine, Int, FluxResolutionNode, JWInteger, MathExpression|pysssss, Note _O, Note _O, Note _O, JjkText, easy showAnything, JjkText, easy textSwitch, easy showAnything, LoadImage, WanVideoVAELoader, WanVideoVACEEncode, WanVideoSampler, WanVideoDecode, ColorMatch, ImageConcatMulti, easy showAnything, RH_Translator, easy showAnything, ImageResize+, PreviewImage, VHS_VideoCombine, VHS_VideoCombine, JjkText]
patterns: []
missing: []
problems: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 7, "checkpoint": "stable-audio-open-1.0.safetensors", "denoise": 1, "height": 1, "sampler_name": "dpmpp_3m_sde_gpu", "scheduler": "exponential", "seed": 892441830667270, "steps": 60, "width": 40}
discoveries: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 视频生成/图生视频/COS专用--图生视频-优化版-wan2.1-VACE_1932694201777672193.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1932694201777672193.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（70 个）：
- `WanVideoTeaCache`
- `LoadWanVideoT5TextEncoder`
- `WanVideoEnhanceAVideo`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `Reroute`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoTextEncode`
- `Int`
- `InversionDemoLazyIndexSwitch`
- `InversionDemoLazyIndexSwitch`
- `MathExpression|pysssss`
- `Int`
- `Int`
- `MMAudioFeatureUtilsLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Evaluate Integers`
- `CheckpointLoaderSimple` ★核心
- `CLIPLoader`
- `EmptyLatentAudio` ★核心
- `VAEDecodeAudio` ★核心
- `KSampler` ★核心
- `MMAudioModelLoader`
- `RH_Captioner`
- `PreviewAudio`
- `MathExpression|pysssss`
- `WanVideoVACEModelSelect`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `ImageResize+`
- `easy showAnything`
- `MMAudioSampler` ★核心
- `PreviewAudio`
- `AudioCombine`
- `SaveAudio`
- `RH_Captioner`
- `RH_Captioner`
- `easy showAnything`
- `RH_Translator`
- `easy showAnything`
- `VHS_VideoCombine`
- `Int`
- `FluxResolutionNode`
- `JWInteger`
- `MathExpression|pysssss`
- `Note _O`
- `Note _O`
- `Note _O`
- `JjkText`
- `easy showAnything`
- `JjkText`
- `easy textSwitch`
- `easy showAnything`
- `LoadImage`
- `WanVideoVAELoader`
- `WanVideoVACEEncode`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `ColorMatch`
- `ImageConcatMulti`
- `easy showAnything`
- `RH_Translator`
- `easy showAnything`
- `ImageResize+`
- `PreviewImage`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `JjkText`

## 关键参数

- `checkpoint` = `stable-audio-open-1.0.safetensors`
- `width` = `40`
- `height` = `1`
- `seed` = `892441830667270`
- `steps` = `60`
- `cfg` = `7`
- `sampler_name` = `dpmpp_3m_sde_gpu`
- `scheduler` = `exponential`
- `denoise` = `1`

## 知识

覆盖率 **83%**（58/70）

**有卡**：`WanVideoTeaCache`、`LoadWanVideoT5TextEncoder`、`WanVideoEnhanceAVideo`、`MathExpression|pysssss`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoTextEncode`、`Int`、`InversionDemoLazyIndexSwitch`、`MMAudioFeatureUtilsLoader`、`CLIPTextEncode`、`Evaluate Integers`、`CheckpointLoaderSimple`、`CLIPLoader`、`EmptyLatentAudio`、`VAEDecodeAudio`、`KSampler`、`MMAudioModelLoader`、`RH_Captioner`、`PreviewAudio`、`WanVideoVACEModelSelect`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`ImageResize+`、`MMAudioSampler`、`AudioCombine`、`SaveAudio`、`RH_Translator`、`VHS_VideoCombine`、`FluxResolutionNode`、`JWInteger`、`Note _O`、`easy textSwitch`、`LoadImage`、`WanVideoVAELoader`、`WanVideoVACEEncode`、`WanVideoSampler`、`WanVideoDecode`、`ColorMatch`、`ImageConcatMulti`

**用到的条目**：KSampler、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、LoadImage、WanVideoSampler、MMAudioSampler、VAEDecodeAudio

## 参数体检

发现 1 个问题：
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

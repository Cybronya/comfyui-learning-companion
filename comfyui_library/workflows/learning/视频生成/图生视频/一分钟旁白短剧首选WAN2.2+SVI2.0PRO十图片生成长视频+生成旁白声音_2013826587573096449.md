---
key: 视频生成/图生视频/一分钟旁白短剧首选WAN2.2+SVI2.0PRO十图片生成长视频+生成旁白声音_2013826587573096449.json
name: 一分钟旁白短剧首选WAN2.2+SVI2.0PRO十图片生成长视频+生成旁白声音_2013826587573096449.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/一分钟旁白短剧首选WAN2.2+SVI2.0PRO十图片生成长视频+生成旁白声音_2013826587573096449.json
hash: edd8d84a843a2a0b
coverage: 0.590909
learned_at: 2026-10-15 22:34:32
nodes: [SetNode, SetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, SetNode, GetNode, GetNode, GetNode, CLIPTextEncode, CLIPTextEncode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, CLIPTextEncode, CLIPLoader, GetNode, SetNode, SetNode, SetNode, SetNode, GetNode, SetNode, ImageResizeKJv2, GetNode, GetNode, GetNode, VAELoader, VAEEncode, VAEEncode, SetNode, ImageResizeKJv2, GetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, INTConstant, SetNode, KSamplerAdvanced, GetNode, KSamplerAdvanced, Any To Any, Any To Any, KSamplerAdvanced, easy forLoopStart, Any To Any, GetNode, SDVM Image List Repeat, Any To String (mtb), ImageListToBatch+, SetNode, Any To Any, GetNode, INTConstant, VHS_SelectImages, SetNode, SimpleMath+, ImpactInt, ImpactInt, DiffusionModelLoaderKJ, DiffusionModelLoaderKJ, KSamplerAdvanced, seed _O, seed _O, WanImageToVideoSVIPro, WanImageToVideoSVIPro, GetNode, VHS_VideoCombine, GetNode, GetNode, Text List Concatenate, VHS_SelectImages, SetNode, easy lengthAnything, SimpleMath+, SetNode, SetNode, SetNode, TextListSelelct, SetNode, TextListSelelct, SimpleMath+, SetNode, SetNode, GetNode, TextListSelelct, CR Prompt Text, CLIPTextEncode, GetNode, GetNode, RH_GetAudioDuration, ToInt, easy showAnything, ImpactInt, SetNode, SetNode, RH_GetAudioDuration, ToInt, easy showAnything, SetNode, GetNode, IndexTTS2Run, VAEDecode, easy cleanGpuUsed, VAEDecode, GetNode, easy forLoopEnd, GetNode, GODMT_SplitString, SetNode, GetNode, ImageBatch, GetNode, SetNode, TextListSelelct, JjkText, CR Text Concatenate, VHS_VideoCombine, SimpleMath+, Any To String (mtb), SimpleMath+, IndexTTS2Run, CR Prompt Text, LoadAudio, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, easy promptList, easy promptList, JjkText, easy cleanGpuUsed, IndexTTS2Run, SaveAudio, SimpleMath+, SimpleMath+, SetNode, SetNode, Int, GetNode, VHS_VideoCombine, Any To Any, Any To Any, GetNode, GetNode, GetNode, Any To Any]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 2, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/一分钟旁白短剧首选WAN2.2+SVI2.0PRO十图片生成长视频+生成旁白声音_2013826587573096449.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2013826587573096449.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（154 个）：
- `SetNode`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAELoader`
- `VAEEncode` ★核心
- `VAEEncode` ★核心
- `SetNode`
- `ImageResizeKJv2`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `INTConstant`
- `SetNode`
- `KSamplerAdvanced` ★核心
- `GetNode`
- `KSamplerAdvanced` ★核心
- `Any To Any`
- `Any To Any`
- `KSamplerAdvanced` ★核心
- `easy forLoopStart`
- `Any To Any`
- `GetNode`
- `SDVM Image List Repeat`
- `Any To String (mtb)`
- `ImageListToBatch+`
- `SetNode`
- `Any To Any`
- `GetNode`
- `INTConstant`
- `VHS_SelectImages`
- `SetNode`
- `SimpleMath+`
- `ImpactInt`
- `ImpactInt`
- `DiffusionModelLoaderKJ`
- `DiffusionModelLoaderKJ`
- `KSamplerAdvanced` ★核心
- `seed _O`
- `seed _O`
- `WanImageToVideoSVIPro`
- `WanImageToVideoSVIPro`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `Text List Concatenate`
- `VHS_SelectImages`
- `SetNode`
- `easy lengthAnything`
- `SimpleMath+`
- `SetNode`
- `SetNode`
- `SetNode`
- `TextListSelelct`
- `SetNode`
- `TextListSelelct`
- `SimpleMath+`
- `SetNode`
- `SetNode`
- `GetNode`
- `TextListSelelct`
- `CR Prompt Text`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `RH_GetAudioDuration`
- `ToInt`
- `easy showAnything`
- `ImpactInt`
- `SetNode`
- `SetNode`
- `RH_GetAudioDuration`
- `ToInt`
- `easy showAnything`
- `SetNode`
- `GetNode`
- `IndexTTS2Run`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `GetNode`
- `easy forLoopEnd`
- `GetNode`
- `GODMT_SplitString`
- `SetNode`
- `GetNode`
- `ImageBatch`
- `GetNode`
- `SetNode`
- `TextListSelelct`
- `JjkText`
- `CR Text Concatenate`
- `VHS_VideoCombine`
- `SimpleMath+`
- `Any To String (mtb)`
- `SimpleMath+`
- `IndexTTS2Run`
- `CR Prompt Text`
- `LoadAudio`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `easy promptList`
- `easy promptList`
- `JjkText`
- `easy cleanGpuUsed`
- `IndexTTS2Run`
- `SaveAudio`
- `SimpleMath+`
- `SimpleMath+`
- `SetNode`
- `SetNode`
- `Int`
- `GetNode`
- `VHS_VideoCombine`
- `Any To Any`
- `Any To Any`
- `GetNode`
- `GetNode`
- `GetNode`
- `Any To Any`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `2`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **59%**（91/154）

**有卡**：`LoraLoaderModelOnly`、`CLIPTextEncode`、`CLIPLoader`、`ImageResizeKJv2`、`VAELoader`、`VAEEncode`、`INTConstant`、`KSamplerAdvanced`、`Any To Any`、`easy forLoopStart`、`SDVM Image List Repeat`、`Any To String (mtb)`、`ImageListToBatch+`、`VHS_SelectImages`、`SimpleMath+`、`ImpactInt`、`DiffusionModelLoaderKJ`、`seed _O`、`WanImageToVideoSVIPro`、`VHS_VideoCombine`、`Text List Concatenate`、`easy lengthAnything`、`TextListSelelct`、`CR Prompt Text`、`RH_GetAudioDuration`、`ToInt`、`IndexTTS2Run`、`VAEDecode`、`easy cleanGpuUsed`、`easy forLoopEnd`、`GODMT_SplitString`、`ImageBatch`、`CR Text Concatenate`、`LoadAudio`、`LoadImage`、`easy promptList`、`SaveAudio`、`Int`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerAdvanced、seed _O

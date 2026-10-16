---
key: 视频生成/图生视频/一分半解说短剧WAN2.2REMIX3+SVI2.0PRO+VBVR十二图片长视频_2046443444645662722.json
name: 一分半解说短剧WAN2.2REMIX3+SVI2.0PRO+VBVR十二图片长视频_2046443444645662722.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2046443444645662722.json
hash: 2d125632b3ca0a55
coverage: 0.614379
learned_at: 2026-10-15 22:36:58
nodes: [SetNode, SetNode, LoraLoaderModelOnly, SetNode, GetNode, GetNode, GetNode, CLIPTextEncode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, CLIPLoader, GetNode, SetNode, GetNode, GetNode, VAELoader, VAEEncode, VAEEncode, ImageResizeKJv2, GetNode, INTConstant, SetNode, GetNode, Any To Any, KSamplerAdvanced, Any To Any, Any To Any, KSamplerAdvanced, easy forLoopStart, Any To Any, GetNode, Any To String (mtb), ImageListToBatch+, Any To Any, GetNode, VHS_SelectImages, SetNode, SetNode, ImpactInt, KSamplerAdvanced, seed _O, seed _O, WanImageToVideoSVIPro, WanImageToVideoSVIPro, GetNode, VHS_VideoCombine, GetNode, GetNode, Text List Concatenate, easy lengthAnything, SetNode, SetNode, SetNode, TextListSelelct, SetNode, SimpleMath+, SetNode, SetNode, GetNode, TextListSelelct, CR Prompt Text, CLIPTextEncode, GetNode, GetNode, Int, RH_GetAudioDuration, ToInt, easy showAnything, ImpactInt, SetNode, SetNode, Int, RH_GetAudioDuration, ToInt, easy showAnything, SetNode, GetNode, VAEDecode, easy cleanGpuUsed, VAEDecode, GetNode, easy forLoopEnd, GetNode, SimpleMath+, SimpleMath+, GODMT_SplitString, SetNode, GetNode, ImageBatch, GetNode, SetNode, TextListSelelct, JjkText, CR Text Concatenate, VHS_VideoCombine, VHS_VideoCombine, SimpleMath+, Any To String (mtb), SimpleMath+, CR Prompt Text, easy cleanGpuUsed, TextListSelelct, INTConstant, ImpactInt, ImageResizeKJv2, SimpleMath+, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SimpleMath+, LoadAudio, SaveAudio, VHS_SelectImages, IndexTTS2Run, IndexTTS2Run, IndexTTS2Run, LoraLoaderModelOnly, DiffusionModelLoaderKJ, DiffusionModelLoaderKJ, SDVM Image List Repeat, SDVM Image List Repeat, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, easy promptList, easy promptList, easy promptList, JjkText, LoraLoaderModelOnly, GetNode, GetNode, KSamplerAdvanced, LoraLoaderModelOnly, CLIPTextEncode, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1.8, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/一分半解说短剧WAN2.2REMIX3+SVI2.0PRO+VBVR十二图片长视频_2046443444645662722.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2046443444645662722.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（153 个）：
- `SetNode`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPLoader`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `VAELoader`
- `VAEEncode` ★核心
- `VAEEncode` ★核心
- `ImageResizeKJv2`
- `GetNode`
- `INTConstant`
- `SetNode`
- `GetNode`
- `Any To Any`
- `KSamplerAdvanced` ★核心
- `Any To Any`
- `Any To Any`
- `KSamplerAdvanced` ★核心
- `easy forLoopStart`
- `Any To Any`
- `GetNode`
- `Any To String (mtb)`
- `ImageListToBatch+`
- `Any To Any`
- `GetNode`
- `VHS_SelectImages`
- `SetNode`
- `SetNode`
- `ImpactInt`
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
- `easy lengthAnything`
- `SetNode`
- `SetNode`
- `SetNode`
- `TextListSelelct`
- `SetNode`
- `SimpleMath+`
- `SetNode`
- `SetNode`
- `GetNode`
- `TextListSelelct`
- `CR Prompt Text`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `Int`
- `RH_GetAudioDuration`
- `ToInt`
- `easy showAnything`
- `ImpactInt`
- `SetNode`
- `SetNode`
- `Int`
- `RH_GetAudioDuration`
- `ToInt`
- `easy showAnything`
- `SetNode`
- `GetNode`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `GetNode`
- `easy forLoopEnd`
- `GetNode`
- `SimpleMath+`
- `SimpleMath+`
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
- `VHS_VideoCombine`
- `SimpleMath+`
- `Any To String (mtb)`
- `SimpleMath+`
- `CR Prompt Text`
- `easy cleanGpuUsed`
- `TextListSelelct`
- `INTConstant`
- `ImpactInt`
- `ImageResizeKJv2`
- `SimpleMath+`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SimpleMath+`
- `LoadAudio`
- `SaveAudio`
- `VHS_SelectImages`
- `IndexTTS2Run`
- `IndexTTS2Run`
- `IndexTTS2Run`
- `LoraLoaderModelOnly` ★核心
- `DiffusionModelLoaderKJ`
- `DiffusionModelLoaderKJ`
- `SDVM Image List Repeat`
- `SDVM Image List Repeat`
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
- `LoadImage`
- `LoadImage`
- `easy promptList`
- `easy promptList`
- `easy promptList`
- `JjkText`
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1.8`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **61%**（94/153）

**有卡**：`LoraLoaderModelOnly`、`CLIPTextEncode`、`CLIPLoader`、`VAELoader`、`VAEEncode`、`ImageResizeKJv2`、`INTConstant`、`Any To Any`、`KSamplerAdvanced`、`easy forLoopStart`、`Any To String (mtb)`、`ImageListToBatch+`、`VHS_SelectImages`、`ImpactInt`、`seed _O`、`WanImageToVideoSVIPro`、`VHS_VideoCombine`、`Text List Concatenate`、`easy lengthAnything`、`TextListSelelct`、`SimpleMath+`、`CR Prompt Text`、`Int`、`RH_GetAudioDuration`、`ToInt`、`VAEDecode`、`easy cleanGpuUsed`、`easy forLoopEnd`、`GODMT_SplitString`、`ImageBatch`、`CR Text Concatenate`、`LoadAudio`、`SaveAudio`、`IndexTTS2Run`、`DiffusionModelLoaderKJ`、`SDVM Image List Repeat`、`LoadImage`、`easy promptList`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerAdvanced、seed _O

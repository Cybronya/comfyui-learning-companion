---
key: 视频生成/文生视频/一分钟旁白短剧首选WAN2.2+SVI2.0PRO十图片生成长视频+生成旁白声音_2015056410270244865.json
name: 一分钟旁白短剧首选WAN2.2+SVI2.0PRO十图片生成长视频+生成旁白声音_2015056410270244865
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/一分钟旁白短剧首选WAN2.2+SVI2.0PRO十图片生成长视频+生成旁白声音_2015056410270244865.json
hash: a3e73a63e4240c37
coverage: 0.604027
learned_at: 2026-10-15 22:47:43
nodes: [SetNode, SetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, SetNode, GetNode, GetNode, GetNode, CLIPTextEncode, CLIPTextEncode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, CLIPTextEncode, CLIPLoader, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, VAELoader, VAEEncode, VAEEncode, ImageResizeKJv2, GetNode, INTConstant, SetNode, KSamplerAdvanced, GetNode, Any To Any, KSamplerAdvanced, Any To Any, Any To Any, KSamplerAdvanced, easy forLoopStart, Any To Any, GetNode, SDVM Image List Repeat, Any To String (mtb), ImageListToBatch+, Any To Any, GetNode, VHS_SelectImages, SetNode, SetNode, ImpactInt, DiffusionModelLoaderKJ, DiffusionModelLoaderKJ, KSamplerAdvanced, seed _O, seed _O, WanImageToVideoSVIPro, WanImageToVideoSVIPro, GetNode, VHS_VideoCombine, GetNode, GetNode, Text List Concatenate, easy lengthAnything, SetNode, SetNode, SetNode, TextListSelelct, SetNode, SimpleMath+, SetNode, SetNode, GetNode, TextListSelelct, CR Prompt Text, CLIPTextEncode, GetNode, GetNode, Int, RH_GetAudioDuration, ToInt, easy showAnything, ImpactInt, SetNode, SetNode, Int, RH_GetAudioDuration, ToInt, easy showAnything, SetNode, GetNode, VAEDecode, easy cleanGpuUsed, VAEDecode, GetNode, easy forLoopEnd, GetNode, SimpleMath+, SimpleMath+, GODMT_SplitString, SetNode, GetNode, ImageBatch, GetNode, SetNode, TextListSelelct, JjkText, CR Text Concatenate, VHS_VideoCombine, VHS_VideoCombine, SimpleMath+, Any To String (mtb), SimpleMath+, CR Prompt Text, easy cleanGpuUsed, LoadImage, LoraLoaderModelOnly, LoraLoaderModelOnly, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, TextListSelelct, INTConstant, ImpactInt, ImageResizeKJv2, SimpleMath+, GetNode, easy promptList, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, easy promptList, LoadImage, LoadImage, SimpleMath+, JjkText, LoadAudio, SaveAudio, VHS_SelectImages, IndexTTS2Run, IndexTTS2Run, IndexTTS2Run]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 2, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 视频生成/文生视频/一分钟旁白短剧首选WAN2.2+SVI2.0PRO十图片生成长视频+生成旁白声音_2015056410270244865.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/一分钟旁白短剧首选WAN2.2+SVI2.0PRO十图片生成长视频+生成旁白声音_2015056410270244865.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（149 个）：
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
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAELoader`
- `VAEEncode` ★核心
- `VAEEncode` ★核心
- `ImageResizeKJv2`
- `GetNode`
- `INTConstant`
- `SetNode`
- `KSamplerAdvanced` ★核心
- `GetNode`
- `Any To Any`
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
- `Any To Any`
- `GetNode`
- `VHS_SelectImages`
- `SetNode`
- `SetNode`
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
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `TextListSelelct`
- `INTConstant`
- `ImpactInt`
- `ImageResizeKJv2`
- `SimpleMath+`
- `GetNode`
- `easy promptList`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `easy promptList`
- `LoadImage`
- `LoadImage`
- `SimpleMath+`
- `JjkText`
- `LoadAudio`
- `SaveAudio`
- `VHS_SelectImages`
- `IndexTTS2Run`
- `IndexTTS2Run`
- `IndexTTS2Run`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `2`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **60%**（90/149）

**有卡**：`LoraLoaderModelOnly`、`CLIPTextEncode`、`CLIPLoader`、`VAELoader`、`VAEEncode`、`ImageResizeKJv2`、`INTConstant`、`KSamplerAdvanced`、`Any To Any`、`easy forLoopStart`、`SDVM Image List Repeat`、`Any To String (mtb)`、`ImageListToBatch+`、`VHS_SelectImages`、`ImpactInt`、`DiffusionModelLoaderKJ`、`seed _O`、`WanImageToVideoSVIPro`、`VHS_VideoCombine`、`Text List Concatenate`、`easy lengthAnything`、`TextListSelelct`、`SimpleMath+`、`CR Prompt Text`、`Int`、`RH_GetAudioDuration`、`ToInt`、`VAEDecode`、`easy cleanGpuUsed`、`easy forLoopEnd`、`GODMT_SplitString`、`ImageBatch`、`CR Text Concatenate`、`LoadImage`、`easy promptList`、`LoadAudio`、`SaveAudio`、`IndexTTS2Run`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerAdvanced、seed _O

---
key: 视频生成/图生视频/一分钟旁白短剧首选稳定版十段视频WAN2.2+SVI2.0PRO十图片生成长视频+生成旁白声音_2015670152976670722.json
name: 一分钟旁白短剧首选稳定版十段视频WAN2.2+SVI2.0PRO十图片生成长视频+生成旁白声音_2015670152976670722.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/一分钟旁白短剧首选稳定版十段视频WAN2.2+SVI2.0PRO十图片生成长视频+生成旁白声音_2015670152976670722.json
hash: fae6445ee344c444
coverage: 0.597403
learned_at: 2026-10-15 22:34:40
nodes: [SetNode, SetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, SetNode, GetNode, GetNode, GetNode, CLIPTextEncode, CLIPTextEncode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, CLIPTextEncode, CLIPLoader, GetNode, SetNode, SetNode, SetNode, SetNode, GetNode, SetNode, ImageResizeKJv2, GetNode, VAELoader, VAEEncode, VAEEncode, SetNode, ImageResizeKJv2, GetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, INTConstant, SetNode, KSamplerAdvanced, GetNode, KSamplerAdvanced, Any To Any, Any To Any, KSamplerAdvanced, Any To Any, GetNode, Any To String (mtb), SetNode, Any To Any, GetNode, INTConstant, VHS_SelectImages, SetNode, SimpleMath+, DiffusionModelLoaderKJ, DiffusionModelLoaderKJ, KSamplerAdvanced, WanImageToVideoSVIPro, WanImageToVideoSVIPro, GetNode, GetNode, GetNode, Text List Concatenate, SetNode, easy lengthAnything, SimpleMath+, SetNode, SetNode, SetNode, TextListSelelct, SetNode, TextListSelelct, SimpleMath+, SetNode, SetNode, GetNode, TextListSelelct, CR Prompt Text, CLIPTextEncode, GetNode, GetNode, RH_GetAudioDuration, ToInt, easy showAnything, ImpactInt, SetNode, SetNode, easy showAnything, GetNode, IndexTTS2Run, VAEDecode, easy cleanGpuUsed, VAEDecode, GetNode, GODMT_SplitString, SetNode, GetNode, GetNode, SetNode, JjkText, Any To String (mtb), IndexTTS2Run, CR Prompt Text, SimpleMath+, SetNode, SetNode, GetNode, VHS_VideoCombine, Any To Any, Any To Any, GetNode, LoadAudio, VHS_SelectImages, ImageListToBatch+, SDVM Image List Repeat, SimpleMath+, RH_GetAudioDuration, ToInt, GetNode, SetNode, seed _O, seed _O, GetNode, GetNode, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, easy promptList, LoadImage, LoadImage, LoadImage, easy promptList, SaveAudio, ImpactInt, ImpactInt, Int, CR Text Concatenate, SimpleMath+, GetNode, easy lengthAnything, SimpleMath+, easy lengthAnything, easy forLoopStart, TextListSelelct, IndexTTS2Run, Display Any (rgthree), easy forLoopEnd, SimpleMath+, VHS_VideoCombine, easy cleanGpuUsed, JjkText]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 2, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/一分钟旁白短剧首选稳定版十段视频WAN2.2+SVI2.0PRO十图片生成长视频+生成旁白声音_2015670152976670722.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2015670152976670722.json`

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
- `Any To Any`
- `GetNode`
- `Any To String (mtb)`
- `SetNode`
- `Any To Any`
- `GetNode`
- `INTConstant`
- `VHS_SelectImages`
- `SetNode`
- `SimpleMath+`
- `DiffusionModelLoaderKJ`
- `DiffusionModelLoaderKJ`
- `KSamplerAdvanced` ★核心
- `WanImageToVideoSVIPro`
- `WanImageToVideoSVIPro`
- `GetNode`
- `GetNode`
- `GetNode`
- `Text List Concatenate`
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
- `easy showAnything`
- `GetNode`
- `IndexTTS2Run`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `GetNode`
- `GODMT_SplitString`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `JjkText`
- `Any To String (mtb)`
- `IndexTTS2Run`
- `CR Prompt Text`
- `SimpleMath+`
- `SetNode`
- `SetNode`
- `GetNode`
- `VHS_VideoCombine`
- `Any To Any`
- `Any To Any`
- `GetNode`
- `LoadAudio`
- `VHS_SelectImages`
- `ImageListToBatch+`
- `SDVM Image List Repeat`
- `SimpleMath+`
- `RH_GetAudioDuration`
- `ToInt`
- `GetNode`
- `SetNode`
- `seed _O`
- `seed _O`
- `GetNode`
- `GetNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `easy promptList`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `easy promptList`
- `SaveAudio`
- `ImpactInt`
- `ImpactInt`
- `Int`
- `CR Text Concatenate`
- `SimpleMath+`
- `GetNode`
- `easy lengthAnything`
- `SimpleMath+`
- `easy lengthAnything`
- `easy forLoopStart`
- `TextListSelelct`
- `IndexTTS2Run`
- `Display Any (rgthree)`
- `easy forLoopEnd`
- `SimpleMath+`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `JjkText`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `2`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **60%**（92/154）

**有卡**：`LoraLoaderModelOnly`、`CLIPTextEncode`、`CLIPLoader`、`ImageResizeKJv2`、`VAELoader`、`VAEEncode`、`INTConstant`、`KSamplerAdvanced`、`Any To Any`、`Any To String (mtb)`、`VHS_SelectImages`、`SimpleMath+`、`DiffusionModelLoaderKJ`、`WanImageToVideoSVIPro`、`Text List Concatenate`、`easy lengthAnything`、`TextListSelelct`、`CR Prompt Text`、`RH_GetAudioDuration`、`ToInt`、`ImpactInt`、`IndexTTS2Run`、`VAEDecode`、`easy cleanGpuUsed`、`GODMT_SplitString`、`VHS_VideoCombine`、`LoadAudio`、`ImageListToBatch+`、`SDVM Image List Repeat`、`seed _O`、`LoadImage`、`easy promptList`、`SaveAudio`、`Int`、`CR Text Concatenate`、`easy forLoopStart`、`Display Any (rgthree)`、`easy forLoopEnd`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerAdvanced、seed _O

---
key: 视频生成/文生视频/一分钟旁白短剧首选稳定版十段视频WAN2.2+SVI2.0PRO十图片生成长视频+生成旁白声音_2049176470618120194.json
name: 一分钟旁白短剧首选稳定版十段视频WAN2.2+SVI2.0PRO十图片生成长视频+生成旁白声音_2049176470618120194
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/一分钟旁白短剧首选稳定版十段视频WAN2.2+SVI2.0PRO十图片生成长视频+生成旁白声音_2049176470618120194.json
hash: 9f113556b9406014
coverage: 0.376623
learned_at: 2026-10-11 19:49:46
nodes: [SetNode, SetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, SetNode, GetNode, GetNode, GetNode, CLIPTextEncode, CLIPTextEncode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, CLIPTextEncode, CLIPLoader, GetNode, SetNode, SetNode, SetNode, SetNode, GetNode, SetNode, ImageResizeKJv2, GetNode, VAELoader, VAEEncode, VAEEncode, SetNode, ImageResizeKJv2, GetNode, INTConstant, SetNode, GetNode, KSamplerAdvanced, Any To Any, Any To Any, KSamplerAdvanced, Any To Any, GetNode, Any To String (mtb), SetNode, Any To Any, GetNode, INTConstant, VHS_SelectImages, SetNode, DiffusionModelLoaderKJ, DiffusionModelLoaderKJ, KSamplerAdvanced, WanImageToVideoSVIPro, WanImageToVideoSVIPro, GetNode, GetNode, GetNode, Text List Concatenate, SetNode, easy lengthAnything, SimpleMath+, SetNode, SetNode, SetNode, TextListSelelct, SetNode, TextListSelelct, SimpleMath+, SetNode, SetNode, GetNode, TextListSelelct, CR Prompt Text, CLIPTextEncode, GetNode, GetNode, RH_GetAudioDuration, ToInt, easy showAnything, SetNode, easy showAnything, GetNode, IndexTTS2Run, VAEDecode, easy cleanGpuUsed, VAEDecode, GetNode, GODMT_SplitString, SetNode, GetNode, GetNode, SetNode, JjkText, Any To String (mtb), IndexTTS2Run, CR Prompt Text, SimpleMath+, SetNode, SetNode, GetNode, VHS_VideoCombine, Any To Any, Any To Any, GetNode, LoadAudio, VHS_SelectImages, ImageListToBatch+, SDVM Image List Repeat, SimpleMath+, RH_GetAudioDuration, ToInt, GetNode, SetNode, seed _O, seed _O, GetNode, GetNode, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, easy promptList, LoadImage, LoadImage, LoadImage, easy promptList, SaveAudio, ImpactInt, ImpactInt, Int, CR Text Concatenate, SimpleMath+, GetNode, easy lengthAnything, SimpleMath+, easy lengthAnything, easy forLoopStart, TextListSelelct, IndexTTS2Run, Display Any (rgthree), easy forLoopEnd, SimpleMath+, VHS_VideoCombine, easy cleanGpuUsed, JjkText, LoadImage, ImpactInt, SimpleMath+, SetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, KSamplerAdvanced]
patterns: []
missing: [Any To Any, Any To Any, Any To Any, Any To Any, Any To Any, Any To Any, Any To String (mtb), Any To String (mtb), CR Text Concatenate, Display Any (rgthree), ImageListToBatch+, SDVM Image List Repeat, SimpleMath+, SimpleMath+, SimpleMath+, SimpleMath+, SimpleMath+, SimpleMath+, SimpleMath+, SimpleMath+, Text List Concatenate, easy cleanGpuUsed, easy cleanGpuUsed, easy forLoopEnd, easy forLoopStart, easy lengthAnything, easy lengthAnything, easy lengthAnything, CR Prompt Text, CR Prompt Text, easy promptList, easy promptList, seed _O, seed _O]
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 2, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
discoveries: [次要节点 `Any To Any` 知识库中没有该节点类型的任何知识, 次要节点 `Any To Any` 知识库中没有该节点类型的任何知识, 次要节点 `Any To Any` 知识库中没有该节点类型的任何知识, 次要节点 `Any To Any` 知识库中没有该节点类型的任何知识, 次要节点 `Any To Any` 知识库中没有该节点类型的任何知识, 次要节点 `Any To Any` 知识库中没有该节点类型的任何知识, 次要节点 `Any To String (mtb)` 知识库中没有该节点类型的任何知识, 次要节点 `Any To String (mtb)` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `Display Any (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `ImageListToBatch+` 知识库中没有该节点类型的任何知识, 次要节点 `SDVM Image List Repeat` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `Text List Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识, 次要节点 `easy lengthAnything` 知识库中没有该节点类型的任何知识, 次要节点 `easy lengthAnything` 知识库中没有该节点类型的任何知识, 次要节点 `easy lengthAnything` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `easy promptList` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `easy promptList` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `seed _O` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `seed _O` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/一分钟旁白短剧首选稳定版十段视频WAN2.2+SVI2.0PRO十图片生成长视频+生成旁白声音_2049176470618120194.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/一分钟旁白短剧首选稳定版十段视频WAN2.2+SVI2.0PRO十图片生成长视频+生成旁白声音_2049176470618120194.json`

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
- `INTConstant`
- `SetNode`
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
- `LoadImage`
- `ImpactInt`
- `SimpleMath+`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `2`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **38%**（58/154）

**有卡**：`LoraLoaderModelOnly`、`CLIPTextEncode`、`CLIPLoader`、`ImageResizeKJv2`、`VAELoader`、`VAEEncode`、`INTConstant`、`KSamplerAdvanced`、`VHS_SelectImages`、`DiffusionModelLoaderKJ`、`WanImageToVideoSVIPro`、`TextListSelelct`、`RH_GetAudioDuration`、`ToInt`、`IndexTTS2Run`、`VAEDecode`、`GODMT_SplitString`、`VHS_VideoCombine`、`LoadAudio`、`LoadImage`、`SaveAudio`、`ImpactInt`、`Int`

**缺卡**（34）：`Any To Any`、`Any To Any`、`Any To Any`、`Any To Any`、`Any To Any`、`Any To Any`、`Any To String (mtb)`、`Any To String (mtb)`、`CR Text Concatenate`、`Display Any (rgthree)`、`ImageListToBatch+`、`SDVM Image List Repeat`、`SimpleMath+`、`SimpleMath+`、`SimpleMath+`、`SimpleMath+`、`SimpleMath+`、`SimpleMath+`、`SimpleMath+`、`SimpleMath+`、`Text List Concatenate`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy forLoopEnd`、`easy forLoopStart`、`easy lengthAnything`、`easy lengthAnything`、`easy lengthAnything`、`CR Prompt Text`、`CR Prompt Text`、`easy promptList`、`easy promptList`、`seed _O`、`seed _O`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerAdvanced、VAEEncode

## 学习发现

- 次要节点 `Any To Any` 知识库中没有该节点类型的任何知识
- 次要节点 `Any To Any` 知识库中没有该节点类型的任何知识
- 次要节点 `Any To Any` 知识库中没有该节点类型的任何知识
- 次要节点 `Any To Any` 知识库中没有该节点类型的任何知识
- 次要节点 `Any To Any` 知识库中没有该节点类型的任何知识
- 次要节点 `Any To Any` 知识库中没有该节点类型的任何知识
- 次要节点 `Any To String (mtb)` 知识库中没有该节点类型的任何知识
- 次要节点 `Any To String (mtb)` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `Display Any (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageListToBatch+` 知识库中没有该节点类型的任何知识
- 次要节点 `SDVM Image List Repeat` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `Text List Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识
- 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识
- 次要节点 `easy lengthAnything` 知识库中没有该节点类型的任何知识
- 次要节点 `easy lengthAnything` 知识库中没有该节点类型的任何知识
- 次要节点 `easy lengthAnything` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `easy promptList` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `easy promptList` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `seed _O` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `seed _O` 仅有 KSampler 的通用知识，没有该节点自己的说明

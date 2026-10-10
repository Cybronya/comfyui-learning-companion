---
key: 视频生成/文生视频/一分钟旁白短剧首选WAN2.2+SVI2.0PRO十图片生成长视频+生成旁白声音_2015056410270244865.json
name: 一分钟旁白短剧首选WAN2.2+SVI2.0PRO十图片生成长视频+生成旁白声音_2015056410270244865
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/一分钟旁白短剧首选WAN2.2+SVI2.0PRO十图片生成长视频+生成旁白声音_2015056410270244865.json
hash: a3e73a63e4240c37
coverage: 0.409396
learned_at: 2026-10-11 03:07:14
nodes: [SetNode, SetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, SetNode, GetNode, GetNode, GetNode, CLIPTextEncode, CLIPTextEncode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, CLIPTextEncode, CLIPLoader, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, VAELoader, VAEEncode, VAEEncode, ImageResizeKJv2, GetNode, INTConstant, SetNode, KSamplerAdvanced, GetNode, Any To Any, KSamplerAdvanced, Any To Any, Any To Any, KSamplerAdvanced, easy forLoopStart, Any To Any, GetNode, SDVM Image List Repeat, Any To String (mtb), ImageListToBatch+, Any To Any, GetNode, VHS_SelectImages, SetNode, SetNode, ImpactInt, DiffusionModelLoaderKJ, DiffusionModelLoaderKJ, KSamplerAdvanced, seed _O, seed _O, WanImageToVideoSVIPro, WanImageToVideoSVIPro, GetNode, VHS_VideoCombine, GetNode, GetNode, Text List Concatenate, easy lengthAnything, SetNode, SetNode, SetNode, TextListSelelct, SetNode, SimpleMath+, SetNode, SetNode, GetNode, TextListSelelct, CR Prompt Text, CLIPTextEncode, GetNode, GetNode, Int, RH_GetAudioDuration, ToInt, easy showAnything, ImpactInt, SetNode, SetNode, Int, RH_GetAudioDuration, ToInt, easy showAnything, SetNode, GetNode, VAEDecode, easy cleanGpuUsed, VAEDecode, GetNode, easy forLoopEnd, GetNode, SimpleMath+, SimpleMath+, GODMT_SplitString, SetNode, GetNode, ImageBatch, GetNode, SetNode, TextListSelelct, JjkText, CR Text Concatenate, VHS_VideoCombine, VHS_VideoCombine, SimpleMath+, Any To String (mtb), SimpleMath+, CR Prompt Text, easy cleanGpuUsed, LoadImage, LoraLoaderModelOnly, LoraLoaderModelOnly, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, TextListSelelct, INTConstant, ImpactInt, ImageResizeKJv2, SimpleMath+, GetNode, easy promptList, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, easy promptList, LoadImage, LoadImage, SimpleMath+, JjkText, LoadAudio, SaveAudio, VHS_SelectImages, IndexTTS2Run, IndexTTS2Run, IndexTTS2Run]
patterns: []
missing: [Any To Any, Any To Any, Any To Any, Any To Any, Any To Any, Any To String (mtb), Any To String (mtb), CR Text Concatenate, ImageListToBatch+, SDVM Image List Repeat, SimpleMath+, SimpleMath+, SimpleMath+, SimpleMath+, SimpleMath+, SimpleMath+, SimpleMath+, Text List Concatenate, easy cleanGpuUsed, easy cleanGpuUsed, easy forLoopEnd, easy forLoopStart, easy lengthAnything, CR Prompt Text, CR Prompt Text, easy promptList, easy promptList, seed _O, seed _O]
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 2, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
discoveries: [次要节点 `Any To Any` 知识库中没有该节点类型的任何知识, 次要节点 `Any To Any` 知识库中没有该节点类型的任何知识, 次要节点 `Any To Any` 知识库中没有该节点类型的任何知识, 次要节点 `Any To Any` 知识库中没有该节点类型的任何知识, 次要节点 `Any To Any` 知识库中没有该节点类型的任何知识, 次要节点 `Any To String (mtb)` 知识库中没有该节点类型的任何知识, 次要节点 `Any To String (mtb)` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `ImageListToBatch+` 知识库中没有该节点类型的任何知识, 次要节点 `SDVM Image List Repeat` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `Text List Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识, 次要节点 `easy lengthAnything` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `easy promptList` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `easy promptList` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `seed _O` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `seed _O` 仅有 KSampler 的通用知识，没有该节点自己的说明]
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

覆盖率 **41%**（61/149）

**有卡**：`LoraLoaderModelOnly`、`CLIPTextEncode`、`CLIPLoader`、`VAELoader`、`VAEEncode`、`ImageResizeKJv2`、`INTConstant`、`KSamplerAdvanced`、`VHS_SelectImages`、`ImpactInt`、`DiffusionModelLoaderKJ`、`WanImageToVideoSVIPro`、`VHS_VideoCombine`、`TextListSelelct`、`Int`、`RH_GetAudioDuration`、`ToInt`、`VAEDecode`、`GODMT_SplitString`、`ImageBatch`、`LoadImage`、`LoadAudio`、`SaveAudio`、`IndexTTS2Run`

**缺卡**（29）：`Any To Any`、`Any To Any`、`Any To Any`、`Any To Any`、`Any To Any`、`Any To String (mtb)`、`Any To String (mtb)`、`CR Text Concatenate`、`ImageListToBatch+`、`SDVM Image List Repeat`、`SimpleMath+`、`SimpleMath+`、`SimpleMath+`、`SimpleMath+`、`SimpleMath+`、`SimpleMath+`、`SimpleMath+`、`Text List Concatenate`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy forLoopEnd`、`easy forLoopStart`、`easy lengthAnything`、`CR Prompt Text`、`CR Prompt Text`、`easy promptList`、`easy promptList`、`seed _O`、`seed _O`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerAdvanced、VAEEncode

## 学习发现

- 次要节点 `Any To Any` 知识库中没有该节点类型的任何知识
- 次要节点 `Any To Any` 知识库中没有该节点类型的任何知识
- 次要节点 `Any To Any` 知识库中没有该节点类型的任何知识
- 次要节点 `Any To Any` 知识库中没有该节点类型的任何知识
- 次要节点 `Any To Any` 知识库中没有该节点类型的任何知识
- 次要节点 `Any To String (mtb)` 知识库中没有该节点类型的任何知识
- 次要节点 `Any To String (mtb)` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageListToBatch+` 知识库中没有该节点类型的任何知识
- 次要节点 `SDVM Image List Repeat` 知识库中没有该节点类型的任何知识
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
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `easy promptList` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `easy promptList` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `seed _O` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `seed _O` 仅有 KSampler 的通用知识，没有该节点自己的说明

---
key: 视频生成/图生视频/WAN2.2+SVI2.0PRO五分镜长视频+旁白声音_2036666010664706050.json
name: WAN2.2+SVI2.0PRO五分镜长视频+旁白声音_2036666010664706050.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2036666010664706050.json
hash: d533e01866a197a0
coverage: 0.647059
learned_at: 2026-10-15 22:35:53
nodes: [SetNode, SetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, SetNode, GetNode, GetNode, GetNode, CLIPTextEncode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, CLIPTextEncode, CLIPLoader, GetNode, SetNode, GetNode, GetNode, VAELoader, VAEEncode, VAEEncode, ImageResizeKJv2, GetNode, INTConstant, SetNode, KSamplerAdvanced, GetNode, Any To Any, KSamplerAdvanced, Any To Any, Any To Any, KSamplerAdvanced, easy forLoopStart, Any To Any, GetNode, SDVM Image List Repeat, Any To String (mtb), Any To Any, GetNode, VHS_SelectImages, ImpactInt, DiffusionModelLoaderKJ, DiffusionModelLoaderKJ, KSamplerAdvanced, seed _O, seed _O, WanImageToVideoSVIPro, WanImageToVideoSVIPro, GetNode, GetNode, GetNode, Text List Concatenate, easy lengthAnything, SetNode, SetNode, SetNode, TextListSelelct, SetNode, SimpleMath+, SetNode, SetNode, GetNode, CR Prompt Text, CLIPTextEncode, GetNode, GetNode, Int, RH_GetAudioDuration, ToInt, easy showAnything, SetNode, Int, RH_GetAudioDuration, ToInt, easy showAnything, SetNode, GetNode, VAEDecode, GetNode, GetNode, SimpleMath+, SimpleMath+, GODMT_SplitString, SetNode, GetNode, ImageBatch, GetNode, SetNode, JjkText, CR Text Concatenate, VHS_VideoCombine, VHS_VideoCombine, SimpleMath+, Any To String (mtb), SimpleMath+, CR Prompt Text, easy cleanGpuUsed, LoraLoaderModelOnly, TextListSelelct, INTConstant, ImpactInt, ImageResizeKJv2, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SimpleMath+, VHS_SelectImages, IndexTTS2Run, IndexTTS2Run, VAEDecode, CLIPTextEncode, TextListSelelct, TextListSelelct, IndexTTS2Run, RH_Translator, HunyuanVideoFoley, SaveAudio, easy forLoopEnd, AudioAdjustVolume, easy promptList, LoadImage, LoadImage, LoadImage, JWStringGetLine, JWStringGetLine, ConcatTextOfUtils, llama_cpp_instruct_adv, ConcatTextOfUtils, ConcatTextOfUtils, ConcatTextOfUtils, ConcatTextOfUtils, llama_cpp_parameters, LoadImage, LoraLoaderModelOnly, VHS_VideoCombine, JWStringGetLine, JWStringGetLine, JWStringGetLine, easy cleanGpuUsed, llama_cpp_instruct_adv, easy cleanGpuUsed, llama_cpp_instruct_adv, easy showAnything, easy cleanGpuUsed, ImageListToBatch+, easy cleanGpuUsed, easy cleanGpuUsed, LoadAudio, easy showAnything, TextBox, ImageSizeInfo, JjkText, llama_cpp_instruct_adv, llama_cpp_instruct_adv, TextBox, ResizeImagesByLongerEdge, LoadImage, SetNode, SetNode, GetNode, GetNode, llama_cpp_model_loader]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 2, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/WAN2.2+SVI2.0PRO五分镜长视频+旁白声音_2036666010664706050.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2036666010664706050.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（170 个）：
- `SetNode`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
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
- `CLIPTextEncode` ★核心
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
- `Any To Any`
- `GetNode`
- `VHS_SelectImages`
- `ImpactInt`
- `DiffusionModelLoaderKJ`
- `DiffusionModelLoaderKJ`
- `KSamplerAdvanced` ★核心
- `seed _O`
- `seed _O`
- `WanImageToVideoSVIPro`
- `WanImageToVideoSVIPro`
- `GetNode`
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
- `CR Prompt Text`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `Int`
- `RH_GetAudioDuration`
- `ToInt`
- `easy showAnything`
- `SetNode`
- `Int`
- `RH_GetAudioDuration`
- `ToInt`
- `easy showAnything`
- `SetNode`
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `SimpleMath+`
- `SimpleMath+`
- `GODMT_SplitString`
- `SetNode`
- `GetNode`
- `ImageBatch`
- `GetNode`
- `SetNode`
- `JjkText`
- `CR Text Concatenate`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `SimpleMath+`
- `Any To String (mtb)`
- `SimpleMath+`
- `CR Prompt Text`
- `easy cleanGpuUsed`
- `LoraLoaderModelOnly` ★核心
- `TextListSelelct`
- `INTConstant`
- `ImpactInt`
- `ImageResizeKJv2`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SimpleMath+`
- `VHS_SelectImages`
- `IndexTTS2Run`
- `IndexTTS2Run`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `TextListSelelct`
- `TextListSelelct`
- `IndexTTS2Run`
- `RH_Translator`
- `HunyuanVideoFoley`
- `SaveAudio`
- `easy forLoopEnd`
- `AudioAdjustVolume`
- `easy promptList`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `JWStringGetLine`
- `JWStringGetLine`
- `ConcatTextOfUtils`
- `llama_cpp_instruct_adv`
- `ConcatTextOfUtils`
- `ConcatTextOfUtils`
- `ConcatTextOfUtils`
- `ConcatTextOfUtils`
- `llama_cpp_parameters`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoCombine`
- `JWStringGetLine`
- `JWStringGetLine`
- `JWStringGetLine`
- `easy cleanGpuUsed`
- `llama_cpp_instruct_adv`
- `easy cleanGpuUsed`
- `llama_cpp_instruct_adv`
- `easy showAnything`
- `easy cleanGpuUsed`
- `ImageListToBatch+`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `LoadAudio`
- `easy showAnything`
- `TextBox`
- `ImageSizeInfo`
- `JjkText`
- `llama_cpp_instruct_adv`
- `llama_cpp_instruct_adv`
- `TextBox`
- `ResizeImagesByLongerEdge`
- `LoadImage`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `llama_cpp_model_loader`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `2`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **65%**（110/170）

**有卡**：`LoraLoaderModelOnly`、`CLIPTextEncode`、`CLIPLoader`、`VAELoader`、`VAEEncode`、`ImageResizeKJv2`、`INTConstant`、`KSamplerAdvanced`、`Any To Any`、`easy forLoopStart`、`SDVM Image List Repeat`、`Any To String (mtb)`、`VHS_SelectImages`、`ImpactInt`、`DiffusionModelLoaderKJ`、`seed _O`、`WanImageToVideoSVIPro`、`Text List Concatenate`、`easy lengthAnything`、`TextListSelelct`、`SimpleMath+`、`CR Prompt Text`、`Int`、`RH_GetAudioDuration`、`ToInt`、`VAEDecode`、`GODMT_SplitString`、`ImageBatch`、`CR Text Concatenate`、`VHS_VideoCombine`、`easy cleanGpuUsed`、`IndexTTS2Run`、`RH_Translator`、`HunyuanVideoFoley`、`SaveAudio`、`easy forLoopEnd`、`AudioAdjustVolume`、`easy promptList`、`LoadImage`、`JWStringGetLine`、`ConcatTextOfUtils`、`llama_cpp_instruct_adv`、`llama_cpp_parameters`、`ImageListToBatch+`、`LoadAudio`、`TextBox`、`ImageSizeInfo`、`ResizeImagesByLongerEdge`、`llama_cpp_model_loader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerAdvanced、seed _O

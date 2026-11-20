---
key: 平台全量/WAN2.2首尾帧运镜极速版_2009509205933297666.json
name: WAN2.2首尾帧运镜极速版_2009509205933297666
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/WAN2.2首尾帧运镜极速版_2009509205933297666.json
hash: e6e4f18f67f03ad2
coverage: 0.768116
learned_at: 2026-11-14 01:03:45
nodes: [easy cleanGpuUsed, WanVideoDecode, INTConstant, LayerUtility: PurgeVRAM, WanVideoSetBlockSwap, WanVideoModelLoader, WanVideoLoraSelect, WanVideoSetBlockSwap, WanVideoSetLoRAs, SimpleMath+, LayerUtility: PurgeVRAM, WanVideoSampler, WanVideoSampler, WanVideoModelLoader, WanVideoBlockSwap, WanVideoLoraSelectMulti, DF_Int_to_Float, WanVideoLoraSelect, WanVideoLoraSelectMulti, Bjornulf_ShowFloat, CreateCFGScheduleFloatList, CLIPTextEncode, LoraLoaderModelOnly, CLIPLoader, VAELoader, TextEncodeQwenImageEditPlus, Note, UNETLoader, LoraLoaderModelOnly, KSampler, LoadWanVideoClipTextEncoder, PrimitiveStringMultiline, WanVideoImageToVideoEncode, ImageResize+, VAEDecode, PrimitiveBoolean, LoadImage, WanVideoSetLoRAs, VHS_VideoCombine, easy ifElse, PrimitiveInt, PrimitiveInt, NumberClamp, PrimitiveInt, PrimitiveInt, WanVideoVAELoader, SaveImage, easy cleanGpuUsed, WanVideoClipVisionEncode, WanVideoTextEncode, LoadWanVideoT5TextEncoder, PrimitiveStringMultiline, EmptyLatentImage, VAEEncode, GetImageSizeAndCount, easy ifElse, easy ifElse, PrimitiveInt, easy ifElse, ImageResize+, JWInteger, easy ifElse, LoadImage, CR SDXL Aspect Ratio, PrimitiveInt, Compare, PrimitiveInt, PrimitiveInt, Compare]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 720, "sampler_name": "euler", "scheduler": "simple", "seed": 273706467552554, "steps": 8, "width": 1280}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/WAN2.2首尾帧运镜极速版_2009509205933297666.json

> 来源文件 `comfyui_library/workflows/平台全量/WAN2.2首尾帧运镜极速版_2009509205933297666.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（69 个）：
- `easy cleanGpuUsed`
- `WanVideoDecode`
- `INTConstant`
- `LayerUtility: PurgeVRAM`
- `WanVideoSetBlockSwap`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `SimpleMath+`
- `LayerUtility: PurgeVRAM`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoLoraSelectMulti`
- `DF_Int_to_Float`
- `WanVideoLoraSelect`
- `WanVideoLoraSelectMulti`
- `Bjornulf_ShowFloat`
- `CreateCFGScheduleFloatList`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `TextEncodeQwenImageEditPlus`
- `Note`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `LoadWanVideoClipTextEncoder` ★核心
- `PrimitiveStringMultiline`
- `WanVideoImageToVideoEncode`
- `ImageResize+`
- `VAEDecode` ★核心
- `PrimitiveBoolean`
- `LoadImage`
- `WanVideoSetLoRAs`
- `VHS_VideoCombine`
- `easy ifElse`
- `PrimitiveInt`
- `PrimitiveInt`
- `NumberClamp`
- `PrimitiveInt`
- `PrimitiveInt`
- `WanVideoVAELoader`
- `SaveImage`
- `easy cleanGpuUsed`
- `WanVideoClipVisionEncode`
- `WanVideoTextEncode`
- `LoadWanVideoT5TextEncoder`
- `PrimitiveStringMultiline`
- `EmptyLatentImage` ★核心
- `VAEEncode` ★核心
- `GetImageSizeAndCount`
- `easy ifElse`
- `easy ifElse`
- `PrimitiveInt`
- `easy ifElse`
- `ImageResize+`
- `JWInteger`
- `easy ifElse`
- `LoadImage`
- `CR SDXL Aspect Ratio`
- `PrimitiveInt`
- `Compare`
- `PrimitiveInt`
- `PrimitiveInt`
- `Compare`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `seed` = `273706467552554`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1280`
- `height` = `720`
- `batch_size` = `1`

## 知识

覆盖率 **77%**（53/69）

**有卡**：`easy cleanGpuUsed`、`WanVideoDecode`、`INTConstant`、`LayerUtility: PurgeVRAM`、`WanVideoSetBlockSwap`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoSetLoRAs`、`SimpleMath+`、`WanVideoSampler`、`WanVideoBlockSwap`、`WanVideoLoraSelectMulti`、`DF_Int_to_Float`、`Bjornulf_ShowFloat`、`CreateCFGScheduleFloatList`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImageEditPlus`、`UNETLoader`、`KSampler`、`LoadWanVideoClipTextEncoder`、`WanVideoImageToVideoEncode`、`ImageResize+`、`VAEDecode`、`PrimitiveBoolean`、`LoadImage`、`VHS_VideoCombine`、`NumberClamp`、`WanVideoVAELoader`、`SaveImage`、`WanVideoClipVisionEncode`、`WanVideoTextEncode`、`LoadWanVideoT5TextEncoder`、`EmptyLatentImage`、`VAEEncode`、`GetImageSizeAndCount`、`JWInteger`、`CR SDXL Aspect Ratio`、`Compare`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、CLIPTextEncode、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

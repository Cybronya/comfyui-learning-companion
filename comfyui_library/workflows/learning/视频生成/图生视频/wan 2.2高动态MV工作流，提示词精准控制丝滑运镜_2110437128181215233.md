---
key: 视频生成/图生视频/wan 2.2高动态MV工作流，提示词精准控制丝滑运镜_2110437128181215233.json
name: wan 2.2高动态MV工作流，提示词精准控制丝滑运镜_2110437128181215233
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan 2.2高动态MV工作流，提示词精准控制丝滑运镜_2110437128181215233.json
hash: 8d9e4e4a8aff5907
coverage: 0.691589
learned_at: 2026-10-18 00:24:08
nodes: [easy clearCacheAll, LayerUtility: PurgeVRAM V2, easy cleanGpuUsed, easy showAnything, GetNode, easy showAnything, Float to Int, GetNode, GetNode, GetNode, Audio Duration (mtb), easy imageSize, GetNode, LoadWanVideoT5TextEncoder, PrimitiveNode, WanVideoVAELoader, MathExpression|pysssss, AudioSeparation, LayerUtility: PurgeVRAM V2, WanVideoSampler, WanVideoSLG, CreateCFGScheduleFloatList, RH_GetAudioDuration, SetNode, WanVideoDecode, GetNode, ImageResizeKJv2, GetNode, GetNode, RIFEInterpolation, FlashVSRNode, SetNode, VHS_LoadVideo, LoadImage, easy ifElse, easy ifElse, SetNode, CR Text, ShowText|pysssss, CR Text, INTConstant, INTConstant, SetNode, INTConstant, INTConstant, easy boolean, GetNode, CR Text, SetNode, AudioCrop, Any Switch (rgthree), SetNode, GetNode, SetNode, easy cleanGpuUsed, WanVideoImageToVideoEncode, Fast Groups Muter (rgthree), SaveAudio, CR Text Concatenate, RH_Captioner, CR Text, WanVideoSampler, VHS_VideoCombine, INTConstant, DownloadAndLoadWav2VecModel, MultiTalkWav2VecEmbeds, WanVideoContextOptions, MathExpression|pysssss, RHHiddenNodes, WanVideoTextEncode, RH_LLMAPI_Pro_Node, GetNode, GetNode, VHS_VideoCombine, VHS_VideoCombine, Fast Groups Muter (rgthree), easy showAnything, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note, SaveImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/wan 2.2高动态MV工作流，提示词精准控制丝滑运镜_2110437128181215233.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/wan 2.2高动态MV工作流，提示词精准控制丝滑运镜_2110437128181215233.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（107 个）：
- `easy clearCacheAll`
- `LayerUtility: PurgeVRAM V2`
- `easy cleanGpuUsed`
- `easy showAnything`
- `GetNode`
- `easy showAnything`
- `Float to Int`
- `GetNode`
- `GetNode`
- `GetNode`
- `Audio Duration (mtb)`
- `easy imageSize`
- `GetNode`
- `LoadWanVideoT5TextEncoder`
- `PrimitiveNode`
- `WanVideoVAELoader`
- `MathExpression|pysssss`
- `AudioSeparation`
- `LayerUtility: PurgeVRAM V2`
- `WanVideoSampler` ★核心
- `WanVideoSLG`
- `CreateCFGScheduleFloatList`
- `RH_GetAudioDuration`
- `SetNode`
- `WanVideoDecode`
- `GetNode`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `RIFEInterpolation`
- `FlashVSRNode`
- `SetNode`
- `VHS_LoadVideo`
- `LoadImage`
- `easy ifElse`
- `easy ifElse`
- `SetNode`
- `CR Text`
- `ShowText|pysssss`
- `CR Text`
- `INTConstant`
- `INTConstant`
- `SetNode`
- `INTConstant`
- `INTConstant`
- `easy boolean`
- `GetNode`
- `CR Text`
- `SetNode`
- `AudioCrop`
- `Any Switch (rgthree)`
- `SetNode`
- `GetNode`
- `SetNode`
- `easy cleanGpuUsed`
- `WanVideoImageToVideoEncode`
- `Fast Groups Muter (rgthree)`
- `SaveAudio`
- `CR Text Concatenate`
- `RH_Captioner`
- `CR Text`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `INTConstant`
- `DownloadAndLoadWav2VecModel`
- `MultiTalkWav2VecEmbeds`
- `WanVideoContextOptions`
- `MathExpression|pysssss`
- `RHHiddenNodes`
- `WanVideoTextEncode`
- `RH_LLMAPI_Pro_Node`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Fast Groups Muter (rgthree)`
- `easy showAnything`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `JjkText`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `VAELoader`
- `solarL_SaveImagesToZip`
- `Note`
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **69%**（74/107）

**有卡**：`easy clearCacheAll`、`LayerUtility: PurgeVRAM V2`、`easy cleanGpuUsed`、`Float to Int`、`Audio Duration (mtb)`、`easy imageSize`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`MathExpression|pysssss`、`AudioSeparation`、`WanVideoSampler`、`WanVideoSLG`、`CreateCFGScheduleFloatList`、`RH_GetAudioDuration`、`WanVideoDecode`、`ImageResizeKJv2`、`RIFEInterpolation`、`FlashVSRNode`、`VHS_LoadVideo`、`LoadImage`、`CR Text`、`INTConstant`、`easy boolean`、`AudioCrop`、`WanVideoImageToVideoEncode`、`SaveAudio`、`CR Text Concatenate`、`RH_Captioner`、`VHS_VideoCombine`、`DownloadAndLoadWav2VecModel`、`MultiTalkWav2VecEmbeds`、`WanVideoContextOptions`、`RHHiddenNodes`、`WanVideoTextEncode`、`RH_LLMAPI_Pro_Node`、`UNETLoader`、`LoraLoaderModelOnly`、`KSampler`、`CLIPTextEncode`、`CLIPLoader`、`VAEDecode`、`EmptyLatentImage`、`VAELoader`、`solarL_SaveImagesToZip`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

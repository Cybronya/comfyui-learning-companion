---
key: 视频生成/图生视频/【Supermate】图生视频+V2V-Infinitetalk高动态数字人_1990442232287301633.json
name: 【Supermate】图生视频+V2V-Infinitetalk高动态数字人_1990442232287301633.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/【Supermate】图生视频+V2V-Infinitetalk高动态数字人_1990442232287301633.json
hash: d1749dd4e031df22
coverage: 0.628099
learned_at: 2026-10-15 22:33:10
nodes: [WanVideoLoraSelect, WanVideoVAELoader, CLIPVisionLoader, Setter, Setter, GetImageRangeFromBatch, WanVideoBlockSwap, WanVideoTextEncodeCached, WanVideoClipVisionEncode, MultiTalkWav2VecEmbeds, Getter, Getter, Getter, Getter, Getter, WanVideoSampler, Getter, Float to Int, SoundFlow_GetLength, AudioSeparation, Setter, Setter, WanVideoDecode, SimpleMath+, WanVideoEncode, Getter, Setter, DownloadAndLoadWav2VecModel, Setter, WanVideoModelLoader, MultiTalkModelLoader, PathchSageAttentionKJ, PathchSageAttentionKJ, Reroute, Reroute, Reroute, ModelPatchTorchSettings, ModelPatchTorchSettings, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, VAELoader, Note, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, wanBlockSwap, Reroute, Reroute, Reroute, Reroute, Note, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, ModelSamplingSD3, Reroute, easy cleanGpuUsed, Reroute, Reroute, VAEDecode, Note, KSamplerAdvanced, KSamplerAdvanced, INTConstant, INTConstant, LayerUtility: ImageScaleByAspectRatio V2, Reroute, Reroute, Reroute, Reroute, LoraLoaderModelOnly, Note, PreviewImage, CLIPLoader, Reroute, Reroute, ModelSamplingSD3, Note, Fast Groups Bypasser (rgthree), Reroute, Qwen3_VQA, easy showAnything, JoinStrings, PainterI2V, UNETLoader, wanBlockSwap, Note, Int, Int, VHS_VideoCombine, ImageConcanate, Getter, TextInput_, Label (rgthree), CLIPTextEncode, CLIPTextEncode, ShowText|pysssss, ImageResizeKJv2, LoadAudio, AudioCrop, PreviewImage, VHS_VideoCombine, CRTFirstLastFrameSelector, VHS_LoadVideo, Fast Groups Bypasser (rgthree), RIFE VFI, Label (rgthree), Label (rgthree), LoadImage, WanVideoImageToVideoMultiTalk]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "normal", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/【Supermate】图生视频+V2V-Infinitetalk高动态数字人_1990442232287301633.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1990442232287301633.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（121 个）：
- `WanVideoLoraSelect`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `Setter`
- `Setter`
- `GetImageRangeFromBatch`
- `WanVideoBlockSwap`
- `WanVideoTextEncodeCached`
- `WanVideoClipVisionEncode`
- `MultiTalkWav2VecEmbeds`
- `Getter`
- `Getter`
- `Getter`
- `Getter`
- `Getter`
- `WanVideoSampler` ★核心
- `Getter`
- `Float to Int`
- `SoundFlow_GetLength`
- `AudioSeparation`
- `Setter`
- `Setter`
- `WanVideoDecode`
- `SimpleMath+`
- `WanVideoEncode`
- `Getter`
- `Setter`
- `DownloadAndLoadWav2VecModel`
- `Setter`
- `WanVideoModelLoader`
- `MultiTalkModelLoader`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `Reroute`
- `Reroute`
- `Reroute`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `VAELoader`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `wanBlockSwap`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Note`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `ModelSamplingSD3`
- `Reroute`
- `easy cleanGpuUsed`
- `Reroute`
- `Reroute`
- `VAEDecode` ★核心
- `Note`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `INTConstant`
- `INTConstant`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `LoraLoaderModelOnly` ★核心
- `Note`
- `PreviewImage`
- `CLIPLoader`
- `Reroute`
- `Reroute`
- `ModelSamplingSD3`
- `Note`
- `Fast Groups Bypasser (rgthree)`
- `Reroute`
- `Qwen3_VQA`
- `easy showAnything`
- `JoinStrings`
- `PainterI2V`
- `UNETLoader` ★核心
- `wanBlockSwap`
- `Note`
- `Int`
- `Int`
- `VHS_VideoCombine`
- `ImageConcanate`
- `Getter`
- `TextInput_`
- `Label (rgthree)`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ShowText|pysssss`
- `ImageResizeKJv2`
- `LoadAudio`
- `AudioCrop`
- `PreviewImage`
- `VHS_VideoCombine`
- `CRTFirstLastFrameSelector`
- `VHS_LoadVideo`
- `Fast Groups Bypasser (rgthree)`
- `RIFE VFI`
- `Label (rgthree)`
- `Label (rgthree)`
- `LoadImage`
- `WanVideoImageToVideoMultiTalk`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `normal`

## 知识

覆盖率 **63%**（76/121）

**有卡**：`WanVideoLoraSelect`、`WanVideoVAELoader`、`CLIPVisionLoader`、`Setter`、`GetImageRangeFromBatch`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`WanVideoClipVisionEncode`、`MultiTalkWav2VecEmbeds`、`Getter`、`WanVideoSampler`、`Float to Int`、`SoundFlow_GetLength`、`AudioSeparation`、`WanVideoDecode`、`SimpleMath+`、`WanVideoEncode`、`DownloadAndLoadWav2VecModel`、`WanVideoModelLoader`、`MultiTalkModelLoader`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`VAELoader`、`LoraLoaderModelOnly`、`UNETLoader`、`wanBlockSwap`、`ModelSamplingSD3`、`easy cleanGpuUsed`、`VAEDecode`、`KSamplerAdvanced`、`INTConstant`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPLoader`、`Qwen3_VQA`、`JoinStrings`、`PainterI2V`、`Int`、`VHS_VideoCombine`、`ImageConcanate`、`TextInput_`、`Label (rgthree)`、`CLIPTextEncode`、`ImageResizeKJv2`、`LoadAudio`、`AudioCrop`、`CRTFirstLastFrameSelector`、`VHS_LoadVideo`、`RIFE VFI`、`LoadImage`、`WanVideoImageToVideoMultiTalk`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2

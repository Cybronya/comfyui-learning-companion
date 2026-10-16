---
key: 视频生成/图生视频/Comfy挑战赛4 Qwen image+Wan2.2 S2V全身姿势控制V1_1965685855086104578.json
name: Comfy挑战赛4 Qwen image+Wan2.2 S2V全身姿势控制V1_1965685855086104578.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1965685855086104578.json
hash: 9b6b9fe1a4fa43ac
coverage: 0.770833
learned_at: 2026-10-15 22:31:37
nodes: [Note, Note, MarkdownNote, WanVideoSetLoRAs, Note, WanVideoSetBlockSwap, Note, WanVideoEmptyEmbeds, WanVideoEncode, GetNode, MelBandRoFormerSampler, NormalizeAudioLoudness, AudioEncoderEncode, MarkdownNote, Reroute, AudioEncoderLoader, MelBandRoFormerModelLoader, WanVideoBlockSwap, WanVideoSampler, WanVideoEncode, ImageResizeKJv2, ImageResizeKJv2, Reroute, ImageResizeKJv2, WanVideoDecode, GetImageSizeAndCount, GetImageRangeFromBatch, ColorMatch, ImageConcatMulti, VHS_VideoCombine, WanVideoModelLoader, LayerUtility: ImageScaleByAspectRatio V2, WanVideoVAELoader, easy anythingIndexSwitch, VHS_LoadVideo, Note, Note, Note, WanVideoTextEncodeCached, Note, Note, Note, Note, WanVideoLoraSelectMulti, JWInteger, CR Prompt Text, CR Prompt Text, LoadAudio, AudioCrop, WanVideoContextOptions, WanVideoAddS2VEmbeds, PreviewAny, CR Prompt Text, CLIPLoader, VAELoader, UNETLoader, ModelSamplingAuraFlow, SetUnionControlNetType, CFGNorm, ControlNetLoader, SaveLatent, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, PreviewImage, ImageFromBatch+, PreviewImage, JWInteger, Note, VHS_LoadVideo, VHS_LoadVideo, VHS_LoadVideo, VHS_LoadVideo, VHS_LoadVideo, VHS_LoadVideo, VHS_LoadVideo, VHS_LoadVideo, ControlNetApplySD3, EmptySD3LatentImage, CLIPTextEncode, ImageConcanate, KSampler, LoraLoaderModelOnly, LayerUtility: PurgeVRAM, PreviewImage, VAEDecode, JWInteger, Reroute, JWInteger, easy cleanGpuUsed, VHS_VideoInfo, CLIPTextEncode, easy anythingIndexSwitch, easy anythingIndexSwitch, VHS_VideoCombine, easy cleanGpuUsed]
patterns: []
missing: []
parameters: {"cfg": 1, "controlnet_strength": 1.0000000000000002, "denoise": 1, "sampler_name": "res_2s", "scheduler": "beta57", "seed": 334904424122557, "steps": 15}
---

# 视频生成/图生视频/Comfy挑战赛4 Qwen image+Wan2.2 S2V全身姿势控制V1_1965685855086104578.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1965685855086104578.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（96 个）：
- `Note`
- `Note`
- `MarkdownNote`
- `WanVideoSetLoRAs`
- `Note`
- `WanVideoSetBlockSwap`
- `Note`
- `WanVideoEmptyEmbeds`
- `WanVideoEncode`
- `GetNode`
- `MelBandRoFormerSampler` ★核心
- `NormalizeAudioLoudness`
- `AudioEncoderEncode`
- `MarkdownNote`
- `Reroute`
- `AudioEncoderLoader`
- `MelBandRoFormerModelLoader`
- `WanVideoBlockSwap`
- `WanVideoSampler` ★核心
- `WanVideoEncode`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `Reroute`
- `ImageResizeKJv2`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `GetImageRangeFromBatch`
- `ColorMatch`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `WanVideoModelLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoVAELoader`
- `easy anythingIndexSwitch`
- `VHS_LoadVideo`
- `Note`
- `Note`
- `Note`
- `WanVideoTextEncodeCached`
- `Note`
- `Note`
- `Note`
- `Note`
- `WanVideoLoraSelectMulti`
- `JWInteger`
- `CR Prompt Text`
- `CR Prompt Text`
- `LoadAudio`
- `AudioCrop`
- `WanVideoContextOptions`
- `WanVideoAddS2VEmbeds`
- `PreviewAny`
- `CR Prompt Text`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `ModelSamplingAuraFlow`
- `SetUnionControlNetType`
- `CFGNorm`
- `ControlNetLoader`
- `SaveLatent`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PreviewImage`
- `ImageFromBatch+`
- `PreviewImage`
- `JWInteger`
- `Note`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `ControlNetApplySD3` ★核心
- `EmptySD3LatentImage`
- `CLIPTextEncode` ★核心
- `ImageConcanate`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: PurgeVRAM`
- `PreviewImage`
- `VAEDecode` ★核心
- `JWInteger`
- `Reroute`
- `JWInteger`
- `easy cleanGpuUsed`
- `VHS_VideoInfo`
- `CLIPTextEncode` ★核心
- `easy anythingIndexSwitch`
- `easy anythingIndexSwitch`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`

## 关键参数

- `controlnet_strength` = `1.0000000000000002`
- `seed` = `334904424122557`
- `steps` = `15`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `beta57`
- `denoise` = `1`

## 知识

覆盖率 **77%**（74/96）

**有卡**：`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoEmptyEmbeds`、`WanVideoEncode`、`MelBandRoFormerSampler`、`NormalizeAudioLoudness`、`AudioEncoderEncode`、`AudioEncoderLoader`、`MelBandRoFormerModelLoader`、`WanVideoBlockSwap`、`WanVideoSampler`、`ImageResizeKJv2`、`WanVideoDecode`、`GetImageSizeAndCount`、`GetImageRangeFromBatch`、`ColorMatch`、`ImageConcatMulti`、`VHS_VideoCombine`、`WanVideoModelLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoVAELoader`、`easy anythingIndexSwitch`、`VHS_LoadVideo`、`WanVideoTextEncodeCached`、`WanVideoLoraSelectMulti`、`JWInteger`、`CR Prompt Text`、`LoadAudio`、`AudioCrop`、`WanVideoContextOptions`、`WanVideoAddS2VEmbeds`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`ModelSamplingAuraFlow`、`SetUnionControlNetType`、`CFGNorm`、`ControlNetLoader`、`SaveLatent`、`LoraLoaderModelOnly`、`ImageFromBatch+`、`ControlNetApplySD3`、`EmptySD3LatentImage`、`CLIPTextEncode`、`ImageConcanate`、`KSampler`、`LayerUtility: PurgeVRAM`、`VAEDecode`、`easy cleanGpuUsed`、`VHS_VideoInfo`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2

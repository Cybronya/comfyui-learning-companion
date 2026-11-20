---
key: 平台全量/wan_vace_inpaint_openclaw_api_2008024997318627330.json
name: wan_vace_inpaint_openclaw_api_2008024997318627330
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/wan_vace_inpaint_openclaw_api_2008024997318627330.json
hash: 1c130ba07cb36aad
coverage: 0.891304
learned_at: 2026-11-14 01:20:04
nodes: [CLIPTextEncode, InvertMask, GetVideoComponents, VAELoader, CLIPLoader, TrimVideoLatent, UNETLoader, LoraLoaderModelOnly, ImageCompositeMasked, ModelSamplingSD3, Reroute, easy sam3ModelLoader, SetNode, GetNode, CLIPTextEncode, BlockifyMask, easy sam3VideoSegmentation, RebatchImages, WanVaceToVideo, SimpleMath+, GetVideoComponents, KSampler, LoadVideo, GetVideoComponents, ImageToMask, TwoWaySwitch, Int, GetImageSize, WanSkipEndFrameImages_F2, VAEDecodeTiled, SimpleMath+, GrowMaskWithBlur, GrowMask, LoadVideo, LoadImage, TwoWaySwitch, SaveVideo, PreviewImage, MaskToImage, ImageResizeKJv2, CreateVideo, ImageMixerWithMask, WanVideoImageResizeToClosest, PreviewImage, GetImageSize, ImageResizeKJv2]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 319301138868115, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 平台全量/wan_vace_inpaint_openclaw_api_2008024997318627330.json

> 来源文件 `comfyui_library/workflows/平台全量/wan_vace_inpaint_openclaw_api_2008024997318627330.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（46 个）：
- `CLIPTextEncode` ★核心
- `InvertMask`
- `GetVideoComponents`
- `VAELoader`
- `CLIPLoader`
- `TrimVideoLatent`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `ImageCompositeMasked`
- `ModelSamplingSD3`
- `Reroute`
- `easy sam3ModelLoader`
- `SetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `BlockifyMask`
- `easy sam3VideoSegmentation`
- `RebatchImages`
- `WanVaceToVideo`
- `SimpleMath+`
- `GetVideoComponents`
- `KSampler` ★核心
- `LoadVideo`
- `GetVideoComponents`
- `ImageToMask`
- `TwoWaySwitch`
- `Int`
- `GetImageSize`
- `WanSkipEndFrameImages_F2`
- `VAEDecodeTiled` ★核心
- `SimpleMath+`
- `GrowMaskWithBlur`
- `GrowMask`
- `LoadVideo`
- `LoadImage`
- `TwoWaySwitch`
- `SaveVideo`
- `PreviewImage`
- `MaskToImage`
- `ImageResizeKJv2`
- `CreateVideo`
- `ImageMixerWithMask`
- `WanVideoImageResizeToClosest`
- `PreviewImage`
- `GetImageSize`
- `ImageResizeKJv2`

## 关键参数

- `seed` = `319301138868115`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **89%**（41/46）

**有卡**：`CLIPTextEncode`、`InvertMask`、`GetVideoComponents`、`VAELoader`、`CLIPLoader`、`TrimVideoLatent`、`UNETLoader`、`LoraLoaderModelOnly`、`ImageCompositeMasked`、`ModelSamplingSD3`、`easy sam3ModelLoader`、`BlockifyMask`、`easy sam3VideoSegmentation`、`RebatchImages`、`WanVaceToVideo`、`SimpleMath+`、`KSampler`、`LoadVideo`、`ImageToMask`、`TwoWaySwitch`、`Int`、`GetImageSize`、`WanSkipEndFrameImages_F2`、`VAEDecodeTiled`、`GrowMaskWithBlur`、`GrowMask`、`LoadImage`、`SaveVideo`、`MaskToImage`、`ImageResizeKJv2`、`CreateVideo`、`ImageMixerWithMask`、`WanVideoImageResizeToClosest`

**用到的条目**：KSampler、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader、TrimVideoLatent

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

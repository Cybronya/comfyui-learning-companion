---
key: 视频生成/图生视频/Wan_2.2_FMLFrame2V 首中尾帧生视频_1988481610276323329.json
name: Wan_2.2_FMLFrame2V 首中尾帧生视频_1988481610276323329.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1988481610276323329.json
hash: e6745c984f80d535
coverage: 0.469697
learned_at: 2026-10-15 22:33:03
nodes: [PrimitiveInt, KSamplerAdvanced, VAEDecode, SetNode, CLIPLoader, SetNode, VAELoader, PathchSageAttentionKJ, Label (rgthree), ModelSamplingSD3, ModelSamplingSD3, Note, GetNode, CLIPTextEncode, SetNode, GetNode, CLIPTextEncode, SetNode, GetNode, GetNode, SetNode, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, SetNode, PrimitiveInt, SetNode, PreviewImage, ImageResizeKJv2, PathchSageAttentionKJ, FloatConstant, GetNode, LayerUtility: PurgeVRAM, CLIPVisionEncode, CLIPVisionEncode, CLIPVisionLoader, PreviewImage, SetNode, ImageResizeKJv2, GetNode, GetNode, GetNode, GetNode, WanFirstLastFrameToVideo, PreviewImage, SetNode, ImageResizeKJv2, GetNode, CLIPVisionEncode, Note, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, UNETLoader, LoadImage, LoadImage, LoadImage, SetNode, VHS_VideoCombine, PrimitiveInt, PrimitiveInt, KSamplerAdvanced, WanFirstMiddleLastFrameToVideo]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "beta", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan_2.2_FMLFrame2V 首中尾帧生视频_1988481610276323329.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1988481610276323329.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（66 个）：
- `PrimitiveInt`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `SetNode`
- `CLIPLoader`
- `SetNode`
- `VAELoader`
- `PathchSageAttentionKJ`
- `Label (rgthree)`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `Note`
- `GetNode`
- `CLIPTextEncode` ★核心
- `SetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `PrimitiveInt`
- `SetNode`
- `PreviewImage`
- `ImageResizeKJv2`
- `PathchSageAttentionKJ`
- `FloatConstant`
- `GetNode`
- `LayerUtility: PurgeVRAM`
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `PreviewImage`
- `SetNode`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanFirstLastFrameToVideo`
- `PreviewImage`
- `SetNode`
- `ImageResizeKJv2`
- `GetNode`
- `CLIPVisionEncode`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `SetNode`
- `VHS_VideoCombine`
- `PrimitiveInt`
- `PrimitiveInt`
- `KSamplerAdvanced` ★核心
- `WanFirstMiddleLastFrameToVideo`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `beta`

## 知识

覆盖率 **47%**（31/66）

**有卡**：`KSamplerAdvanced`、`VAEDecode`、`CLIPLoader`、`VAELoader`、`PathchSageAttentionKJ`、`Label (rgthree)`、`ModelSamplingSD3`、`CLIPTextEncode`、`ImageResizeKJv2`、`FloatConstant`、`LayerUtility: PurgeVRAM`、`CLIPVisionEncode`、`CLIPVisionLoader`、`WanFirstLastFrameToVideo`、`LoraLoaderModelOnly`、`UNETLoader`、`LoadImage`、`VHS_VideoCombine`、`WanFirstMiddleLastFrameToVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced

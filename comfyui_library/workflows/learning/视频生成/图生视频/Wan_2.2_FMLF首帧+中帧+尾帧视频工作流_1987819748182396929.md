---
key: 视频生成/图生视频/Wan_2.2_FMLF首帧+中帧+尾帧视频工作流_1987819748182396929.json
name: Wan_2.2_FMLF首帧+中帧+尾帧视频工作流_1987819748182396929.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan_2.2_FMLF首帧+中帧+尾帧视频工作流_1987819748182396929.json
hash: 8e1b74edb61838e4
coverage: 0.485294
learned_at: 2026-10-15 22:33:00
nodes: [VAEDecode, SetNode, Label (rgthree), SetNode, SetNode, SetNode, PrimitiveInt, SetNode, PrimitiveInt, SetNode, PreviewImage, ImageResizeKJv2, FloatConstant, SetNode, PreviewImage, SetNode, ImageResizeKJv2, GetNode, GetNode, PreviewImage, SetNode, GetNode, VAELoader, VHS_VideoCombine, LoadImage, LoadImage, LoadImage, ImageResizeKJv2, SetNode, SetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, CLIPVisionEncode, CLIPVisionEncode, CLIPVisionEncode, CLIPVisionLoader, PrimitiveInt, LoraLoaderModelOnly, LoraLoaderModelOnly, Note, PathchSageAttentionKJ, wanBlockSwap, wanBlockSwap, CLIPLoader, PathchSageAttentionKJ, LayerUtility: PurgeVRAM, GetNode, Note, CLIPTextEncode, ModelSamplingSD3, ModelSamplingSD3, GetNode, GetNode, CLIPTextEncode, WanFirstMiddleLastFrameToVideo, LayerUtility: PurgeVRAM, UNETLoader, UNETLoader, PrimitiveInt, KSamplerAdvanced, KSamplerAdvanced]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "beta", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan_2.2_FMLF首帧+中帧+尾帧视频工作流_1987819748182396929.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1987819748182396929.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（68 个）：
- `VAEDecode` ★核心
- `SetNode`
- `Label (rgthree)`
- `SetNode`
- `SetNode`
- `SetNode`
- `PrimitiveInt`
- `SetNode`
- `PrimitiveInt`
- `SetNode`
- `PreviewImage`
- `ImageResizeKJv2`
- `FloatConstant`
- `SetNode`
- `PreviewImage`
- `SetNode`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `SetNode`
- `GetNode`
- `VAELoader`
- `VHS_VideoCombine`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ImageResizeKJv2`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `PrimitiveInt`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`
- `PathchSageAttentionKJ`
- `wanBlockSwap`
- `wanBlockSwap`
- `CLIPLoader`
- `PathchSageAttentionKJ`
- `LayerUtility: PurgeVRAM`
- `GetNode`
- `Note`
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `WanFirstMiddleLastFrameToVideo`
- `LayerUtility: PurgeVRAM`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `PrimitiveInt`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `beta`

## 知识

覆盖率 **49%**（33/68）

**有卡**：`VAEDecode`、`Label (rgthree)`、`ImageResizeKJv2`、`FloatConstant`、`VAELoader`、`VHS_VideoCombine`、`LoadImage`、`CLIPVisionEncode`、`CLIPVisionLoader`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`wanBlockSwap`、`CLIPLoader`、`LayerUtility: PurgeVRAM`、`CLIPTextEncode`、`ModelSamplingSD3`、`WanFirstMiddleLastFrameToVideo`、`UNETLoader`、`KSamplerAdvanced`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced

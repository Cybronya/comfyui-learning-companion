---
key: 视频生成/文生视频/Wan_2.2_img2vid 6 场景 30 秒 长视频角色一致性工作流_1979468056202219521.json
name: Wan_2.2_img2vid 6 场景 30 秒 长视频角色一致性工作流_1979468056202219521
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan_2.2_img2vid 6 场景 30 秒 长视频角色一致性工作流_1979468056202219521.json
hash: afa9b6a8d4e1129a
coverage: 0.427184
learned_at: 2026-10-10 23:08:14
nodes: [PrimitiveInt, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, LayerUtility: PurgeVRAM V2, SetNode, SetNode, UnetLoaderGGUF, wanBlockSwap, UnetLoaderGGUF, wanBlockSwap, PathchSageAttentionKJ, Label (rgthree), ModelSamplingSD3, Note, Note, GetNode, easy seed, CLIPTextEncode, SetNode, GetNode, CLIPTextEncode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, StringConcatenate, WanImageToVideo, PrimitiveInt, SetNode, SetNode, PrimitiveInt, GetNode, GetNode, GetNode, SetNode, PrimitiveInt, ImageResizeKJv2, TorchCompileModel, KSamplerAdvanced, PathchSageAttentionKJ, TorchCompileModel, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, GetNode, GetNode, GetNode, VAEDecode, GetNode, ModelSamplingSD3, LayerUtility: PurgeVRAM V2, WanImageToVideo, GetNode, GetNode, GetNode, VHS_VideoCombine, GetNode, GetNode, GetNode, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, GetNode, GetNode, GetNode, VAEDecode, GetNode, ModelSamplingSD3, LayerUtility: PurgeVRAM V2, WanImageToVideo, GetNode, GetNode, GetNode, VHS_VideoCombine, GetNode, GetNode, GetNode, GetNode, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, GetNode, GetNode, GetNode, VAEDecode, GetNode, ModelSamplingSD3, LayerUtility: PurgeVRAM V2, WanImageToVideo, GetNode, GetNode, GetNode, VHS_VideoCombine, GetNode, GetNode, GetNode, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, GetNode, GetNode, GetNode, VAEDecode, GetNode, ModelSamplingSD3, LayerUtility: PurgeVRAM V2, WanImageToVideo, GetNode, GetNode, GetNode, VHS_VideoCombine, GetNode, GetNode, GetNode, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, GetNode, GetNode, GetNode, VAEDecode, GetNode, ModelSamplingSD3, LayerUtility: PurgeVRAM V2, WanImageToVideo, GetNode, GetNode, GetNode, VHS_VideoCombine, GetNode, GetNode, StringConcatenate, GetNode, GetNode, GetNode, CLIPTextEncode, ImageResizeKJv2, StringConcatenate, GetNode, GetNode, GetNode, CLIPTextEncode, ImageResizeKJv2, StringConcatenate, GetNode, GetNode, GetNode, CLIPTextEncode, ImageResizeKJv2, StringConcatenate, GetNode, GetNode, GetNode, CLIPTextEncode, ImageResizeKJv2, StringConcatenate, GetNode, GetNode, GetNode, CLIPTextEncode, ImageResizeKJv2, ImageBatchMulti, VHS_VideoCombine, FloatConstant, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, Fast Groups Bypasser (rgthree), ModelSamplingSD3, SetNode, VAELoader, CLIPLoader, LoraLoaderModelOnly, Note, LoraLoaderModelOnly, Note, LoraLoaderModelOnly, Note, LoraLoaderModelOnly, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, VHS_VideoCombine, RIFE VFI, UNETLoader, UNETLoader, VHS_VideoCombine]
patterns: []
missing: [Label (rgthree), LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, RIFE VFI, easy seed]
parameters: {"cfg": 8, "denoise": "beta", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
discoveries: [次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/Wan_2.2_img2vid 6 场景 30 秒 长视频角色一致性工作流_1979468056202219521.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan_2.2_img2vid 6 场景 30 秒 长视频角色一致性工作流_1979468056202219521.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（206 个）：
- `PrimitiveInt`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM V2`
- `SetNode`
- `SetNode`
- `UnetLoaderGGUF` ★核心
- `wanBlockSwap`
- `UnetLoaderGGUF` ★核心
- `wanBlockSwap`
- `PathchSageAttentionKJ`
- `Label (rgthree)`
- `ModelSamplingSD3`
- `Note`
- `Note`
- `GetNode`
- `easy seed`
- `CLIPTextEncode` ★核心
- `SetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `StringConcatenate`
- `WanImageToVideo`
- `PrimitiveInt`
- `SetNode`
- `SetNode`
- `PrimitiveInt`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `PrimitiveInt`
- `ImageResizeKJv2`
- `TorchCompileModel`
- `KSamplerAdvanced` ★核心
- `PathchSageAttentionKJ`
- `TorchCompileModel`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `ModelSamplingSD3`
- `LayerUtility: PurgeVRAM V2`
- `WanImageToVideo`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `ModelSamplingSD3`
- `LayerUtility: PurgeVRAM V2`
- `WanImageToVideo`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `ModelSamplingSD3`
- `LayerUtility: PurgeVRAM V2`
- `WanImageToVideo`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `ModelSamplingSD3`
- `LayerUtility: PurgeVRAM V2`
- `WanImageToVideo`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `ModelSamplingSD3`
- `LayerUtility: PurgeVRAM V2`
- `WanImageToVideo`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `StringConcatenate`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `ImageResizeKJv2`
- `StringConcatenate`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `ImageResizeKJv2`
- `StringConcatenate`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `ImageResizeKJv2`
- `StringConcatenate`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `ImageResizeKJv2`
- `StringConcatenate`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `ImageResizeKJv2`
- `ImageBatchMulti`
- `VHS_VideoCombine`
- `FloatConstant`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Fast Groups Bypasser (rgthree)`
- `ModelSamplingSD3`
- `SetNode`
- `VAELoader`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `Note`
- `LoraLoaderModelOnly` ★核心
- `Note`
- `LoraLoaderModelOnly` ★核心
- `Note`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `VHS_VideoCombine`
- `RIFE VFI`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `VHS_VideoCombine`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `beta`

## 知识

覆盖率 **43%**（88/206）

**有卡**：`KSamplerAdvanced`、`VAEDecode`、`UnetLoaderGGUF`、`wanBlockSwap`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`CLIPTextEncode`、`StringConcatenate`、`WanImageToVideo`、`ImageResizeKJv2`、`TorchCompileModel`、`VHS_VideoCombine`、`ImageBatchMulti`、`FloatConstant`、`VAELoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`LoadImage`、`UNETLoader`

**缺卡**（9）：`Label (rgthree)`、`LayerUtility: PurgeVRAM V2`、`LayerUtility: PurgeVRAM V2`、`LayerUtility: PurgeVRAM V2`、`LayerUtility: PurgeVRAM V2`、`LayerUtility: PurgeVRAM V2`、`LayerUtility: PurgeVRAM V2`、`RIFE VFI`、`easy seed`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced

## 学习发现

- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明

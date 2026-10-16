---
key: 视频生成/图生视频/fusionx+comfyui native vace 首尾帧工作流_1934269405759234050.json
name: fusionx+comfyui native vace 首尾帧工作流_1934269405759234050.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1934269405759234050.json
hash: 4d34074ca76d3a9f
coverage: 0.532468
learned_at: 2026-10-15 22:30:16
nodes: [SetNode, SetNode, SetNode, PreviewImage, GetNode, GetNode, LoadImage, ImageResizeKJv2, GetNode, GetNode, PreviewImage, MaskPreview+, WanVideoVACEStartToEndFrame, VHS_LoadVideo, VAEDecode, ImageResizeKJv2, WanVideoVACEStartToEndFrame, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, ImageResizeKJv2, KSampler, GetNode, GetNode, SetNode, GetNode, SetNode, SetNode, SetNode, VHS_VideoCombine, SetNode, SetNode, CLIPLoader, VAELoader, TorchCompileModelWanVideo, PathchSageAttentionKJ, INTConstant, INTConstant, INTConstant, ImageResizeKJv2, AIO_Preprocessor, DWPreprocessor, VHS_VideoCombine, VHS_VideoCombine, ImageResizeKJv2, GetNode, GetNode, GetNode, MaskPreview+, PreviewImage, GetNode, CLIPTextEncode, WanVaceToVideo, CLIPTextEncode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, ModelSamplingSD3, TrimVideoLatent, Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), WanVaceToVideo, UNETLoader, UnetLoaderGGUFAdvanced]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "lcm", "scheduler": "simple", "seed": 905074390800411, "steps": 10}
---

# 视频生成/图生视频/fusionx+comfyui native vace 首尾帧工作流_1934269405759234050.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1934269405759234050.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（77 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `LoadImage`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `MaskPreview+`
- `WanVideoVACEStartToEndFrame`
- `VHS_LoadVideo`
- `VAEDecode` ★核心
- `ImageResizeKJv2`
- `WanVideoVACEStartToEndFrame`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `KSampler` ★核心
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `VHS_VideoCombine`
- `SetNode`
- `SetNode`
- `CLIPLoader`
- `VAELoader`
- `TorchCompileModelWanVideo`
- `PathchSageAttentionKJ`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `ImageResizeKJv2`
- `AIO_Preprocessor`
- `DWPreprocessor`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `GetNode`
- `MaskPreview+`
- `PreviewImage`
- `GetNode`
- `CLIPTextEncode` ★核心
- `WanVaceToVideo`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `ModelSamplingSD3`
- `TrimVideoLatent`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `WanVaceToVideo`
- `UNETLoader` ★核心
- `UnetLoaderGGUFAdvanced` ★核心

## 关键参数

- `seed` = `905074390800411`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `lcm`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **53%**（41/77）

**有卡**：`LoadImage`、`ImageResizeKJv2`、`MaskPreview+`、`WanVideoVACEStartToEndFrame`、`VHS_LoadVideo`、`VAEDecode`、`KSampler`、`VHS_VideoCombine`、`CLIPLoader`、`VAELoader`、`TorchCompileModelWanVideo`、`PathchSageAttentionKJ`、`INTConstant`、`AIO_Preprocessor`、`DWPreprocessor`、`CLIPTextEncode`、`WanVaceToVideo`、`ModelSamplingSD3`、`TrimVideoLatent`、`Label (rgthree)`、`UNETLoader`、`UnetLoaderGGUFAdvanced`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、TrimVideoLatent

---
key: 视频生成/图生视频/Remix3.0图生视频&首尾帧合集+By+像素幻想Lab_2036420599651770369.json
name: Remix3.0图生视频&首尾帧合集+By+像素幻想Lab_2036420599651770369.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Remix3.0图生视频&首尾帧合集+By+像素幻想Lab_2036420599651770369.json
hash: 1023cfd93d867db0
coverage: 0.960526
learned_at: 2026-10-15 22:35:52
nodes: [CLIPVisionEncode, CLIPVisionEncode, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelSamplingSD3, easy setNode, ModelPatchTorchSettings, ModelSamplingSD3, easy setNode, easy setNode, easy setNode, VAEDecode, easy getNode, CLIPTextEncode, CLIPTextEncode, easy getNode, easy setNode, easy setNode, INTConstant, easy setNode, easy setNode, INTConstant, easy setNode, easy setNode, FloatConstant, easy getNode, easy getNode, easy getNode, PainterI2V, ImageResizeKJv2, easy getNode, easy getNode, KSamplerAdvanced, KSamplerAdvanced, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, CLIPVisionLoader, CLIPTextEncode, CLIPVisionLoader, easy getNode, VAEDecode, easy getNode, easy getNode, CLIPLoader, VAELoader, UNETLoader, UNETLoader, INTConstant, easy getNode, easy getNode, ImageResizeKJv2, ImageResizeKJv2, easy getNode, easy getNode, KSamplerAdvanced, KSamplerAdvanced, PainterFLF2V, Fast Groups Bypasser (rgthree), easy getNode, LoadImage, LoadImage, RH_LLMAPI_NODE, CLIPTextEncode, easy showAnything, LoadImage, VHS_VideoCombine, CR Text, RH_LLMAPI_NODE, easy showAnything, INTConstant, INTConstant, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/Remix3.0图生视频&首尾帧合集+By+像素幻想Lab_2036420599651770369.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2036420599651770369.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（76 个）：
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `easy setNode`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `easy setNode`
- `easy setNode`
- `easy setNode`
- `VAEDecode` ★核心
- `easy getNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `easy getNode`
- `easy setNode`
- `easy setNode`
- `INTConstant`
- `easy setNode`
- `easy setNode`
- `INTConstant`
- `easy setNode`
- `easy setNode`
- `FloatConstant`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `PainterI2V`
- `ImageResizeKJv2`
- `easy getNode`
- `easy getNode`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `CLIPVisionLoader`
- `CLIPTextEncode` ★核心
- `CLIPVisionLoader`
- `easy getNode`
- `VAEDecode` ★核心
- `easy getNode`
- `easy getNode`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `INTConstant`
- `easy getNode`
- `easy getNode`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `easy getNode`
- `easy getNode`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `PainterFLF2V`
- `Fast Groups Bypasser (rgthree)`
- `easy getNode`
- `LoadImage`
- `LoadImage`
- `RH_LLMAPI_NODE`
- `CLIPTextEncode` ★核心
- `easy showAnything`
- `LoadImage`
- `VHS_VideoCombine`
- `CR Text`
- `RH_LLMAPI_NODE`
- `easy showAnything`
- `INTConstant`
- `INTConstant`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **96%**（73/76）

**有卡**：`CLIPVisionEncode`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`ModelSamplingSD3`、`easy setNode`、`VAEDecode`、`easy getNode`、`CLIPTextEncode`、`INTConstant`、`FloatConstant`、`PainterI2V`、`ImageResizeKJv2`、`KSamplerAdvanced`、`CLIPVisionLoader`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`PainterFLF2V`、`LoadImage`、`RH_LLMAPI_NODE`、`VHS_VideoCombine`、`CR Text`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、CLIPVisionEncode

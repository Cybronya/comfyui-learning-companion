---
key: 视频生成/图生视频/图生视频 高动态 Smooth Mix  Wan 2.2_1979531861057769474.json
name: 图生视频 高动态 Smooth Mix  Wan 2.2_1979531861057769474.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/图生视频 高动态 Smooth Mix  Wan 2.2_1979531861057769474.json
hash: 38c1c5ba30e694e3
coverage: 0.794872
learned_at: 2026-10-15 22:32:24
nodes: [ModelSamplingSD3, UNETLoader, ModelSamplingSD3, CLIPLoader, VAELoader, wanBlockSwap, ModelPatchTorchSettings, wanBlockSwap, ModelPatchTorchSettings, UNETLoader, CLIPTextEncode, KSamplerAdvanced, PathchSageAttentionKJ, PathchSageAttentionKJ, CLIPVisionEncode, SimpleMath+, CLIPVisionLoader, WanImageToVideo, ImageResizeKJv2, KSamplerAdvanced, ImpactInt, ImpactInt, ImpactInt, GetNode, GetNode, GetNode, LoadImage, easy textSwitch, Note, PrimitiveStringMultiline, RH_LLMAPI_NODE, CLIPTextEncode, ShowText, VHS_VideoCombine, SetNode, SetNode, SetNode, VHS_VideoCombine, VAEDecode]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/图生视频 高动态 Smooth Mix  Wan 2.2_1979531861057769474.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1979531861057769474.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（39 个）：
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `CLIPLoader`
- `VAELoader`
- `wanBlockSwap`
- `ModelPatchTorchSettings`
- `wanBlockSwap`
- `ModelPatchTorchSettings`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `CLIPVisionEncode`
- `SimpleMath+`
- `CLIPVisionLoader`
- `WanImageToVideo`
- `ImageResizeKJv2`
- `KSamplerAdvanced` ★核心
- `ImpactInt`
- `ImpactInt`
- `ImpactInt`
- `GetNode`
- `GetNode`
- `GetNode`
- `LoadImage`
- `easy textSwitch`
- `Note`
- `PrimitiveStringMultiline`
- `RH_LLMAPI_NODE`
- `CLIPTextEncode` ★核心
- `ShowText`
- `VHS_VideoCombine`
- `SetNode`
- `SetNode`
- `SetNode`
- `VHS_VideoCombine`
- `VAEDecode` ★核心

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **79%**（31/39）

**有卡**：`ModelSamplingSD3`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`wanBlockSwap`、`ModelPatchTorchSettings`、`CLIPTextEncode`、`KSamplerAdvanced`、`PathchSageAttentionKJ`、`CLIPVisionEncode`、`SimpleMath+`、`CLIPVisionLoader`、`WanImageToVideo`、`ImageResizeKJv2`、`ImpactInt`、`LoadImage`、`easy textSwitch`、`RH_LLMAPI_NODE`、`ShowText`、`VHS_VideoCombine`、`VAEDecode`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、CLIPVisionEncode

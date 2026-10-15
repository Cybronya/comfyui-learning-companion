---
key: 视频生成/文生视频/Wan2.2 Smooth Mix首尾帧_1980878054304206850.json
name: Wan2.2 Smooth Mix首尾帧_1980878054304206850
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2 Smooth Mix首尾帧_1980878054304206850.json
hash: fc136c852a2e05b9
coverage: 0.744681
learned_at: 2026-10-15 22:47:10
nodes: [wanBlockSwap, wanBlockSwap, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, UNETLoader, UNETLoader, GetNode, GetNode, KSamplerAdvanced, KSamplerAdvanced, SetNode, ModelSamplingSD3, ModelSamplingSD3, SetNode, ImageConcanate, CLIPVisionEncode, CLIPVisionLoader, WanFirstLastFrameToVideo, CLIPVisionEncode, VHS_VideoCombine, VAEDecode, ImageConcanate, ImageConcanate, CLIPLoader, SetNode, VAELoader, SetNode, CLIPTextEncode, CLIPTextEncode, GetNode, ImageResizeKJ, MathExpression|pysssss, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, JWInteger, VHS_VideoCombine, GetNode, Note, RH_LLMAPI_NODE, LoadImage, LoadImage, easy showAnything, CR Text, ImpactSwitch, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "randomize"}
---

# 视频生成/文生视频/Wan2.2 Smooth Mix首尾帧_1980878054304206850.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2 Smooth Mix首尾帧_1980878054304206850.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（47 个）：
- `wanBlockSwap`
- `wanBlockSwap`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `GetNode`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `SetNode`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `SetNode`
- `ImageConcanate`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `WanFirstLastFrameToVideo`
- `CLIPVisionEncode`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `ImageConcanate`
- `ImageConcanate`
- `CLIPLoader`
- `SetNode`
- `VAELoader`
- `SetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `ImageResizeKJ`
- `MathExpression|pysssss`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JWInteger`
- `JWInteger`
- `VHS_VideoCombine`
- `GetNode`
- `Note`
- `RH_LLMAPI_NODE`
- `LoadImage`
- `LoadImage`
- `easy showAnything`
- `CR Text`
- `ImpactSwitch`
- `Fast Groups Bypasser (rgthree)`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **74%**（35/47）

**有卡**：`wanBlockSwap`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`UNETLoader`、`KSamplerAdvanced`、`ModelSamplingSD3`、`ImageConcanate`、`CLIPVisionEncode`、`CLIPVisionLoader`、`WanFirstLastFrameToVideo`、`VHS_VideoCombine`、`VAEDecode`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`ImageResizeKJ`、`MathExpression|pysssss`、`LayerUtility: ImageScaleByAspectRatio V2`、`JWInteger`、`RH_LLMAPI_NODE`、`LoadImage`、`CR Text`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、KSamplerAdvanced

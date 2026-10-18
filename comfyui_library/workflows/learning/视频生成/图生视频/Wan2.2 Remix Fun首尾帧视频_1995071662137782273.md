---
key: 视频生成/图生视频/Wan2.2 Remix Fun首尾帧视频_1995071662137782273.json
name: Wan2.2 Remix Fun首尾帧视频_1995071662137782273.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 Remix Fun首尾帧视频_1995071662137782273.json
hash: d6e4fe1ce12552b6
coverage: 0.913043
learned_at: 2026-10-15 22:33:22
nodes: [easy promptReplace, easy imageConcat, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, ModelSamplingSD3, ModelSamplingSD3, wanBlockSwap, wanBlockSwap, PathchSageAttentionKJ, ModelPatchTorchSettings, CLIPLoader, CLIPVisionEncode, AILab_QwenVL, PrimitiveStringMultiline, easy convertAnything, CLIPVisionLoader, PathchSageAttentionKJ, ModelPatchTorchSettings, VAELoader, ImpactInt, LayerUtility: ImageScaleByAspectRatio V2, ImpactInt, ImpactInt, RIFE VFI, CLIPTextEncode, CLIPTextEncode, WanFirstLastFrameToVideo, easy convertAnything, VHS_VideoCombine, VHS_VideoCombine, Fast Groups Bypasser (rgthree), VAEDecode, WanMoeKSampler, easy seed, MathExpression|pysssss, MathExpression|pysssss, PreviewAny, LoadImage, LoadImage, PrimitiveStringMultiline, easy anythingIndexSwitch, CLIPVisionEncode, ImageResizeKJ]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "euler_ancestral", "sampler_name": 1, "scheduler": 1, "seed": 0.875, "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2 Remix Fun首尾帧视频_1995071662137782273.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1995071662137782273.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（46 个）：
- `easy promptReplace`
- `easy imageConcat`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `wanBlockSwap`
- `wanBlockSwap`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `CLIPLoader`
- `CLIPVisionEncode`
- `AILab_QwenVL`
- `PrimitiveStringMultiline`
- `easy convertAnything`
- `CLIPVisionLoader`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `VAELoader`
- `ImpactInt`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImpactInt`
- `ImpactInt`
- `RIFE VFI`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `WanFirstLastFrameToVideo`
- `easy convertAnything`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Fast Groups Bypasser (rgthree)`
- `VAEDecode` ★核心
- `WanMoeKSampler` ★核心
- `easy seed`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `PreviewAny`
- `LoadImage`
- `LoadImage`
- `PrimitiveStringMultiline`
- `easy anythingIndexSwitch`
- `CLIPVisionEncode`
- `ImageResizeKJ`

## 关键参数

- `seed` = `0.875`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `euler_ancestral`

## 知识

覆盖率 **91%**（42/46）

**有卡**：`easy promptReplace`、`easy imageConcat`、`UNETLoader`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`wanBlockSwap`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`CLIPLoader`、`CLIPVisionEncode`、`AILab_QwenVL`、`easy convertAnything`、`CLIPVisionLoader`、`VAELoader`、`ImpactInt`、`LayerUtility: ImageScaleByAspectRatio V2`、`RIFE VFI`、`CLIPTextEncode`、`WanFirstLastFrameToVideo`、`VHS_VideoCombine`、`VAEDecode`、`WanMoeKSampler`、`easy seed`、`MathExpression|pysssss`、`LoadImage`、`easy anythingIndexSwitch`、`ImageResizeKJ`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2

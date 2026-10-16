---
key: 视频生成/图生视频/Wan2.2 14B+LightX2V 超极速图生视频＋首尾帧＋高清频_2033413593969987586.json
name: Wan2.2 14B+LightX2V 超极速图生视频＋首尾帧＋高清频_2033413593969987586.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2033413593969987586.json
hash: f781e5eb496a890c
coverage: 0.854839
learned_at: 2026-10-15 22:35:39
nodes: [VAEDecode, CLIPLoader, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, UNETLoader, UNETLoader, VAELoader, CLIPLoader, LoraLoaderModelOnly, PathchSageAttentionKJ, LoraLoaderModelOnly, PathchSageAttentionKJ, UNETLoader, Note, ModelSamplingSD3, ModelSamplingSD3, VAELoader, VAEDecode, CLIPTextEncode, LayerUtility: PurgeVRAM, Note, Note, Note, Note, WanFirstLastFrameToVideo, KSamplerAdvanced, KSamplerAdvanced, WanImageToVideo, VHS_VideoInfo, RIFE VFI, Note, MathExpression|pysssss, Note, WanMoeKSampler, VHS_VideoCombine, Note, FlashVSRNode, JWInteger, VHS_LoadVideo, JWInteger, JWImageResize, JWImageResize, JWInteger, JWInteger, CLIPTextEncode, CLIPTextEncode, JWInteger, JWInteger, UNETLoader, LoadImage, VHS_VideoCombine, VHS_VideoCombine, LoadImage, LoadImage, CLIPTextEncode, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "lcm", "sampler_name": 1, "scheduler": 1, "seed": 0.9, "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2 14B+LightX2V 超极速图生视频＋首尾帧＋高清频_2033413593969987586.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2033413593969987586.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（62 个）：
- `VAEDecode` ★核心
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `Note`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `VAELoader`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `LayerUtility: PurgeVRAM`
- `Note`
- `Note`
- `Note`
- `Note`
- `WanFirstLastFrameToVideo`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `WanImageToVideo`
- `VHS_VideoInfo`
- `RIFE VFI`
- `Note`
- `MathExpression|pysssss`
- `Note`
- `WanMoeKSampler` ★核心
- `VHS_VideoCombine`
- `Note`
- `FlashVSRNode`
- `JWInteger`
- `VHS_LoadVideo`
- `JWInteger`
- `JWImageResize`
- `JWImageResize`
- `JWInteger`
- `JWInteger`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `JWInteger`
- `JWInteger`
- `UNETLoader` ★核心
- `LoadImage`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LoadImage`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `Fast Groups Bypasser (rgthree)`

## 关键参数

- `seed` = `0.9`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `lcm`

## 知识

覆盖率 **85%**（53/62）

**有卡**：`VAEDecode`、`CLIPLoader`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`LayerUtility: PurgeVRAM`、`UNETLoader`、`VAELoader`、`CLIPTextEncode`、`WanFirstLastFrameToVideo`、`KSamplerAdvanced`、`WanImageToVideo`、`VHS_VideoInfo`、`RIFE VFI`、`MathExpression|pysssss`、`WanMoeKSampler`、`VHS_VideoCombine`、`FlashVSRNode`、`JWInteger`、`VHS_LoadVideo`、`JWImageResize`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced

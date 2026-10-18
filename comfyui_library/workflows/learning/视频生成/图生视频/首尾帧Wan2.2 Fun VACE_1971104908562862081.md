---
key: 视频生成/图生视频/首尾帧Wan2.2 Fun VACE_1971104908562862081.json
name: 首尾帧Wan2.2 Fun VACE_1971104908562862081.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/首尾帧Wan2.2 Fun VACE_1971104908562862081.json
hash: f3fa8ddefbdbc502
coverage: 0.870968
learned_at: 2026-10-15 22:31:55
nodes: [KSamplerAdvanced, KSamplerAdvanced, WanVaceToVideo, CLIPTextEncode, WanVideoVACEStartToEndFrame, TrimVideoLatent, VAEDecode, ModelSamplingSD3, Note, Note, INTConstant, ZML_DualInteger, Text Multiline, Note, Note, ImageResizeKJv2, ImageResizeKJv2, VHS_VideoCombine, ImpactFloat, ModelSamplingSD3, LoraLoaderModelOnly, VAELoader, CLIPLoader, LoadImage, LoadImage, CLIPTextEncode, DiffusionModelSelector, DiffusionModelLoaderKJ, LoraLoaderModelOnly, DiffusionModelSelector, DiffusionModelLoaderKJ]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/首尾帧Wan2.2 Fun VACE_1971104908562862081.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1971104908562862081.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（31 个）：
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `WanVaceToVideo`
- `CLIPTextEncode` ★核心
- `WanVideoVACEStartToEndFrame`
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `Note`
- `Note`
- `INTConstant`
- `ZML_DualInteger`
- `Text Multiline`
- `Note`
- `Note`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `VHS_VideoCombine`
- `ImpactFloat`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `CLIPLoader`
- `LoadImage`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `DiffusionModelSelector`
- `DiffusionModelLoaderKJ`
- `LoraLoaderModelOnly` ★核心
- `DiffusionModelSelector`
- `DiffusionModelLoaderKJ`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **87%**（27/31）

**有卡**：`KSamplerAdvanced`、`WanVaceToVideo`、`CLIPTextEncode`、`WanVideoVACEStartToEndFrame`、`TrimVideoLatent`、`VAEDecode`、`ModelSamplingSD3`、`INTConstant`、`ZML_DualInteger`、`Text Multiline`、`ImageResizeKJv2`、`VHS_VideoCombine`、`ImpactFloat`、`LoraLoaderModelOnly`、`VAELoader`、`CLIPLoader`、`LoadImage`、`DiffusionModelSelector`、`DiffusionModelLoaderKJ`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerAdvanced、TrimVideoLatent

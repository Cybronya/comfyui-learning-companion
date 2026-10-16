---
key: 视频生成/图生视频/Ltxvideo0.9.7-13B-3图首尾帧图生视频_1922227928325636097.json
name: Ltxvideo0.9.7-13B-3图首尾帧图生视频_1922227928325636097.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1922227928325636097.json
hash: 5702c337b1b5ac0e
coverage: 1
learned_at: 2026-10-15 22:29:45
nodes: [KSamplerSelect, BasicScheduler, ImageBatch, STGAdvancedPresets, VHS_VideoCombine, ImageBatch, LTXVConditioning, CLIPTextEncode, ImageResizeKJ, ImageResizeKJ, LoadImage, LoadImage, LoadImage, Set VAE Decoder Noise, VAEDecode, RandomNoise, CLIPTextEncode, ImageResizeKJ, STGGuiderAdvanced, LTXVBaseSampler, Int, CLIPLoader, CheckpointLoaderSimple]
patterns: []
missing: []
parameters: {"checkpoint": "ltxv-13b-0.9.7-dev_fp8_e4m3fn.safetensors"}
---

# 视频生成/图生视频/Ltxvideo0.9.7-13B-3图首尾帧图生视频_1922227928325636097.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1922227928325636097.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（23 个）：
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `ImageBatch`
- `STGAdvancedPresets`
- `VHS_VideoCombine`
- `ImageBatch`
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `ImageResizeKJ`
- `ImageResizeKJ`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Set VAE Decoder Noise`
- `VAEDecode` ★核心
- `RandomNoise`
- `CLIPTextEncode` ★核心
- `ImageResizeKJ`
- `STGGuiderAdvanced`
- `LTXVBaseSampler` ★核心
- `Int`
- `CLIPLoader`
- `CheckpointLoaderSimple` ★核心

## 关键参数

- `checkpoint` = `ltxv-13b-0.9.7-dev_fp8_e4m3fn.safetensors`

## 知识

覆盖率 **100%**（23/23）

**有卡**：`KSamplerSelect`、`BasicScheduler`、`ImageBatch`、`STGAdvancedPresets`、`VHS_VideoCombine`、`LTXVConditioning`、`CLIPTextEncode`、`ImageResizeKJ`、`LoadImage`、`Set VAE Decoder Noise`、`VAEDecode`、`RandomNoise`、`STGGuiderAdvanced`、`LTXVBaseSampler`、`Int`、`CLIPLoader`、`CheckpointLoaderSimple`

**用到的条目**：VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerSelect、LTXVBaseSampler、Set VAE Decoder Noise

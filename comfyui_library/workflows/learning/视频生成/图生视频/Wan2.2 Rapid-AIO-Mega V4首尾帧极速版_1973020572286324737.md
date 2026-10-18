---
key: 视频生成/图生视频/Wan2.2 Rapid-AIO-Mega V4首尾帧极速版_1973020572286324737.json
name: Wan2.2 Rapid-AIO-Mega V4首尾帧极速版_1973020572286324737.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 Rapid-AIO-Mega V4首尾帧极速版_1973020572286324737.json
hash: 6c82122231772b25
coverage: 0.869565
learned_at: 2026-10-15 22:32:01
nodes: [KSampler, ModelSamplingSD3, CLIPTextEncode, WanVaceToVideo, Note, WanVideoVACEStartToEndFrame, LayerUtility: ImageScaleByAspectRatio V2, ImageConcanate, ImageConcanate, VAEDecode, VHS_VideoCombine, PDIMAGE_LongerSize, ApplySageAttention, ImageResizeKJv2, CLIPTextEncode, LoadImage, VHS_VideoCombine, LoadImage, JWInteger, JWInteger, Note, Note, CheckpointLoaderSimple]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-rapid-mega-aio-v4.safetensors", "denoise": 1, "sampler_name": "ipndm", "scheduler": "sgm_uniform", "seed": 7567358653673, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Wan2.2 Rapid-AIO-Mega V4首尾帧极速版_1973020572286324737.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1973020572286324737.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（23 个）：
- `KSampler` ★核心
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `WanVaceToVideo`
- `Note`
- `WanVideoVACEStartToEndFrame`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageConcanate`
- `ImageConcanate`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `PDIMAGE_LongerSize`
- `ApplySageAttention`
- `ImageResizeKJv2`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `VHS_VideoCombine`
- `LoadImage`
- `JWInteger`
- `JWInteger`
- `Note`
- `Note`
- `CheckpointLoaderSimple` ★核心

## 关键参数

- `seed` = `7567358653673`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `ipndm`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`
- `checkpoint` = `wan2.2-rapid-mega-aio-v4.safetensors`

## 知识

覆盖率 **87%**（20/23）

**有卡**：`KSampler`、`ModelSamplingSD3`、`CLIPTextEncode`、`WanVaceToVideo`、`WanVideoVACEStartToEndFrame`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageConcanate`、`VAEDecode`、`VHS_VideoCombine`、`PDIMAGE_LongerSize`、`ApplySageAttention`、`ImageResizeKJv2`、`LoadImage`、`JWInteger`、`CheckpointLoaderSimple`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、ImageResizeKJv2、PDIMAGE_LongerSize

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

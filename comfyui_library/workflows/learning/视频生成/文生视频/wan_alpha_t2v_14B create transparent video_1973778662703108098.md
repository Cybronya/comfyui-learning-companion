---
key: 视频生成/文生视频/wan_alpha_t2v_14B create transparent video_1973778662703108098.json
name: wan_alpha_t2v_14B create transparent video_1973778662703108098
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan_alpha_t2v_14B create transparent video_1973778662703108098.json
hash: 7f24adc328958401
coverage: 1
learned_at: 2026-10-10 23:09:58
nodes: [UNETLoader, EmptyHunyuanLatentVideo, CLIPLoader, VAELoader, ImageToMask, ImageCompositeMasked, INTConstant, INTConstant, VHS_VideoCombine, VHS_LoadVideo, INTConstant, CLIPTextEncode, VAELoader, LoraLoaderModelOnly, ModelSamplingSD3, LoraLoaderModelOnly, KSampler, VAEDecode, SavePNGZIP_and_Preview_RGBA_AnimatedWEBP, VHS_VideoCombine, LoraLoaderModelOnly, VHS_VideoCombine, VAEDecode, CLIPTextEncode]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "lcm", "scheduler": "simple", "seed": 640051545856950, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/wan_alpha_t2v_14B create transparent video_1973778662703108098.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/wan_alpha_t2v_14B create transparent video_1973778662703108098.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（24 个）：
- `UNETLoader` ★核心
- `EmptyHunyuanLatentVideo`
- `CLIPLoader`
- `VAELoader`
- `ImageToMask`
- `ImageCompositeMasked`
- `INTConstant`
- `INTConstant`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `INTConstant`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SavePNGZIP_and_Preview_RGBA_AnimatedWEBP`
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `640051545856950`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `lcm`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（24/24）

**有卡**：`UNETLoader`、`EmptyHunyuanLatentVideo`、`CLIPLoader`、`VAELoader`、`ImageToMask`、`ImageCompositeMasked`、`INTConstant`、`VHS_VideoCombine`、`VHS_LoadVideo`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`KSampler`、`VAEDecode`、`SavePNGZIP_and_Preview_RGBA_AnimatedWEBP`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、EmptyHunyuanLatentVideo

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

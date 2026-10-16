---
key: 视频生成/文生视频/Wan2.1 T2V 原生文生视频_1947883118252408834.json
name: Wan2.1 T2V 原生文生视频_1947883118252408834.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1947883118252408834.json
hash: 75b46f1d94838981
coverage: 1
learned_at: 2026-10-15 22:43:32
nodes: [ModelSamplingSD3, KSampler, VAELoader, EmptyHunyuanLatentVideo, UNETLoader, CLIPLoader, CLIPTextEncode, VAEDecode, Note Plus (mtb), LoadImageFromUrl, SaveAnimatedWEBP, CLIPTextEncode, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 704000290446434, "steps": 30}
---

# 视频生成/文生视频/Wan2.1 T2V 原生文生视频_1947883118252408834.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1947883118252408834.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（13 个）：
- `ModelSamplingSD3`
- `KSampler` ★核心
- `VAELoader`
- `EmptyHunyuanLatentVideo`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `Note Plus (mtb)`
- `LoadImageFromUrl`
- `SaveAnimatedWEBP`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`

## 关键参数

- `seed` = `704000290446434`
- `steps` = `30`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（13/13）

**有卡**：`ModelSamplingSD3`、`KSampler`、`VAELoader`、`EmptyHunyuanLatentVideo`、`UNETLoader`、`CLIPLoader`、`CLIPTextEncode`、`VAEDecode`、`Note Plus (mtb)`、`LoadImageFromUrl`、`SaveAnimatedWEBP`、`VHS_VideoCombine`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、EmptyHunyuanLatentVideo、SaveAnimatedWEBP

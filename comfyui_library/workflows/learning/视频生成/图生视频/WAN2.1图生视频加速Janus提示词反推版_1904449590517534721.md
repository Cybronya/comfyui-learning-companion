---
key: 视频生成/图生视频/WAN2.1图生视频加速Janus提示词反推版_1904449590517534721.json
name: WAN2.1图生视频加速Janus提示词反推版_1904449590517534721.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1904449590517534721.json
hash: 49b0e769557c38e2
coverage: 0.944444
learned_at: 2026-10-15 22:29:25
nodes: [VAEDecode, CLIPVisionEncode, CLIPTextEncode, CLIPTextEncode, KSampler, TeaCache, WanImageToVideo, JanusImageUnderstanding, StringFunction|pysssss, ShowText|pysssss, StringFunction|pysssss, VHS_VideoCombine, CLIPVisionLoader, LoadImage, JanusModelLoader, VAELoader, CLIPLoader, UNETLoader]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 406450093112888, "steps": 20}
---

# 视频生成/图生视频/WAN2.1图生视频加速Janus提示词反推版_1904449590517534721.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1904449590517534721.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（18 个）：
- `VAEDecode` ★核心
- `CLIPVisionEncode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `TeaCache`
- `WanImageToVideo`
- `JanusImageUnderstanding`
- `StringFunction|pysssss`
- `ShowText|pysssss`
- `StringFunction|pysssss`
- `VHS_VideoCombine`
- `CLIPVisionLoader`
- `LoadImage`
- `JanusModelLoader`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心

## 关键参数

- `seed` = `406450093112888`
- `steps` = `20`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **94%**（17/18）

**有卡**：`VAEDecode`、`CLIPVisionEncode`、`CLIPTextEncode`、`KSampler`、`TeaCache`、`WanImageToVideo`、`JanusImageUnderstanding`、`StringFunction|pysssss`、`VHS_VideoCombine`、`CLIPVisionLoader`、`LoadImage`、`JanusModelLoader`、`VAELoader`、`CLIPLoader`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、CLIPVisionEncode

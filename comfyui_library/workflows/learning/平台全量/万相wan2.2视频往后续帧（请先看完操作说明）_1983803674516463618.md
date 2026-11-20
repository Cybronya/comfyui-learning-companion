---
key: 平台全量/万相wan2.2视频往后续帧（请先看完操作说明）_1983803674516463618.json
name: 万相wan2.2视频往后续帧（请先看完操作说明）_1983803674516463618
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/万相wan2.2视频往后续帧（请先看完操作说明）_1983803674516463618.json
hash: 2dd5a6ab2a14cd92
coverage: 0.84
learned_at: 2026-11-14 01:32:25
nodes: [KSamplerAdvanced, ModelSamplingSD3, ModelSamplingSD3, UNETLoader, LoraLoaderModelOnly, KSamplerAdvanced, LoraLoaderModelOnly, UNETLoader, WanImageToVideo, VAELoader, VAEDecode, CLIPTextEncode, SimpleMath+, CLIPLoader, VHS_VideoInfo, VHS_VideoCombine, VHS_LoadVideo, easy showAnything, VHS_LoadVideo, CLIPTextEncode, Int, easy showAnything, VHS_VideoInfo, Fast Groups Bypasser (rgthree), Note]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 平台全量/万相wan2.2视频往后续帧（请先看完操作说明）_1983803674516463618.json

> 来源文件 `comfyui_library/workflows/平台全量/万相wan2.2视频往后续帧（请先看完操作说明）_1983803674516463618.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（25 个）：
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `WanImageToVideo`
- `VAELoader`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `SimpleMath+`
- `CLIPLoader`
- `VHS_VideoInfo`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `easy showAnything`
- `VHS_LoadVideo`
- `CLIPTextEncode` ★核心
- `Int`
- `easy showAnything`
- `VHS_VideoInfo`
- `Fast Groups Bypasser (rgthree)`
- `Note`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **84%**（21/25）

**有卡**：`KSamplerAdvanced`、`ModelSamplingSD3`、`UNETLoader`、`LoraLoaderModelOnly`、`WanImageToVideo`、`VAELoader`、`VAEDecode`、`CLIPTextEncode`、`SimpleMath+`、`CLIPLoader`、`VHS_VideoInfo`、`VHS_VideoCombine`、`VHS_LoadVideo`、`Int`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、UNETLoader、KSamplerAdvanced、Int

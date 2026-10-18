---
key: 视频生成/文生视频/Ltxvideo0.9.8文生视频_1947954012728492034.json
name: Ltxvideo0.9.8文生视频_1947954012728492034.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Ltxvideo0.9.8文生视频_1947954012728492034.json
hash: 1862368a5c86d986
coverage: 1
learned_at: 2026-10-15 22:43:32
nodes: [LTXVConditioning, KSamplerSelect, LTXVScheduler, SamplerCustom, VAEDecode, VHS_VideoCombine, CLIPLoader, CLIPTextEncode, CLIPTextEncode, EmptyLTXVLatentVideo, CheckpointLoaderSimple]
patterns: []
missing: []
parameters: {"checkpoint": "ltxv-13b-0.9.8-distilled-fp8.safetensors"}
---

# 视频生成/文生视频/Ltxvideo0.9.8文生视频_1947954012728492034.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1947954012728492034.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（11 个）：
- `LTXVConditioning`
- `KSamplerSelect` ★核心
- `LTXVScheduler`
- `SamplerCustom` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `EmptyLTXVLatentVideo`
- `CheckpointLoaderSimple` ★核心

## 关键参数

- `checkpoint` = `ltxv-13b-0.9.8-distilled-fp8.safetensors`

## 知识

覆盖率 **100%**（11/11）

**有卡**：`LTXVConditioning`、`KSamplerSelect`、`LTXVScheduler`、`SamplerCustom`、`VAEDecode`、`VHS_VideoCombine`、`CLIPLoader`、`CLIPTextEncode`、`EmptyLTXVLatentVideo`、`CheckpointLoaderSimple`

**用到的条目**：VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、KSamplerSelect、SamplerCustom、EmptyLTXVLatentVideo、LTXVConditioning

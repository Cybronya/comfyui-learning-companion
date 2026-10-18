---
key: 视频生成/文生视频/Ltxvideo0.9.6文生视频_1920699444994441217.json
name: Ltxvideo0.9.6文生视频_1920699444994441217.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Ltxvideo0.9.6文生视频_1920699444994441217.json
hash: c65117215c2f1b13
coverage: 1
learned_at: 2026-10-15 22:43:23
nodes: [CheckpointLoaderSimple, LTXVConditioning, KSamplerSelect, LTXVScheduler, SamplerCustom, VAEDecode, VHS_VideoCombine, CLIPLoader, CLIPTextEncode, CLIPTextEncode, EmptyLTXVLatentVideo]
patterns: []
missing: []
parameters: {"checkpoint": "ltxv-2b-0.9.6-dev-04-25-v1.safetensors"}
---

# 视频生成/文生视频/Ltxvideo0.9.6文生视频_1920699444994441217.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1920699444994441217.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（11 个）：
- `CheckpointLoaderSimple` ★核心
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

## 关键参数

- `checkpoint` = `ltxv-2b-0.9.6-dev-04-25-v1.safetensors`

## 知识

覆盖率 **100%**（11/11）

**有卡**：`CheckpointLoaderSimple`、`LTXVConditioning`、`KSamplerSelect`、`LTXVScheduler`、`SamplerCustom`、`VAEDecode`、`VHS_VideoCombine`、`CLIPLoader`、`CLIPTextEncode`、`EmptyLTXVLatentVideo`

**用到的条目**：VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、KSamplerSelect、SamplerCustom、EmptyLTXVLatentVideo、LTXVConditioning

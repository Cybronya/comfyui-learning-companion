---
key: 视频生成/文生视频/Wan2.2_文生视频_4步极速版_ComfyUI官方流_2044033029278011394.json
name: Wan2.2_文生视频_4步极速版_ComfyUI官方流_2044033029278011394
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2_文生视频_4步极速版_ComfyUI官方流_2044033029278011394.json
hash: f6a5b8fffeff66cd
coverage: 1
learned_at: 2026-10-15 22:47:13
nodes: [ModelSamplingSD3, ModelSamplingSD3, CLIPTextEncode, VAEDecode, CLIPTextEncode, UNETLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, VAELoader, CLIPLoader, EmptyHunyuanLatentVideo, KSamplerAdvanced, KSamplerAdvanced, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "increment"}
---

# 视频生成/文生视频/Wan2.2_文生视频_4步极速版_ComfyUI官方流_2044033029278011394.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2_文生视频_4步极速版_ComfyUI官方流_2044033029278011394.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（15 个）：
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `CLIPLoader`
- `EmptyHunyuanLatentVideo`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VHS_VideoCombine`

## 关键参数

- `seed` = `disable`
- `steps` = `increment`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（15/15）

**有卡**：`ModelSamplingSD3`、`CLIPTextEncode`、`VAEDecode`、`UNETLoader`、`LoraLoaderModelOnly`、`VAELoader`、`CLIPLoader`、`EmptyHunyuanLatentVideo`、`KSamplerAdvanced`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo

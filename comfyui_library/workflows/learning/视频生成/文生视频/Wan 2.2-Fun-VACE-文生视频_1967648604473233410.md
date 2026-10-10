---
key: 视频生成/文生视频/Wan 2.2-Fun-VACE-文生视频_1967648604473233410.json
name: Wan 2.2-Fun-VACE-文生视频_1967648604473233410
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan 2.2-Fun-VACE-文生视频_1967648604473233410.json
hash: ad66c76f07794208
coverage: 1
learned_at: 2026-10-10 23:06:11
nodes: [TrimVideoLatent, VAEDecode, CLIPTextEncode, ModelSamplingSD3, ModelSamplingSD3, CLIPLoader, VAELoader, KSamplerAdvanced, KSamplerAdvanced, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, UNETLoader, LoraLoaderModelOnly, INTConstant, INTConstant, INTConstant, CLIPTextEncode, LoraLoaderModelOnly, VHS_VideoCombine, WanVaceToVideo]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "sa_solver_pece", "seed": "enable", "steps": "randomize"}
---

# 视频生成/文生视频/Wan 2.2-Fun-VACE-文生视频_1967648604473233410.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan 2.2-Fun-VACE-文生视频_1967648604473233410.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（23 个）：
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPLoader`
- `VAELoader`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoCombine`
- `WanVaceToVideo`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `sa_solver_pece`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（23/23）

**有卡**：`TrimVideoLatent`、`VAEDecode`、`CLIPTextEncode`、`ModelSamplingSD3`、`CLIPLoader`、`VAELoader`、`KSamplerAdvanced`、`LoraLoaderModelOnly`、`UNETLoader`、`INTConstant`、`VHS_VideoCombine`、`WanVaceToVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、TrimVideoLatent

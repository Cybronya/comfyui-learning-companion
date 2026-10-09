---
key: 图片生成/文生图/wan2.2-ti2v-5B文生图_1951273402428502018.json
name: wan2.2-ti2v-5B文生图_1951273402428502018.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/wan2.2-ti2v-5B文生图_1951273402428502018.json
hash: 08c259aeda032401
coverage: 1
learned_at: 2026-10-07 23:04:11
nodes: [KSampler, CLIPLoader, VAELoader, ModelSamplingSD3, UNETLoader, CLIPTextEncode, VHS_VideoCombine, VAEDecode, SaveImage, Wan22ImageToVideoLatent, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 5, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 132741281615021, "steps": 30}
---

# 图片生成/文生图/wan2.2-ti2v-5B文生图_1951273402428502018.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1951273402428502018.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（11 个）：
- `KSampler` ★核心
- `CLIPLoader`
- `VAELoader`
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `SaveImage`
- `Wan22ImageToVideoLatent`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `132741281615021`
- `steps` = `30`
- `cfg` = `5`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（11/11）

**有卡**：`KSampler`、`CLIPLoader`、`VAELoader`、`ModelSamplingSD3`、`UNETLoader`、`CLIPTextEncode`、`VHS_VideoCombine`、`VAEDecode`、`SaveImage`、`Wan22ImageToVideoLatent`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、Wan22ImageToVideoLatent、SaveImage

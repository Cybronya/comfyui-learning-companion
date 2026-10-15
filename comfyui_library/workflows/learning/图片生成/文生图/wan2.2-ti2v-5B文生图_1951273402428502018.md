---
key: 图片生成/文生图/wan2.2-ti2v-5B文生图_1951273402428502018.json
name: wan2.2-ti2v-5B文生图_1951273402428502018
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/wan2.2-ti2v-5B文生图_1951273402428502018.json
hash: 08c259aeda032401
coverage: 1
learned_at: 2026-10-10 20:59:27
nodes: [KSampler, CLIPLoader, VAELoader, ModelSamplingSD3, UNETLoader, CLIPTextEncode, VHS_VideoCombine, VAEDecode, SaveImage, Wan22ImageToVideoLatent, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 5, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 132741281615021, "steps": 30}
---

# 图片生成/文生图/wan2.2-ti2v-5B文生图_1951273402428502018.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/wan2.2-ti2v-5B文生图_1951273402428502018.json`

## 结构

**节点**（11 个）：
- `KSampler`
- `CLIPLoader`
- `VAELoader`
- `ModelSamplingSD3`
- `UNETLoader`
- `CLIPTextEncode`
- `VHS_VideoCombine`
- `VAEDecode`
- `SaveImage`
- `Wan22ImageToVideoLatent`
- `CLIPTextEncode`

## 关键参数

- `cfg` = `5`
- `denoise` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `seed` = `132741281615021`
- `steps` = `30`

## 知识

覆盖率 **100%**（11/11）

**有卡**：`KSampler`、`CLIPLoader`、`VAELoader`、`ModelSamplingSD3`、`UNETLoader`、`CLIPTextEncode`、`VHS_VideoCombine`、`VAEDecode`、`SaveImage`、`Wan22ImageToVideoLatent`

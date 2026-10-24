---
key: 图片生成/图生图/wan2.2-ti2v-5B图生图_1952197317170548738.json
name: wan2.2-ti2v-5B图生图_1952197317170548738
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/wan2.2-ti2v-5B图生图_1952197317170548738.json
hash: 0e367f411457eeb5
coverage: 1
learned_at: 2026-10-23 11:45:59
nodes: [KSampler, UNETLoader, CLIPLoader, VAELoader, Wan22ImageToVideoLatent, VHS_VideoCombine, VAEDecode, SaveImage, CLIPTextEncode, CLIPTextEncode, ModelSamplingSD3, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 5, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 240590134222845, "steps": 30}
---

# 图片生成/图生图/wan2.2-ti2v-5B图生图_1952197317170548738.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/wan2.2-ti2v-5B图生图_1952197317170548738.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（12 个）：
- `KSampler` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `Wan22ImageToVideoLatent`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `SaveImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `LoadImage`

## 关键参数

- `seed` = `240590134222845`
- `steps` = `30`
- `cfg` = `5`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（12/12）

**有卡**：`KSampler`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`Wan22ImageToVideoLatent`、`VHS_VideoCombine`、`VAEDecode`、`SaveImage`、`CLIPTextEncode`、`ModelSamplingSD3`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、Wan22ImageToVideoLatent

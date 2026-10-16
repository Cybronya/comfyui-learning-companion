---
key: 视频生成/图生视频/wan2.2-ti2v-5B文生视频摆尾猫_1952539360614920193.json
name: wan2.2-ti2v-5B文生视频摆尾猫_1952539360614920193.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1952539360614920193.json
hash: 4898b5c4f94b70bd
coverage: 1
learned_at: 2026-10-15 22:31:01
nodes: [UNETLoader, VAEDecode, KSampler, ModelSamplingSD3, VAELoader, LoadImage, Wan22ImageToVideoLatent, VHS_VideoCombine, CLIPTextEncode, CLIPTextEncode, LoraLoaderModelOnly, CLIPLoader]
patterns: []
missing: []
parameters: {"cfg": 5, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 380871567989921, "steps": 30}
---

# 视频生成/图生视频/wan2.2-ti2v-5B文生视频摆尾猫_1952539360614920193.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1952539360614920193.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（12 个）：
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `ModelSamplingSD3`
- `VAELoader`
- `LoadImage`
- `Wan22ImageToVideoLatent`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`

## 关键参数

- `seed` = `380871567989921`
- `steps` = `30`
- `cfg` = `5`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（12/12）

**有卡**：`UNETLoader`、`VAEDecode`、`KSampler`、`ModelSamplingSD3`、`VAELoader`、`LoadImage`、`Wan22ImageToVideoLatent`、`VHS_VideoCombine`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`CLIPLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

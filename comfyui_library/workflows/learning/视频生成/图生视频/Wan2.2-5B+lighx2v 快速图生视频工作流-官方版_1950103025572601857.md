---
key: 视频生成/图生视频/Wan2.2-5B+lighx2v 快速图生视频工作流-官方版_1950103025572601857.json
name: Wan2.2-5B+lighx2v 快速图生视频工作流-官方版_1950103025572601857.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1950103025572601857.json
hash: 9fcd5d2373dc6d58
coverage: 1
learned_at: 2026-10-15 22:30:53
nodes: [CLIPLoader, VAELoader, UNETLoader, ModelSamplingSD3, PathchSageAttentionKJ, LoraLoaderModelOnly, CLIPTextEncode, Wan22ImageToVideoLatent, CLIPTextEncode, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, KSampler, VAEDecode, JWInteger, JWInteger, JWInteger, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 582996876915255, "steps": 10}
---

# 视频生成/图生视频/Wan2.2-5B+lighx2v 快速图生视频工作流-官方版_1950103025572601857.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1950103025572601857.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（17 个）：
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `Wan22ImageToVideoLatent`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `582996876915255`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（17/17）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`Wan22ImageToVideoLatent`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`KSampler`、`VAEDecode`、`JWInteger`、`VHS_VideoCombine`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

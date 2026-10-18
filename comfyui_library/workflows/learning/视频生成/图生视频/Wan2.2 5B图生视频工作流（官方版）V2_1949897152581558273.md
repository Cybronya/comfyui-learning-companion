---
key: 视频生成/图生视频/Wan2.2 5B图生视频工作流（官方版）V2_1949897152581558273.json
name: Wan2.2 5B图生视频工作流（官方版）V2_1949897152581558273.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 5B图生视频工作流（官方版）V2_1949897152581558273.json
hash: 07ff34e670cdcb4b
coverage: 0.941176
learned_at: 2026-10-15 22:30:50
nodes: [CLIPTextEncode, Note, Wan22ImageToVideoLatent, KSampler, VAEDecode, CLIPTextEncode, ModelSamplingSD3, PathchSageAttentionKJ, UNETLoader, CLIPLoader, VAELoader, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, JWInteger, JWInteger, JWInteger, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 5, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 496380081541396, "steps": 30}
---

# 视频生成/图生视频/Wan2.2 5B图生视频工作流（官方版）V2_1949897152581558273.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1949897152581558273.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（17 个）：
- `CLIPTextEncode` ★核心
- `Note`
- `Wan22ImageToVideoLatent`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `496380081541396`
- `steps` = `30`
- `cfg` = `5`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **94%**（16/17）

**有卡**：`CLIPTextEncode`、`Wan22ImageToVideoLatent`、`KSampler`、`VAEDecode`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`JWInteger`、`VHS_VideoCombine`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、Wan22ImageToVideoLatent

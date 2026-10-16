---
key: 视频生成/图生视频/WAN 2.2 XX_Palingenesis  首尾帧图像转视频工作流【结构清晰版】_1974340627162861570.json
name: WAN 2.2 XX_Palingenesis  首尾帧图像转视频工作流【结构清晰版】_1974340627162861570.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1974340627162861570.json
hash: d9bc6461104beed7
coverage: 0.875
learned_at: 2026-10-15 22:32:05
nodes: [CLIPTextEncode, VAEDecode, PathchSageAttentionKJ, TorchCompileModel, VAELoader, LoadImage, Int, Int, Int, WanFirstLastFrameToVideo, VHS_VideoCombine, Int, Note, SaveImage, RIFE VFI, Note, UNETLoader, UNETLoader, ModelSamplingSD3, ModelSamplingSD3, PathchSageAttentionKJ, WanVideoNAG, CLIPLoader, WanVideoNAG, LoraLoaderModelOnly, LoraLoaderModelOnly, TorchCompileModel, LoraLoaderModelOnly, Note, LoadImage, CLIPTextEncode, ImageResizeKJv2, ImageResizeKJv2, Fast Groups Muter (rgthree), VHS_VideoCombine, KSamplerAdvanced, Fast Groups Muter (rgthree), KSamplerAdvanced, PurgeVRAM_UTK, PurgeVRAM_UTK]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/WAN 2.2 XX_Palingenesis  首尾帧图像转视频工作流【结构清晰版】_1974340627162861570.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1974340627162861570.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（40 个）：
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `PathchSageAttentionKJ`
- `TorchCompileModel`
- `VAELoader`
- `LoadImage`
- `Int`
- `Int`
- `Int`
- `WanFirstLastFrameToVideo`
- `VHS_VideoCombine`
- `Int`
- `Note`
- `SaveImage`
- `RIFE VFI`
- `Note`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `WanVideoNAG`
- `CLIPLoader`
- `WanVideoNAG`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `TorchCompileModel`
- `LoraLoaderModelOnly` ★核心
- `Note`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `Fast Groups Muter (rgthree)`
- `VHS_VideoCombine`
- `KSamplerAdvanced` ★核心
- `Fast Groups Muter (rgthree)`
- `KSamplerAdvanced` ★核心
- `PurgeVRAM_UTK`
- `PurgeVRAM_UTK`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **88%**（35/40）

**有卡**：`CLIPTextEncode`、`VAEDecode`、`PathchSageAttentionKJ`、`TorchCompileModel`、`VAELoader`、`LoadImage`、`Int`、`WanFirstLastFrameToVideo`、`VHS_VideoCombine`、`SaveImage`、`RIFE VFI`、`UNETLoader`、`ModelSamplingSD3`、`WanVideoNAG`、`CLIPLoader`、`LoraLoaderModelOnly`、`ImageResizeKJv2`、`KSamplerAdvanced`、`PurgeVRAM_UTK`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced

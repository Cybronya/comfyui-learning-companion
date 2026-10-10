---
key: 视频生成/文生视频/Wan2.2官网14B图生视频&文生视频&5B文or图生视频_1950378020252073986.json
name: Wan2.2官网14B图生视频&文生视频&5B文or图生视频_1950378020252073986
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2官网14B图生视频&文生视频&5B文or图生视频_1950378020252073986.json
hash: 57dbe50f535ab862
coverage: 0.926829
learned_at: 2026-10-10 23:07:27
nodes: [CLIPLoader, KSamplerAdvanced, KSamplerAdvanced, CLIPTextEncode, VAELoader, ModelSamplingSD3, ModelSamplingSD3, MarkdownNote, CLIPTextEncode, LoadImage, UNETLoader, UNETLoader, WanImageToVideo, VAEDecode, VHS_VideoCombine, CLIPLoader, CLIPTextEncode, VAELoader, ModelSamplingSD3, ModelSamplingSD3, KSamplerAdvanced, KSamplerAdvanced, UNETLoader, UNETLoader, CLIPTextEncode, MarkdownNote, VAEDecode, VHS_VideoCombine, EmptyHunyuanLatentVideo, UNETLoader, CLIPLoader, VAELoader, Wan22ImageToVideoLatent, LoadImage, CLIPTextEncode, MarkdownNote, CLIPTextEncode, KSampler, ModelSamplingSD3, VAEDecode, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 5, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 283713045682736, "steps": 20}
---

# 视频生成/文生视频/Wan2.2官网14B图生视频&文生视频&5B文or图生视频_1950378020252073986.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2官网14B图生视频&文生视频&5B文or图生视频_1950378020252073986.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（41 个）：
- `CLIPLoader`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `WanImageToVideo`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `EmptyHunyuanLatentVideo`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `Wan22ImageToVideoLatent`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `VHS_VideoCombine`

## 关键参数

- `seed` = `283713045682736`
- `steps` = `20`
- `cfg` = `5`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **93%**（38/41）

**有卡**：`CLIPLoader`、`KSamplerAdvanced`、`CLIPTextEncode`、`VAELoader`、`ModelSamplingSD3`、`LoadImage`、`UNETLoader`、`WanImageToVideo`、`VAEDecode`、`VHS_VideoCombine`、`EmptyHunyuanLatentVideo`、`Wan22ImageToVideoLatent`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced

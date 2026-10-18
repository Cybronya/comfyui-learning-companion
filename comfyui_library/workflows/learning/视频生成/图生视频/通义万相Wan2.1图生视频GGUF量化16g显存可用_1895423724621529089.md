---
key: 视频生成/图生视频/通义万相Wan2.1图生视频GGUF量化16g显存可用_1895423724621529089.json
name: 通义万相Wan2.1图生视频GGUF量化16g显存可用_1895423724621529089.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/通义万相Wan2.1图生视频GGUF量化16g显存可用_1895423724621529089.json
hash: c74d4947f6815eed
coverage: 1
learned_at: 2026-10-15 22:29:17
nodes: [VAEDecode, CLIPVisionEncode, CLIPLoader, CLIPTextEncode, KSampler, UnetLoaderGGUF, LoadImage, CLIPTextEncode, WanImageToVideo, CLIPVisionLoader, VAELoader, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 1080570604468223, "steps": 20}
---

# 视频生成/图生视频/通义万相Wan2.1图生视频GGUF量化16g显存可用_1895423724621529089.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1895423724621529089.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（12 个）：
- `VAEDecode` ★核心
- `CLIPVisionEncode`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `UnetLoaderGGUF` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心
- `WanImageToVideo`
- `CLIPVisionLoader`
- `VAELoader`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `1080570604468223`
- `steps` = `20`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（12/12）

**有卡**：`VAEDecode`、`CLIPVisionEncode`、`CLIPLoader`、`CLIPTextEncode`、`KSampler`、`UnetLoaderGGUF`、`LoadImage`、`WanImageToVideo`、`CLIPVisionLoader`、`VAELoader`、`VHS_VideoCombine`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、CLIPVisionEncode、CLIPVisionLoader

---
key: 视频生成/图生视频/Wan2.2-Lightx2v latest_1988041568177295362.json
name: Wan2.2-Lightx2v latest_1988041568177295362.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1988041568177295362.json
hash: 335af63bdf2af277
coverage: 1
learned_at: 2026-10-15 22:33:01
nodes: [CLIPLoader, VAELoader, UNETLoader, UNETLoader, SaveVideo, LoadImage, CLIPTextEncode, workflow>LORA1, workflow>LORA2, KSamplerAdvanced, KSamplerAdvanced, WanImageToVideo, CLIPTextEncode, VAEDecode, CreateVideo]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2-Lightx2v latest_1988041568177295362.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1988041568177295362.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（15 个）：
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `SaveVideo`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `workflow>LORA1`
- `workflow>LORA2`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `WanImageToVideo`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `CreateVideo`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（15/15）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`SaveVideo`、`LoadImage`、`CLIPTextEncode`、`workflow>LORA1`、`workflow>LORA2`、`KSamplerAdvanced`、`WanImageToVideo`、`VAEDecode`、`CreateVideo`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、workflow>LORA1

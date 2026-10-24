---
key: 图片生成/图生图/Flux Redux - Official Flux Tools by BFL - Beginner_1864884851341217793.json
name: Flux Redux - Official Flux Tools by BFL - Beginner_1864884851341217793
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux Redux - Official Flux Tools by BFL - Beginner_1864884851341217793.json
hash: 9450db8ab706acda
coverage: 0.933333
learned_at: 2026-10-23 10:58:02
nodes: [UNETLoader, DualCLIPLoader, VAELoader, CLIPTextEncodeFlux, CLIPVisionLoader, CLIPTextEncodeFlux, LoadImage, StyleModelLoader, StyleModelApply, CLIPVisionEncode, KSampler, EmptyLatentImage, SaveImage, PreviewImage, VAEDecode]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "normal", "seed": 675983976624206, "steps": 25, "width": 1024}
---

# 图片生成/图生图/Flux Redux - Official Flux Tools by BFL - Beginner_1864884851341217793.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux Redux - Official Flux Tools by BFL - Beginner_1864884851341217793.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（15 个）：
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `CLIPTextEncodeFlux` ★核心
- `CLIPVisionLoader`
- `CLIPTextEncodeFlux` ★核心
- `LoadImage`
- `StyleModelLoader`
- `StyleModelApply`
- `CLIPVisionEncode`
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `SaveImage`
- `PreviewImage`
- `VAEDecode` ★核心

## 关键参数

- `seed` = `675983976624206`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **93%**（14/15）

**有卡**：`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`CLIPTextEncodeFlux`、`CLIPVisionLoader`、`LoadImage`、`StyleModelLoader`、`StyleModelApply`、`CLIPVisionEncode`、`KSampler`、`EmptyLatentImage`、`SaveImage`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、EmptyLatentImage、LoadImage、CLIPTextEncodeFlux、CLIPVisionEncode

---
key: 图片生成/图生图/Kandinsky 5.0 图生视频_1999008065406033921.json
name: Kandinsky 5.0 图生视频_1999008065406033921
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Kandinsky 5.0 图生视频_1999008065406033921.json
hash: a1ef69a7fc97f33b
coverage: 1
learned_at: 2026-10-23 11:04:07
nodes: [UNETLoader, VAELoader, DualCLIPLoader, CLIPTextEncode, CLIPTextEncode, ImageScale, ReplaceVideoLatentFrames, NormalizeVideoLatentStart, KSampler, Kandinsky5ImageToVideo, VAEDecode, ModelSamplingSD3, CreateVideo, SaveVideo, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 5, "denoise": 1, "sampler_name": "euler_ancestral", "scheduler": "beta", "seed": 913529313586024, "steps": 50}
---

# 图片生成/图生图/Kandinsky 5.0 图生视频_1999008065406033921.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Kandinsky 5.0 图生视频_1999008065406033921.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（15 个）：
- `UNETLoader` ★核心
- `VAELoader`
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ImageScale`
- `ReplaceVideoLatentFrames`
- `NormalizeVideoLatentStart`
- `KSampler` ★核心
- `Kandinsky5ImageToVideo`
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `CreateVideo`
- `SaveVideo`
- `LoadImage`

## 关键参数

- `seed` = `913529313586024`
- `steps` = `50`
- `cfg` = `5`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **100%**（15/15）

**有卡**：`UNETLoader`、`VAELoader`、`DualCLIPLoader`、`CLIPTextEncode`、`ImageScale`、`ReplaceVideoLatentFrames`、`NormalizeVideoLatentStart`、`KSampler`、`Kandinsky5ImageToVideo`、`VAEDecode`、`ModelSamplingSD3`、`CreateVideo`、`SaveVideo`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、LoadImage、UNETLoader、ReplaceVideoLatentFrames、NormalizeVideoLatentStart

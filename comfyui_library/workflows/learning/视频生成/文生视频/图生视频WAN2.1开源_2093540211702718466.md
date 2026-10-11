---
key: 视频生成/文生视频/图生视频WAN2.1开源_2093540211702718466.json
name: 图生视频WAN2.1开源_2093540211702718466
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/图生视频WAN2.1开源_2093540211702718466.json
hash: de9a75954aa071e9
coverage: 1
learned_at: 2026-10-11 21:30:37
nodes: [CLIPVisionLoader, UNETLoader, CLIPTextEncode, VAELoader, VAEDecode, KSampler, CLIPVisionEncode, LoadImage, WanImageToVideo, CLIPTextEncode, CLIPLoader, SaveAnimatedWEBP, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 930396267856037, "steps": 20}
---

# 视频生成/文生视频/图生视频WAN2.1开源_2093540211702718466.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/图生视频WAN2.1开源_2093540211702718466.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（13 个）：
- `CLIPVisionLoader`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `CLIPVisionEncode`
- `LoadImage`
- `WanImageToVideo`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `SaveAnimatedWEBP`
- `SaveImage`

## 关键参数

- `seed` = `930396267856037`
- `steps` = `20`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（13/13）

**有卡**：`CLIPVisionLoader`、`UNETLoader`、`CLIPTextEncode`、`VAELoader`、`VAEDecode`、`KSampler`、`CLIPVisionEncode`、`LoadImage`、`WanImageToVideo`、`CLIPLoader`、`SaveAnimatedWEBP`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、CLIPVisionEncode

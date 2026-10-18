---
key: 视频生成/图生视频/🚀FSampler采样器实测：Wan2.2生成视频时间缩短36.63%！_1978720948956319746.json
name: 🚀FSampler采样器实测：Wan2.2生成视频时间缩短36.63%！_1978720948956319746.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/🚀FSampler采样器实测：Wan2.2生成视频时间缩短36.63%！_1978720948956319746.json
hash: f4106cb194d9f2c2
coverage: 1
learned_at: 2026-10-15 22:32:20
nodes: [CLIPLoader, CLIPTextEncode, VAELoader, UNETLoader, UNETLoader, CreateVideo, VAEDecode, SaveVideo, ModelSamplingSD3, ModelSamplingSD3, WanImageToVideo, LoadImage, CLIPTextEncode, FSamplerAdvanced, FSamplerAdvanced, Label (rgthree)]
patterns: []
missing: []
---

# 视频生成/图生视频/🚀FSampler采样器实测：Wan2.2生成视频时间缩短36.63%！_1978720948956319746.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1978720948956319746.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（16 个）：
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CreateVideo`
- `VAEDecode` ★核心
- `SaveVideo`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `WanImageToVideo`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `FSamplerAdvanced` ★核心
- `FSamplerAdvanced` ★核心
- `Label (rgthree)`

## 知识

覆盖率 **100%**（16/16）

**有卡**：`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`UNETLoader`、`CreateVideo`、`VAEDecode`、`SaveVideo`、`ModelSamplingSD3`、`WanImageToVideo`、`LoadImage`、`FSamplerAdvanced`、`Label (rgthree)`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、FSamplerAdvanced、SaveVideo

---
key: 视频生成/图生视频/【阡陌】wan2.2+light4步加速lora图生视频工作流_1967772488862150657.json
name: 【阡陌】wan2.2+light4步加速lora图生视频工作流_1967772488862150657.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/【阡陌】wan2.2+light4步加速lora图生视频工作流_1967772488862150657.json
hash: e9074b6263ca6514
coverage: 1
learned_at: 2026-10-15 22:31:42
nodes: [VAEDecode, ModelSamplingSD3, ModelSamplingSD3, KSamplerAdvanced, CreateVideo, SaveVideo, CLIPLoader, KSamplerAdvanced, CLIPTextEncode, VAELoader, LoadImage, UNETLoader, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, WanImageToVideo, CLIPTextEncode, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/【阡陌】wan2.2+light4步加速lora图生视频工作流_1967772488862150657.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1967772488862150657.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（18 个）：
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `CreateVideo`
- `SaveVideo`
- `CLIPLoader`
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `LoadImage`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `WanImageToVideo`
- `CLIPTextEncode` ★核心
- `LoadImage`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（18/18）

**有卡**：`VAEDecode`、`ModelSamplingSD3`、`KSamplerAdvanced`、`CreateVideo`、`SaveVideo`、`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`LoadImage`、`UNETLoader`、`LoraLoaderModelOnly`、`WanImageToVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced

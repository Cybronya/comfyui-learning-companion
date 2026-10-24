---
key: 图片生成/图生图/超强FLUX洗图神器FLUX.1_1906179257314234370.json
name: 超强FLUX洗图神器FLUX.1_1906179257314234370
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/超强FLUX洗图神器FLUX.1_1906179257314234370.json
hash: bcc7a5fc1e8e00a6
coverage: 0.944444
learned_at: 2026-10-23 13:29:00
nodes: [SamplerCustomAdvanced, VAEDecode, RandomNoise, BasicGuider, CLIPTextEncode, VAEEncode, Joy_caption_load, VAELoader, KSamplerSelect, ImageResize+, BasicScheduler, CR Latent Batch Size, PreviewImage, LoadImage, UNETLoader, DualCLIPLoader, Joy_caption, SaveImage]
patterns: []
missing: []
---

# 图片生成/图生图/超强FLUX洗图神器FLUX.1_1906179257314234370.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/超强FLUX洗图神器FLUX.1_1906179257314234370.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `RandomNoise`
- `BasicGuider`
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `Joy_caption_load`
- `VAELoader`
- `KSamplerSelect` ★核心
- `ImageResize+`
- `BasicScheduler`
- `CR Latent Batch Size`
- `PreviewImage`
- `LoadImage`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `Joy_caption`
- `SaveImage`

## 知识

覆盖率 **94%**（17/18）

**有卡**：`SamplerCustomAdvanced`、`VAEDecode`、`RandomNoise`、`BasicGuider`、`CLIPTextEncode`、`VAEEncode`、`Joy_caption_load`、`VAELoader`、`KSamplerSelect`、`ImageResize+`、`BasicScheduler`、`CR Latent Batch Size`、`LoadImage`、`UNETLoader`、`DualCLIPLoader`、`Joy_caption`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced、VAEEncode

---
key: PixelWave FLUX.1-dev 03 文生图丨自修室_1898750459816169473.json
name: PixelWave FLUX.1-dev 03 文生图丨自修室_1898750459816169473
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/PixelWave FLUX.1-dev 03 文生图丨自修室_1898750459816169473.json
hash: 92b14b71543b9f6d
coverage: 0.882353
learned_at: 2026-10-10 20:58:49
nodes: [PreviewImage, VAELoader, KSamplerSelect, AdvancedLyingSigmaSampler, DisplayText_Zho, SaveImage, VAEDecode, RH_Prompter, EmptyLatentImage, UNETLoader, DualCLIPLoader, BasicScheduler, CLIPTextEncode, CLIPTextEncode, SamplerCustom, SeargePromptText, Note]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1152, "width": 1920}
---

# PixelWave FLUX.1-dev 03 文生图丨自修室_1898750459816169473.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/PixelWave FLUX.1-dev 03 文生图丨自修室_1898750459816169473.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（17 个）：
- `PreviewImage`
- `VAELoader`
- `KSamplerSelect` ★核心
- `AdvancedLyingSigmaSampler` ★核心
- `DisplayText_Zho`
- `SaveImage`
- `VAEDecode` ★核心
- `RH_Prompter`
- `EmptyLatentImage` ★核心
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `BasicScheduler`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SamplerCustom` ★核心
- `SeargePromptText`
- `Note`

## 关键参数

- `width` = `1920`
- `height` = `1152`
- `batch_size` = `1`

## 知识

覆盖率 **88%**（15/17）

**有卡**：`VAELoader`、`KSamplerSelect`、`AdvancedLyingSigmaSampler`、`DisplayText_Zho`、`SaveImage`、`VAEDecode`、`RH_Prompter`、`EmptyLatentImage`、`UNETLoader`、`DualCLIPLoader`、`BasicScheduler`、`CLIPTextEncode`、`SamplerCustom`、`SeargePromptText`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、EmptyLatentImage、UNETLoader、KSamplerSelect、SamplerCustom、AdvancedLyingSigmaSampler

---
key: 图片生成/文生图/Z-Image+seedvr2.5.1放大电影级文生图+画质色彩增强版_1996033169059201026.json
name: Z-Image+seedvr2.5.1放大电影级文生图+画质色彩增强版_1996033169059201026
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-Image+seedvr2.5.1放大电影级文生图+画质色彩增强版_1996033169059201026.json
hash: 2325edcf5d63dda4
coverage: 0.882353
learned_at: 2026-10-19 21:32:50
nodes: [KSampler, SeedVR2LoadVAEModel, ConditioningZeroOut, SaveImage, SeedVR2LoadDiTModel, PreviewImage, ImpactInt, CR SDXL Aspect Ratio, CLIPTextEncode, UNETLoader, CLIPLoader, LoraLoaderModelOnly, SeedVR2VideoUpscaler, LayerUtility: PurgeVRAM V2, VAEDecode, VAELoader, Note]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 283459580872173, "steps": 10}
---

# 图片生成/文生图/Z-Image+seedvr2.5.1放大电影级文生图+画质色彩增强版_1996033169059201026.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-Image+seedvr2.5.1放大电影级文生图+画质色彩增强版_1996033169059201026.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `KSampler` ★核心
- `SeedVR2LoadVAEModel`
- `ConditioningZeroOut`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `PreviewImage`
- `ImpactInt`
- `CR SDXL Aspect Ratio`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `SeedVR2VideoUpscaler`
- `LayerUtility: PurgeVRAM V2`
- `VAEDecode` ★核心
- `VAELoader`
- `Note`

## 关键参数

- `seed` = `283459580872173`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（15/17）

**有卡**：`KSampler`、`SeedVR2LoadVAEModel`、`ConditioningZeroOut`、`SaveImage`、`SeedVR2LoadDiTModel`、`ImpactInt`、`CR SDXL Aspect Ratio`、`CLIPTextEncode`、`UNETLoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`SeedVR2VideoUpscaler`、`LayerUtility: PurgeVRAM V2`、`VAEDecode`、`VAELoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

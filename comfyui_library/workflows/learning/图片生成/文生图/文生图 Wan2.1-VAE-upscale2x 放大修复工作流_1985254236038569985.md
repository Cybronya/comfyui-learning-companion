---
key: 图片生成/文生图/文生图 Wan2.1-VAE-upscale2x 放大修复工作流_1985254236038569985.json
name: 文生图 Wan2.1-VAE-upscale2x 放大修复工作流_1985254236038569985
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/文生图 Wan2.1-VAE-upscale2x 放大修复工作流_1985254236038569985.json
hash: 51634ab71883b6df
coverage: 0.789474
learned_at: 2026-10-15 22:28:46
nodes: [NunchakuQwenImageDiTLoader, VAEUtils_VAEDecodeTiled, LayerFilter: HDREffects, StringFunction|pysssss, Image Comparer (rgthree), PreviewImage, PreviewImage, VAEUtils_CustomVAELoader, ModelSamplingAuraFlow, VAELoader, ConditioningZeroOut, CLIPLoader, CLIPTextEncode, CLIPTextEncode, KSampler (Efficient), EmptyLatentImage, Note, LayerFilter: HDREffects, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 504, "sampler_name": "euler", "scheduler": "simple", "seed": 438647852229906, "steps": 8, "width": 1200}
---

# 图片生成/文生图/文生图 Wan2.1-VAE-upscale2x 放大修复工作流_1985254236038569985.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/文生图 Wan2.1-VAE-upscale2x 放大修复工作流_1985254236038569985.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（19 个）：
- `NunchakuQwenImageDiTLoader`
- `VAEUtils_VAEDecodeTiled` ★核心
- `LayerFilter: HDREffects`
- `StringFunction|pysssss`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `PreviewImage`
- `VAEUtils_CustomVAELoader`
- `ModelSamplingAuraFlow`
- `VAELoader`
- `ConditioningZeroOut`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSampler (Efficient)` ★核心
- `EmptyLatentImage` ★核心
- `Note`
- `LayerFilter: HDREffects`
- `SaveImage`

## 关键参数

- `seed` = `438647852229906`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1200`
- `height` = `504`
- `batch_size` = `1`

## 知识

覆盖率 **79%**（15/19）

**有卡**：`NunchakuQwenImageDiTLoader`、`VAEUtils_VAEDecodeTiled`、`LayerFilter: HDREffects`、`StringFunction|pysssss`、`VAEUtils_CustomVAELoader`、`ModelSamplingAuraFlow`、`VAELoader`、`ConditioningZeroOut`、`CLIPLoader`、`CLIPTextEncode`、`KSampler (Efficient)`、`EmptyLatentImage`、`SaveImage`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、KSampler (Efficient)、VAEUtils_CustomVAELoader、VAEUtils_VAEDecodeTiled

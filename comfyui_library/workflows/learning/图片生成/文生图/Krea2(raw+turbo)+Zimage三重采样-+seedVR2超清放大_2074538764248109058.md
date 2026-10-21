---
key: 图片生成/文生图/Krea2(raw+turbo)+Zimage三重采样-+seedVR2超清放大_2074538764248109058.json
name: Krea2(raw+turbo)+Zimage三重采样-+seedVR2超清放大_2074538764248109058
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Krea2(raw+turbo)+Zimage三重采样-+seedVR2超清放大_2074538764248109058.json
hash: f5117df598c8fccb
coverage: 0.969697
learned_at: 2026-10-20 00:19:22
nodes: [UNETLoader, ModelSamplingAuraFlow, ModelSamplingAuraFlow, VAELoader, CLIPLoader, CLIPTextEncode, UNETLoader, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, Note, easy int, TTResolutionSelector, EmptyLatentImage, UNETLoader, VAELoader, CLIPLoaderGGUF, ConditioningZeroOut, CLIPTextEncode, CLIPTextEncode, ConditioningZeroOut, VAEEncodeTiled, KSampler, SeedVR2VideoUpscaler, VAEDecodeTiled, SaveImage, PurgeVRAM_UTK, CR Text, CR Text, CR Text, KSamplerAdvanced, KSamplerAdvanced, VAEDecodeTiled, DisTorchPurgeVRAMV2]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"batch_size": 1, "cfg": 12, "denoise": "simple", "height": 1024, "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "randomize", "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 图片生成/文生图/Krea2(raw+turbo)+Zimage三重采样-+seedVR2超清放大_2074538764248109058.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Krea2(raw+turbo)+Zimage三重采样-+seedVR2超清放大_2074538764248109058.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（33 个）：
- `UNETLoader` ★核心
- `ModelSamplingAuraFlow`
- `ModelSamplingAuraFlow`
- `VAELoader`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `Note`
- `easy int`
- `TTResolutionSelector`
- `EmptyLatentImage` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoaderGGUF`
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `VAEEncodeTiled` ★核心
- `KSampler` ★核心
- `SeedVR2VideoUpscaler`
- `VAEDecodeTiled` ★核心
- `SaveImage`
- `PurgeVRAM_UTK`
- `CR Text`
- `CR Text`
- `CR Text`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecodeTiled` ★核心
- `DisTorchPurgeVRAMV2`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `12`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **97%**（32/33）

**有卡**：`UNETLoader`、`ModelSamplingAuraFlow`、`VAELoader`、`CLIPLoader`、`CLIPTextEncode`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`easy int`、`TTResolutionSelector`、`EmptyLatentImage`、`CLIPLoaderGGUF`、`ConditioningZeroOut`、`VAEEncodeTiled`、`KSampler`、`SeedVR2VideoUpscaler`、`VAEDecodeTiled`、`SaveImage`、`PurgeVRAM_UTK`、`CR Text`、`KSamplerAdvanced`、`DisTorchPurgeVRAMV2`

**用到的条目**：KSampler、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、UNETLoader、KSamplerAdvanced

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

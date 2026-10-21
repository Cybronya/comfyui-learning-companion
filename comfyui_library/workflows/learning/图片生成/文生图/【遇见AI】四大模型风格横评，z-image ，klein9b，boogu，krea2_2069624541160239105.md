---
key: 图片生成/文生图/【遇见AI】四大模型风格横评，z-image ，klein9b，boogu，krea2_2069624541160239105.json
name: 【遇见AI】四大模型风格横评，z-image ，klein9b，boogu，krea2_2069624541160239105
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/【遇见AI】四大模型风格横评，z-image ，klein9b，boogu，krea2_2069624541160239105.json
hash: dbd3671037bc1f8b
coverage: 0.98
learned_at: 2026-10-19 23:42:55
nodes: [ConditioningZeroOut, EmptyLatentImage, KSampler, CLIPTextEncode, SaveImage, ImageConcanate, KSampler, ConditioningZeroOut, SaveImage, CLIPTextEncode, EmptyLatentImage, RandomNoise, BasicGuider, KSamplerSelect, SamplerCustomAdvanced, CLIPTextEncode, Flux2Scheduler, EmptyFlux2LatentImage, FluxGuidance, ConditioningZeroOut, KSampler, CLIPTextEncode, EmptyLatentImage, SaveImage, VAEDecode, VAEDecode, VAEDecode, VAEDecode, Seed_, CR Aspect Ratio, ImageConcanate, ImageConcanate, SaveImage, MarkdownNote, LoadImage, LoadImage, UNETLoader, CLIPLoader, VAELoader, UNETLoader, CLIPLoader, VAELoader, UNETLoader, CLIPLoader, VAELoader, UNETLoader, CLIPLoader, VAELoader, SaveImage, easy promptLine]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "lcm", "scheduler": "sgm_uniform", "seed": 117533082977772, "steps": 4, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/【遇见AI】四大模型风格横评，z-image ，klein9b，boogu，krea2_2069624541160239105.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/【遇见AI】四大模型风格横评，z-image ，klein9b，boogu，krea2_2069624541160239105.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（50 个）：
- `ConditioningZeroOut`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `SaveImage`
- `ImageConcanate`
- `KSampler` ★核心
- `ConditioningZeroOut`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `RandomNoise`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `Flux2Scheduler`
- `EmptyFlux2LatentImage`
- `FluxGuidance`
- `ConditioningZeroOut`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `Seed_`
- `CR Aspect Ratio`
- `ImageConcanate`
- `ImageConcanate`
- `SaveImage`
- `MarkdownNote`
- `LoadImage`
- `LoadImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `SaveImage`
- `easy promptLine`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `117533082977772`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `lcm`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`

## 知识

覆盖率 **98%**（49/50）

**有卡**：`ConditioningZeroOut`、`EmptyLatentImage`、`KSampler`、`CLIPTextEncode`、`SaveImage`、`ImageConcanate`、`RandomNoise`、`BasicGuider`、`KSamplerSelect`、`SamplerCustomAdvanced`、`Flux2Scheduler`、`EmptyFlux2LatentImage`、`FluxGuidance`、`VAEDecode`、`Seed_`、`CR Aspect Ratio`、`LoadImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`easy promptLine`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 3 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

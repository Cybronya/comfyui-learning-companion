---
key: 图片生成/文生图/VividMuse Lens VS FLUX2-Klein VS Z-Image-Turbo_2063252783754727425.json
name: VividMuse Lens VS FLUX2-Klein VS Z-Image-Turbo_2063252783754727425
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/VividMuse Lens VS FLUX2-Klein VS Z-Image-Turbo_2063252783754727425.json
hash: 2a305dd62b8e3c30
coverage: 0.955556
learned_at: 2026-10-19 23:02:48
nodes: [VAELoader, CLIPLoader, CLIPLoader, VAELoader, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, CLIPLoader, VAELoader, CLIPTextEncode, ConditioningZeroOut, RandomNoise, CFGGuider, SamplerCustomAdvanced, UNETLoader, CLIPTextEncode, KSampler, UNETLoader, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, KSampler, UNETLoader, VAELoader, KSampler, EmptyLatentImage, SaveImage, SaveImage, SaveImage, VAEDecode, VAEDecode, VAEDecode, VAEDecode, easy promptList, PrimitiveStringMultiline, Fast Groups Bypasser (rgthree), easy promptList, Flux2Scheduler, KSamplerSelect, UNETLoader, SaveImage, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, SaveImage, Seed (rgthree)]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1664, "sampler_name": "euler_ancestral", "scheduler": "FlowMatchEulerDiscreteScheduler", "seed": 341944834472914, "steps": 8, "width": 1248}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/VividMuse Lens VS FLUX2-Klein VS Z-Image-Turbo_2063252783754727425.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/VividMuse Lens VS FLUX2-Klein VS Z-Image-Turbo_2063252783754727425.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（45 个）：
- `VAELoader`
- `CLIPLoader`
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `RandomNoise`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `easy promptList`
- `PrimitiveStringMultiline`
- `Fast Groups Bypasser (rgthree)`
- `easy promptList`
- `Flux2Scheduler`
- `KSamplerSelect` ★核心
- `UNETLoader` ★核心
- `SaveImage`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `SaveImage`
- `Seed (rgthree)`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `341944834472914`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `FlowMatchEulerDiscreteScheduler`
- `denoise` = `1`
- `width` = `1248`
- `height` = `1664`
- `batch_size` = `1`

## 知识

覆盖率 **96%**（43/45）

**有卡**：`VAELoader`、`CLIPLoader`、`CLIPTextEncode`、`ConditioningZeroOut`、`RandomNoise`、`CFGGuider`、`SamplerCustomAdvanced`、`UNETLoader`、`KSampler`、`EmptyLatentImage`、`SaveImage`、`VAEDecode`、`easy promptList`、`Flux2Scheduler`、`KSamplerSelect`、`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`、`Seed (rgthree)`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

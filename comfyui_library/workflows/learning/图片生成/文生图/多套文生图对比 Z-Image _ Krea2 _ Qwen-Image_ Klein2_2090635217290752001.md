---
key: 图片生成/文生图/多套文生图对比 Z-Image _ Krea2 _ Qwen-Image_ Klein2_2090635217290752001.json
name: 多套文生图对比 Z-Image _ Krea2 _ Qwen-Image_ Klein2_2090635217290752001
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/多套文生图对比 Z-Image _ Krea2 _ Qwen-Image_ Klein2_2090635217290752001.json
hash: 31a7efec09342db1
coverage: 0.938776
learned_at: 2026-10-21 02:59:46
nodes: [CLIPLoader, VAELoader, ConditioningZeroOut, UNETLoader, KSampler, CLIPTextEncode, EmptyLatentImage, UNETLoader, ImpactInt, ImpactInt, VAELoader, EmptyLatentImage, ConditioningZeroOut, VAELoader, CLIPLoader, ConditioningZeroOut, LoraLoaderModelOnly, easy seed, UNETLoader, LoraLoaderModelOnly, KSampler, CLIPLoader, VAELoader, KSampler, CLIPLoader, KSampler, UNETLoader, CLIPTextEncode, LoraLoaderModelOnly, SaveImage, SaveImage, LoraLoaderModelOnly, LoraLoaderModelOnly, SaveImage, VAEDecode, KSampler, VAEDecode, SaveImage, VAEDecode, PreviewImage, VAEDecode, PreviewImage, CLIPTextEncode, VAEDecode, SaveImage, PreviewImage, LoadImage, EmptyLatentImage, PainterFluxImageEdit]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1320, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 1090198336722397, "steps": 10, "width": 864}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/多套文生图对比 Z-Image _ Krea2 _ Qwen-Image_ Klein2_2090635217290752001.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/多套文生图对比 Z-Image _ Krea2 _ Qwen-Image_ Klein2_2090635217290752001.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（49 个）：
- `CLIPLoader`
- `VAELoader`
- `ConditioningZeroOut`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `UNETLoader` ★核心
- `ImpactInt`
- `ImpactInt`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `ConditioningZeroOut`
- `VAELoader`
- `CLIPLoader`
- `ConditioningZeroOut`
- `LoraLoaderModelOnly` ★核心
- `easy seed`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `CLIPLoader`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `PreviewImage`
- `VAEDecode` ★核心
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `PreviewImage`
- `LoadImage`
- `EmptyLatentImage` ★核心
- `PainterFluxImageEdit`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `1090198336722397`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `864`
- `height` = `1320`
- `batch_size` = `1`

## 知识

覆盖率 **94%**（46/49）

**有卡**：`CLIPLoader`、`VAELoader`、`ConditioningZeroOut`、`UNETLoader`、`KSampler`、`CLIPTextEncode`、`EmptyLatentImage`、`ImpactInt`、`LoraLoaderModelOnly`、`easy seed`、`SaveImage`、`VAEDecode`、`LoadImage`、`PainterFluxImageEdit`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 3 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

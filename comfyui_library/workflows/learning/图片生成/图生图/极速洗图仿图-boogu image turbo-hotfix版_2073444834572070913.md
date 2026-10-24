---
key: 图片生成/图生图/极速洗图仿图-boogu image turbo-hotfix版_2073444834572070913.json
name: 极速洗图仿图-boogu image turbo-hotfix版_2073444834572070913
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/极速洗图仿图-boogu image turbo-hotfix版_2073444834572070913.json
hash: 483d499b54f0a5fe
coverage: 0.952381
learned_at: 2026-10-23 13:09:37
nodes: [VAEDecode, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, VAELoader, VAEDecode, SaveImage, KSampler, KSampler, easy showAnything, easy cleanGpuUsed, easy imageConcat, SaveImage, SaveImage, UNETLoader, ResolutionSelector, CR Text, easy seed, RH_LLMAPI_Pro_Node, LoadImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "ddim", "scheduler": "beta57", "seed": 980835690271613, "steps": 4, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/极速洗图仿图-boogu image turbo-hotfix版_2073444834572070913.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/极速洗图仿图-boogu image turbo-hotfix版_2073444834572070913.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `VAEDecode` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `EmptyLatentImage` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `SaveImage`
- `KSampler` ★核心
- `KSampler` ★核心
- `easy showAnything`
- `easy cleanGpuUsed`
- `easy imageConcat`
- `SaveImage`
- `SaveImage`
- `UNETLoader` ★核心
- `ResolutionSelector`
- `CR Text`
- `easy seed`
- `RH_LLMAPI_Pro_Node`
- `LoadImage`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `980835690271613`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `ddim`
- `scheduler` = `beta57`
- `denoise` = `1`

## 知识

覆盖率 **95%**（20/21）

**有卡**：`VAEDecode`、`CLIPLoader`、`CLIPTextEncode`、`ConditioningZeroOut`、`EmptyLatentImage`、`VAELoader`、`SaveImage`、`KSampler`、`easy cleanGpuUsed`、`easy imageConcat`、`UNETLoader`、`ResolutionSelector`、`CR Text`、`easy seed`、`RH_LLMAPI_Pro_Node`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

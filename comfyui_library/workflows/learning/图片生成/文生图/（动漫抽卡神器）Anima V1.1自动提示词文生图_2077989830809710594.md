---
key: 图片生成/文生图/（动漫抽卡神器）Anima V1.1自动提示词文生图_2077989830809710594.json
name: （动漫抽卡神器）Anima V1.1自动提示词文生图_2077989830809710594
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/（动漫抽卡神器）Anima V1.1自动提示词文生图_2077989830809710594.json
hash: 32e880659ca6d96e
coverage: 0.85
learned_at: 2026-10-20 00:21:41
nodes: [CLIPLoader, RHLLMChatNode, RHLLMChatNode, Random Line, easy showAnything, ConcatTextOfUtils, easy showAnything, CR Prompt Text, CLIPTextEncode, VAELoader, EmptyLatentImage, CLIPTextEncode, VAEDecode, CR Prompt Text, CR Prompt Text, easy showAnything, easy cleanGpuUsed, SaveImage, KSampler, UNETLoader]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 1920, "sampler_name": "er_sde", "scheduler": "beta", "seed": 496683216090412, "steps": 40, "width": 1080}
---

# 图片生成/文生图/（动漫抽卡神器）Anima V1.1自动提示词文生图_2077989830809710594.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/（动漫抽卡神器）Anima V1.1自动提示词文生图_2077989830809710594.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（20 个）：
- `CLIPLoader`
- `RHLLMChatNode`
- `RHLLMChatNode`
- `Random Line`
- `easy showAnything`
- `ConcatTextOfUtils`
- `easy showAnything`
- `CR Prompt Text`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `CR Prompt Text`
- `CR Prompt Text`
- `easy showAnything`
- `easy cleanGpuUsed`
- `SaveImage`
- `KSampler` ★核心
- `UNETLoader` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`
- `seed` = `496683216090412`
- `steps` = `40`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **85%**（17/20）

**有卡**：`CLIPLoader`、`RHLLMChatNode`、`Random Line`、`ConcatTextOfUtils`、`CR Prompt Text`、`CLIPTextEncode`、`VAELoader`、`EmptyLatentImage`、`VAEDecode`、`easy cleanGpuUsed`、`SaveImage`、`KSampler`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader、CR Prompt Text

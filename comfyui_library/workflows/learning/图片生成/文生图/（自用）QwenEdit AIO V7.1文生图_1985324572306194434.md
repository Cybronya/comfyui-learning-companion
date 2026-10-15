---
key: 图片生成/文生图/（自用）QwenEdit AIO V7.1文生图_1985324572306194434.json
name: （自用）QwenEdit AIO V7.1文生图_1985324572306194434
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/（自用）QwenEdit AIO V7.1文生图_1985324572306194434.json
hash: 00d70c7b5dd6cbee
coverage: 0.9375
learned_at: 2026-10-15 22:29:11
nodes: [Int, EmptyLatentImage, KSampler, Int, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, VAEDecode, TT_img_enc, Int, Text Multiline, SaveImage, SaveImage, CR Prompt Text, PrimitiveInt, CheckpointLoaderSimple, TT_img_enc_v2]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "Qwen-Rapid-AIO-NSFW-v7.1.safetensors", "denoise": 1, "height": 512, "sampler_name": "euler_ancestral", "scheduler": "beta", "seed": 134261077877488, "steps": 8, "width": 512}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/（自用）QwenEdit AIO V7.1文生图_1985324572306194434.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/（自用）QwenEdit AIO V7.1文生图_1985324572306194434.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Output → Other

**节点**（16 个）：
- `Int`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `Int`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode` ★核心
- `TT_img_enc`
- `Int`
- `Text Multiline`
- `SaveImage`
- `SaveImage`
- `CR Prompt Text`
- `PrimitiveInt`
- `CheckpointLoaderSimple` ★核心
- `TT_img_enc_v2`

## 关键参数

- `width` = `512`
- `height` = `512`
- `batch_size` = `1`
- `seed` = `134261077877488`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `Qwen-Rapid-AIO-NSFW-v7.1.safetensors`

## 知识

覆盖率 **94%**（15/16）

**有卡**：`Int`、`EmptyLatentImage`、`KSampler`、`TextEncodeQwenImageEditPlus`、`VAEDecode`、`TT_img_enc`、`Text Multiline`、`SaveImage`、`CR Prompt Text`、`CheckpointLoaderSimple`、`TT_img_enc_v2`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、EmptyLatentImage、TextEncodeQwenImageEditPlus、CR Prompt Text、SaveImage、Int

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

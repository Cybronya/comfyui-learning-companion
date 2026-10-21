---
key: 图片生成/文生图/（贞贞Lora）Z-image Engineer V4& Flow Dop文生图V2（11000步）_2028503409036365825.json
name: （贞贞Lora）Z-image Engineer V4& Flow Dop文生图V2（11000步）_2028503409036365825
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/（贞贞Lora）Z-image Engineer V4& Flow Dop文生图V2（11000步）_2028503409036365825.json
hash: 8d978a20724d36ab
coverage: 1
learned_at: 2026-10-20 23:22:22
nodes: [VAEDecode, ConditioningZeroOut, KSampler, VAELoader, easy promptLine, CLIPTextEncode, LoraLoaderModelOnly, SaveImage, ClipLoaderGGUF, UNETLoader, LoraLoaderModelOnly, CR Prompt Text, EmptyLatentImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 4, "cfg": 1, "denoise": 1, "height": 1080, "sampler_name": "euler", "scheduler": "simple", "seed": 718496499840956, "steps": 10, "width": 1920}
---

# 图片生成/文生图/（贞贞Lora）Z-image Engineer V4& Flow Dop文生图V2（11000步）_2028503409036365825.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/（贞贞Lora）Z-image Engineer V4& Flow Dop文生图V2（11000步）_2028503409036365825.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（13 个）：
- `VAEDecode` ★核心
- `ConditioningZeroOut`
- `KSampler` ★核心
- `VAELoader`
- `easy promptLine`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `ClipLoaderGGUF`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CR Prompt Text`
- `EmptyLatentImage` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `718496499840956`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1920`
- `height` = `1080`
- `batch_size` = `4`

## 知识

覆盖率 **100%**（13/13）

**有卡**：`VAEDecode`、`ConditioningZeroOut`、`KSampler`、`VAELoader`、`easy promptLine`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`SaveImage`、`ClipLoaderGGUF`、`UNETLoader`、`CR Prompt Text`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage、UNETLoader

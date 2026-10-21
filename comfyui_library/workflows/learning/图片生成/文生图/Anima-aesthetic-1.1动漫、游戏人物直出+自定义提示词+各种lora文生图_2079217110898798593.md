---
key: 图片生成/文生图/Anima-aesthetic-1.1动漫、游戏人物直出+自定义提示词+各种lora文生图_2079217110898798593.json
name: Anima-aesthetic-1.1动漫、游戏人物直出+自定义提示词+各种lora文生图_2079217110898798593
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Anima-aesthetic-1.1动漫、游戏人物直出+自定义提示词+各种lora文生图_2079217110898798593.json
hash: 3d0b71b5dcd90f71
coverage: 0.833333
learned_at: 2026-10-20 00:18:49
nodes: [DapaoGeminiInstructionZhenzhenNode, 忽略多组孤海, CLIPTextEncode, CLIPTextEncode, VAEDecode, easy cleanGpuUsed, SaveImage, CR Prompt Text, 孤海注释, CR Prompt Text, ConcatTextOfUtils, easy showAnything, KSampler, CR Prompt Text, ConcatTextOfUtils, easy showAnything, FastGroupsBypassSwitch, Note, UNETLoader, LoraLoaderModelOnly, CLIPLoader, VAELoader, CR Prompt Text, EmptyLatentImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 1800, "sampler_name": "er_sde", "scheduler": "beta", "seed": 248171572096272, "steps": 40, "width": 1200}
---

# 图片生成/文生图/Anima-aesthetic-1.1动漫、游戏人物直出+自定义提示词+各种lora文生图_2079217110898798593.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Anima-aesthetic-1.1动漫、游戏人物直出+自定义提示词+各种lora文生图_2079217110898798593.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（24 个）：
- `DapaoGeminiInstructionZhenzhenNode`
- `忽略多组孤海`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `SaveImage`
- `CR Prompt Text`
- `孤海注释`
- `CR Prompt Text`
- `ConcatTextOfUtils`
- `easy showAnything`
- `KSampler` ★核心
- `CR Prompt Text`
- `ConcatTextOfUtils`
- `easy showAnything`
- `FastGroupsBypassSwitch`
- `Note`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `CR Prompt Text`
- `EmptyLatentImage` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `248171572096272`
- `steps` = `40`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `1200`
- `height` = `1800`
- `batch_size` = `1`

## 知识

覆盖率 **83%**（20/24）

**有卡**：`DapaoGeminiInstructionZhenzhenNode`、`忽略多组孤海`、`CLIPTextEncode`、`VAEDecode`、`easy cleanGpuUsed`、`SaveImage`、`CR Prompt Text`、`ConcatTextOfUtils`、`KSampler`、`FastGroupsBypassSwitch`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader

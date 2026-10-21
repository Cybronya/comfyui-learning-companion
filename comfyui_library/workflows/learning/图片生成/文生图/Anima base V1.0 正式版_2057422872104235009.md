---
key: 图片生成/文生图/Anima base V1.0 正式版_2057422872104235009.json
name: Anima base V1.0 正式版_2057422872104235009
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Anima base V1.0 正式版_2057422872104235009.json
hash: 7c6a30c52bf5a4c7
coverage: 0.805556
learned_at: 2026-10-19 22:45:21
nodes: [CLIPLoader, VAELoader, VAEDecode, RHLLMChatNode, easy showAnything, CR Prompt Text, Random Line, CR Prompt Text, easy showAnything, CLIPTextEncode, KSampler, UNETLoader, Note, Florence2Run, EmptyLatentImage, MarkdownNote, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, CLIPTextEncode, Florence2ModelLoader, CR Prompt Text, CR Prompt Text, CR Prompt Text, easy showAnything, ConcatTextOfUtils, SaveImage, easy showAnything, CR Prompt Text, Reroute, CR Prompt Text, CR Prompt Text, RHLLMChatNode, LoadImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 1920, "sampler_name": "er_sde", "scheduler": "beta", "seed": 651675080241387, "steps": 40, "width": 1080}
---

# 图片生成/文生图/Anima base V1.0 正式版_2057422872104235009.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Anima base V1.0 正式版_2057422872104235009.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（36 个）：
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `RHLLMChatNode`
- `easy showAnything`
- `CR Prompt Text`
- `Random Line`
- `CR Prompt Text`
- `easy showAnything`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `UNETLoader` ★核心
- `Note`
- `Florence2Run`
- `EmptyLatentImage` ★核心
- `MarkdownNote`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `CLIPTextEncode` ★核心
- `Florence2ModelLoader`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `easy showAnything`
- `ConcatTextOfUtils`
- `SaveImage`
- `easy showAnything`
- `CR Prompt Text`
- `Reroute`
- `CR Prompt Text`
- `CR Prompt Text`
- `RHLLMChatNode`
- `LoadImage`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `651675080241387`
- `steps` = `40`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`

## 知识

覆盖率 **81%**（29/36）

**有卡**：`CLIPLoader`、`VAELoader`、`VAEDecode`、`RHLLMChatNode`、`CR Prompt Text`、`Random Line`、`CLIPTextEncode`、`KSampler`、`UNETLoader`、`Florence2Run`、`EmptyLatentImage`、`Florence2ModelLoader`、`ConcatTextOfUtils`、`SaveImage`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage、UNETLoader

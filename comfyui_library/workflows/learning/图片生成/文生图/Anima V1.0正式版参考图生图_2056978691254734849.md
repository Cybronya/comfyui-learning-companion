---
key: 图片生成/文生图/Anima V1.0正式版参考图生图_2056978691254734849.json
name: Anima V1.0正式版参考图生图_2056978691254734849
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Anima V1.0正式版参考图生图_2056978691254734849.json
hash: 6d65cb6d739f0908
coverage: 0.826087
learned_at: 2026-10-21 02:51:21
nodes: [UNETLoader, CLIPLoader, VAELoader, VAEDecode, EmptyLatentImage, RHLLMChatNode, RHLLMChatNode, easy showAnything, CR Prompt Text, Random Line, LoadImage, Florence2ModelLoader, CR Prompt Text, easy showAnything, Florence2Run, CR Prompt Text, CLIPTextEncode, easy showAnything, CLIPTextEncode, SaveImage, ConcatTextOfUtils, KSampler, easy showAnything]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 1080, "sampler_name": "er_sde", "scheduler": "beta", "seed": 850517044652519, "steps": 40, "width": 1920}
---

# 图片生成/文生图/Anima V1.0正式版参考图生图_2056978691254734849.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Anima V1.0正式版参考图生图_2056978691254734849.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（23 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `RHLLMChatNode`
- `RHLLMChatNode`
- `easy showAnything`
- `CR Prompt Text`
- `Random Line`
- `LoadImage`
- `Florence2ModelLoader`
- `CR Prompt Text`
- `easy showAnything`
- `Florence2Run`
- `CR Prompt Text`
- `CLIPTextEncode` ★核心
- `easy showAnything`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `ConcatTextOfUtils`
- `KSampler` ★核心
- `easy showAnything`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1920`
- `height` = `1080`
- `batch_size` = `1`
- `seed` = `850517044652519`
- `steps` = `40`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **83%**（19/23）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`VAEDecode`、`EmptyLatentImage`、`RHLLMChatNode`、`CR Prompt Text`、`Random Line`、`LoadImage`、`Florence2ModelLoader`、`Florence2Run`、`CLIPTextEncode`、`SaveImage`、`ConcatTextOfUtils`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage、UNETLoader

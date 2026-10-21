---
key: 图片生成/文生图/（动漫抽卡神器）Anima V1.0正式版自动提示词文生图V4_2056904337720430594.json
name: （动漫抽卡神器）Anima V1.0正式版自动提示词文生图V4_2056904337720430594
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/（动漫抽卡神器）Anima V1.0正式版自动提示词文生图V4_2056904337720430594.json
hash: ab731d846d6ea175
coverage: 0.75
learned_at: 2026-10-19 22:46:55
nodes: [UNETLoader, CLIPTextEncode, CLIPLoader, VAEDecode, EmptyLatentImage, LoadImage, Florence2ModelLoader, easy showAnything, easy showAnything, AnimaPromptCombinerT8, KSampler, PreviewImage, easy showAnything, VRGDG_ShowAny, VRGDG_ShowAny, VRGDG_ShowAny, VRGDG_ShowAny, AnimaPromptT8, AnimaArtistStyleT8, Florence2Run, SaveImage, CR Prompt Text, easy showAnything, RHLLMChatNode, easy showAnything, RHLLMChatNode, CR Prompt Text, Random Line, easy showAnything, ConcatTextOfUtils, easy showAnything, CR Prompt Text, AnimaPromptT8, CLIPTextEncode, easy showAnything, VAELoader]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 1080, "sampler_name": "er_sde", "scheduler": "beta", "seed": 1026648973453826, "steps": 40, "width": 1920}
---

# 图片生成/文生图/（动漫抽卡神器）Anima V1.0正式版自动提示词文生图V4_2056904337720430594.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/（动漫抽卡神器）Anima V1.0正式版自动提示词文生图V4_2056904337720430594.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（36 个）：
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `LoadImage`
- `Florence2ModelLoader`
- `easy showAnything`
- `easy showAnything`
- `AnimaPromptCombinerT8`
- `KSampler` ★核心
- `PreviewImage`
- `easy showAnything`
- `VRGDG_ShowAny`
- `VRGDG_ShowAny`
- `VRGDG_ShowAny`
- `VRGDG_ShowAny`
- `AnimaPromptT8`
- `AnimaArtistStyleT8`
- `Florence2Run`
- `SaveImage`
- `CR Prompt Text`
- `easy showAnything`
- `RHLLMChatNode`
- `easy showAnything`
- `RHLLMChatNode`
- `CR Prompt Text`
- `Random Line`
- `easy showAnything`
- `ConcatTextOfUtils`
- `easy showAnything`
- `CR Prompt Text`
- `AnimaPromptT8`
- `CLIPTextEncode` ★核心
- `easy showAnything`
- `VAELoader`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1920`
- `height` = `1080`
- `batch_size` = `1`
- `seed` = `1026648973453826`
- `steps` = `40`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **75%**（27/36）

**有卡**：`UNETLoader`、`CLIPTextEncode`、`CLIPLoader`、`VAEDecode`、`EmptyLatentImage`、`LoadImage`、`Florence2ModelLoader`、`AnimaPromptCombinerT8`、`KSampler`、`VRGDG_ShowAny`、`AnimaPromptT8`、`AnimaArtistStyleT8`、`Florence2Run`、`SaveImage`、`CR Prompt Text`、`RHLLMChatNode`、`Random Line`、`ConcatTextOfUtils`、`VAELoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage、UNETLoader

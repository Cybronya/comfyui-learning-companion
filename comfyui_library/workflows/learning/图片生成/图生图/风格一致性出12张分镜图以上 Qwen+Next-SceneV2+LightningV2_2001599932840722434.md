---
key: 图片生成/图生图/风格一致性出12张分镜图以上 Qwen+Next-SceneV2+LightningV2_2001599932840722434.json
name: 风格一致性出12张分镜图以上 Qwen+Next-SceneV2+LightningV2_2001599932840722434
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/风格一致性出12张分镜图以上 Qwen+Next-SceneV2+LightningV2_2001599932840722434.json
hash: cac4692acbc2721f
coverage: 0.857143
learned_at: 2026-10-23 13:32:07
nodes: [TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, VAEEncode, ProcessString, VAEDecode, RH_LLMAPI_NODE, Int, ShellAgentPluginOutputText, CLIPLoader, VAELoader, Anything Everywhere3, easy promptLine, LoraLoaderModelOnly, LoraLoaderModelOnly, LayerUtility: ImageScaleByAspectRatio V2, KSampler, LoadImage, JjkText, UNETLoader, easy showAnything, SaveImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "sa_solver", "scheduler": "simple", "seed": 63212190220166, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/风格一致性出12张分镜图以上 Qwen+Next-SceneV2+LightningV2_2001599932840722434.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/风格一致性出12张分镜图以上 Qwen+Next-SceneV2+LightningV2_2001599932840722434.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `VAEEncode` ★核心
- `ProcessString`
- `VAEDecode` ★核心
- `RH_LLMAPI_NODE`
- `Int`
- `ShellAgentPluginOutputText`
- `CLIPLoader`
- `VAELoader`
- `Anything Everywhere3`
- `easy promptLine`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `KSampler` ★核心
- `LoadImage`
- `JjkText`
- `UNETLoader` ★核心
- `easy showAnything`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `63212190220166`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **86%**（18/21）

**有卡**：`TextEncodeQwenImageEditPlus`、`VAEEncode`、`ProcessString`、`VAEDecode`、`RH_LLMAPI_NODE`、`Int`、`ShellAgentPluginOutputText`、`CLIPLoader`、`VAELoader`、`easy promptLine`、`LoraLoaderModelOnly`、`LayerUtility: ImageScaleByAspectRatio V2`、`KSampler`、`LoadImage`、`UNETLoader`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、SaveImage、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

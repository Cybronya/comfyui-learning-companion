---
key: 图片生成/图生图/qwen-image2.1巨物专用（支持文生、角色参考图生）多模式通用_2106719510433714177.json
name: qwen-image2.1巨物专用（支持文生、角色参考图生）多模式通用_2106719510433714177
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen-image2.1巨物专用（支持文生、角色参考图生）多模式通用_2106719510433714177.json
hash: 194d975b143f6904
coverage: 0.875
learned_at: 2026-10-21 00:46:09
nodes: [CLIPLoader, QwenImage21SageAttentionT8, ManualSigmas, LoadImage, TextEncodeQwenImage21, VAELoader, easy showAnything, SaveImage, VAEDecode, UNETLoader, ClownsharKSampler_Beta, WujiImagePrompt, WujiUpscaler2, RH_Screenwriter, PrimitiveStringMultiline, WujiPromptEditor]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": 1, "sampler_name": -1, "scheduler": 1, "seed": 0.5, "steps": "bong_tangent"}
---

# 图片生成/图生图/qwen-image2.1巨物专用（支持文生、角色参考图生）多模式通用_2106719510433714177.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen-image2.1巨物专用（支持文生、角色参考图生）多模式通用_2106719510433714177.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（16 个）：
- `CLIPLoader`
- `QwenImage21SageAttentionT8`
- `ManualSigmas`
- `LoadImage`
- `TextEncodeQwenImage21`
- `VAELoader`
- `easy showAnything`
- `SaveImage`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `ClownsharKSampler_Beta` ★核心
- `WujiImagePrompt`
- `WujiUpscaler2`
- `RH_Screenwriter`
- `PrimitiveStringMultiline`
- `WujiPromptEditor`

## 关键参数

- `seed` = `0.5`
- `steps` = `bong_tangent`
- `cfg` = `8`
- `sampler_name` = `-1`
- `scheduler` = `1`
- `denoise` = `1`

## 知识

覆盖率 **88%**（14/16）

**有卡**：`CLIPLoader`、`QwenImage21SageAttentionT8`、`ManualSigmas`、`LoadImage`、`TextEncodeQwenImage21`、`VAELoader`、`SaveImage`、`VAEDecode`、`UNETLoader`、`ClownsharKSampler_Beta`、`WujiImagePrompt`、`WujiUpscaler2`、`RH_Screenwriter`、`WujiPromptEditor`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、UNETLoader、ClownsharKSampler_Beta、WujiUpscaler2

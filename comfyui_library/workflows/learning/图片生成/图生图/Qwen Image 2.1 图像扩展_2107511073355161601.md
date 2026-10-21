---
key: 图片生成/图生图/Qwen Image 2.1 图像扩展_2107511073355161601.json
name: Qwen Image 2.1 图像扩展_2107511073355161601
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 图像扩展_2107511073355161601.json
hash: 685304f76406fa6c
coverage: 0.703704
learned_at: 2026-10-21 00:42:10
nodes: [Reroute, VAEDecode, CLIPLoader, VAELoader, Reroute, UNETLoader, GoohaiRouteBlocker, QwenImage21SageAttentionT8, KSampler, 孤海注释, ShowText|pysssss, QwenImagePromptOptimizer, QwenImage21BlockCacheT8, QwenImage21SpectrumT8, RestoreQwenImage21GH, TextEncodeQwenImage21GH, SetNode, LoadImageGoohai, GoohaiRouteBlocker, CM_FloatToInt, CM_FloatToInt, GetNode, SaveImage, DF_Text_Box, GoohaiRatioAndResolution, PrimitiveNode, PrimitiveNode]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 195314286887116, "steps": 30}
---

# 图片生成/图生图/Qwen Image 2.1 图像扩展_2107511073355161601.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 图像扩展_2107511073355161601.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `Reroute`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `Reroute`
- `UNETLoader` ★核心
- `GoohaiRouteBlocker`
- `QwenImage21SageAttentionT8`
- `KSampler` ★核心
- `孤海注释`
- `ShowText|pysssss`
- `QwenImagePromptOptimizer`
- `QwenImage21BlockCacheT8`
- `QwenImage21SpectrumT8`
- `RestoreQwenImage21GH`
- `TextEncodeQwenImage21GH`
- `SetNode`
- `LoadImageGoohai`
- `GoohaiRouteBlocker`
- `CM_FloatToInt`
- `CM_FloatToInt`
- `GetNode`
- `SaveImage`
- `DF_Text_Box`
- `GoohaiRatioAndResolution`
- `PrimitiveNode`
- `PrimitiveNode`

## 关键参数

- `seed` = `195314286887116`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **70%**（19/27）

**有卡**：`VAEDecode`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`GoohaiRouteBlocker`、`QwenImage21SageAttentionT8`、`KSampler`、`QwenImagePromptOptimizer`、`QwenImage21BlockCacheT8`、`QwenImage21SpectrumT8`、`RestoreQwenImage21GH`、`TextEncodeQwenImage21GH`、`LoadImageGoohai`、`CM_FloatToInt`、`SaveImage`、`DF_Text_Box`、`GoohaiRatioAndResolution`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、UNETLoader、TextEncodeQwenImage21GH、QwenImagePromptOptimizer、GoohaiRatioAndResolution

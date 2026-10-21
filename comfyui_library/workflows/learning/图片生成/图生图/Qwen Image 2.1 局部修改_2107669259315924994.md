---
key: 图片生成/图生图/Qwen Image 2.1 局部修改_2107669259315924994.json
name: Qwen Image 2.1 局部修改_2107669259315924994
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 局部修改_2107669259315924994.json
hash: 5e47272b34d6ddde
coverage: 0.73913
learned_at: 2026-10-21 00:42:14
nodes: [Reroute, CLIPLoader, VAELoader, Reroute, UNETLoader, GoohaiRouteBlocker, QwenImage21SageAttentionT8, 孤海注释, ShowText|pysssss, QwenImagePromptOptimizer, QwenImage21BlockCacheT8, QwenImage21SpectrumT8, TextEncodeQwenImage21GH, SetNode, GetNode, GoohaiRouteBlocker, LoadImageGoohai, DF_Text_Box, GoohaiRatioAndResolution, SaveImage, KSampler, VAEDecode, RestoreQwenImage21GH]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 525012052254303, "steps": 30}
---

# 图片生成/图生图/Qwen Image 2.1 局部修改_2107669259315924994.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 局部修改_2107669259315924994.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `Reroute`
- `CLIPLoader`
- `VAELoader`
- `Reroute`
- `UNETLoader` ★核心
- `GoohaiRouteBlocker`
- `QwenImage21SageAttentionT8`
- `孤海注释`
- `ShowText|pysssss`
- `QwenImagePromptOptimizer`
- `QwenImage21BlockCacheT8`
- `QwenImage21SpectrumT8`
- `TextEncodeQwenImage21GH`
- `SetNode`
- `GetNode`
- `GoohaiRouteBlocker`
- `LoadImageGoohai`
- `DF_Text_Box`
- `GoohaiRatioAndResolution`
- `SaveImage`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `RestoreQwenImage21GH`

## 关键参数

- `seed` = `525012052254303`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **74%**（17/23）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`GoohaiRouteBlocker`、`QwenImage21SageAttentionT8`、`QwenImagePromptOptimizer`、`QwenImage21BlockCacheT8`、`QwenImage21SpectrumT8`、`TextEncodeQwenImage21GH`、`LoadImageGoohai`、`DF_Text_Box`、`GoohaiRatioAndResolution`、`SaveImage`、`KSampler`、`VAEDecode`、`RestoreQwenImage21GH`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、UNETLoader、TextEncodeQwenImage21GH、QwenImagePromptOptimizer、GoohaiRatioAndResolution

---
key: 图片生成/图生图/服装迁移图像编辑Clothing Transfer Image Editing Qwen  2.1_2111978235830562818.json
name: 服装迁移图像编辑Clothing Transfer Image Editing Qwen  2.1_2111978235830562818
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/服装迁移图像编辑Clothing Transfer Image Editing Qwen  2.1_2111978235830562818.json
hash: f6bd1dfca9fbb4fe
coverage: 0.676471
learned_at: 2026-10-23 13:08:45
nodes: [LoadImage, LoadImage, Reroute, LoadImage, Reroute, Reroute, Reroute, Reroute, Reroute, SetNode, VAEDecode, CLIPLoader, VAELoader, Reroute, LoadImage, LoadImage, UNETLoader, GoohaiRouteBlocker, GoohaiRatioAndResolution, 忽略多组孤海, QwenImage21SageAttentionT8, GetNode, KSampler, GoohaiRouteBlocker, ShowText|pysssss, Image Comparer (rgthree), QwenImagePromptOptimizer, QwenImage21BlockCacheT8, QwenImage21SpectrumT8, RestoreQwenImage21GH, TextEncodeQwenImage21GH, SaveImage, LoadImageGoohai, DF_Text_Box]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1004543670550547, "steps": 30}
---

# 图片生成/图生图/服装迁移图像编辑Clothing Transfer Image Editing Qwen  2.1_2111978235830562818.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/服装迁移图像编辑Clothing Transfer Image Editing Qwen  2.1_2111978235830562818.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（34 个）：
- `LoadImage`
- `LoadImage`
- `Reroute`
- `LoadImage`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `SetNode`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `Reroute`
- `LoadImage`
- `LoadImage`
- `UNETLoader` ★核心
- `GoohaiRouteBlocker`
- `GoohaiRatioAndResolution`
- `忽略多组孤海`
- `QwenImage21SageAttentionT8`
- `GetNode`
- `KSampler` ★核心
- `GoohaiRouteBlocker`
- `ShowText|pysssss`
- `Image Comparer (rgthree)`
- `QwenImagePromptOptimizer`
- `QwenImage21BlockCacheT8`
- `QwenImage21SpectrumT8`
- `RestoreQwenImage21GH`
- `TextEncodeQwenImage21GH`
- `SaveImage`
- `LoadImageGoohai`
- `DF_Text_Box`

## 关键参数

- `seed` = `1004543670550547`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **68%**（23/34）

**有卡**：`LoadImage`、`VAEDecode`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`GoohaiRouteBlocker`、`GoohaiRatioAndResolution`、`忽略多组孤海`、`QwenImage21SageAttentionT8`、`KSampler`、`QwenImagePromptOptimizer`、`QwenImage21BlockCacheT8`、`QwenImage21SpectrumT8`、`RestoreQwenImage21GH`、`TextEncodeQwenImage21GH`、`SaveImage`、`LoadImageGoohai`、`DF_Text_Box`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、LoadImage、UNETLoader、TextEncodeQwenImage21GH、QwenImagePromptOptimizer

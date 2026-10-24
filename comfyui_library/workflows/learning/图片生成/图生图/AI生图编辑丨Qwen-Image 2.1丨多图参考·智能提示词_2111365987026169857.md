---
key: 图片生成/图生图/AI生图编辑丨Qwen-Image 2.1丨多图参考·智能提示词_2111365987026169857.json
name: AI生图编辑丨Qwen-Image 2.1丨多图参考·智能提示词_2111365987026169857
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/AI生图编辑丨Qwen-Image 2.1丨多图参考·智能提示词_2111365987026169857.json
hash: f8601c3c6f8b5c20
coverage: 0.861111
learned_at: 2026-10-23 10:50:46
nodes: [LoadImage, LoadImage, LoadImage, VAEDecode, CLIPLoader, VAELoader, LoadImage, LoadImage, UNETLoader, GoohaiRouteBlocker, GoohaiRatioAndResolution, 忽略多组孤海, QwenImage21SageAttentionT8, KSampler, GoohaiRouteBlocker, ShowText|pysssss, Image Comparer (rgthree), QwenImagePromptOptimizer, DF_Text_Box, QwenImage21BlockCacheT8, QwenImage21SpectrumT8, RestoreQwenImage21GH, TextEncodeQwenImage21GH, LoadImageGoohai, SaveImage, PrimitiveBoolean, ComfySwitchNode, ComfySwitchNode, PrimitiveBoolean, PrimitiveBoolean, ComfySwitchNode, GoohaiRouteBlocker, GoohaiRouteBlocker, GoohaiRouteBlocker, GoohaiRouteBlocker, GoohaiRouteBlocker]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 746237649349839, "steps": 30}
---

# 图片生成/图生图/AI生图编辑丨Qwen-Image 2.1丨多图参考·智能提示词_2111365987026169857.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/AI生图编辑丨Qwen-Image 2.1丨多图参考·智能提示词_2111365987026169857.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（36 个）：
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoadImage`
- `LoadImage`
- `UNETLoader` ★核心
- `GoohaiRouteBlocker`
- `GoohaiRatioAndResolution`
- `忽略多组孤海`
- `QwenImage21SageAttentionT8`
- `KSampler` ★核心
- `GoohaiRouteBlocker`
- `ShowText|pysssss`
- `Image Comparer (rgthree)`
- `QwenImagePromptOptimizer`
- `DF_Text_Box`
- `QwenImage21BlockCacheT8`
- `QwenImage21SpectrumT8`
- `RestoreQwenImage21GH`
- `TextEncodeQwenImage21GH`
- `LoadImageGoohai`
- `SaveImage`
- `PrimitiveBoolean`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `PrimitiveBoolean`
- `PrimitiveBoolean`
- `ComfySwitchNode`
- `GoohaiRouteBlocker`
- `GoohaiRouteBlocker`
- `GoohaiRouteBlocker`
- `GoohaiRouteBlocker`
- `GoohaiRouteBlocker`

## 关键参数

- `seed` = `746237649349839`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **86%**（31/36）

**有卡**：`LoadImage`、`VAEDecode`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`GoohaiRouteBlocker`、`GoohaiRatioAndResolution`、`忽略多组孤海`、`QwenImage21SageAttentionT8`、`KSampler`、`QwenImagePromptOptimizer`、`DF_Text_Box`、`QwenImage21BlockCacheT8`、`QwenImage21SpectrumT8`、`RestoreQwenImage21GH`、`TextEncodeQwenImage21GH`、`LoadImageGoohai`、`SaveImage`、`PrimitiveBoolean`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、LoadImage、UNETLoader、TextEncodeQwenImage21GH、QwenImagePromptOptimizer

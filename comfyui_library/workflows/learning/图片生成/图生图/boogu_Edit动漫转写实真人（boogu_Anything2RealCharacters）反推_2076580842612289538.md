---
key: 图片生成/图生图/boogu_Edit动漫转写实真人（boogu_Anything2RealCharacters）反推_2076580842612289538.json
name: boogu_Edit动漫转写实真人（boogu_Anything2RealCharacters）反推_2076580842612289538
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/boogu_Edit动漫转写实真人（boogu_Anything2RealCharacters）反推_2076580842612289538.json
hash: 5f9dc254e4472c87
coverage: 0.904762
learned_at: 2026-10-23 11:34:12
nodes: [VAELoader, GetImageSize, EmptyLatentImage, KSamplerSelect, VAEDecode, CLIPLoader, BasicScheduler, SamplerCustom, UNETLoader, SaveImage, MarkdownNote, LoadImage, llama_cpp_parameters, llama_cpp_model_loader, Text, JoinStrings, ShowText|pysssss, TextEncodeBooguEdit, ColorCorrect, LayerUtility: ImageScaleByAspectRatio V2, llama_cpp_instruct_adv]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 512, "width": 512}
---

# 图片生成/图生图/boogu_Edit动漫转写实真人（boogu_Anything2RealCharacters）反推_2076580842612289538.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/boogu_Edit动漫转写实真人（boogu_Anything2RealCharacters）反推_2076580842612289538.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `VAELoader`
- `GetImageSize`
- `EmptyLatentImage` ★核心
- `KSamplerSelect` ★核心
- `VAEDecode` ★核心
- `CLIPLoader`
- `BasicScheduler`
- `SamplerCustom` ★核心
- `UNETLoader` ★核心
- `SaveImage`
- `MarkdownNote`
- `LoadImage`
- `llama_cpp_parameters`
- `llama_cpp_model_loader`
- `Text`
- `JoinStrings`
- `ShowText|pysssss`
- `TextEncodeBooguEdit`
- `ColorCorrect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `llama_cpp_instruct_adv`

## 关键参数

- `width` = `512`
- `height` = `512`
- `batch_size` = `1`

## 知识

覆盖率 **90%**（19/21）

**有卡**：`VAELoader`、`GetImageSize`、`EmptyLatentImage`、`KSamplerSelect`、`VAEDecode`、`CLIPLoader`、`BasicScheduler`、`SamplerCustom`、`UNETLoader`、`SaveImage`、`LoadImage`、`llama_cpp_parameters`、`llama_cpp_model_loader`、`Text`、`JoinStrings`、`TextEncodeBooguEdit`、`ColorCorrect`、`LayerUtility: ImageScaleByAspectRatio V2`、`llama_cpp_instruct_adv`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、EmptyLatentImage、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom

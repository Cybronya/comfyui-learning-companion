---
key: 图片生成/图生图/boogu_Edit动漫转写实真人（boogu_Anything2RealCharacters）_2076639003436208129.json
name: boogu_Edit动漫转写实真人（boogu_Anything2RealCharacters）_2076639003436208129
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/boogu_Edit动漫转写实真人（boogu_Anything2RealCharacters）_2076639003436208129.json
hash: 9ee22b22389d4bbd
coverage: 0.933333
learned_at: 2026-10-23 11:34:11
nodes: [VAELoader, GetImageSize, EmptyLatentImage, TextEncodeBooguEdit, KSamplerSelect, VAEDecode, CLIPLoader, BasicScheduler, SamplerCustom, ColorCorrect, UNETLoader, SaveImage, LoadImage, MarkdownNote, LayerUtility: ImageScaleByAspectRatio V2]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 512, "width": 512}
---

# 图片生成/图生图/boogu_Edit动漫转写实真人（boogu_Anything2RealCharacters）_2076639003436208129.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/boogu_Edit动漫转写实真人（boogu_Anything2RealCharacters）_2076639003436208129.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（15 个）：
- `VAELoader`
- `GetImageSize`
- `EmptyLatentImage` ★核心
- `TextEncodeBooguEdit`
- `KSamplerSelect` ★核心
- `VAEDecode` ★核心
- `CLIPLoader`
- `BasicScheduler`
- `SamplerCustom` ★核心
- `ColorCorrect`
- `UNETLoader` ★核心
- `SaveImage`
- `LoadImage`
- `MarkdownNote`
- `LayerUtility: ImageScaleByAspectRatio V2`

## 关键参数

- `width` = `512`
- `height` = `512`
- `batch_size` = `1`

## 知识

覆盖率 **93%**（14/15）

**有卡**：`VAELoader`、`GetImageSize`、`EmptyLatentImage`、`TextEncodeBooguEdit`、`KSamplerSelect`、`VAEDecode`、`CLIPLoader`、`BasicScheduler`、`SamplerCustom`、`ColorCorrect`、`UNETLoader`、`SaveImage`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、EmptyLatentImage、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom

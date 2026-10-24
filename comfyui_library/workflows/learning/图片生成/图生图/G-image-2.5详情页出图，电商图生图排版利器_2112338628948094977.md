---
key: 图片生成/图生图/G-image-2.5详情页出图，电商图生图排版利器_2112338628948094977.json
name: G-image-2.5详情页出图，电商图生图排版利器_2112338628948094977
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/G-image-2.5详情页出图，电商图生图排版利器_2112338628948094977.json
hash: 29615d8a435c592b
coverage: 0.6
learned_at: 2026-10-23 11:02:30
nodes: [easy promptConcat, easy promptConcat, easy promptConcat, easy promptConcat, PrimitiveStringMultiline, easy promptConcat, easy promptConcat, PrimitiveStringMultiline, easy promptConcat, PrimitiveStringMultiline, PrimitiveStringMultiline, easy promptConcat, PrimitiveStringMultiline, PrimitiveStringMultiline, ShowText|pysssss, PrimitiveStringMultiline, easy promptConcat, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, RH_RhartImageG2ImageToImage, RH_RhartImageG2OfficialImageToImage, SaveImage, PreviewImage, RH_LLMAPI_Pro_Node, SaveImage, JoinStringMulti, PrimitiveStringMultiline, easy promptConcat, PrimitiveStringMultiline, ShowText|pysssss, RH_LLMAPI_Pro_Node, ShowText|pysssss, ShowText|pysssss, easy showAnything, PreviewImage, easy int, SaveImage, PreviewImage, LoadImage, RH_RhartImageG25FlareImageToImage, LoadImage, PrimitiveStringMultiline, easy promptConcat, RHHiddenNodes, TextSplitByDelimiterEnhanced, ShowText|pysssss, ShowText|pysssss, PrimitiveStringMultiline, LoadImage, RH_RhartImageG25SunburstImageToImage, SaveImage, PreviewImage, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, LoadImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/G-image-2.5详情页出图，电商图生图排版利器_2112338628948094977.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/G-image-2.5详情页出图，电商图生图排版利器_2112338628948094977.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（90 个）：
- `easy promptConcat`
- `easy promptConcat`
- `easy promptConcat`
- `easy promptConcat`
- `PrimitiveStringMultiline`
- `easy promptConcat`
- `easy promptConcat`
- `PrimitiveStringMultiline`
- `easy promptConcat`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `easy promptConcat`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `ShowText|pysssss`
- `PrimitiveStringMultiline`
- `easy promptConcat`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `RH_RhartImageG2ImageToImage`
- `RH_RhartImageG2OfficialImageToImage`
- `SaveImage`
- `PreviewImage`
- `RH_LLMAPI_Pro_Node`
- `SaveImage`
- `JoinStringMulti`
- `PrimitiveStringMultiline`
- `easy promptConcat`
- `PrimitiveStringMultiline`
- `ShowText|pysssss`
- `RH_LLMAPI_Pro_Node`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `easy showAnything`
- `PreviewImage`
- `easy int`
- `SaveImage`
- `PreviewImage`
- `LoadImage`
- `RH_RhartImageG25FlareImageToImage`
- `LoadImage`
- `PrimitiveStringMultiline`
- `easy promptConcat`
- `RHHiddenNodes`
- `TextSplitByDelimiterEnhanced`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `PrimitiveStringMultiline`
- `LoadImage`
- `RH_RhartImageG25SunburstImageToImage`
- `SaveImage`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `LoadImage`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `JjkText`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `VAELoader`
- `solarL_SaveImagesToZip`
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **60%**（54/90）

**有卡**：`easy promptConcat`、`RH_RhartImageG2ImageToImage`、`RH_RhartImageG2OfficialImageToImage`、`SaveImage`、`RH_LLMAPI_Pro_Node`、`JoinStringMulti`、`easy int`、`LoadImage`、`RH_RhartImageG25FlareImageToImage`、`RHHiddenNodes`、`TextSplitByDelimiterEnhanced`、`RH_RhartImageG25SunburstImageToImage`、`UNETLoader`、`LoraLoaderModelOnly`、`KSampler`、`CLIPTextEncode`、`CLIPLoader`、`VAEDecode`、`EmptyLatentImage`、`VAELoader`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

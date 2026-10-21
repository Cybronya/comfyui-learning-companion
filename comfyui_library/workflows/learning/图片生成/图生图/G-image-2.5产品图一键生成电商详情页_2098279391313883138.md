---
key: 图片生成/图生图/G-image-2.5产品图一键生成电商详情页_2098279391313883138.json
name: G-image-2.5产品图一键生成电商详情页_2098279391313883138
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/G-image-2.5产品图一键生成电商详情页_2098279391313883138.json
hash: 1c8e7a0676b8f08a
coverage: 0.6
learned_at: 2026-10-21 00:40:08
nodes: [easy promptConcat, easy promptConcat, easy promptConcat, easy promptConcat, PrimitiveStringMultiline, easy promptConcat, easy promptConcat, PrimitiveStringMultiline, easy promptConcat, PrimitiveStringMultiline, PrimitiveStringMultiline, easy promptConcat, PrimitiveStringMultiline, PrimitiveStringMultiline, TextSplitByDelimiterEnhanced, ShowText|pysssss, ShowText|pysssss, PrimitiveStringMultiline, easy promptConcat, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, ShowText|pysssss, PrimitiveStringMultiline, RH_RhartImageG2ImageToImage, RH_RhartImageG2OfficialImageToImage, SaveImage, PreviewImage, RH_LLMAPI_Pro_Node, SaveImage, JoinStringMulti, PrimitiveStringMultiline, easy promptConcat, PrimitiveStringMultiline, ShowText|pysssss, RH_LLMAPI_Pro_Node, ShowText|pysssss, PrimitiveStringMultiline, ShowText|pysssss, easy showAnything, RHHiddenNodes, PreviewImage, easy int, SaveImage, SaveImage, PreviewImage, LoadImage, LoadImage, LoadImage, RH_RhartImageG25FlareImageToImage, LoadImage, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, easy promptConcat, RH_RhartImageG25SunburstImageToImage, PreviewImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPLoader, CLIPTextEncode, JjkText, EmptyLatentImage, solarL_SaveImagesToZip, VAEDecode, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/G-image-2.5产品图一键生成电商详情页_2098279391313883138.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/G-image-2.5产品图一键生成电商详情页_2098279391313883138.json`

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
- `TextSplitByDelimiterEnhanced`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `PrimitiveStringMultiline`
- `easy promptConcat`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `ShowText|pysssss`
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
- `PrimitiveStringMultiline`
- `ShowText|pysssss`
- `easy showAnything`
- `RHHiddenNodes`
- `PreviewImage`
- `easy int`
- `SaveImage`
- `SaveImage`
- `PreviewImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `RH_RhartImageG25FlareImageToImage`
- `LoadImage`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `easy promptConcat`
- `RH_RhartImageG25SunburstImageToImage`
- `PreviewImage`
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
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `JjkText`
- `EmptyLatentImage` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `VAELoader`
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

**有卡**：`easy promptConcat`、`TextSplitByDelimiterEnhanced`、`RH_RhartImageG2ImageToImage`、`RH_RhartImageG2OfficialImageToImage`、`SaveImage`、`RH_LLMAPI_Pro_Node`、`JoinStringMulti`、`RHHiddenNodes`、`easy int`、`LoadImage`、`RH_RhartImageG25FlareImageToImage`、`RH_RhartImageG25SunburstImageToImage`、`UNETLoader`、`LoraLoaderModelOnly`、`KSampler`、`CLIPTextEncode`、`CLIPLoader`、`EmptyLatentImage`、`solarL_SaveImagesToZip`、`VAEDecode`、`VAELoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

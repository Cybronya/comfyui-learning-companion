---
key: 图片生成/图生图/最新G_image2官方全量稳定版V1.0｜跨境电商主图详情页图生图一键出_2100503932853379073.json
name: 最新G_image2官方全量稳定版V1.0｜跨境电商主图详情页图生图一键出_2100503932853379073
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/最新G_image2官方全量稳定版V1.0｜跨境电商主图详情页图生图一键出_2100503932853379073.json
hash: 675a2b9c76207ac1
coverage: 0.875
learned_at: 2026-10-21 00:54:21
nodes: [HAIGC_Layer, ShowText|pysssss, HAIGC_CombineUnits, RH_LLMAPI_Pro_Node, RH_RhartImageNG31FlashOfficialImageToImage, SaveImage, LoadImage, Text, Text, Text, RH_LLMAPI_Pro_Node, ShowText|pysssss, easy promptConcat, easy promptConcat, easy promptConcat, ProcessString, easy promptLine, easy showAnything, HAIGC_SavePSD, EmptyImage, PreviewImage, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/最新G_image2官方全量稳定版V1.0｜跨境电商主图详情页图生图一键出_2100503932853379073.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/最新G_image2官方全量稳定版V1.0｜跨境电商主图详情页图生图一键出_2100503932853379073.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（64 个）：
- `HAIGC_Layer`
- `ShowText|pysssss`
- `HAIGC_CombineUnits`
- `RH_LLMAPI_Pro_Node`
- `RH_RhartImageNG31FlashOfficialImageToImage`
- `SaveImage`
- `LoadImage`
- `Text`
- `Text`
- `Text`
- `RH_LLMAPI_Pro_Node`
- `ShowText|pysssss`
- `easy promptConcat`
- `easy promptConcat`
- `easy promptConcat`
- `ProcessString`
- `easy promptLine`
- `easy showAnything`
- `HAIGC_SavePSD`
- `EmptyImage`
- `PreviewImage`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `solarL_SaveImagesToZip`
- `JjkText`
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
- `CLIPTextEncode` ★核心
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **88%**（56/64）

**有卡**：`HAIGC_Layer`、`HAIGC_CombineUnits`、`RH_LLMAPI_Pro_Node`、`RH_RhartImageNG31FlashOfficialImageToImage`、`SaveImage`、`LoadImage`、`Text`、`easy promptConcat`、`ProcessString`、`easy promptLine`、`HAIGC_SavePSD`、`EmptyImage`、`UNETLoader`、`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

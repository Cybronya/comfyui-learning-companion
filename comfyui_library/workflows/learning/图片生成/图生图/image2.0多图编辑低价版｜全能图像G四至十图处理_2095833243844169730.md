---
key: 图片生成/图生图/image2.0多图编辑低价版｜全能图像G四至十图处理_2095833243844169730.json
name: image2.0多图编辑低价版｜全能图像G四至十图处理_2095833243844169730
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/image2.0多图编辑低价版｜全能图像G四至十图处理_2095833243844169730.json
hash: 6133e524a5bca997
coverage: 0.94898
learned_at: 2026-10-21 00:45:29
nodes: [RH_RhartImageG2ImageToImage, SaveImage, RH_RhartImageG2ImageToImage, LoadImage, LoadImage, LoadImage, LoadImage, CR Text, LoadImage, SaveImage, RH_RhartImageG2ImageToImage, LoadImage, LoadImage, LoadImage, LoadImage, CR Text, LoadImage, LoadImage, SaveImage, RH_RhartImageG2ImageToImage, LoadImage, LoadImage, LoadImage, LoadImage, CR Text, LoadImage, LoadImage, SaveImage, LoadImage, RH_RhartImageG2ImageToImage, LoadImage, LoadImage, LoadImage, LoadImage, CR Text, LoadImage, LoadImage, LoadImage, LoadImage, SaveImage, RH_RhartImageG2ImageToImage, LoadImage, LoadImage, LoadImage, LoadImage, CR Text, LoadImage, LoadImage, LoadImage, LoadImage, SaveImage, LoadImage, RH_RhartImageG2ImageToImage, LoadImage, LoadImage, LoadImage, LoadImage, CR Text, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, SaveImage, LoadImage, Fast Groups Bypasser (rgthree), LoadImage, LoadImage, LoadImage, LoadImage, CR Text, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, JjkText, solarL_SaveImagesToZip, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/image2.0多图编辑低价版｜全能图像G四至十图处理_2095833243844169730.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/image2.0多图编辑低价版｜全能图像G四至十图处理_2095833243844169730.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（98 个）：
- `RH_RhartImageG2ImageToImage`
- `SaveImage`
- `RH_RhartImageG2ImageToImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CR Text`
- `LoadImage`
- `SaveImage`
- `RH_RhartImageG2ImageToImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CR Text`
- `LoadImage`
- `LoadImage`
- `SaveImage`
- `RH_RhartImageG2ImageToImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CR Text`
- `LoadImage`
- `LoadImage`
- `SaveImage`
- `LoadImage`
- `RH_RhartImageG2ImageToImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CR Text`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `SaveImage`
- `RH_RhartImageG2ImageToImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CR Text`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `SaveImage`
- `LoadImage`
- `RH_RhartImageG2ImageToImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CR Text`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `SaveImage`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CR Text`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `JjkText`
- `solarL_SaveImagesToZip`
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

覆盖率 **95%**（93/98）

**有卡**：`RH_RhartImageG2ImageToImage`、`SaveImage`、`LoadImage`、`CR Text`、`UNETLoader`、`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

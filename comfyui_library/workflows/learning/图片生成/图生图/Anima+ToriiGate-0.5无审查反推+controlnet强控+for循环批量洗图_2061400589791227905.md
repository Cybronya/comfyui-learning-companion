---
key: 图片生成/图生图/Anima+ToriiGate-0.5无审查反推+controlnet强控+for循环批量洗图_2061400589791227905.json
name: Anima+ToriiGate-0.5无审查反推+controlnet强控+for循环批量洗图_2061400589791227905
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Anima+ToriiGate-0.5无审查反推+controlnet强控+for循环批量洗图_2061400589791227905.json
hash: 528f98cc58f84645
coverage: 0.884615
learned_at: 2026-10-23 10:51:07
nodes: [VAELoader, CLIPTextEncode, ConcatTextOfUtils, CLIPTextEncode, KSampler, VAEDecode, EmptyLatentImage, SaveImage, CR Prompt Text, ImageListToBatch+, ImageListToBatch+, VHS_GetImageCount, easy forLoopStart, ComfyMathExpression, ImageFromBatch, easy batchAnything, easy forLoopEnd, PreviewImage, PrimitiveInt, easy showAnything, LayerUtility: ImageScaleByAspectRatio V2, ToriiGateT8_LlamaCppVisionGenerate, UNETLoader, CLIPLoader, AnimaLLLiteApply, HAIGC_LoadImagesFromZip]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 1920, "sampler_name": "dpmpp_2m_sde_gpu", "scheduler": "beta57", "seed": 630720803433662, "steps": 40, "width": 1080}
---

# 图片生成/图生图/Anima+ToriiGate-0.5无审查反推+controlnet强控+for循环批量洗图_2061400589791227905.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Anima+ToriiGate-0.5无审查反推+controlnet强控+for循环批量洗图_2061400589791227905.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `VAELoader`
- `CLIPTextEncode` ★核心
- `ConcatTextOfUtils`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `SaveImage`
- `CR Prompt Text`
- `ImageListToBatch+`
- `ImageListToBatch+`
- `VHS_GetImageCount`
- `easy forLoopStart`
- `ComfyMathExpression`
- `ImageFromBatch`
- `easy batchAnything`
- `easy forLoopEnd`
- `PreviewImage`
- `PrimitiveInt`
- `easy showAnything`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ToriiGateT8_LlamaCppVisionGenerate`
- `UNETLoader` ★核心
- `CLIPLoader`
- `AnimaLLLiteApply`
- `HAIGC_LoadImagesFromZip`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `630720803433662`
- `steps` = `40`
- `cfg` = `4.5`
- `sampler_name` = `dpmpp_2m_sde_gpu`
- `scheduler` = `beta57`
- `denoise` = `1`
- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`

## 知识

覆盖率 **88%**（23/26）

**有卡**：`VAELoader`、`CLIPTextEncode`、`ConcatTextOfUtils`、`KSampler`、`VAEDecode`、`EmptyLatentImage`、`SaveImage`、`CR Prompt Text`、`ImageListToBatch+`、`VHS_GetImageCount`、`easy forLoopStart`、`ComfyMathExpression`、`ImageFromBatch`、`easy batchAnything`、`easy forLoopEnd`、`LayerUtility: ImageScaleByAspectRatio V2`、`ToriiGateT8_LlamaCppVisionGenerate`、`UNETLoader`、`CLIPLoader`、`AnimaLLLiteApply`、`HAIGC_LoadImagesFromZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader、CR Prompt Text

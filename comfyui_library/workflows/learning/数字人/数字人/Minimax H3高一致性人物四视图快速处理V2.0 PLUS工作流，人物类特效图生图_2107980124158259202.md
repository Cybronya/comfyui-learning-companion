---
key: 数字人/数字人/Minimax H3高一致性人物四视图快速处理V2.0 PLUS工作流，人物类特效图生图_2107980124158259202.json
name: Minimax H3高一致性人物四视图快速处理V2.0 PLUS工作流，人物类特效图生图_2107980124158259202
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/Minimax H3高一致性人物四视图快速处理V2.0 PLUS工作流，人物类特效图生图_2107980124158259202.json
hash: 2b36b713a5d7600c
coverage: 0.728395
learned_at: 2026-10-19 00:41:03
nodes: [MiniMaxH3ReferenceToVideo, VAELoader, VAELoader, GetNode, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, SetNode, VAEDecodeAudio, VAEDecode, SamplerCustomAdvanced, BasicScheduler, BasicGuider, RandomNoise, KSamplerSelect, LoadImage, LoadImage, LoadImage, LoadImage, PrimitiveFloat, ComfyMathExpression, VHS_VideoCombine, Any Switch (rgthree), ImageConcatFromBatch, ImageConcatFromBatch, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, CLIPLoader, MiniMaxH3MemoryEfficientSageAttentionPatch, CreateVideo, GetVideoComponents, Fast Groups Bypasser (rgthree), ResizeImageMaskNode, workflow>SeedVR放大节点, GetImagesFromBatchIndexed, Any Switch (rgthree), ResolutionSelector, UNETLoader, LoraLoaderModelOnly, AutoCropFaces, PreviewImage, SaveImage, Image Comparer (rgthree), SaveImage, Fast Groups Bypasser (rgthree), Fast Muter (rgthree), PrimitiveStringMultiline, LoadImage, LoadImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 数字人/数字人/Minimax H3高一致性人物四视图快速处理V2.0 PLUS工作流，人物类特效图生图_2107980124158259202.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/Minimax H3高一致性人物四视图快速处理V2.0 PLUS工作流，人物类特效图生图_2107980124158259202.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（81 个）：
- `MiniMaxH3ReferenceToVideo`
- `VAELoader`
- `VAELoader`
- `GetNode`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `SetNode`
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `BasicScheduler`
- `BasicGuider`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PrimitiveFloat`
- `ComfyMathExpression`
- `VHS_VideoCombine`
- `Any Switch (rgthree)`
- `ImageConcatFromBatch`
- `ImageConcatFromBatch`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `CLIPLoader`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `CreateVideo`
- `GetVideoComponents`
- `Fast Groups Bypasser (rgthree)`
- `ResizeImageMaskNode`
- `workflow>SeedVR放大节点`
- `GetImagesFromBatchIndexed`
- `Any Switch (rgthree)`
- `ResolutionSelector`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `AutoCropFaces`
- `PreviewImage`
- `SaveImage`
- `Image Comparer (rgthree)`
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`
- `Fast Muter (rgthree)`
- `PrimitiveStringMultiline`
- `LoadImage`
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
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `CLIPLoader`
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

覆盖率 **73%**（59/81）

**有卡**：`MiniMaxH3ReferenceToVideo`、`VAELoader`、`VAEDecodeAudio`、`VAEDecode`、`SamplerCustomAdvanced`、`BasicScheduler`、`BasicGuider`、`RandomNoise`、`KSamplerSelect`、`LoadImage`、`ComfyMathExpression`、`VHS_VideoCombine`、`ImageConcatFromBatch`、`CLIPLoader`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`CreateVideo`、`GetVideoComponents`、`ResizeImageMaskNode`、`workflow>SeedVR放大节点`、`GetImagesFromBatchIndexed`、`ResolutionSelector`、`UNETLoader`、`LoraLoaderModelOnly`、`AutoCropFaces`、`SaveImage`、`Fast Muter (rgthree)`、`KSampler`、`EmptyLatentImage`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

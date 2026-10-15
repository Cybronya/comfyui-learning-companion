---
key: 图片生成/文生图/Qwen Image InstantX Controlnet线稿控制V1_1960762275642707970.json
name: Qwen Image InstantX Controlnet线稿控制V1_1960762275642707970
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image InstantX Controlnet线稿控制V1_1960762275642707970.json
hash: dd3625688ebcccb6
coverage: 0.862069
learned_at: 2026-10-10 20:58:55
nodes: [CLIPTextEncode, EmptySD3LatentImage, CLIPLoader, VAELoader, UNETLoader, ControlNetApplySD3, PreviewImage, SeedVR2BlockSwap, PreviewImage, ModelSamplingAuraFlow, ControlNetLoader, VAEDecode, SeedVR2GGUF, Image Compare (mtb), SetUnionControlNetType, SaveLatent, ImageConcanate, LoraLoaderModelOnly, SaveImage, CLIPTextEncode, CFGNorm, ModelSamplingAuraFlow, SaveImage, PreviewImage, AIO_Preprocessor, LoadImage, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler]
patterns: []
missing: [Image Compare (mtb)]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "controlnet_strength": 0.75, "denoise": 1, "sampler_name": "res_2s", "scheduler": "beta57", "seed": 397623419622816, "steps": 8}
discoveries: [次要节点 `Image Compare (mtb)` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen Image InstantX Controlnet线稿控制V1_1960762275642707970.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image InstantX Controlnet线稿控制V1_1960762275642707970.json`

## 结构

**节点**（29 个）：
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader`
- `ControlNetApplySD3`
- `PreviewImage`
- `SeedVR2BlockSwap`
- `PreviewImage`
- `ModelSamplingAuraFlow`
- `ControlNetLoader`
- `VAEDecode`
- `SeedVR2GGUF`
- `Image Compare (mtb)`
- `SetUnionControlNetType`
- `SaveLatent`
- `ImageConcanate`
- `LoraLoaderModelOnly`
- `SaveImage`
- `CLIPTextEncode`
- `CFGNorm`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `PreviewImage`
- `AIO_Preprocessor`
- `LoadImage`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `KSampler`

## 关键参数

- `cfg` = `1`
- `controlnet_strength` = `0.75`
- `denoise` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `beta57`
- `seed` = `397623419622816`
- `steps` = `8`

## 知识

覆盖率 **86%**（25/29）

**有卡**：`CLIPTextEncode`、`EmptySD3LatentImage`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`ControlNetApplySD3`、`PreviewImage`、`SeedVR2BlockSwap`、`ModelSamplingAuraFlow`、`ControlNetLoader`、`VAEDecode`、`SeedVR2GGUF`、`Image Compare (mtb)`、`SetUnionControlNetType`、`SaveLatent`、`ImageConcanate`、`LoraLoaderModelOnly`、`SaveImage`、`CFGNorm`、`AIO_Preprocessor`

**缺卡**（1）：`Image Compare (mtb)`

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `Image Compare (mtb)` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

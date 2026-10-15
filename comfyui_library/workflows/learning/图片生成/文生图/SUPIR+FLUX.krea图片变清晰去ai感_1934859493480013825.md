---
key: 图片生成/文生图/SUPIR+FLUX.krea图片变清晰去ai感_1934859493480013825.json
name: SUPIR+FLUX.krea图片变清晰去ai感_1934859493480013825
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/SUPIR+FLUX.krea图片变清晰去ai感_1934859493480013825.json
hash: 0480c1fd561bc97b
coverage: 0.833333
learned_at: 2026-10-10 20:59:11
nodes: [UpscaleModelLoader, UpscaleModelLoader, SUPIR_model_loader_v2, CheckpointLoaderSimple, SUPIR_first_stage, SUPIR_conditioner, SUPIR_encode, SUPIR_sample, SUPIR_decode, ImageUpscaleWithModel, ImageScaleBy, ImageUpscaleWithModel, ImageScaleBy, LoadImage, ImageResize+, easy int, CR Image Input Switch, KSampler, ColorMatch, VAEDecodeTiled, NunchakuTextEncoderLoader, VAELoader, VAEEncodeTiled, PreviewImage, SaveImage, NunchakuFluxDiTLoader, CLIPTextEncode, CLIPTextEncode, NunchakuFluxLoraLoader, Image Comparer (rgthree)]
patterns: []
missing: [CR Image Input Switch, easy int, ImageResize+]
problems: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "XLL dreamshaperXL_lightningDPMSDE.safetensors", "denoise": 0.25000000000000006, "sampler_name": "euler", "scheduler": "beta", "seed": 1106494094380806, "steps": 20}
discoveries: [次要节点 `CR Image Input Switch` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 图片生成/文生图/SUPIR+FLUX.krea图片变清晰去ai感_1934859493480013825.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/SUPIR+FLUX.krea图片变清晰去ai感_1934859493480013825.json`

## 结构

**节点**（30 个）：
- `UpscaleModelLoader`
- `UpscaleModelLoader`
- `SUPIR_model_loader_v2`
- `CheckpointLoaderSimple`
- `SUPIR_first_stage`
- `SUPIR_conditioner`
- `SUPIR_encode`
- `SUPIR_sample`
- `SUPIR_decode`
- `ImageUpscaleWithModel`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `ImageScaleBy`
- `LoadImage`
- `ImageResize+`
- `easy int`
- `CR Image Input Switch`
- `KSampler`
- `ColorMatch`
- `VAEDecodeTiled`
- `NunchakuTextEncoderLoader`
- `VAELoader`
- `VAEEncodeTiled`
- `PreviewImage`
- `SaveImage`
- `NunchakuFluxDiTLoader`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `NunchakuFluxLoraLoader`
- `Image Comparer (rgthree)`

## 关键参数

- `cfg` = `1`
- `checkpoint` = `XLL dreamshaperXL_lightningDPMSDE.safetensors`
- `denoise` = `0.25000000000000006`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `seed` = `1106494094380806`
- `steps` = `20`

## 知识

覆盖率 **83%**（25/30）

**有卡**：`UpscaleModelLoader`、`SUPIR_model_loader_v2`、`CheckpointLoaderSimple`、`SUPIR_first_stage`、`SUPIR_conditioner`、`SUPIR_encode`、`SUPIR_sample`、`SUPIR_decode`、`ImageUpscaleWithModel`、`ImageScaleBy`、`LoadImage`、`ImageResize+`、`easy int`、`CR Image Input Switch`、`KSampler`、`ColorMatch`、`VAEDecodeTiled`、`NunchakuTextEncoderLoader`、`VAELoader`、`VAEEncodeTiled`、`PreviewImage`、`SaveImage`

**缺卡**（3）：`CR Image Input Switch`、`easy int`、`ImageResize+`

## 参数体检

发现 1 个问题：
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- 次要节点 `CR Image Input Switch` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

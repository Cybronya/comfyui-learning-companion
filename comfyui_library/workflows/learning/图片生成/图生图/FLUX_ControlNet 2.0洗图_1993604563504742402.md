---
key: 图片生成/图生图/FLUX_ControlNet 2.0洗图_1993604563504742402.json
name: FLUX_ControlNet 2.0洗图_1993604563504742402
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX_ControlNet 2.0洗图_1993604563504742402.json
hash: 91e311e1864388cf
coverage: 0.888889
learned_at: 2026-10-23 10:54:43
nodes: [CLIPTextEncodeFlux, SaveImage, VAELoader, EmptyLatentImage, DualCLIPLoader, PreviewImage, ControlNetApplySD3, VAEDecode, easy cleanGpuUsed, LoraLoaderModelOnly, PreviewImage, LayerMask: SegmentAnythingUltra V2, RH_Captioner, LayerUtility: ImageRemoveAlpha, PreviewImage, ControlNetApplySD3, ControlNetLoader, UNETLoader, LayerUtility: ColorPicker, LoadImage, GetImageSize, KSampler, AIO_Preprocessor, SetUnionControlNetType, SetUnionControlNetType, AIO_Preprocessor, CLIPTextEncode]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "controlnet_strength": 1, "denoise": 1, "height": 1536, "sampler_name": "euler", "scheduler": "beta", "seed": 977041924351538, "steps": 20, "width": 1024}
---

# 图片生成/图生图/FLUX_ControlNet 2.0洗图_1993604563504742402.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX_ControlNet 2.0洗图_1993604563504742402.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `CLIPTextEncodeFlux` ★核心
- `SaveImage`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `DualCLIPLoader`
- `PreviewImage`
- `ControlNetApplySD3` ★核心
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `LoraLoaderModelOnly` ★核心
- `PreviewImage`
- `LayerMask: SegmentAnythingUltra V2`
- `RH_Captioner`
- `LayerUtility: ImageRemoveAlpha`
- `PreviewImage`
- `ControlNetApplySD3` ★核心
- `ControlNetLoader`
- `UNETLoader` ★核心
- `LayerUtility: ColorPicker`
- `LoadImage`
- `GetImageSize`
- `KSampler` ★核心
- `AIO_Preprocessor`
- `SetUnionControlNetType`
- `SetUnionControlNetType`
- `AIO_Preprocessor`
- `CLIPTextEncode` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`
- `controlnet_strength` = `1`
- `seed` = `977041924351538`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **89%**（24/27）

**有卡**：`CLIPTextEncodeFlux`、`SaveImage`、`VAELoader`、`EmptyLatentImage`、`DualCLIPLoader`、`ControlNetApplySD3`、`VAEDecode`、`easy cleanGpuUsed`、`LoraLoaderModelOnly`、`LayerMask: SegmentAnythingUltra V2`、`RH_Captioner`、`LayerUtility: ImageRemoveAlpha`、`ControlNetLoader`、`UNETLoader`、`LayerUtility: ColorPicker`、`LoadImage`、`GetImageSize`、`KSampler`、`AIO_Preprocessor`、`SetUnionControlNetType`、`CLIPTextEncode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、EmptyLatentImage、LoadImage

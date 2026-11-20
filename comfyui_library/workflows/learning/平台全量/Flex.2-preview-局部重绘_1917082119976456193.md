---
key: 平台全量/Flex.2-preview-局部重绘_1917082119976456193.json
name: Flex.2-preview-局部重绘_1917082119976456193
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Flex.2-preview-局部重绘_1917082119976456193.json
hash: 366671439defee0b
coverage: 0.944444
learned_at: 2026-11-14 00:27:22
nodes: [DualCLIPLoader, UNETLoader, CLIPTextEncode, VAELoader, VAEDecode, KSampler, LoadFlorence2Model, MaskToImage, PreviewImage, ImageScaleToTotalPixels, LayerMask: SAM2VideoUltra, Flex2Conditioner, LoraLoaderModelOnly, CLIPTextEncode, GrowMaskWithBlur, LayerMask: ObjectDetectorFL2, LoadImage, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "deis", "scheduler": "beta", "seed": 1083558217549307, "steps": 25}
---

# 平台全量/Flex.2-preview-局部重绘_1917082119976456193.json

> 来源文件 `comfyui_library/workflows/平台全量/Flex.2-preview-局部重绘_1917082119976456193.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `LoadFlorence2Model`
- `MaskToImage`
- `PreviewImage`
- `ImageScaleToTotalPixels`
- `LayerMask: SAM2VideoUltra`
- `Flex2Conditioner`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `GrowMaskWithBlur`
- `LayerMask: ObjectDetectorFL2`
- `LoadImage`
- `SaveImage`

## 关键参数

- `seed` = `1083558217549307`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `deis`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **94%**（17/18）

**有卡**：`DualCLIPLoader`、`UNETLoader`、`CLIPTextEncode`、`VAELoader`、`VAEDecode`、`KSampler`、`LoadFlorence2Model`、`MaskToImage`、`ImageScaleToTotalPixels`、`LayerMask: SAM2VideoUltra`、`Flex2Conditioner`、`LoraLoaderModelOnly`、`GrowMaskWithBlur`、`LayerMask: ObjectDetectorFL2`、`LoadImage`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、SaveImage

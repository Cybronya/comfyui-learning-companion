---
key: 平台全量/Flex.2-preview+Redux-512强劲参考_1917238666479992833.json
name: Flex.2-preview+Redux-512强劲参考_1917238666479992833
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Flex.2-preview+Redux-512强劲参考_1917238666479992833.json
hash: 1314837bede08d19
coverage: 1
learned_at: 2026-11-14 00:27:22
nodes: [KSampler, UNETLoader, DualCLIPLoader, VAELoader, CLIPTextEncode, AdvancedVisionLoader, StyleModelLoader, CLIPTextEncode, VAEDecode, CLIPVisionEncode, Flex2Conditioner, StyleModelApply, EmptyLatentImage, ImageResizeKJ, LoadImage, SaveImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 512, "sampler_name": "deis", "scheduler": "beta", "seed": 394608250364696, "steps": 25, "width": 512}
---

# 平台全量/Flex.2-preview+Redux-512强劲参考_1917238666479992833.json

> 来源文件 `comfyui_library/workflows/平台全量/Flex.2-preview+Redux-512强劲参考_1917238666479992833.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（16 个）：
- `KSampler` ★核心
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `AdvancedVisionLoader`
- `StyleModelLoader`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `CLIPVisionEncode`
- `Flex2Conditioner`
- `StyleModelApply`
- `EmptyLatentImage` ★核心
- `ImageResizeKJ`
- `LoadImage`
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `394608250364696`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `deis`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `512`
- `height` = `512`
- `batch_size` = `1`

## 知识

覆盖率 **100%**（16/16）

**有卡**：`KSampler`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`CLIPTextEncode`、`AdvancedVisionLoader`、`StyleModelLoader`、`VAEDecode`、`CLIPVisionEncode`、`Flex2Conditioner`、`StyleModelApply`、`EmptyLatentImage`、`ImageResizeKJ`、`LoadImage`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、EmptyLatentImage、LoadImage、UNETLoader、CLIPVisionEncode

---
key: 平台全量/DreamO1.1官方10秒加速_IP&ID&Try-On和Style轻松搞定_字节开源服装一致性_1928807838402121730.json
name: DreamO1.1官方10秒加速_IP&ID&Try-On和Style轻松搞定_字节开源服装一致性_1928807838402121730
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/DreamO1.1官方10秒加速_IP&ID&Try-On和Style轻松搞定_字节开源服装一致性_1928807838402121730.json
hash: 62bfcf20956b62bf
coverage: 0.923077
learned_at: 2026-11-14 00:23:51
nodes: [FluxGuidance, CLIPTextEncode, FluxGuidance, CLIPTextEncode, ApplyDreamO, VAELoader, DualCLIPLoader, DreamOProcessorLoader, VAEDecode, PreviewImage, SaveImage, ImageConcanate, SaveImage, SaveImage, VAEDecode, DreamOProcessorLoader, PreviewImage, ImageScaleDownToSize, DualCLIPLoader, ImageConcanate, ImageConcanate, ImageScaleDownToSize, CLIPTextEncode, KSampler, ImageScaleDownToSize, LoadImage, LoadImage, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, VAELoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Fast Groups Bypasser (rgthree), LoadImage, CLIPTextEncode, CR SDXL Aspect Ratio, PreviewImage, SaveImage, CR SDXL Aspect Ratio, ApplyDreamO, DreamORefEncode, DreamORefEncode, DreamORefEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1003176042640026, "steps": 15}
---

# 平台全量/DreamO1.1官方10秒加速_IP&ID&Try-On和Style轻松搞定_字节开源服装一致性_1928807838402121730.json

> 来源文件 `comfyui_library/workflows/平台全量/DreamO1.1官方10秒加速_IP&ID&Try-On和Style轻松搞定_字节开源服装一致性_1928807838402121730.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（52 个）：
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `ApplyDreamO`
- `VAELoader`
- `DualCLIPLoader`
- `DreamOProcessorLoader`
- `VAEDecode` ★核心
- `PreviewImage`
- `SaveImage`
- `ImageConcanate`
- `SaveImage`
- `SaveImage`
- `VAEDecode` ★核心
- `DreamOProcessorLoader`
- `PreviewImage`
- `ImageScaleDownToSize`
- `DualCLIPLoader`
- `ImageConcanate`
- `ImageConcanate`
- `ImageScaleDownToSize`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `ImageScaleDownToSize`
- `LoadImage`
- `LoadImage`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `CR SDXL Aspect Ratio`
- `PreviewImage`
- `SaveImage`
- `CR SDXL Aspect Ratio`
- `ApplyDreamO`
- `DreamORefEncode`
- `DreamORefEncode`
- `DreamORefEncode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心

## 关键参数

- `seed` = `1003176042640026`
- `steps` = `15`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（48/52）

**有卡**：`FluxGuidance`、`CLIPTextEncode`、`ApplyDreamO`、`VAELoader`、`DualCLIPLoader`、`DreamOProcessorLoader`、`VAEDecode`、`SaveImage`、`ImageConcanate`、`ImageScaleDownToSize`、`KSampler`、`LoadImage`、`UNETLoader`、`LoraLoaderModelOnly`、`CR SDXL Aspect Ratio`、`DreamORefEncode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance

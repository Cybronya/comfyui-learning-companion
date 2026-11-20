---
key: 平台全量/【阡陌】小红书FireRed-Image-Edit-1.1双图_多图图像编辑工作流_2031561725320892418.json
name: 【阡陌】小红书FireRed-Image-Edit-1.1双图_多图图像编辑工作流_2031561725320892418
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/【阡陌】小红书FireRed-Image-Edit-1.1双图_多图图像编辑工作流_2031561725320892418.json
hash: c084c1fcaa35f284
coverage: 0.740741
learned_at: 2026-11-14 01:26:30
nodes: [LoraLoaderModelOnly, CLIPLoader, PrimitiveInt, PrimitiveInt, PrimitiveFloat, PrimitiveFloat, ComfySwitchNode, ComfySwitchNode, VAELoader, ComfySwitchNode, PrimitiveBoolean, LoadImage, ModelSamplingAuraFlow, CFGNorm, SaveImage, UNETLoader, VAEDecode, FluxKontextImageScale, KSampler, MuyeSizeSelector, LoadImage, ConditioningZeroOut, LoadImage, LoadImage, EmptyLatentImage, VAEEncode, TextEncodeQwenImageEditPlus]
patterns: [image_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 4, "denoise": 1, "height": 1600, "sampler_name": "euler", "scheduler": "simple", "seed": 139422194755976, "steps": 40, "width": 1200}
---

# 平台全量/【阡陌】小红书FireRed-Image-Edit-1.1双图_多图图像编辑工作流_2031561725320892418.json

> 来源文件 `comfyui_library/workflows/平台全量/【阡陌】小红书FireRed-Image-Edit-1.1双图_多图图像编辑工作流_2031561725320892418.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Output → Other

**节点**（27 个）：
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `VAELoader`
- `ComfySwitchNode`
- `PrimitiveBoolean`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `SaveImage`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `FluxKontextImageScale`
- `KSampler` ★核心
- `MuyeSizeSelector`
- `LoadImage`
- `ConditioningZeroOut`
- `LoadImage`
- `LoadImage`
- `EmptyLatentImage` ★核心
- `VAEEncode` ★核心
- `TextEncodeQwenImageEditPlus`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `139422194755976`
- `steps` = `40`
- `cfg` = `4`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1200`
- `height` = `1600`
- `batch_size` = `1`

## 知识

覆盖率 **74%**（20/27）

**有卡**：`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`PrimitiveBoolean`、`LoadImage`、`ModelSamplingAuraFlow`、`CFGNorm`、`SaveImage`、`UNETLoader`、`VAEDecode`、`FluxKontextImageScale`、`KSampler`、`MuyeSizeSelector`、`ConditioningZeroOut`、`EmptyLatentImage`、`VAEEncode`、`TextEncodeQwenImageEditPlus`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

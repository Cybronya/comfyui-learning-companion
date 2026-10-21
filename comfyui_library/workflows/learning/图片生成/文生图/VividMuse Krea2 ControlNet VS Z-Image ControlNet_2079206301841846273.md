---
key: 图片生成/文生图/VividMuse Krea2 ControlNet VS Z-Image ControlNet_2079206301841846273.json
name: VividMuse Krea2 ControlNet VS Z-Image ControlNet_2079206301841846273
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/VividMuse Krea2 ControlNet VS Z-Image ControlNet_2079206301841846273.json
hash: 0fa43e92a20bcf0e
coverage: 0.934783
learned_at: 2026-10-20 00:20:10
nodes: [UNETLoader, CLIPLoader, VAELoader, CLIPTextEncode, ConditioningZeroOut, AIO_Preprocessor, Krea2ControlImageEncode, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, UNETLoader, VAELoader, easy loraStack, SaveImage, easy loraStackApply, easy loraStackApply, ModelPatchLoader, EmptyLatentImage, AIO_Preprocessor, QwenImageDiffsynthControlnet, KSamplerAdvanced, UNETLoader, easy imageRemBg, SaveImage, VAEDecode, VAEDecode, easy imageRemBg, Krea2ControlApply, Krea2ControlLoRALoader, KSamplerAdvanced, KSamplerAdvanced, easy loraStack, Seed (rgthree), PrimitiveStringMultiline, ResolutionSelector, ImageResize+, ImageResize+, Image Comparer (rgthree), easy promptList, Fast Groups Bypasser (rgthree), easy promptList, easy promptList, LoadImage, KSamplerAdvanced, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 8, "denoise": "beta57", "height": 512, "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed", "width": 512}
---

# 图片生成/文生图/VividMuse Krea2 ControlNet VS Z-Image ControlNet_2079206301841846273.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/VividMuse Krea2 ControlNet VS Z-Image ControlNet_2079206301841846273.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（46 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `AIO_Preprocessor`
- `Krea2ControlImageEncode`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `UNETLoader` ★核心
- `VAELoader`
- `easy loraStack`
- `SaveImage`
- `easy loraStackApply`
- `easy loraStackApply`
- `ModelPatchLoader`
- `EmptyLatentImage` ★核心
- `AIO_Preprocessor`
- `QwenImageDiffsynthControlnet`
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `easy imageRemBg`
- `SaveImage`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `easy imageRemBg`
- `Krea2ControlApply`
- `Krea2ControlLoRALoader` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `easy loraStack`
- `Seed (rgthree)`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `ImageResize+`
- `ImageResize+`
- `Image Comparer (rgthree)`
- `easy promptList`
- `Fast Groups Bypasser (rgthree)`
- `easy promptList`
- `easy promptList`
- `LoadImage`
- `KSamplerAdvanced` ★核心
- `LoadImage`
- `LoadImage`

## 关键参数

- `width` = `512`
- `height` = `512`
- `batch_size` = `1`
- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `beta57`

## 知识

覆盖率 **93%**（43/46）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`ConditioningZeroOut`、`AIO_Preprocessor`、`Krea2ControlImageEncode`、`easy loraStack`、`SaveImage`、`easy loraStackApply`、`ModelPatchLoader`、`EmptyLatentImage`、`QwenImageDiffsynthControlnet`、`KSamplerAdvanced`、`easy imageRemBg`、`VAEDecode`、`Krea2ControlApply`、`Krea2ControlLoRALoader`、`Seed (rgthree)`、`ResolutionSelector`、`ImageResize+`、`easy promptList`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、ResolutionSelector、LoadImage

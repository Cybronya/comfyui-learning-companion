---
key: 图片生成/图生图/Qwen Image 2.1职业照换脸保五官，SeedVR2超分保住皮肤质感_2117120288856039425.json
name: Qwen Image 2.1职业照换脸保五官，SeedVR2超分保住皮肤质感_2117120288856039425
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1职业照换脸保五官，SeedVR2超分保住皮肤质感_2117120288856039425.json
hash: 0ec0ad43c55eb3e8
coverage: 0.525
learned_at: 2026-11-02 19:12:46
nodes: [EmptyFlux2LatentImage, VAEDecode, SamplerCustomAdvanced, InpaintCropImproved, InpaintStitchImproved, InpaintCropImproved, PreviewImage, Reroute, Reroute, ComfyMathExpression, GetImageSize+, ComfyMathExpression, PreviewImage, PreviewImage, AnySwitch, PreviewImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SaveImage, CLIPLoader, LoraLoaderModelOnly, PrimitiveStringMultiline, RandomNoise, ManualSigmas, CFGGuider, KSamplerSelect, CLIPTextEncode, CLIPTextEncode, PrimitiveStringMultiline, CLIPLoader, PrimitiveStringMultiline, ComfySwitchNode, UNETLoader, easy isNone, CLIPLoader, ComfySwitchNode, VAELoader, TextGenerate, TextEncodeQwenImage21, UNETLoader, JsonExtractString, ComfySwitchNode, ComfySwitchNode, ComfySwitchNode, ComfySwitchNode, LoadImage, Any Switch (rgthree), LoadImage, SkipLayerGuidanceDiTSimple, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, VAELoader, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, 孤海注释, 孤海注释]
patterns: []
missing: []
---

# 图片生成/图生图/Qwen Image 2.1职业照换脸保五官，SeedVR2超分保住皮肤质感_2117120288856039425.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1职业照换脸保五官，SeedVR2超分保住皮肤质感_2117120288856039425.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（80 个）：
- `EmptyFlux2LatentImage`
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `InpaintCropImproved`
- `InpaintStitchImproved`
- `InpaintCropImproved`
- `PreviewImage`
- `Reroute`
- `Reroute`
- `ComfyMathExpression`
- `GetImageSize+`
- `ComfyMathExpression`
- `PreviewImage`
- `PreviewImage`
- `AnySwitch`
- `PreviewImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SaveImage`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ManualSigmas`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `PrimitiveStringMultiline`
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `ComfySwitchNode`
- `UNETLoader` ★核心
- `easy isNone`
- `CLIPLoader`
- `ComfySwitchNode`
- `VAELoader`
- `TextGenerate`
- `TextEncodeQwenImage21`
- `UNETLoader` ★核心
- `JsonExtractString`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `LoadImage`
- `Any Switch (rgthree)`
- `LoadImage`
- `SkipLayerGuidanceDiTSimple`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `VAELoader`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `孤海注释`
- `孤海注释`

## 知识

覆盖率 **52%**（42/80）

**有卡**：`EmptyFlux2LatentImage`、`VAEDecode`、`SamplerCustomAdvanced`、`InpaintCropImproved`、`InpaintStitchImproved`、`ComfyMathExpression`、`GetImageSize+`、`AnySwitch`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`SaveImage`、`CLIPLoader`、`LoraLoaderModelOnly`、`RandomNoise`、`ManualSigmas`、`CFGGuider`、`KSamplerSelect`、`CLIPTextEncode`、`UNETLoader`、`easy isNone`、`VAELoader`、`TextGenerate`、`TextEncodeQwenImage21`、`JsonExtractString`、`LoadImage`、`SkipLayerGuidanceDiTSimple`

**用到的条目**：TextEncodeQwenImage21、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、CLIPTextEncode、LoadImage

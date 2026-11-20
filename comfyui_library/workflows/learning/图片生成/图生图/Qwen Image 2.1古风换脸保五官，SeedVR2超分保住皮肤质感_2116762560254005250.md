---
key: 图片生成/图生图/Qwen Image 2.1古风换脸保五官，SeedVR2超分保住皮肤质感_2116762560254005250.json
name: Qwen Image 2.1古风换脸保五官，SeedVR2超分保住皮肤质感_2116762560254005250
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1古风换脸保五官，SeedVR2超分保住皮肤质感_2116762560254005250.json
hash: c7560fd1ac0c2cf2
coverage: 0.69697
learned_at: 2026-11-02 19:12:44
nodes: [EmptyFlux2LatentImage, VAEDecode, SamplerCustomAdvanced, ImageColorMatch+, ImageRemoveAlpha+, InpaintCropImproved, InpaintStitchImproved, InpaintCropImproved, PreviewImage, Reroute, Reroute, ComfyMathExpression, GetImageSize+, ComfyMathExpression, PreviewImage, PreviewImage, AnySwitch, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SaveImage, CLIPLoader, LoraLoaderModelOnly, PrimitiveStringMultiline, RandomNoise, ManualSigmas, CFGGuider, KSamplerSelect, CLIPTextEncode, CLIPTextEncode, PrimitiveStringMultiline, CLIPLoader, PrimitiveStringMultiline, ComfySwitchNode, UNETLoader, easy isNone, CLIPLoader, ComfySwitchNode, VAELoader, TextGenerate, TextEncodeQwenImage21, UNETLoader, JsonExtractString, ComfySwitchNode, ComfySwitchNode, ComfySwitchNode, ComfySwitchNode, LoadImage, Any Switch (rgthree), LoadImage, SkipLayerGuidanceDiTSimple, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, 孤海注释, 孤海注释, VAELoader, SaveImage, 孤海注释, 孤海注释]
patterns: []
missing: []
---

# 图片生成/图生图/Qwen Image 2.1古风换脸保五官，SeedVR2超分保住皮肤质感_2116762560254005250.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1古风换脸保五官，SeedVR2超分保住皮肤质感_2116762560254005250.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（66 个）：
- `EmptyFlux2LatentImage`
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `ImageColorMatch+`
- `ImageRemoveAlpha+`
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
- `SaveImage`
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
- `孤海注释`
- `孤海注释`
- `VAELoader`
- `SaveImage`
- `孤海注释`
- `孤海注释`

## 知识

覆盖率 **70%**（46/66）

**有卡**：`EmptyFlux2LatentImage`、`VAEDecode`、`SamplerCustomAdvanced`、`ImageColorMatch+`、`ImageRemoveAlpha+`、`InpaintCropImproved`、`InpaintStitchImproved`、`ComfyMathExpression`、`GetImageSize+`、`AnySwitch`、`SaveImage`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`CLIPLoader`、`LoraLoaderModelOnly`、`RandomNoise`、`ManualSigmas`、`CFGGuider`、`KSamplerSelect`、`CLIPTextEncode`、`UNETLoader`、`easy isNone`、`VAELoader`、`TextGenerate`、`TextEncodeQwenImage21`、`JsonExtractString`、`LoadImage`、`SkipLayerGuidanceDiTSimple`

**用到的条目**：TextEncodeQwenImage21、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、CLIPTextEncode、LoadImage

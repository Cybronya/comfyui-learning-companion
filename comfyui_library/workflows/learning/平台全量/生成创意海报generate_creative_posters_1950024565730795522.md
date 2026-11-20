---
key: 平台全量/生成创意海报generate_creative_posters_1950024565730795522.json
name: 生成创意海报generate_creative_posters_1950024565730795522
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/生成创意海报generate_creative_posters_1950024565730795522.json
hash: 8bf37dd9435e7637
coverage: 0.710843
learned_at: 2026-11-14 02:22:08
nodes: [SetNode, RH_Prompter, MZ_ChatGLM3_V2, MZ_ChatGLM3_V2, UNETLoader, LayerMask: MaskGrow, JjkText, TextCombinerSix, JjkText, RH_Captioner, JjkText, RH_Captioner, CLIPTextEncode, CLIPTextEncode, MZ_KolorsCLIPVisionLoader, MZ_IPAdapterModelLoaderKolors, MZ_ChatGLM3Loader, VAELoader, Reroute, Reroute, GetImageSize, PrimitiveNode, Display Int (rgthree), Display Int (rgthree), SetNode, MZ_KolorsControlNetPatch, ControlNetLoader, PreviewImage, MaskToImage, LayerColor: ColorAdapter, MaskPreview+, MZ_KolorsUNETLoaderV2, FluxGuidance, VAEEncodeForInpaint, SetNode, ImageResize+, SetNode, SaveImage, VAEDecode, LayerMask: MaskPreview, SetNode, easy cleanGpuUsed, AV_VAELoader, LoraLoader, DualCLIPLoader, CLIPTextEncode, MaskToSEGS, ControlNetApplyAdvanced, PreviewImage, PreviewImage, ImagePadForOutpaint, LoadImage, GetNode, LayerMask: SegmentAnythingUltra V2, Reroute, ShowText|pysssss, VAEEncode, RandomNoise, KSamplerSelect, BasicGuider, VAELoader, easy cleanGpuUsed, LoadImage, LayerUtility: ImageBlendAdvance, Reroute, PreviewImage, MaskPreview+, PreviewImage, Mask Invert, MZ_IPAdapterAdvancedKolors, Label (rgthree), BasicScheduler, CheckpointLoaderSimple, VAEDecode, PreviewImage, Image Comparer (rgthree), SamplerCustomAdvanced, LoraLoaderModelOnly, KSampler, PreviewImage, DetailerForEach, PreviewImage, Label (rgthree)]
patterns: [image_to_image, lora]
missing: []
parameters: {"cfg": 3, "checkpoint": "Adam-Doll.XL丨玩偶盲盒丨3D手办_V2.safetensors", "controlnet_strength": 0.5, "denoise": 1, "lora_name": null, "sampler_name": "euler_ancestral", "scheduler": "normal", "seed": 727373523822780, "steps": 20, "strength_clip": 1, "strength_model": 1}
---

# 平台全量/生成创意海报generate_creative_posters_1950024565730795522.json

> 来源文件 `comfyui_library/workflows/平台全量/生成创意海报generate_creative_posters_1950024565730795522.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（83 个）：
- `SetNode`
- `RH_Prompter`
- `MZ_ChatGLM3_V2`
- `MZ_ChatGLM3_V2`
- `UNETLoader` ★核心
- `LayerMask: MaskGrow`
- `JjkText`
- `TextCombinerSix`
- `JjkText`
- `RH_Captioner`
- `JjkText`
- `RH_Captioner`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `MZ_KolorsCLIPVisionLoader`
- `MZ_IPAdapterModelLoaderKolors`
- `MZ_ChatGLM3Loader`
- `VAELoader`
- `Reroute`
- `Reroute`
- `GetImageSize`
- `PrimitiveNode`
- `Display Int (rgthree)`
- `Display Int (rgthree)`
- `SetNode`
- `MZ_KolorsControlNetPatch`
- `ControlNetLoader`
- `PreviewImage`
- `MaskToImage`
- `LayerColor: ColorAdapter`
- `MaskPreview+`
- `MZ_KolorsUNETLoaderV2` ★核心
- `FluxGuidance`
- `VAEEncodeForInpaint` ★核心
- `SetNode`
- `ImageResize+`
- `SetNode`
- `SaveImage`
- `VAEDecode` ★核心
- `LayerMask: MaskPreview`
- `SetNode`
- `easy cleanGpuUsed`
- `AV_VAELoader`
- `LoraLoader` ★核心
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `MaskToSEGS`
- `ControlNetApplyAdvanced` ★核心
- `PreviewImage`
- `PreviewImage`
- `ImagePadForOutpaint`
- `LoadImage`
- `GetNode`
- `LayerMask: SegmentAnythingUltra V2`
- `Reroute`
- `ShowText|pysssss`
- `VAEEncode` ★核心
- `RandomNoise`
- `KSamplerSelect` ★核心
- `BasicGuider`
- `VAELoader`
- `easy cleanGpuUsed`
- `LoadImage`
- `LayerUtility: ImageBlendAdvance`
- `Reroute`
- `PreviewImage`
- `MaskPreview+`
- `PreviewImage`
- `Mask Invert`
- `MZ_IPAdapterAdvancedKolors`
- `Label (rgthree)`
- `BasicScheduler`
- `CheckpointLoaderSimple` ★核心
- `VAEDecode` ★核心
- `PreviewImage`
- `Image Comparer (rgthree)`
- `SamplerCustomAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `PreviewImage`
- `DetailerForEach`
- `PreviewImage`
- `Label (rgthree)`

**识别到的模式**：image_to_image、lora

## 关键参数

- `lora_name` = `None`
- `strength_model` = `1`
- `strength_clip` = `1`
- `controlnet_strength` = `0.5`
- `checkpoint` = `Adam-Doll.XL丨玩偶盲盒丨3D手办_V2.safetensors`
- `seed` = `727373523822780`
- `steps` = `20`
- `cfg` = `3`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **71%**（59/83）

**有卡**：`RH_Prompter`、`MZ_ChatGLM3_V2`、`UNETLoader`、`LayerMask: MaskGrow`、`TextCombinerSix`、`RH_Captioner`、`CLIPTextEncode`、`MZ_KolorsCLIPVisionLoader`、`MZ_IPAdapterModelLoaderKolors`、`MZ_ChatGLM3Loader`、`VAELoader`、`GetImageSize`、`Display Int (rgthree)`、`MZ_KolorsControlNetPatch`、`ControlNetLoader`、`MaskToImage`、`LayerColor: ColorAdapter`、`MaskPreview+`、`MZ_KolorsUNETLoaderV2`、`FluxGuidance`、`VAEEncodeForInpaint`、`ImageResize+`、`SaveImage`、`VAEDecode`、`LayerMask: MaskPreview`、`easy cleanGpuUsed`、`AV_VAELoader`、`LoraLoader`、`DualCLIPLoader`、`MaskToSEGS`、`ControlNetApplyAdvanced`、`ImagePadForOutpaint`、`LoadImage`、`LayerMask: SegmentAnythingUltra V2`、`VAEEncode`、`RandomNoise`、`KSamplerSelect`、`BasicGuider`、`LayerUtility: ImageBlendAdvance`、`Mask Invert`、`MZ_IPAdapterAdvancedKolors`、`Label (rgthree)`、`BasicScheduler`、`CheckpointLoaderSimple`、`SamplerCustomAdvanced`、`LoraLoaderModelOnly`、`KSampler`、`DetailerForEach`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、LoadImage

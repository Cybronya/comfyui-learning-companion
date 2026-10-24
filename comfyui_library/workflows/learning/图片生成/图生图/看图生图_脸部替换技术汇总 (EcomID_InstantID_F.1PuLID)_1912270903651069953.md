---
key: 图片生成/图生图/看图生图_脸部替换技术汇总 (EcomID_InstantID_F.1PuLID)_1912270903651069953.json
name: 看图生图_脸部替换技术汇总 (EcomID_InstantID_F.1PuLID)_1912270903651069953
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/看图生图_脸部替换技术汇总 (EcomID_InstantID_F.1PuLID)_1912270903651069953.json
hash: 2f87fe96f2e4ebe4
coverage: 0.736842
learned_at: 2026-10-23 13:18:31
nodes: [CLIPVisionLoader, easy setNode, PulidInsightFaceLoader, PulidFluxEvaClipLoader, RandomNoise, ModelSamplingFlux, KSamplerSelect, NunchakuFluxLoraLoader, NunchakuFluxLoraLoader, NunchakuFluxDiTLoader, BasicGuider, ControlNetLoader, EcomIDFaceAnalysis, EcomIDEvaClipLoader, EcomID_PulidModelLoader, InstantID_IPA_ModelLoader, ApplyEcomID, PreviewImage, MaskPreview+, PulidFluxModelLoader, NunchakuTextEncoderLoader, ControlNetLoader, InstantIDFaceAnalysis, InstantIDModelLoader, Segment, Reroute, RandomNoise, KSamplerSelect, NunchakuTextEncoderLoader, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, CLIPTextEncode, FluxGuidance, VAEDecode, VAEDecode, SamplerCustomAdvanced, DifferentialDiffusion, PrepImageForClipVision, ImageMaskSwitch, CheckpointLoaderSimple, CLIPTextEncode, MaskToSEGS, PreviewImage, MaskPreview+, CLIPTextEncode, PrimitiveNode, PrimitiveNode, PreviewImage, MaskPreview+, CLIPTextEncode, ttN pipeLoaderSDXL_v2, VAEEncode, ApplyInstantIDAdvanced, LayerMask: PersonMaskUltra, SaveImage, Bjornulf_ShowStringText, LayerUtility: JoyCaption2, PreviewImage, SaveImage, BasicGuider, Note, LayerMask: PersonMaskUltra, Reroute, Note, VAELoader, VAEEncodeForInpaint, Note, Reroute, BasicScheduler, ModelSamplingFlux, VAELoader, FluxGuidance, Note, Reroute, LayerMask: PersonMaskUltra, Reroute, easy cleanGpuUsed, Reroute, Note, Reroute, PreviewImage, Reroute, VAEEncodeForInpaint, PreviewImage, Reroute, CLIPTextEncode, CLIPTextEncode, VAEDecode, Note, Reroute, Reroute, PreviewImage, Note, easy cleanGpuUsed, VAELoader, Reroute, Reroute, easy anythingIndexSwitch, ControlNetLoader, KSampler, SeedGenerator, PrimitiveFloat, DualCLIPLoader, EmptyLatentImage, Reroute, ControlNetApplyAdvanced, PreviewImage, UNETLoader, Reroute, Note, Reroute, PreviewImage, AIO_Preprocessor, Reroute, Reroute, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, CLIPVisionLoader, DifferentialDiffusion, PrepImageForClipVision, easy setNode, WD14Tagger|pysssss, PreviewImage, PreviewImage, PreviewImage, IPAdapterModelLoader, DifferentialDiffusion, LoadImage, Note, ControlNetApplyAdvanced, OpenposePreprocessor, ControlNetLoader, ControlNetApplyAdvanced, ControlNetLoader, ControlNetApplyAdvanced, ControlNetLoader, Reroute, CLIPVisionLoader, ImageResize+, PrepImageForClipVision, IPAdapterFaceID, IPAdapterInsightFaceLoader, PreviewImage, easy cleanGpuUsed, LoRALoader, easy pipeToBasicPipe, OpenposePreprocessor, FromBasicPipe, ttN pipeLoaderSDXL_v2, ttN pipeKSamplerSDXL_v2, VAEEncode, easy cleanGpuUsed, NunchakuFluxLoraLoader, easy cleanGpuUsed, SamplerCustomAdvanced, EmptyLatentImage, easy cleanGpuUsed, VAEEncode, ImageResize+, IPAdapterModelLoader, IPAdapterAdvanced, SetShakkerLabsUnionControlNetType, TextBox, TextBox, easy textSwitch, LoadImage, EmptyLatentImage, ControlNetLoader, easy getNode, ttN pipeLoaderSDXL_v2, Reroute, SetNode, ttN pipeKSamplerSDXL_v2, easy cleanGpuUsed, ImageResize+, IPAdapterAdvanced, IPAdapterModelLoader, GetNode, GetNode, ttN pipeLoaderSDXL_v2, PreviewImage, ControlNetApplyAdvanced, Reroute, OpenposePreprocessor, OpenposePreprocessor, CLIPTextEncode, MaskToSEGS, CLIPTextEncode, CheckpointLoaderSimple, ttN pipeKSamplerSDXL_v2, Reroute, MaskBlur+, BasicScheduler, PreviewImage, PreviewImage, SaveImage, ApplyPulidFlux, ImageConcatMulti, PreviewImage, DetailerForEach, SaveImage, DetailerForEach, SaveImage, ttN pipeKSamplerSDXL_v2, Reroute, SaveImage]
patterns: [text_to_image, image_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": "1x-ReFocus-V3.pth", "checkpoint": "waiREALMIX_v11.safetensors", "controlnet_strength": 0.6000000000000001, "denoise": 50, "height": 1216, "sampler_name": 2, "scheduler": "by percentage", "seed": "None", "steps": "None", "width": 768}
---

# 图片生成/图生图/看图生图_脸部替换技术汇总 (EcomID_InstantID_F.1PuLID)_1912270903651069953.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/看图生图_脸部替换技术汇总 (EcomID_InstantID_F.1PuLID)_1912270903651069953.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（209 个）：
- `CLIPVisionLoader`
- `easy setNode`
- `PulidInsightFaceLoader`
- `PulidFluxEvaClipLoader`
- `RandomNoise`
- `ModelSamplingFlux`
- `KSamplerSelect` ★核心
- `NunchakuFluxLoraLoader` ★核心
- `NunchakuFluxLoraLoader` ★核心
- `NunchakuFluxDiTLoader`
- `BasicGuider`
- `ControlNetLoader`
- `EcomIDFaceAnalysis`
- `EcomIDEvaClipLoader`
- `EcomID_PulidModelLoader`
- `InstantID_IPA_ModelLoader`
- `ApplyEcomID`
- `PreviewImage`
- `MaskPreview+`
- `PulidFluxModelLoader`
- `NunchakuTextEncoderLoader`
- `ControlNetLoader`
- `InstantIDFaceAnalysis`
- `InstantIDModelLoader`
- `Segment`
- `Reroute`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `NunchakuTextEncoderLoader`
- `NunchakuFluxDiTLoader`
- `NunchakuFluxLoraLoader` ★核心
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `DifferentialDiffusion`
- `PrepImageForClipVision`
- `ImageMaskSwitch`
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `MaskToSEGS`
- `PreviewImage`
- `MaskPreview+`
- `CLIPTextEncode` ★核心
- `PrimitiveNode`
- `PrimitiveNode`
- `PreviewImage`
- `MaskPreview+`
- `CLIPTextEncode` ★核心
- `ttN pipeLoaderSDXL_v2`
- `VAEEncode` ★核心
- `ApplyInstantIDAdvanced`
- `LayerMask: PersonMaskUltra`
- `SaveImage`
- `Bjornulf_ShowStringText`
- `LayerUtility: JoyCaption2`
- `PreviewImage`
- `SaveImage`
- `BasicGuider`
- `Note`
- `LayerMask: PersonMaskUltra`
- `Reroute`
- `Note`
- `VAELoader`
- `VAEEncodeForInpaint` ★核心
- `Note`
- `Reroute`
- `BasicScheduler`
- `ModelSamplingFlux`
- `VAELoader`
- `FluxGuidance`
- `Note`
- `Reroute`
- `LayerMask: PersonMaskUltra`
- `Reroute`
- `easy cleanGpuUsed`
- `Reroute`
- `Note`
- `Reroute`
- `PreviewImage`
- `Reroute`
- `VAEEncodeForInpaint` ★核心
- `PreviewImage`
- `Reroute`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `Note`
- `Reroute`
- `Reroute`
- `PreviewImage`
- `Note`
- `easy cleanGpuUsed`
- `VAELoader`
- `Reroute`
- `Reroute`
- `easy anythingIndexSwitch`
- `ControlNetLoader`
- `KSampler` ★核心
- `SeedGenerator`
- `PrimitiveFloat`
- `DualCLIPLoader`
- `EmptyLatentImage` ★核心
- `Reroute`
- `ControlNetApplyAdvanced` ★核心
- `PreviewImage`
- `UNETLoader` ★核心
- `Reroute`
- `Note`
- `Reroute`
- `PreviewImage`
- `AIO_Preprocessor`
- `Reroute`
- `Reroute`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `CLIPVisionLoader`
- `DifferentialDiffusion`
- `PrepImageForClipVision`
- `easy setNode`
- `WD14Tagger|pysssss`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `IPAdapterModelLoader`
- `DifferentialDiffusion`
- `LoadImage`
- `Note`
- `ControlNetApplyAdvanced` ★核心
- `OpenposePreprocessor`
- `ControlNetLoader`
- `ControlNetApplyAdvanced` ★核心
- `ControlNetLoader`
- `ControlNetApplyAdvanced` ★核心
- `ControlNetLoader`
- `Reroute`
- `CLIPVisionLoader`
- `ImageResize+`
- `PrepImageForClipVision`
- `IPAdapterFaceID`
- `IPAdapterInsightFaceLoader`
- `PreviewImage`
- `easy cleanGpuUsed`
- `LoRALoader` ★核心
- `easy pipeToBasicPipe`
- `OpenposePreprocessor`
- `FromBasicPipe`
- `ttN pipeLoaderSDXL_v2`
- `ttN pipeKSamplerSDXL_v2` ★核心
- `VAEEncode` ★核心
- `easy cleanGpuUsed`
- `NunchakuFluxLoraLoader` ★核心
- `easy cleanGpuUsed`
- `SamplerCustomAdvanced` ★核心
- `EmptyLatentImage` ★核心
- `easy cleanGpuUsed`
- `VAEEncode` ★核心
- `ImageResize+`
- `IPAdapterModelLoader`
- `IPAdapterAdvanced`
- `SetShakkerLabsUnionControlNetType`
- `TextBox`
- `TextBox`
- `easy textSwitch`
- `LoadImage`
- `EmptyLatentImage` ★核心
- `ControlNetLoader`
- `easy getNode`
- `ttN pipeLoaderSDXL_v2`
- `Reroute`
- `SetNode`
- `ttN pipeKSamplerSDXL_v2` ★核心
- `easy cleanGpuUsed`
- `ImageResize+`
- `IPAdapterAdvanced`
- `IPAdapterModelLoader`
- `GetNode`
- `GetNode`
- `ttN pipeLoaderSDXL_v2`
- `PreviewImage`
- `ControlNetApplyAdvanced` ★核心
- `Reroute`
- `OpenposePreprocessor`
- `OpenposePreprocessor`
- `CLIPTextEncode` ★核心
- `MaskToSEGS`
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `ttN pipeKSamplerSDXL_v2` ★核心
- `Reroute`
- `MaskBlur+`
- `BasicScheduler`
- `PreviewImage`
- `PreviewImage`
- `SaveImage`
- `ApplyPulidFlux`
- `ImageConcatMulti`
- `PreviewImage`
- `DetailerForEach`
- `SaveImage`
- `DetailerForEach`
- `SaveImage`
- `ttN pipeKSamplerSDXL_v2` ★核心
- `Reroute`
- `SaveImage`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `checkpoint` = `waiREALMIX_v11.safetensors`
- `seed` = `None`
- `steps` = `None`
- `cfg` = `1x-ReFocus-V3.pth`
- `sampler_name` = `2`
- `scheduler` = `by percentage`
- `denoise` = `50`
- `width` = `768`
- `height` = `1216`
- `batch_size` = `1`
- `controlnet_strength` = `0.6000000000000001`

## 知识

覆盖率 **74%**（154/209）

**有卡**：`CLIPVisionLoader`、`easy setNode`、`PulidInsightFaceLoader`、`PulidFluxEvaClipLoader`、`RandomNoise`、`ModelSamplingFlux`、`KSamplerSelect`、`NunchakuFluxLoraLoader`、`NunchakuFluxDiTLoader`、`BasicGuider`、`ControlNetLoader`、`EcomIDFaceAnalysis`、`EcomIDEvaClipLoader`、`EcomID_PulidModelLoader`、`InstantID_IPA_ModelLoader`、`ApplyEcomID`、`MaskPreview+`、`PulidFluxModelLoader`、`NunchakuTextEncoderLoader`、`InstantIDFaceAnalysis`、`InstantIDModelLoader`、`Segment`、`CLIPTextEncode`、`FluxGuidance`、`VAEDecode`、`SamplerCustomAdvanced`、`DifferentialDiffusion`、`PrepImageForClipVision`、`ImageMaskSwitch`、`CheckpointLoaderSimple`、`MaskToSEGS`、`ttN pipeLoaderSDXL_v2`、`VAEEncode`、`ApplyInstantIDAdvanced`、`LayerMask: PersonMaskUltra`、`SaveImage`、`Bjornulf_ShowStringText`、`LayerUtility: JoyCaption2`、`VAELoader`、`VAEEncodeForInpaint`、`BasicScheduler`、`easy cleanGpuUsed`、`easy anythingIndexSwitch`、`KSampler`、`SeedGenerator`、`DualCLIPLoader`、`EmptyLatentImage`、`ControlNetApplyAdvanced`、`UNETLoader`、`AIO_Preprocessor`、`WD14Tagger|pysssss`、`IPAdapterModelLoader`、`LoadImage`、`OpenposePreprocessor`、`ImageResize+`、`IPAdapterFaceID`、`IPAdapterInsightFaceLoader`、`LoRALoader`、`easy pipeToBasicPipe`、`FromBasicPipe`、`ttN pipeKSamplerSDXL_v2`、`IPAdapterAdvanced`、`SetShakkerLabsUnionControlNetType`、`TextBox`、`easy textSwitch`、`easy getNode`、`MaskBlur+`、`ApplyPulidFlux`、`ImageConcatMulti`、`DetailerForEach`

**用到的条目**：KSampler、VAEDecode、VAELoader、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、EmptyLatentImage、LoadImage

---
key: 平台全量/灵仙儿和二狗子AI摄影小助手1.0版_1817516213399388162.json
name: 灵仙儿和二狗子AI摄影小助手1.0版_1817516213399388162
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/灵仙儿和二狗子AI摄影小助手1.0版_1817516213399388162.json
hash: 4c2c410bcdb7ec41
coverage: 0.661417
learned_at: 2026-11-14 02:21:15
nodes: [IPAdapterModelLoader, InsightFaceLoader, CR Load LoRA, CheckpointLoaderSimple, CR Load LoRA, CR Load LoRA, SaveImage, SaveImage, KSampler Config (rgthree), Note, Note, Note, Note, Note, Note, Note, SetLatentNoiseMask, VAEEncode, VAEEncodeForInpaint, ControlNetLoader, ControlNetLoader, KSampler, KSampler, PrepImageForClipVision, PrimitiveNode, PrimitiveNode, Note, IPAdapterModelLoader, IPAdapterApply, PrimitiveNode, Note, PrimitiveNode, PrimitiveNode, KSampler, ConstrainImage|pysssss, Any Switch (rgthree), BNK_CLIPTextEncodeAdvanced, Note, KSampler, InvertMask, ImpactImageInfo, StringFunction|pysssss, SetLatentNoiseMask, VAEDecode, ImageBlend, StringFunction|pysssss, VAEDecode, ControlNetLoader, LoraLoaderModelOnly, Note, Note, BNK_TiledKSampler, SaveImage, SaveImage, SaveImage, VAEEncode, UpscaleModelLoader, SaveImage, SaveImage, PreviewImage, LoadImage, Note, LoadImage, Note, LoadImage, Note, Note, LoadImage, Note, LoadImageMask, SAMLoader, GroundingDinoModelLoader (segment anything), Note, Note, Note, Note, FeatheredMask, Note, PreviewImage, ImageCompositeMasked, Any Switch (rgthree), MaskToImage, Convert Masks to Images, ImageToMask, Any Switch (rgthree), AIO_Preprocessor, ControlNetApplyAdvanced, AIO_Preprocessor, ControlNetApplyAdvanced, InpaintPreprocessor, BNK_CLIPTextEncodeAdvanced, ControlNetApplyAdvanced, ImageScaleBy, KSampler Config (rgthree), PrimitiveNode, Note, VAEDecode, VAEDecode, VAEDecode, VAEDecode, CLIPVisionLoader, Note, Note, Note, Note, Any Switch (rgthree), WD14Tagger|pysssss, ImageUpscaleWithModel, ImageCompositeMasked, VAEEncode, InvertMask, MaskToImage, ImageToMask, MaskToImage, ImageToMask, GroundingDinoSAMSegment (segment anything), ImageScale, PrepImageForClipVision, IPAdapterApply, GrowMask, PrimitiveNode, KSampler, BNK_CLIPTextEncodeAdvanced, CR Load LoRA, Any Switch (rgthree), Fast Groups Muter (rgthree), Note]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 8, "checkpoint": "majicMIX realistic 麦橘写实_v6.safetensors", "controlnet_strength": 1, "denoise": 0.4, "sampler_name": "dpmpp_sde", "scheduler": "karras", "seed": 388898890208537, "steps": 28}
---

# 平台全量/灵仙儿和二狗子AI摄影小助手1.0版_1817516213399388162.json

> 来源文件 `comfyui_library/workflows/平台全量/灵仙儿和二狗子AI摄影小助手1.0版_1817516213399388162.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（127 个）：
- `IPAdapterModelLoader`
- `InsightFaceLoader`
- `CR Load LoRA`
- `CheckpointLoaderSimple` ★核心
- `CR Load LoRA`
- `CR Load LoRA`
- `SaveImage`
- `SaveImage`
- `KSampler Config (rgthree)` ★核心
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `SetLatentNoiseMask`
- `VAEEncode` ★核心
- `VAEEncodeForInpaint` ★核心
- `ControlNetLoader`
- `ControlNetLoader`
- `KSampler` ★核心
- `KSampler` ★核心
- `PrepImageForClipVision`
- `PrimitiveNode`
- `PrimitiveNode`
- `Note`
- `IPAdapterModelLoader`
- `IPAdapterApply` ★核心
- `PrimitiveNode`
- `Note`
- `PrimitiveNode`
- `PrimitiveNode`
- `KSampler` ★核心
- `ConstrainImage|pysssss`
- `Any Switch (rgthree)`
- `BNK_CLIPTextEncodeAdvanced` ★核心
- `Note`
- `KSampler` ★核心
- `InvertMask`
- `ImpactImageInfo`
- `StringFunction|pysssss`
- `SetLatentNoiseMask`
- `VAEDecode` ★核心
- `ImageBlend`
- `StringFunction|pysssss`
- `VAEDecode` ★核心
- `ControlNetLoader`
- `LoraLoaderModelOnly` ★核心
- `Note`
- `Note`
- `BNK_TiledKSampler` ★核心
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `VAEEncode` ★核心
- `UpscaleModelLoader`
- `SaveImage`
- `SaveImage`
- `PreviewImage`
- `LoadImage`
- `Note`
- `LoadImage`
- `Note`
- `LoadImage`
- `Note`
- `Note`
- `LoadImage`
- `Note`
- `LoadImageMask`
- `SAMLoader`
- `GroundingDinoModelLoader (segment anything)`
- `Note`
- `Note`
- `Note`
- `Note`
- `FeatheredMask`
- `Note`
- `PreviewImage`
- `ImageCompositeMasked`
- `Any Switch (rgthree)`
- `MaskToImage`
- `Convert Masks to Images`
- `ImageToMask`
- `Any Switch (rgthree)`
- `AIO_Preprocessor`
- `ControlNetApplyAdvanced` ★核心
- `AIO_Preprocessor`
- `ControlNetApplyAdvanced` ★核心
- `InpaintPreprocessor`
- `BNK_CLIPTextEncodeAdvanced` ★核心
- `ControlNetApplyAdvanced` ★核心
- `ImageScaleBy`
- `KSampler Config (rgthree)` ★核心
- `PrimitiveNode`
- `Note`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `CLIPVisionLoader`
- `Note`
- `Note`
- `Note`
- `Note`
- `Any Switch (rgthree)`
- `WD14Tagger|pysssss`
- `ImageUpscaleWithModel`
- `ImageCompositeMasked`
- `VAEEncode` ★核心
- `InvertMask`
- `MaskToImage`
- `ImageToMask`
- `MaskToImage`
- `ImageToMask`
- `GroundingDinoSAMSegment (segment anything)`
- `ImageScale`
- `PrepImageForClipVision`
- `IPAdapterApply` ★核心
- `GrowMask`
- `PrimitiveNode`
- `KSampler` ★核心
- `BNK_CLIPTextEncodeAdvanced` ★核心
- `CR Load LoRA`
- `Any Switch (rgthree)`
- `Fast Groups Muter (rgthree)`
- `Note`

**识别到的模式**：image_to_image

## 关键参数

- `checkpoint` = `majicMIX realistic 麦橘写实_v6.safetensors`
- `seed` = `388898890208537`
- `steps` = `28`
- `cfg` = `8`
- `sampler_name` = `dpmpp_sde`
- `scheduler` = `karras`
- `denoise` = `0.4`
- `controlnet_strength` = `1`

## 知识

覆盖率 **66%**（84/127）

**有卡**：`IPAdapterModelLoader`、`InsightFaceLoader`、`CR Load LoRA`、`CheckpointLoaderSimple`、`SaveImage`、`KSampler Config (rgthree)`、`SetLatentNoiseMask`、`VAEEncode`、`VAEEncodeForInpaint`、`ControlNetLoader`、`KSampler`、`PrepImageForClipVision`、`IPAdapterApply`、`ConstrainImage|pysssss`、`BNK_CLIPTextEncodeAdvanced`、`InvertMask`、`ImpactImageInfo`、`StringFunction|pysssss`、`VAEDecode`、`ImageBlend`、`LoraLoaderModelOnly`、`BNK_TiledKSampler`、`UpscaleModelLoader`、`LoadImage`、`LoadImageMask`、`SAMLoader`、`GroundingDinoModelLoader (segment anything)`、`FeatheredMask`、`ImageCompositeMasked`、`MaskToImage`、`Convert Masks to Images`、`ImageToMask`、`AIO_Preprocessor`、`ControlNetApplyAdvanced`、`InpaintPreprocessor`、`ImageScaleBy`、`CLIPVisionLoader`、`WD14Tagger|pysssss`、`ImageUpscaleWithModel`、`GroundingDinoSAMSegment (segment anything)`、`ImageScale`、`GrowMask`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、LoadImage、ControlNetApplyAdvanced、ControlNetLoader、BNK_TiledKSampler

---
key: 平台全量/重叠帧视频转视频生成  Wan 2.1  fusionX Vace_1941737675923865602.json
name: 重叠帧视频转视频生成  Wan 2.1  fusionX Vace_1941737675923865602
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/重叠帧视频转视频生成  Wan 2.1  fusionX Vace_1941737675923865602.json
hash: c0979839543ec04d
coverage: 0.494949
learned_at: 2026-11-14 02:48:57
nodes: [SetNode, SetNode, GetNode, GetNode, VHS_VideoInfo, GetNode, GetNode, GetNode, GetNode, GetImageRangeFromBatch, GetNode, GetNode, MathExpression|pysssss, GetNode, MathExpression|pysssss, SetNode, GetNode, MathExpression|pysssss, MathExpression|pysssss, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, VAEDecode, GetNode, GetNode, GetNode, GetNode, MathExpression|pysssss, MathExpression|pysssss, GetNode, GetNode, GetNode, PreviewImage, GetNode, GetNode, VHS_GetImageCount, MathExpression|pysssss, GetNode, SetNode, GetNode, GetImageRangeFromBatch, MathExpression|pysssss, GetImageRangeFromBatch, MathExpression|pysssss, MathExpression|pysssss, GetNode, GetNode, VHS_GetImageCount, GetNode, ImageFromBatch, SetNode, ImageFromBatch, SetNode, GetNode, SetNode, GetNode, GetNode, SetNode, SetNode, VAEDecode, TrimVideoLatent, GetNode, GetNode, GetImageRangeFromBatch, GetImageRangeFromBatch, DWPreprocessor, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, VAELoader, WanVaceToVideo, GetImageRangeFromBatch, WanVideoVACEStartToEndFrame, Label (rgthree), Label (rgthree), WanVideoVACEStartToEndFrame, MathExpression|pysssss, MathExpression|pysssss, DWPreprocessor, KSampler, EmptySD3LatentImage, SetNode, DualCLIPLoader, VAELoader, MathExpression|pysssss, VAEDecode, GetNode, GetNode, ReferenceLatent, VAEEncode, ConditioningZeroOut, FluxGuidance, SetNode, KSampler, LayerUtility: PurgeVRAM, VAEEncode, ReferenceLatent, ImageResizeKJv2, PreviewImage, GetNode, SetNode, TrimVideoLatent, PreviewImage, GetNode, SetNode, MathExpression|pysssss, GetNode, GetNode, GetNode, SetNode, WanVaceToVideo, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, VHS_VideoCombine, VHS_VideoCombine, LayerUtility: PurgeVRAM, ImageResizeKJv2, ImageFromBatch, PreviewImage, Fast Groups Bypasser (rgthree), Note, GetNode, GetNode, CLIPTextEncode, MathExpression|pysssss, LoadImage, GetNode, Note, Reroute, UnetLoaderGGUF, CLIPLoader, SetNode, GetNode, PathchSageAttentionKJ, TorchCompileModelWanVideo, GetNode, PatchModelPatcherOrder, LoraLoaderModelOnly, ModelSamplingSD3, SetNode, VAEDecode, SetNode, GetNode, GetNode, TrimVideoLatent, GetNode, GetNode, GetNode, CLIPVisionEncode, CLIPVisionLoader, SetNode, CLIPTextEncode, GetNode, GetNode, INTConstant, GetNode, SetNode, WanVaceToVideo, GetImageRangeFromBatch, DownloadAndLoadDepthAnythingV2Model, WanVaceToVideo, DepthAnything_V2, DWPreprocessor, PreviewImage, LoadImage, RH_Translator, PreviewImage, KSampler, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, TextEncodeHunyuanVideo_ImageToVideo, VHS_LoadVideo, ImageBatchMulti, GetNode, GetNode, KSampler, ImageResizeKJv2, SetNode, VHS_VideoCombine, INTConstant, INTConstant, INTConstant, VHS_VideoCombine, UNETLoader, UnetLoaderGGUF]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 50, "steps": 10}
---

# 平台全量/重叠帧视频转视频生成  Wan 2.1  fusionX Vace_1941737675923865602.json

> 来源文件 `comfyui_library/workflows/平台全量/重叠帧视频转视频生成  Wan 2.1  fusionX Vace_1941737675923865602.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（198 个）：
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoInfo`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetImageRangeFromBatch`
- `GetNode`
- `GetNode`
- `MathExpression|pysssss`
- `GetNode`
- `MathExpression|pysssss`
- `SetNode`
- `GetNode`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `GetNode`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `VHS_GetImageCount`
- `MathExpression|pysssss`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetImageRangeFromBatch`
- `MathExpression|pysssss`
- `GetImageRangeFromBatch`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `GetNode`
- `GetNode`
- `VHS_GetImageCount`
- `GetNode`
- `ImageFromBatch`
- `SetNode`
- `ImageFromBatch`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `VAEDecode` ★核心
- `TrimVideoLatent`
- `GetNode`
- `GetNode`
- `GetImageRangeFromBatch`
- `GetImageRangeFromBatch`
- `DWPreprocessor`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `VAELoader`
- `WanVaceToVideo`
- `GetImageRangeFromBatch`
- `WanVideoVACEStartToEndFrame`
- `Label (rgthree)`
- `Label (rgthree)`
- `WanVideoVACEStartToEndFrame`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `DWPreprocessor`
- `KSampler` ★核心
- `EmptySD3LatentImage`
- `SetNode`
- `DualCLIPLoader`
- `VAELoader`
- `MathExpression|pysssss`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `ConditioningZeroOut`
- `FluxGuidance`
- `SetNode`
- `KSampler` ★核心
- `LayerUtility: PurgeVRAM`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ImageResizeKJv2`
- `PreviewImage`
- `GetNode`
- `SetNode`
- `TrimVideoLatent`
- `PreviewImage`
- `GetNode`
- `SetNode`
- `MathExpression|pysssss`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `WanVaceToVideo`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LayerUtility: PurgeVRAM`
- `ImageResizeKJv2`
- `ImageFromBatch`
- `PreviewImage`
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `MathExpression|pysssss`
- `LoadImage`
- `GetNode`
- `Note`
- `Reroute`
- `UnetLoaderGGUF` ★核心
- `CLIPLoader`
- `SetNode`
- `GetNode`
- `PathchSageAttentionKJ`
- `TorchCompileModelWanVideo`
- `GetNode`
- `PatchModelPatcherOrder`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `SetNode`
- `VAEDecode` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `TrimVideoLatent`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `SetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `INTConstant`
- `GetNode`
- `SetNode`
- `WanVaceToVideo`
- `GetImageRangeFromBatch`
- `DownloadAndLoadDepthAnythingV2Model`
- `WanVaceToVideo`
- `DepthAnything_V2`
- `DWPreprocessor`
- `PreviewImage`
- `LoadImage`
- `RH_Translator`
- `PreviewImage`
- `KSampler` ★核心
- `NunchakuFluxDiTLoader`
- `NunchakuFluxLoraLoader` ★核心
- `TextEncodeHunyuanVideo_ImageToVideo`
- `VHS_LoadVideo`
- `ImageBatchMulti`
- `GetNode`
- `GetNode`
- `KSampler` ★核心
- `ImageResizeKJv2`
- `SetNode`
- `VHS_VideoCombine`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `UnetLoaderGGUF` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `50`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **49%**（98/198）

**有卡**：`VHS_VideoInfo`、`GetImageRangeFromBatch`、`MathExpression|pysssss`、`VAEDecode`、`VHS_GetImageCount`、`ImageFromBatch`、`TrimVideoLatent`、`DWPreprocessor`、`VAELoader`、`WanVaceToVideo`、`WanVideoVACEStartToEndFrame`、`Label (rgthree)`、`KSampler`、`EmptySD3LatentImage`、`DualCLIPLoader`、`ReferenceLatent`、`VAEEncode`、`ConditioningZeroOut`、`FluxGuidance`、`LayerUtility: PurgeVRAM`、`ImageResizeKJv2`、`VHS_VideoCombine`、`CLIPTextEncode`、`LoadImage`、`UnetLoaderGGUF`、`CLIPLoader`、`PathchSageAttentionKJ`、`TorchCompileModelWanVideo`、`PatchModelPatcherOrder`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`CLIPVisionEncode`、`CLIPVisionLoader`、`INTConstant`、`DownloadAndLoadDepthAnythingV2Model`、`DepthAnything_V2`、`RH_Translator`、`NunchakuFluxDiTLoader`、`NunchakuFluxLoraLoader`、`TextEncodeHunyuanVideo_ImageToVideo`、`VHS_LoadVideo`、`ImageBatchMulti`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut

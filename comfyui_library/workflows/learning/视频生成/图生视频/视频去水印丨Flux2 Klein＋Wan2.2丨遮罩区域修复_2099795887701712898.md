---
key: 视频生成/图生视频/视频去水印丨Flux2 Klein＋Wan2.2丨遮罩区域修复_2099795887701712898.json
name: 视频去水印丨Flux2 Klein＋Wan2.2丨遮罩区域修复_2099795887701712898
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/视频去水印丨Flux2 Klein＋Wan2.2丨遮罩区域修复_2099795887701712898.json
hash: ee47056715d8d3e2
coverage: 0.901408
learned_at: 2026-10-17 02:00:10
nodes: [RandomNoise, ReferenceLatent, CLIPVisionLoader, WanVideoClipVisionEncode, KSamplerSelect, EmptyFlux2LatentImage, Flux2Scheduler, ReferenceLatent, VAEEncode, Image Filter Adjustments, WanVideoDecode, ImageFromBatch, ImageToMask, ImageScale, WanVideoAnimateEmbeds, WanVideoModelLoader, easy mathInt, LayerUtility: ImageScaleByAspectRatio V2, ConditioningZeroOut, CFGGuider, SamplerCustomAdvanced, VAEDecode, CLIPLoader, easy cleanGpuUsed, LayerUtility: ImageScaleByAspectRatio V2, VHS_DuplicateMasks, WanVideoVAELoader, WanVideoLoraSelectMulti, easy cleanGpuUsed, WanVideoTextEncodeCached, ImageScale, ImageFromBatch, GrowMaskWithBlur, ImageAndMaskPreview, BlendInpaint, UNETLoader, Note, VHS_VideoInfo, ImageFromBatch, MathExpression|pysssss, RepeatImageBatch, ImageBatch, BlockifyMask, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ColorImage V2, easy int, CreateVideo, VHS_VideoCombine, WanVideoSampler, MaskToImage, GrowMaskWithBlur, VAELoader, BatchCount+, LayerUtility: ImageBlend, RepeatImageBatch, DrawMaskOnImage, BatchCount+, easy imageSize, WanVideoContextOptions, Note, HAIGC_VideoRelay, Note, PreviewImage, CLIPTextEncode, VHS_VideoCombine, PreviewImage, LoadImage, VHS_VideoCombine, Note, Note, VHS_LoadVideoFFmpeg]
patterns: []
missing: []
---

# 视频生成/图生视频/视频去水印丨Flux2 Klein＋Wan2.2丨遮罩区域修复_2099795887701712898.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/视频去水印丨Flux2 Klein＋Wan2.2丨遮罩区域修复_2099795887701712898.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（71 个）：
- `RandomNoise`
- `ReferenceLatent`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `KSamplerSelect` ★核心
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `Image Filter Adjustments`
- `WanVideoDecode`
- `ImageFromBatch`
- `ImageToMask`
- `ImageScale`
- `WanVideoAnimateEmbeds`
- `WanVideoModelLoader`
- `easy mathInt`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ConditioningZeroOut`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `CLIPLoader`
- `easy cleanGpuUsed`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_DuplicateMasks`
- `WanVideoVAELoader`
- `WanVideoLoraSelectMulti`
- `easy cleanGpuUsed`
- `WanVideoTextEncodeCached`
- `ImageScale`
- `ImageFromBatch`
- `GrowMaskWithBlur`
- `ImageAndMaskPreview`
- `BlendInpaint`
- `UNETLoader` ★核心
- `Note`
- `VHS_VideoInfo`
- `ImageFromBatch`
- `MathExpression|pysssss`
- `RepeatImageBatch`
- `ImageBatch`
- `BlockifyMask`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ColorImage V2`
- `easy int`
- `CreateVideo`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `MaskToImage`
- `GrowMaskWithBlur`
- `VAELoader`
- `BatchCount+`
- `LayerUtility: ImageBlend`
- `RepeatImageBatch`
- `DrawMaskOnImage`
- `BatchCount+`
- `easy imageSize`
- `WanVideoContextOptions`
- `Note`
- `HAIGC_VideoRelay`
- `Note`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `PreviewImage`
- `LoadImage`
- `VHS_VideoCombine`
- `Note`
- `Note`
- `VHS_LoadVideoFFmpeg`

## 知识

覆盖率 **90%**（64/71）

**有卡**：`RandomNoise`、`ReferenceLatent`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`KSamplerSelect`、`EmptyFlux2LatentImage`、`Flux2Scheduler`、`VAEEncode`、`Image Filter Adjustments`、`WanVideoDecode`、`ImageFromBatch`、`ImageToMask`、`ImageScale`、`WanVideoAnimateEmbeds`、`WanVideoModelLoader`、`easy mathInt`、`LayerUtility: ImageScaleByAspectRatio V2`、`ConditioningZeroOut`、`CFGGuider`、`SamplerCustomAdvanced`、`VAEDecode`、`CLIPLoader`、`easy cleanGpuUsed`、`VHS_DuplicateMasks`、`WanVideoVAELoader`、`WanVideoLoraSelectMulti`、`WanVideoTextEncodeCached`、`GrowMaskWithBlur`、`ImageAndMaskPreview`、`BlendInpaint`、`UNETLoader`、`VHS_VideoInfo`、`MathExpression|pysssss`、`RepeatImageBatch`、`ImageBatch`、`BlockifyMask`、`LayerUtility: ColorImage V2`、`easy int`、`CreateVideo`、`VHS_VideoCombine`、`WanVideoSampler`、`MaskToImage`、`VAELoader`、`BatchCount+`、`LayerUtility: ImageBlend`、`DrawMaskOnImage`、`easy imageSize`、`WanVideoContextOptions`、`HAIGC_VideoRelay`、`CLIPTextEncode`、`LoadImage`、`VHS_LoadVideoFFmpeg`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、CFGGuider

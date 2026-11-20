---
key: 平台全量/Wan2.2 Animate -视频转绘动作面部迁移_1985250259951566849.json
name: Wan2.2 Animate -视频转绘动作面部迁移_1985250259951566849
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2 Animate -视频转绘动作面部迁移_1985250259951566849.json
hash: 92d5d428569bc070
coverage: 0.807692
learned_at: 2026-11-14 01:04:51
nodes: [VAEEncode, ReferenceLatent, FluxGuidance, FluxKontextImageScale, ConditioningZeroOut, VAELoader, CLIPTextEncode, LoraLoaderModelOnly, String, UNETLoader, WanVideoDecode, WanVideoModelLoader, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoSampler, WanVideoVAELoader, CLIPVisionLoader, WanVideoClipVisionEncode, Reroute, WanVideoSetBlockSwap, VHS_VideoCombine, Reroute, OnnxDetectionModelLoader, PoseAndFaceDetection, DrawViTPose, Reroute, Reroute, SaveImage, KSampler, CR Text Concatenate, ImageFromBatch, ConstrainImage|pysssss, DualCLIPLoader, DeepTranslatorTextNode, VAEDecode, PreviewImage, SUPIR_Upscale, Reroute, VHS_VideoCombine, WanVideoLoraSelectMulti, MuyeLoadImage, WanVideoAnimateEmbeds, Reroute, Reroute, VHS_VideoCombine, VHS_LoadVideo, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, Reroute, WanVideoTextEncodeCached, PreviewImage, SeargeIntegerConstant]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 226861859563641, "steps": 25}
---

# 平台全量/Wan2.2 Animate -视频转绘动作面部迁移_1985250259951566849.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2 Animate -视频转绘动作面部迁移_1985250259951566849.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（52 个）：
- `VAEEncode` ★核心
- `ReferenceLatent`
- `FluxGuidance`
- `FluxKontextImageScale`
- `ConditioningZeroOut`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `String`
- `UNETLoader` ★核心
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoSampler` ★核心
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `Reroute`
- `WanVideoSetBlockSwap`
- `VHS_VideoCombine`
- `Reroute`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `DrawViTPose`
- `Reroute`
- `Reroute`
- `SaveImage`
- `KSampler` ★核心
- `CR Text Concatenate`
- `ImageFromBatch`
- `ConstrainImage|pysssss`
- `DualCLIPLoader`
- `DeepTranslatorTextNode`
- `VAEDecode` ★核心
- `PreviewImage`
- `SUPIR_Upscale`
- `Reroute`
- `VHS_VideoCombine`
- `WanVideoLoraSelectMulti`
- `MuyeLoadImage`
- `WanVideoAnimateEmbeds`
- `Reroute`
- `Reroute`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Reroute`
- `WanVideoTextEncodeCached`
- `PreviewImage`
- `SeargeIntegerConstant`

## 关键参数

- `seed` = `226861859563641`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **81%**（42/52）

**有卡**：`VAEEncode`、`ReferenceLatent`、`FluxGuidance`、`FluxKontextImageScale`、`ConditioningZeroOut`、`VAELoader`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`String`、`UNETLoader`、`WanVideoDecode`、`WanVideoModelLoader`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoSampler`、`WanVideoVAELoader`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoSetBlockSwap`、`VHS_VideoCombine`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`DrawViTPose`、`SaveImage`、`KSampler`、`CR Text Concatenate`、`ImageFromBatch`、`ConstrainImage|pysssss`、`DualCLIPLoader`、`DeepTranslatorTextNode`、`VAEDecode`、`SUPIR_Upscale`、`WanVideoLoraSelectMulti`、`MuyeLoadImage`、`WanVideoAnimateEmbeds`、`VHS_LoadVideo`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoTextEncodeCached`、`SeargeIntegerConstant`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、FluxGuidance

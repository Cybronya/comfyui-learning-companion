---
key: 视频生成/图生视频/Wan2.2真人变身3D动漫首尾帧视频_1952335209725407234.json
name: Wan2.2真人变身3D动漫首尾帧视频_1952335209725407234.json
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1952335209725407234.json
hash: 83682698022a6491
coverage: 0.93617
learned_at: 2026-10-15 22:31:01
nodes: [CLIPTextEncode, ReferenceLatent, VAEEncode, ConditioningZeroOut, easy cleanGpuUsed, FluxGuidance, Reroute, UNETLoader, DualCLIPLoader, easy cleanGpuUsed, CLIPTextEncode, VAELoader, LoadImage, CR Text, LoraLoaderModelOnly, VAELoader, CLIPVisionEncode, CLIPVisionEncode, VAEDecode, CLIPTextEncode, WanFirstLastFrameToVideo, GIMMVFI_interpolate, DownloadAndLoadGIMMVFIModel, LoadImage, LoadImage, CLIPVisionLoader, CreateVideo, CLIPLoader, KSamplerAdvanced, KSamplerAdvanced, PathchSageAttentionKJ, CLIPTextEncode, ModelSamplingSD3, PathchSageAttentionKJ, UNETLoader, UNETLoader, ModelSamplingSD3, VAEDecode, CR Text Concatenate, PreviewImage, FluxKontextImageScale, RH_Translator, KSampler, SaveVideo, LayerUtility: ImageRemoveAlpha, ShowText|pysssss, CR Text]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 543502134469075, "steps": 20}
---

# 视频生成/图生视频/Wan2.2真人变身3D动漫首尾帧视频_1952335209725407234.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1952335209725407234.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（47 个）：
- `CLIPTextEncode` ★核心
- `ReferenceLatent`
- `VAEEncode` ★核心
- `ConditioningZeroOut`
- `easy cleanGpuUsed`
- `FluxGuidance`
- `Reroute`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `LoadImage`
- `CR Text`
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `WanFirstLastFrameToVideo`
- `GIMMVFI_interpolate`
- `DownloadAndLoadGIMMVFIModel`
- `LoadImage`
- `LoadImage`
- `CLIPVisionLoader`
- `CreateVideo`
- `CLIPLoader`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `CR Text Concatenate`
- `PreviewImage`
- `FluxKontextImageScale`
- `RH_Translator`
- `KSampler` ★核心
- `SaveVideo`
- `LayerUtility: ImageRemoveAlpha`
- `ShowText|pysssss`
- `CR Text`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `543502134469075`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **94%**（44/47）

**有卡**：`CLIPTextEncode`、`ReferenceLatent`、`VAEEncode`、`ConditioningZeroOut`、`easy cleanGpuUsed`、`FluxGuidance`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`LoadImage`、`CR Text`、`LoraLoaderModelOnly`、`CLIPVisionEncode`、`VAEDecode`、`WanFirstLastFrameToVideo`、`GIMMVFI_interpolate`、`DownloadAndLoadGIMMVFIModel`、`CLIPVisionLoader`、`CreateVideo`、`CLIPLoader`、`KSamplerAdvanced`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`CR Text Concatenate`、`FluxKontextImageScale`、`RH_Translator`、`KSampler`、`SaveVideo`、`LayerUtility: ImageRemoveAlpha`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

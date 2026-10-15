---
key: 视频生成/文生视频/wan2.2 smooth Vs Lightning V2混合低噪+原版10+4对比T2V工作流_1987403122442219521.json
name: wan2.2 smooth Vs Lightning V2混合低噪+原版10+4对比T2V工作流_1987403122442219521
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2 smooth Vs Lightning V2混合低噪+原版10+4对比T2V工作流_1987403122442219521.json
hash: b7a2761e5e695bfe
coverage: 1
learned_at: 2026-10-15 22:47:34
nodes: [PathchSageAttentionKJ, CLIPTextEncode, PathchSageAttentionKJ, TorchCompileModel, TorchCompileModel, ModelSamplingSD3, EmptyHunyuanLatentVideo, easy cleanGpuUsed, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, VAEDecode, CLIPTextEncode, TT_img_enc, SaveImage, VAEDecode, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, INTConstant, INTConstant, CLIPTextEncode, TT_img_enc, SaveImage, VAEDecode, LoraLoaderModelOnly, PathchSageAttentionKJ, ImageSharpen, DownloadAndLoadGIMMVFIModel, ImageFromBatch+, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, CLIPTextEncode, KSamplerAdvanced, INTConstant, INTConstant, ModelSamplingSD3, ModelSamplingSD3, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, GIMMVFI_interpolate, ImageFromBatch+, ImageFromBatch+, LoraLoaderModelOnly, VAELoader, LoraLoaderModelOnly, LoraLoaderModelOnly, KSamplerAdvanced, KSamplerAdvanced, PathchSageAttentionKJ, PathchSageAttentionKJ, INTConstant, JWInteger, EmptyHunyuanLatentVideo, JWInteger, JWInteger, VHS_VideoCombine, VHS_VideoCombine, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, LoraLoaderModelOnly, CLIPTextEncode, CLIPLoader, EmptyHunyuanLatentVideo, ModelSamplingSD3, ModelSamplingSD3, ModelSamplingSD3, INTConstant, UNETLoader, CLIPTextEncode, TT_img_enc, SaveImage, VAEDecode, LoraLoaderModelOnly, PathchSageAttentionKJ, LayerUtility: PurgeVRAM, KSamplerAdvanced, ModelSamplingSD3, KSamplerAdvanced, PathchSageAttentionKJ, LoraLoaderModelOnly, CLIPTextEncode, EmptyHunyuanLatentVideo, ModelSamplingSD3, VHS_VideoCombine, ImageConcanate, ImageConcanate, ImageConcanate, ImageFromBatch+, UNETLoader, UNETLoader, INTConstant, INTConstant, LoraLoaderModelOnly, Text Multiline, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 12, "denoise": "beta", "sampler_name": 1, "scheduler": "uni_pc", "seed": "enable", "steps": "fixed"}
---

# 视频生成/文生视频/wan2.2 smooth Vs Lightning V2混合低噪+原版10+4对比T2V工作流_1987403122442219521.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/wan2.2 smooth Vs Lightning V2混合低噪+原版10+4对比T2V工作流_1987403122442219521.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（100 个）：
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `PathchSageAttentionKJ`
- `TorchCompileModel`
- `TorchCompileModel`
- `ModelSamplingSD3`
- `EmptyHunyuanLatentVideo`
- `easy cleanGpuUsed`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `TT_img_enc`
- `SaveImage`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `INTConstant`
- `INTConstant`
- `CLIPTextEncode` ★核心
- `TT_img_enc`
- `SaveImage`
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ImageSharpen`
- `DownloadAndLoadGIMMVFIModel`
- `ImageFromBatch+`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `INTConstant`
- `INTConstant`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `GIMMVFI_interpolate`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `INTConstant`
- `JWInteger`
- `EmptyHunyuanLatentVideo`
- `JWInteger`
- `JWInteger`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `EmptyHunyuanLatentVideo`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `INTConstant`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `TT_img_enc`
- `SaveImage`
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `LayerUtility: PurgeVRAM`
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `EmptyHunyuanLatentVideo`
- `ModelSamplingSD3`
- `VHS_VideoCombine`
- `ImageConcanate`
- `ImageConcanate`
- `ImageConcanate`
- `ImageFromBatch+`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `INTConstant`
- `INTConstant`
- `LoraLoaderModelOnly` ★核心
- `Text Multiline`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `12`
- `sampler_name` = `1`
- `scheduler` = `uni_pc`
- `denoise` = `beta`

## 知识

覆盖率 **100%**（100/100）

**有卡**：`PathchSageAttentionKJ`、`CLIPTextEncode`、`TorchCompileModel`、`ModelSamplingSD3`、`EmptyHunyuanLatentVideo`、`easy cleanGpuUsed`、`LoraLoaderModelOnly`、`VAEDecode`、`TT_img_enc`、`SaveImage`、`INTConstant`、`ImageSharpen`、`DownloadAndLoadGIMMVFIModel`、`ImageFromBatch+`、`LayerUtility: PurgeVRAM`、`KSamplerAdvanced`、`GIMMVFI_interpolate`、`VAELoader`、`JWInteger`、`VHS_VideoCombine`、`CLIPLoader`、`UNETLoader`、`ImageConcanate`、`Text Multiline`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo

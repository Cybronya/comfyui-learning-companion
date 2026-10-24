---
key: 图片生成/图生图/wan2.2首尾帧加速流（自动提示词）_2006270195232415746.json
name: wan2.2首尾帧加速流（自动提示词）_2006270195232415746
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/wan2.2首尾帧加速流（自动提示词）_2006270195232415746.json
hash: f4d495b3f35d7df8
coverage: 0.788462
learned_at: 2026-10-23 11:46:10
nodes: [Note, ImageUpscaleWithModel, VAEDecode, ModelPatchTorchSettings, CLIPVisionLoader, wanBlockSwap, wanBlockSwap, UpscaleModelLoader, SimpleMath+, WanVideoNAG, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelPatchTorchSettings, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, DownloadAndLoadGIMMVFIModel, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Note, ModelSamplingSD3, ModelSamplingSD3, Note, INTConstant, UnetLoaderGGUF, UnetLoaderGGUF, VAELoader, Power Lora Loader (rgthree), Power Lora Loader (rgthree), KSamplerAdvanced, KSamplerAdvanced, CLIPLoader, LoadImage, WanFirstLastFrameToVideo, CLIPTextEncode, PreviewImage, PreviewImage, ImageResizeKJ, ImageResizeKJ, CLIPVisionEncode, CLIPVisionEncode, LoadImage, Note, easy showAnything, RH_Captioner, ImageStitch, CLIPTextEncode, VHS_VideoCombine, GIMMVFI_interpolate, BooleanPrimitive, easy ifElse, Note, Textbox]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 图片生成/图生图/wan2.2首尾帧加速流（自动提示词）_2006270195232415746.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/wan2.2首尾帧加速流（自动提示词）_2006270195232415746.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（52 个）：
- `Note`
- `ImageUpscaleWithModel`
- `VAEDecode` ★核心
- `ModelPatchTorchSettings`
- `CLIPVisionLoader`
- `wanBlockSwap`
- `wanBlockSwap`
- `UpscaleModelLoader`
- `SimpleMath+`
- `WanVideoNAG`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `DownloadAndLoadGIMMVFIModel`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `Note`
- `INTConstant`
- `UnetLoaderGGUF` ★核心
- `UnetLoaderGGUF` ★核心
- `VAELoader`
- `Power Lora Loader (rgthree)`
- `Power Lora Loader (rgthree)`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPLoader`
- `LoadImage`
- `WanFirstLastFrameToVideo`
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `PreviewImage`
- `ImageResizeKJ`
- `ImageResizeKJ`
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `LoadImage`
- `Note`
- `easy showAnything`
- `RH_Captioner`
- `ImageStitch`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `GIMMVFI_interpolate`
- `BooleanPrimitive`
- `easy ifElse`
- `Note`
- `Textbox`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **79%**（41/52）

**有卡**：`ImageUpscaleWithModel`、`VAEDecode`、`ModelPatchTorchSettings`、`CLIPVisionLoader`、`wanBlockSwap`、`UpscaleModelLoader`、`SimpleMath+`、`WanVideoNAG`、`PathchSageAttentionKJ`、`LayerUtility: PurgeVRAM`、`DownloadAndLoadGIMMVFIModel`、`ModelSamplingSD3`、`INTConstant`、`UnetLoaderGGUF`、`VAELoader`、`Power Lora Loader (rgthree)`、`KSamplerAdvanced`、`CLIPLoader`、`LoadImage`、`WanFirstLastFrameToVideo`、`CLIPTextEncode`、`ImageResizeKJ`、`CLIPVisionEncode`、`RH_Captioner`、`ImageStitch`、`VHS_VideoCombine`、`GIMMVFI_interpolate`、`BooleanPrimitive`、`Textbox`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerAdvanced、CLIPVisionEncode、Power Lora Loader (rgthree)

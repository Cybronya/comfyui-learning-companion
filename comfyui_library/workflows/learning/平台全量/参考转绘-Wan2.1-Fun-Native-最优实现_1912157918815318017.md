---
key: 平台全量/参考转绘-Wan2.1-Fun-Native-最优实现_1912157918815318017.json
name: 参考转绘-Wan2.1-Fun-Native-最优实现_1912157918815318017
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/参考转绘-Wan2.1-Fun-Native-最优实现_1912157918815318017.json
hash: e32735dafc92dca9
coverage: 0.970588
learned_at: 2026-11-14 01:50:42
nodes: [WanFunControlToVideo, CLIPVisionLoader, CLIPTextEncode, CLIPTextEncode, CLIPVisionEncode, ImageBlend, AIO_Preprocessor, TorchCompileModelWanVideo, PatchModelPatcherOrder, VHS_VideoInfoLoaded, CLIPLoader, VHS_VideoCombine, VAELoader, StringConstantMultiline, KSampler, WanVideoEnhanceAVideoKJ, SkipLayerGuidanceWanVideo, CFGZeroStarAndInit, ModelSamplingSD3, VAEDecode, VHS_VideoCombine, ImageResizeKJ, INTConstant, AIO_Preprocessor, ImageResizeKJ, WanVideoTeaCacheKJ, UNETLoader, LoraLoaderModelOnly, ImageResizeKJ, PreviewImage, INTConstant, INTConstant, LoadImage, VHS_LoadVideo]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 752198028409443, "steps": 30}
---

# 平台全量/参考转绘-Wan2.1-Fun-Native-最优实现_1912157918815318017.json

> 来源文件 `comfyui_library/workflows/平台全量/参考转绘-Wan2.1-Fun-Native-最优实现_1912157918815318017.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（34 个）：
- `WanFunControlToVideo`
- `CLIPVisionLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPVisionEncode`
- `ImageBlend`
- `AIO_Preprocessor`
- `TorchCompileModelWanVideo`
- `PatchModelPatcherOrder`
- `VHS_VideoInfoLoaded`
- `CLIPLoader`
- `VHS_VideoCombine`
- `VAELoader`
- `StringConstantMultiline`
- `KSampler` ★核心
- `WanVideoEnhanceAVideoKJ`
- `SkipLayerGuidanceWanVideo`
- `CFGZeroStarAndInit`
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `ImageResizeKJ`
- `INTConstant`
- `AIO_Preprocessor`
- `ImageResizeKJ`
- `WanVideoTeaCacheKJ`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `ImageResizeKJ`
- `PreviewImage`
- `INTConstant`
- `INTConstant`
- `LoadImage`
- `VHS_LoadVideo`

## 关键参数

- `seed` = `752198028409443`
- `steps` = `30`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **97%**（33/34）

**有卡**：`WanFunControlToVideo`、`CLIPVisionLoader`、`CLIPTextEncode`、`CLIPVisionEncode`、`ImageBlend`、`AIO_Preprocessor`、`TorchCompileModelWanVideo`、`PatchModelPatcherOrder`、`VHS_VideoInfoLoaded`、`CLIPLoader`、`VHS_VideoCombine`、`VAELoader`、`StringConstantMultiline`、`KSampler`、`WanVideoEnhanceAVideoKJ`、`SkipLayerGuidanceWanVideo`、`CFGZeroStarAndInit`、`ModelSamplingSD3`、`VAEDecode`、`ImageResizeKJ`、`INTConstant`、`WanVideoTeaCacheKJ`、`UNETLoader`、`LoraLoaderModelOnly`、`LoadImage`、`VHS_LoadVideo`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader

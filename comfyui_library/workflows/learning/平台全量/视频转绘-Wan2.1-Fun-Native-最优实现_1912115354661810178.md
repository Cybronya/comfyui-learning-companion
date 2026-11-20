---
key: 平台全量/视频转绘-Wan2.1-Fun-Native-最优实现_1912115354661810178.json
name: 视频转绘-Wan2.1-Fun-Native-最优实现_1912115354661810178
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/视频转绘-Wan2.1-Fun-Native-最优实现_1912115354661810178.json
hash: b60e1d7d79fdf64a
coverage: 1
learned_at: 2026-11-14 02:41:44
nodes: [WanFunControlToVideo, CLIPTextEncode, CLIPTextEncode, CLIPVisionEncode, PatchModelPatcherOrder, VHS_VideoCombine, KSampler, WanVideoEnhanceAVideoKJ, SkipLayerGuidanceWanVideo, CFGZeroStarAndInit, ModelSamplingSD3, VAEDecode, ImageResizeKJ, ImageBlend, TorchCompileModelWanVideo, CLIPLoader, VAELoader, CLIPVisionLoader, VHS_VideoInfoLoaded, VHS_VideoCombine, AIO_Preprocessor, AIO_Preprocessor, INTConstant, INTConstant, INTConstant, ImageResizeKJ, WanVideoTeaCacheKJ, UNETLoader, LoraLoaderModelOnly, StringConstantMultiline, VHS_LoadVideo]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 444937735435673, "steps": 30}
---

# 平台全量/视频转绘-Wan2.1-Fun-Native-最优实现_1912115354661810178.json

> 来源文件 `comfyui_library/workflows/平台全量/视频转绘-Wan2.1-Fun-Native-最优实现_1912115354661810178.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（31 个）：
- `WanFunControlToVideo`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPVisionEncode`
- `PatchModelPatcherOrder`
- `VHS_VideoCombine`
- `KSampler` ★核心
- `WanVideoEnhanceAVideoKJ`
- `SkipLayerGuidanceWanVideo`
- `CFGZeroStarAndInit`
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `ImageResizeKJ`
- `ImageBlend`
- `TorchCompileModelWanVideo`
- `CLIPLoader`
- `VAELoader`
- `CLIPVisionLoader`
- `VHS_VideoInfoLoaded`
- `VHS_VideoCombine`
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `ImageResizeKJ`
- `WanVideoTeaCacheKJ`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `StringConstantMultiline`
- `VHS_LoadVideo`

## 关键参数

- `seed` = `444937735435673`
- `steps` = `30`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（31/31）

**有卡**：`WanFunControlToVideo`、`CLIPTextEncode`、`CLIPVisionEncode`、`PatchModelPatcherOrder`、`VHS_VideoCombine`、`KSampler`、`WanVideoEnhanceAVideoKJ`、`SkipLayerGuidanceWanVideo`、`CFGZeroStarAndInit`、`ModelSamplingSD3`、`VAEDecode`、`ImageResizeKJ`、`ImageBlend`、`TorchCompileModelWanVideo`、`CLIPLoader`、`VAELoader`、`CLIPVisionLoader`、`VHS_VideoInfoLoaded`、`AIO_Preprocessor`、`INTConstant`、`WanVideoTeaCacheKJ`、`UNETLoader`、`LoraLoaderModelOnly`、`StringConstantMultiline`、`VHS_LoadVideo`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、UNETLoader、CFGZeroStarAndInit

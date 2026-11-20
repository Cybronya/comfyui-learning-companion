---
key: 平台全量/wan2.1官方首尾帧-Native-flf2v-720p-最优实现_1914962819446702082.json
name: wan2.1官方首尾帧-Native-flf2v-720p-最优实现_1914962819446702082
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/wan2.1官方首尾帧-Native-flf2v-720p-最优实现_1914962819446702082.json
hash: 81b124d7795e12b3
coverage: 1
learned_at: 2026-11-14 01:19:12
nodes: [CLIPTextEncode, WanFirstLastFrameToVideo, TorchCompileModelWanVideo, PatchModelPatcherOrder, KSampler, VAEDecode, CLIPVisionEncode, CLIPVisionEncode, CLIPLoader, WanVideoTeaCacheKJ, VAELoader, ModelSamplingSD3, CFGZeroStarAndInit, SkipLayerGuidanceWanVideo, WanVideoEnhanceAVideoKJ, VHS_VideoCombine, CLIPVisionLoader, CLIPTextEncode, LoadImage, LoadImage, INTConstant, INTConstant, ImageResizeKJ, ImageResizeKJ, INTConstant, UNETLoader]
patterns: []
missing: []
parameters: {"cfg": 3, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 618697952804774, "steps": 20}
---

# 平台全量/wan2.1官方首尾帧-Native-flf2v-720p-最优实现_1914962819446702082.json

> 来源文件 `comfyui_library/workflows/平台全量/wan2.1官方首尾帧-Native-flf2v-720p-最优实现_1914962819446702082.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（26 个）：
- `CLIPTextEncode` ★核心
- `WanFirstLastFrameToVideo`
- `TorchCompileModelWanVideo`
- `PatchModelPatcherOrder`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `CLIPLoader`
- `WanVideoTeaCacheKJ`
- `VAELoader`
- `ModelSamplingSD3`
- `CFGZeroStarAndInit`
- `SkipLayerGuidanceWanVideo`
- `WanVideoEnhanceAVideoKJ`
- `VHS_VideoCombine`
- `CLIPVisionLoader`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `LoadImage`
- `INTConstant`
- `INTConstant`
- `ImageResizeKJ`
- `ImageResizeKJ`
- `INTConstant`
- `UNETLoader` ★核心

## 关键参数

- `seed` = `618697952804774`
- `steps` = `20`
- `cfg` = `3`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（26/26）

**有卡**：`CLIPTextEncode`、`WanFirstLastFrameToVideo`、`TorchCompileModelWanVideo`、`PatchModelPatcherOrder`、`KSampler`、`VAEDecode`、`CLIPVisionEncode`、`CLIPLoader`、`WanVideoTeaCacheKJ`、`VAELoader`、`ModelSamplingSD3`、`CFGZeroStarAndInit`、`SkipLayerGuidanceWanVideo`、`WanVideoEnhanceAVideoKJ`、`VHS_VideoCombine`、`CLIPVisionLoader`、`LoadImage`、`INTConstant`、`ImageResizeKJ`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader、CFGZeroStarAndInit

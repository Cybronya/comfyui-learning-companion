---
key: 平台全量/首尾帧-Wan2.1-Fun-Native +Reward-LoRA-最优实现_1912162790059245570.json
name: 首尾帧-Wan2.1-Fun-Native +Reward-LoRA-最优实现_1912162790059245570
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/首尾帧-Wan2.1-Fun-Native +Reward-LoRA-最优实现_1912162790059245570.json
hash: efc71f960e1844cd
coverage: 1
learned_at: 2026-11-14 02:51:14
nodes: [PathchSageAttentionKJ, TorchCompileModelWanVideo, PatchModelPatcherOrder, KSampler, SkipLayerGuidanceWanVideo, CFGZeroStarAndInit, VAEDecode, CLIPTextEncode, CLIPTextEncode, VHS_VideoCombine, VAELoader, CLIPLoader, ImageResizeKJ, CLIPVisionLoader, CLIPVisionEncode, WanVideoEnhanceAVideoKJ, UNETLoader, ModelSamplingSD3, WanVideoTeaCacheKJ, WanFunInpaintToVideo, INTConstant, LoraLoaderModelOnly, ImageResizeKJ, LoadImage, LoadImage, INTConstant, INTConstant, StringConstantMultiline]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 317385472335877, "steps": 30}
---

# 平台全量/首尾帧-Wan2.1-Fun-Native +Reward-LoRA-最优实现_1912162790059245570.json

> 来源文件 `comfyui_library/workflows/平台全量/首尾帧-Wan2.1-Fun-Native +Reward-LoRA-最优实现_1912162790059245570.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（28 个）：
- `PathchSageAttentionKJ`
- `TorchCompileModelWanVideo`
- `PatchModelPatcherOrder`
- `KSampler` ★核心
- `SkipLayerGuidanceWanVideo`
- `CFGZeroStarAndInit`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `VAELoader`
- `CLIPLoader`
- `ImageResizeKJ`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `WanVideoEnhanceAVideoKJ`
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `WanVideoTeaCacheKJ`
- `WanFunInpaintToVideo`
- `INTConstant`
- `LoraLoaderModelOnly` ★核心
- `ImageResizeKJ`
- `LoadImage`
- `LoadImage`
- `INTConstant`
- `INTConstant`
- `StringConstantMultiline`

## 关键参数

- `seed` = `317385472335877`
- `steps` = `30`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（28/28）

**有卡**：`PathchSageAttentionKJ`、`TorchCompileModelWanVideo`、`PatchModelPatcherOrder`、`KSampler`、`SkipLayerGuidanceWanVideo`、`CFGZeroStarAndInit`、`VAEDecode`、`CLIPTextEncode`、`VHS_VideoCombine`、`VAELoader`、`CLIPLoader`、`ImageResizeKJ`、`CLIPVisionLoader`、`CLIPVisionEncode`、`WanVideoEnhanceAVideoKJ`、`UNETLoader`、`ModelSamplingSD3`、`WanVideoTeaCacheKJ`、`WanFunInpaintToVideo`、`INTConstant`、`LoraLoaderModelOnly`、`LoadImage`、`StringConstantMultiline`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader

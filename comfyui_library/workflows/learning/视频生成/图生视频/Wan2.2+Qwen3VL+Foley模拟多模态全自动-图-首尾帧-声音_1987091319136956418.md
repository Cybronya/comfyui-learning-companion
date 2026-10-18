---
key: 视频生成/图生视频/Wan2.2+Qwen3VL+Foley模拟多模态全自动-图-首尾帧-声音_1987091319136956418.json
name: Wan2.2+Qwen3VL+Foley模拟多模态全自动-图-首尾帧-声音_1987091319136956418.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2+Qwen3VL+Foley模拟多模态全自动-图-首尾帧-声音_1987091319136956418.json
hash: 73608db2ffeb3447
coverage: 0.410526
learned_at: 2026-10-15 22:32:57
nodes: [PathchSageAttentionKJ, PathchSageAttentionKJ, CLIPTextEncode, Reroute, Reroute, Reroute, ModelPatchTorchSettings, ModelPatchTorchSettings, Reroute, Reroute, Reroute, Reroute, Note, CLIPLoader, Note, wanBlockSwap, Reroute, Reroute, Reroute, Reroute, Note, Reroute, ModelSamplingSD3, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, ModelSamplingSD3, Reroute, Reroute, Reroute, Note, INTConstant, INTConstant, Reroute, Reroute, Reroute, Note, WanFirstLastFrameToVideo, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, VAELoader, Int, CLIPTextEncode, Reroute, Reroute, Reroute, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, ImageResizeKJv2, PreviewImage, ImageResizeKJv2, PreviewImage, wanBlockSwap, ImageLoader, ImageLoader, UNETLoader, UNETLoader, Fast Groups Bypasser (rgthree), easy showAnything, Any To Any, MultiplePathsInput, VHS_SelectFilename, VHS_VideoCombine, Reroute, RIFE VFI, Reroute, VAEDecode, LayerUtility: PurgeVRAM V2, Note, Reroute, LayerUtility: PurgeVRAM V2, Reroute, Reroute, easy float, Reroute, HunyuanVideoFoley, Reroute, VHS_VideoCombine, Reroute, Qwen3_VQA, KSamplerAdvanced, KSamplerAdvanced, Int]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "normal", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2+Qwen3VL+Foley模拟多模态全自动-图-首尾帧-声音_1987091319136956418.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1987091319136956418.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（95 个）：
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Note`
- `CLIPLoader`
- `Note`
- `wanBlockSwap`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Note`
- `Reroute`
- `ModelSamplingSD3`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `ModelSamplingSD3`
- `Reroute`
- `Reroute`
- `Reroute`
- `Note`
- `INTConstant`
- `INTConstant`
- `Reroute`
- `Reroute`
- `Reroute`
- `Note`
- `WanFirstLastFrameToVideo`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `VAELoader`
- `Int`
- `CLIPTextEncode` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageResizeKJv2`
- `PreviewImage`
- `ImageResizeKJv2`
- `PreviewImage`
- `wanBlockSwap`
- `ImageLoader`
- `ImageLoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `Fast Groups Bypasser (rgthree)`
- `easy showAnything`
- `Any To Any`
- `MultiplePathsInput`
- `VHS_SelectFilename`
- `VHS_VideoCombine`
- `Reroute`
- `RIFE VFI`
- `Reroute`
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM V2`
- `Note`
- `Reroute`
- `LayerUtility: PurgeVRAM V2`
- `Reroute`
- `Reroute`
- `easy float`
- `Reroute`
- `HunyuanVideoFoley`
- `Reroute`
- `VHS_VideoCombine`
- `Reroute`
- `Qwen3_VQA`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `Int`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `normal`

## 知识

覆盖率 **41%**（39/95）

**有卡**：`PathchSageAttentionKJ`、`CLIPTextEncode`、`ModelPatchTorchSettings`、`CLIPLoader`、`wanBlockSwap`、`ModelSamplingSD3`、`INTConstant`、`WanFirstLastFrameToVideo`、`VAELoader`、`Int`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageResizeKJv2`、`ImageLoader`、`UNETLoader`、`Any To Any`、`MultiplePathsInput`、`VHS_SelectFilename`、`VHS_VideoCombine`、`RIFE VFI`、`VAEDecode`、`LayerUtility: PurgeVRAM V2`、`easy float`、`HunyuanVideoFoley`、`Qwen3_VQA`、`KSamplerAdvanced`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、KSamplerAdvanced、ImageResizeKJv2

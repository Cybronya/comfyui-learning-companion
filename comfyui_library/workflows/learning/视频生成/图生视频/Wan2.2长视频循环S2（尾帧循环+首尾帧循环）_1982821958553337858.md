---
key: 视频生成/图生视频/Wan2.2长视频循环S2（尾帧循环+首尾帧循环）_1982821958553337858.json
name: Wan2.2长视频循环S2（尾帧循环+首尾帧循环）_1982821958553337858.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2长视频循环S2（尾帧循环+首尾帧循环）_1982821958553337858.json
hash: 9b27b3f519ec0226
coverage: 0.862069
learned_at: 2026-10-15 22:32:43
nodes: [PathchSageAttentionKJ, PathchSageAttentionKJ, wanBlockSwap, wanBlockSwap, VAELoader, UNETLoader, ImageBatch, easy forLoopEnd, PathchSageAttentionKJ, CLIPVisionLoader, PathchSageAttentionKJ, Reroute, VAELoader, wanBlockSwap, wanBlockSwap, ImageResizeKJv2, CR Load Image List, easy cleanGpuUsed, CR Index Increment, ImageResizeKJv2, CLIPVisionEncode, CLIPVisionEncode, CLIPTextEncode, CR Load Image List, Reroute, PreviewImage, PreviewImage, easy forLoopStart, CLIPTextEncode, CLIPTextEncode, UNETLoader, UNETLoader, ImageBatch, easy forLoopEnd, ModelPatchTorchSettings, ModelPatchTorchSettings, RIFE VFI, CLIPLoader, CLIPLoader, ShowText|pysssss, CLIPVisionLoader, CR Prompt List, easy cleanGpuUsed, ModelPatchTorchSettings, ModelPatchTorchSettings, ModelSamplingSD3, ModelSamplingSD3, UNETLoader, WanFirstLastFrameToVideo, VAEDecode, easy cleanGpuUsed, VHS_VideoCombine, easy cleanGpuUsed, KSamplerAdvanced, KSamplerAdvanced, PreviewAny, VRAM_Debug, ZML_DualInteger, LoadImage, ImpactInt, ShowText|pysssss, VHS_VideoCombine, easy forLoopStart, GetNode, CR Prompt List, SetNode, ImpactInt, ZML_DualInteger, WanImageToVideo, PreviewImage, CLIPVisionEncode, VHS_SplitImages, ImageResizeKJv2, VAEDecode, easy cleanGpuUsed, VHS_VideoCombine, CR Text, KSamplerAdvanced, VRAM_Debug, PreviewAny, CLIPTextEncode, KSamplerAdvanced, Label (rgthree), LoadImage, Fast Groups Bypasser (rgthree), RIFE VFI, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2长视频循环S2（尾帧循环+首尾帧循环）_1982821958553337858.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1982821958553337858.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（87 个）：
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `wanBlockSwap`
- `wanBlockSwap`
- `VAELoader`
- `UNETLoader` ★核心
- `ImageBatch`
- `easy forLoopEnd`
- `PathchSageAttentionKJ`
- `CLIPVisionLoader`
- `PathchSageAttentionKJ`
- `Reroute`
- `VAELoader`
- `wanBlockSwap`
- `wanBlockSwap`
- `ImageResizeKJv2`
- `CR Load Image List`
- `easy cleanGpuUsed`
- `CR Index Increment`
- `ImageResizeKJv2`
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `CLIPTextEncode` ★核心
- `CR Load Image List`
- `Reroute`
- `PreviewImage`
- `PreviewImage`
- `easy forLoopStart`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `ImageBatch`
- `easy forLoopEnd`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `RIFE VFI`
- `CLIPLoader`
- `CLIPLoader`
- `ShowText|pysssss`
- `CLIPVisionLoader`
- `CR Prompt List`
- `easy cleanGpuUsed`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `WanFirstLastFrameToVideo`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `PreviewAny`
- `VRAM_Debug`
- `ZML_DualInteger`
- `LoadImage`
- `ImpactInt`
- `ShowText|pysssss`
- `VHS_VideoCombine`
- `easy forLoopStart`
- `GetNode`
- `CR Prompt List`
- `SetNode`
- `ImpactInt`
- `ZML_DualInteger`
- `WanImageToVideo`
- `PreviewImage`
- `CLIPVisionEncode`
- `VHS_SplitImages`
- `ImageResizeKJv2`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `CR Text`
- `KSamplerAdvanced` ★核心
- `VRAM_Debug`
- `PreviewAny`
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `Label (rgthree)`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `RIFE VFI`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **86%**（75/87）

**有卡**：`PathchSageAttentionKJ`、`wanBlockSwap`、`VAELoader`、`UNETLoader`、`ImageBatch`、`easy forLoopEnd`、`CLIPVisionLoader`、`ImageResizeKJv2`、`CR Load Image List`、`easy cleanGpuUsed`、`CR Index Increment`、`CLIPVisionEncode`、`CLIPTextEncode`、`easy forLoopStart`、`ModelPatchTorchSettings`、`RIFE VFI`、`CLIPLoader`、`CR Prompt List`、`ModelSamplingSD3`、`WanFirstLastFrameToVideo`、`VAEDecode`、`VHS_VideoCombine`、`KSamplerAdvanced`、`VRAM_Debug`、`ZML_DualInteger`、`LoadImage`、`ImpactInt`、`WanImageToVideo`、`VHS_SplitImages`、`CR Text`、`Label (rgthree)`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、CLIPVisionEncode

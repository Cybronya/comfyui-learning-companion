---
key: 视频生成/图生视频/Wan_2.2_首中尾三帧视频工作流_1995538932051927042.json
name: Wan_2.2_首中尾三帧视频工作流_1995538932051927042.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1995538932051927042.json
hash: bc8ac8241a5b6f0e
coverage: 0.888889
learned_at: 2026-10-15 22:33:23
nodes: [CLIPVisionEncode, ImageStitch, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPVisionLoader, wanBlockSwap, UNETLoader, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, ModelPatchTorchSettings, wanBlockSwap, ModelSamplingSD3, PathchSageAttentionKJ, CLIPLoader, ImageConcatMulti, PrimitiveStringMultiline, Wan22PromptSelector, Text Concatenate, ImageConcatMulti, ImageScaleToTotalPixels, CLIPTextEncode, CLIPTextEncode, VAELoader, CLIPVisionEncode, RH_LLMAPI_NODE, ImpactSwitch, ShowText|pysssss, VAEDecode, ImageBatchMulti, LayerUtility: ImageScaleByAspectRatio V2, ImageResizeKJv2, ImageResizeKJv2, WanMultiFrameRefToVideo, MathExpression|pysssss, PrimitiveInt, PrimitiveInt, VHS_VideoCombine, KSamplerAdvanced, KSamplerAdvanced, LoadImage, LoadImage, LoadImage, ModelPatchTorchSettings]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/Wan_2.2_首中尾三帧视频工作流_1995538932051927042.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1995538932051927042.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（45 个）：
- `CLIPVisionEncode`
- `ImageStitch`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPVisionLoader`
- `wanBlockSwap`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `wanBlockSwap`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `CLIPLoader`
- `ImageConcatMulti`
- `PrimitiveStringMultiline`
- `Wan22PromptSelector`
- `Text Concatenate`
- `ImageConcatMulti`
- `ImageScaleToTotalPixels`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `CLIPVisionEncode`
- `RH_LLMAPI_NODE`
- `ImpactSwitch`
- `ShowText|pysssss`
- `VAEDecode` ★核心
- `ImageBatchMulti`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `WanMultiFrameRefToVideo`
- `MathExpression|pysssss`
- `PrimitiveInt`
- `PrimitiveInt`
- `VHS_VideoCombine`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ModelPatchTorchSettings`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **89%**（40/45）

**有卡**：`CLIPVisionEncode`、`ImageStitch`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPVisionLoader`、`wanBlockSwap`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`CLIPLoader`、`ImageConcatMulti`、`Wan22PromptSelector`、`Text Concatenate`、`ImageScaleToTotalPixels`、`CLIPTextEncode`、`VAELoader`、`RH_LLMAPI_NODE`、`VAEDecode`、`ImageBatchMulti`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageResizeKJv2`、`WanMultiFrameRefToVideo`、`MathExpression|pysssss`、`VHS_VideoCombine`、`KSamplerAdvanced`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2

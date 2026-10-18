---
key: 视频生成/图生视频/Wan2.2 PainterI2V慢动作优化无限长视频生成(QwenVL增强)_1992287754939854849.json
name: Wan2.2 PainterI2V慢动作优化无限长视频生成(QwenVL增强)_1992287754939854849.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 PainterI2V慢动作优化无限长视频生成(QwenVL增强)_1992287754939854849.json
hash: 3395940e48255372
coverage: 0.474359
learned_at: 2026-10-15 22:33:16
nodes: [SetNode, SetNode, GetNode, GetNode, SetNode, GetNode, GetNode, SetNode, SetNode, SetNode, ImageResizeKJv2, SetNode, SetNode, GetImageRangeFromBatch, GetNode, SetNode, LoraLoaderModelOnly, INTConstant, INTConstant, GetNode, GetNode, GetNode, GetNode, CFGZeroStar, UNETLoader, CLIPTextEncode, CLIPLoader, VAELoader, CLIPVisionLoader, GetNode, GetNode, GetNode, KSamplerAdvanced, KSamplerAdvanced, WanVideoNAG, GetNode, CLIPVisionEncode, SetNode, GetNode, GetNode, ModelSamplingSD3, ModelSamplingSD3, PainterI2V, GetNode, SetNode, GetNode, CLIPVisionEncode, GetNode, easy batchAnything, VAEDecode, GetImageRangeFromBatch, SetNode, GetNode, SetNode, AILab_QwenVL, PreviewAny, GetNode, SetNode, INTConstant, CLIPTextEncode, GetNode, GetNode, GetNode, ForLoopClose, VHS_VideoCombine, SetNode, PathchSageAttentionKJ, UNETLoader, LoraLoaderModelOnly, SetNode, WanImageToVideo, ForLoopOpen, GetNode, VHS_VideoCombine, LoadImage, INTConstant, LoraLoaderModelOnly, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2 PainterI2V慢动作优化无限长视频生成(QwenVL增强)_1992287754939854849.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1992287754939854849.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（78 个）：
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `SetNode`
- `SetNode`
- `GetImageRangeFromBatch`
- `GetNode`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `INTConstant`
- `INTConstant`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CFGZeroStar`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPVisionLoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `WanVideoNAG`
- `GetNode`
- `CLIPVisionEncode`
- `SetNode`
- `GetNode`
- `GetNode`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `PainterI2V`
- `GetNode`
- `SetNode`
- `GetNode`
- `CLIPVisionEncode`
- `GetNode`
- `easy batchAnything`
- `VAEDecode` ★核心
- `GetImageRangeFromBatch`
- `SetNode`
- `GetNode`
- `SetNode`
- `AILab_QwenVL`
- `PreviewAny`
- `GetNode`
- `SetNode`
- `INTConstant`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `ForLoopClose`
- `VHS_VideoCombine`
- `SetNode`
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `WanImageToVideo`
- `ForLoopOpen`
- `GetNode`
- `VHS_VideoCombine`
- `LoadImage`
- `INTConstant`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **47%**（37/78）

**有卡**：`ImageResizeKJv2`、`GetImageRangeFromBatch`、`LoraLoaderModelOnly`、`INTConstant`、`CFGZeroStar`、`UNETLoader`、`CLIPTextEncode`、`CLIPLoader`、`VAELoader`、`CLIPVisionLoader`、`KSamplerAdvanced`、`WanVideoNAG`、`CLIPVisionEncode`、`ModelSamplingSD3`、`PainterI2V`、`easy batchAnything`、`VAEDecode`、`AILab_QwenVL`、`ForLoopClose`、`VHS_VideoCombine`、`PathchSageAttentionKJ`、`WanImageToVideo`、`ForLoopOpen`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced

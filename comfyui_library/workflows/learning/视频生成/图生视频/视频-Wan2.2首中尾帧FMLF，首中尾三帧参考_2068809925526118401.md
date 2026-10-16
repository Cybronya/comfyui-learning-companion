---
key: 视频生成/图生视频/视频-Wan2.2首中尾帧FMLF，首中尾三帧参考_2068809925526118401.json
name: 视频-Wan2.2首中尾帧FMLF，首中尾三帧参考_2068809925526118401.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2068809925526118401.json
hash: 54638f79d5dd3c95
coverage: 0.432099
learned_at: 2026-10-15 22:40:22
nodes: [CFGZeroStar, SetNode, CLIPLoader, SetNode, SetNode, SetNode, GetNode, WanVideoNAG, SetNode, SetNode, GetNode, GetNode, ImageResizeKJv2, SetNode, INTConstant, INTConstant, GetNode, GetNode, ImageResizeKJv2, SetNode, GetNode, GetNode, ImageResizeKJv2, SetNode, GetNode, GetNode, CLIPVisionEncode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, ModelSamplingSD3, ModelSamplingSD3, VAEDecode, KSamplerAdvanced, LoadImage, LoadImage, CLIPTextEncode, CLIPTextEncode, SetNode, SetNode, CLIPVisionEncode, GetNode, GetNode, GetNode, CLIPVisionEncode, GetNode, CLIPVisionLoader, PathchSageAttentionKJ, SetNode, GetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, WanFirstMiddleLastFrameToVideo, VAELoader, UNETLoader, UNETLoader, KSamplerAdvanced, LoadImage, GetNode, CR Seed, SetNode, INTConstant, SetNode, VHS_VideoCombine, GetNode, CM_IntToFloat, INTConstant, SetNode, GetNode, GetNode, ComfyMathExpression]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/视频-Wan2.2首中尾帧FMLF，首中尾三帧参考_2068809925526118401.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2068809925526118401.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（81 个）：
- `CFGZeroStar`
- `SetNode`
- `CLIPLoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `WanVideoNAG`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `SetNode`
- `INTConstant`
- `INTConstant`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `SetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `SetNode`
- `GetNode`
- `GetNode`
- `CLIPVisionEncode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `LoadImage`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SetNode`
- `SetNode`
- `CLIPVisionEncode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPVisionEncode`
- `GetNode`
- `CLIPVisionLoader`
- `PathchSageAttentionKJ`
- `SetNode`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `WanFirstMiddleLastFrameToVideo`
- `VAELoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `KSamplerAdvanced` ★核心
- `LoadImage`
- `GetNode`
- `CR Seed`
- `SetNode`
- `INTConstant`
- `SetNode`
- `VHS_VideoCombine`
- `GetNode`
- `CM_IntToFloat`
- `INTConstant`
- `SetNode`
- `GetNode`
- `GetNode`
- `ComfyMathExpression`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **43%**（35/81）

**有卡**：`CFGZeroStar`、`CLIPLoader`、`WanVideoNAG`、`ImageResizeKJv2`、`INTConstant`、`CLIPVisionEncode`、`ModelSamplingSD3`、`VAEDecode`、`KSamplerAdvanced`、`LoadImage`、`CLIPTextEncode`、`CLIPVisionLoader`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`WanFirstMiddleLastFrameToVideo`、`VAELoader`、`UNETLoader`、`CR Seed`、`VHS_VideoCombine`、`CM_IntToFloat`、`ComfyMathExpression`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced

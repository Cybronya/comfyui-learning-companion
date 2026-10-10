---
key: 视频生成/文生视频/Wan2.2-VACE-首尾帧_1950435330224775169.json
name: Wan2.2-VACE-首尾帧_1950435330224775169
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2-VACE-首尾帧_1950435330224775169.json
hash: 9650073f0dfce0af
coverage: 0.909091
learned_at: 2026-10-10 23:07:18
nodes: [CLIPLoader, CLIPTextEncode, CFGZeroStarAndInit, CLIPTextEncode, ImageResizeKJ, INTConstant, GetImageSizeAndCount, ImageResizeKJ, WanVideoVACEStartToEndFrame, VAEDecode, TrimVideoLatent, KSamplerAdvanced, KSamplerAdvanced, easy int, easy int, WanVideoEnhanceAVideoKJ, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, CFGZeroStarAndInit, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, WanVideoEnhanceAVideoKJ, WanVaceToVideo, String Literal, VAELoader, UnetLoaderGGUF, UnetLoaderGGUF, INTConstant, LoadImage, LoadImage, VHS_VideoCombine]
patterns: []
missing: [String Literal, easy int, easy int]
parameters: {"cfg": 10, "denoise": "beta", "sampler_name": 1, "scheduler": "lcm", "seed": "disable", "steps": "fixed"}
discoveries: [次要节点 `String Literal` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/Wan2.2-VACE-首尾帧_1950435330224775169.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2-VACE-首尾帧_1950435330224775169.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（33 个）：
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CFGZeroStarAndInit`
- `CLIPTextEncode` ★核心
- `ImageResizeKJ`
- `INTConstant`
- `GetImageSizeAndCount`
- `ImageResizeKJ`
- `WanVideoVACEStartToEndFrame`
- `VAEDecode` ★核心
- `TrimVideoLatent`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `easy int`
- `easy int`
- `WanVideoEnhanceAVideoKJ`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `CFGZeroStarAndInit`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `WanVideoEnhanceAVideoKJ`
- `WanVaceToVideo`
- `String Literal`
- `VAELoader`
- `UnetLoaderGGUF` ★核心
- `UnetLoaderGGUF` ★核心
- `INTConstant`
- `LoadImage`
- `LoadImage`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `10`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `beta`

## 知识

覆盖率 **91%**（30/33）

**有卡**：`CLIPLoader`、`CLIPTextEncode`、`CFGZeroStarAndInit`、`ImageResizeKJ`、`INTConstant`、`GetImageSizeAndCount`、`WanVideoVACEStartToEndFrame`、`VAEDecode`、`TrimVideoLatent`、`KSamplerAdvanced`、`WanVideoEnhanceAVideoKJ`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`WanVaceToVideo`、`VAELoader`、`UnetLoaderGGUF`、`LoadImage`、`VHS_VideoCombine`

**缺卡**（3）：`String Literal`、`easy int`、`easy int`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerAdvanced、CFGZeroStarAndInit

## 学习发现

- 次要节点 `String Literal` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识

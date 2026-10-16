---
key: 视频生成/文生视频/LTXV0.9.6-秒级视频生成-文生视频_1897511691662348290.json
name: LTXV0.9.6-秒级视频生成-文生视频_1897511691662348290.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1897511691662348290.json
hash: a3a1f32ddebce768
coverage: 0.939394
learned_at: 2026-10-15 22:43:20
nodes: [LTXVScheduler, SamplerCustom, CLIPTextEncode, KSamplerSelect, LTXVConditioning, VAEDecode, LTXVScheduler, KSamplerSelect, CLIPLoader, VAEDecode, CLIPTextEncode, Note, EmptyLTXVLatentVideo, LTXVConditioning, SamplerCustom, VHS_VideoCombine, CLIPLoader, VHS_VideoCombine, Primitive integer [Crystools], Primitive integer [Crystools], Primitive integer [Crystools], CheckpointLoaderSimple, CheckpointLoaderSimple, LTXVImgToVideo, LTXVPreprocess, LTXVPromptEnhancerLoader, LoadImage, LTXVPromptEnhancer, CLIPTextEncode, CLIPTextEncode, Text Concatenate, Text Multiline, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
parameters: {"checkpoint": "ltxv-2b-0.9.6-dev-04-25-v1.safetensors"}
---

# 视频生成/文生视频/LTXV0.9.6-秒级视频生成-文生视频_1897511691662348290.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1897511691662348290.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（33 个）：
- `LTXVScheduler`
- `SamplerCustom` ★核心
- `CLIPTextEncode` ★核心
- `KSamplerSelect` ★核心
- `LTXVConditioning`
- `VAEDecode` ★核心
- `LTXVScheduler`
- `KSamplerSelect` ★核心
- `CLIPLoader`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `Note`
- `EmptyLTXVLatentVideo`
- `LTXVConditioning`
- `SamplerCustom` ★核心
- `VHS_VideoCombine`
- `CLIPLoader`
- `VHS_VideoCombine`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `CheckpointLoaderSimple` ★核心
- `CheckpointLoaderSimple` ★核心
- `LTXVImgToVideo`
- `LTXVPreprocess`
- `LTXVPromptEnhancerLoader`
- `LoadImage`
- `LTXVPromptEnhancer`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Text Concatenate`
- `Text Multiline`
- `Fast Groups Bypasser (rgthree)`

## 关键参数

- `checkpoint` = `ltxv-2b-0.9.6-dev-04-25-v1.safetensors`

## 知识

覆盖率 **94%**（31/33）

**有卡**：`LTXVScheduler`、`SamplerCustom`、`CLIPTextEncode`、`KSamplerSelect`、`LTXVConditioning`、`VAEDecode`、`CLIPLoader`、`EmptyLTXVLatentVideo`、`VHS_VideoCombine`、`Primitive integer [Crystools]`、`CheckpointLoaderSimple`、`LTXVImgToVideo`、`LTXVPreprocess`、`LTXVPromptEnhancerLoader`、`LoadImage`、`LTXVPromptEnhancer`、`Text Concatenate`、`Text Multiline`

**用到的条目**：VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerSelect、SamplerCustom、EmptyLTXVLatentVideo

---
key: 视频生成/图生视频/wan2.1-FUN-小姐姐跳舞V1（详细讲解使用）_1912620115643564034.json
name: wan2.1-FUN-小姐姐跳舞V1（详细讲解使用）_1912620115643564034.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.1-FUN-小姐姐跳舞V1（详细讲解使用）_1912620115643564034.json
hash: 40c82d1fb2156a13
coverage: 0.692308
learned_at: 2026-10-15 22:29:32
nodes: [LoraLoaderModelOnly, CLIPTextEncode, CLIPTextEncode, CLIPVisionEncode, RandomNoise, CFGGuider, KSamplerSelect, BasicScheduler, easy cleanGpuUsed, Anything Everywhere, CLIPVisionLoader, Anything Everywhere, OpenposePreprocessor, ImageScale, EmptyHunyuanLatentVideo, VAELoader, Anything Everywhere, Anything Everywhere, Anything Everywhere, LoadImage, VHS_VideoCombine, VHS_VideoCombine, VAEDecode, SamplerCustomAdvanced, ShowText|pysssss, Joy_caption_two_load, Joy_caption_two, ImageCASharpening+, UNETLoader, CLIPLoader, WanFunControlToVideo, Note, Note, Note, workflow>1, Note, Note, VHS_LoadVideo, Note]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.1-FUN-小姐姐跳舞V1（详细讲解使用）_1912620115643564034.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1912620115643564034.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（39 个）：
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPVisionEncode`
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `easy cleanGpuUsed`
- `Anything Everywhere`
- `CLIPVisionLoader`
- `Anything Everywhere`
- `OpenposePreprocessor`
- `ImageScale`
- `EmptyHunyuanLatentVideo`
- `VAELoader`
- `Anything Everywhere`
- `Anything Everywhere`
- `Anything Everywhere`
- `LoadImage`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `ShowText|pysssss`
- `Joy_caption_two_load`
- `Joy_caption_two`
- `ImageCASharpening+`
- `UNETLoader` ★核心
- `CLIPLoader`
- `WanFunControlToVideo`
- `Note`
- `Note`
- `Note`
- `workflow>1`
- `Note`
- `Note`
- `VHS_LoadVideo`
- `Note`

## 知识

覆盖率 **69%**（27/39）

**有卡**：`LoraLoaderModelOnly`、`CLIPTextEncode`、`CLIPVisionEncode`、`RandomNoise`、`CFGGuider`、`KSamplerSelect`、`BasicScheduler`、`easy cleanGpuUsed`、`CLIPVisionLoader`、`OpenposePreprocessor`、`ImageScale`、`EmptyHunyuanLatentVideo`、`VAELoader`、`LoadImage`、`VHS_VideoCombine`、`VAEDecode`、`SamplerCustomAdvanced`、`Joy_caption_two_load`、`Joy_caption_two`、`ImageCASharpening+`、`UNETLoader`、`CLIPLoader`、`WanFunControlToVideo`、`workflow>1`、`VHS_LoadVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、OpenposePreprocessor

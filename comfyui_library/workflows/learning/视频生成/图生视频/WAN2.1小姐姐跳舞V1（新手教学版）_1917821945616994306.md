---
key: 视频生成/图生视频/WAN2.1小姐姐跳舞V1（新手教学版）_1917821945616994306.json
name: WAN2.1小姐姐跳舞V1（新手教学版）_1917821945616994306.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1917821945616994306.json
hash: 072a5e93e9ab5a4c
coverage: 0.692308
learned_at: 2026-10-15 22:29:40
nodes: [LoraLoaderModelOnly, CLIPTextEncode, CLIPTextEncode, CLIPVisionEncode, RandomNoise, CFGGuider, KSamplerSelect, BasicScheduler, easy cleanGpuUsed, Anything Everywhere, CLIPVisionLoader, Anything Everywhere, OpenposePreprocessor, ImageScale, EmptyHunyuanLatentVideo, VAELoader, Anything Everywhere, Anything Everywhere, Anything Everywhere, VHS_VideoCombine, VHS_VideoCombine, VAEDecode, SamplerCustomAdvanced, ShowText|pysssss, Joy_caption_two_load, Joy_caption_two, ImageCASharpening+, UNETLoader, CLIPLoader, WanFunControlToVideo, Note, Note, Note, workflow>1, Note, Note, Note, LoadImage, VHS_LoadVideo]
patterns: []
missing: []
---

# 视频生成/图生视频/WAN2.1小姐姐跳舞V1（新手教学版）_1917821945616994306.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1917821945616994306.json`

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
- `Note`
- `LoadImage`
- `VHS_LoadVideo`

## 知识

覆盖率 **69%**（27/39）

**有卡**：`LoraLoaderModelOnly`、`CLIPTextEncode`、`CLIPVisionEncode`、`RandomNoise`、`CFGGuider`、`KSamplerSelect`、`BasicScheduler`、`easy cleanGpuUsed`、`CLIPVisionLoader`、`OpenposePreprocessor`、`ImageScale`、`EmptyHunyuanLatentVideo`、`VAELoader`、`VHS_VideoCombine`、`VAEDecode`、`SamplerCustomAdvanced`、`Joy_caption_two_load`、`Joy_caption_two`、`ImageCASharpening+`、`UNETLoader`、`CLIPLoader`、`WanFunControlToVideo`、`workflow>1`、`LoadImage`、`VHS_LoadVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、OpenposePreprocessor

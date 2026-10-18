---
key: 视频生成/图生视频/Images to Video+Bernini图生视频+YC+Foley音效Sound+Effect_2104029726410100737.json
name: Images to Video+Bernini图生视频+YC+Foley音效Sound+Effect_2104029726410100737
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Images to Video+Bernini图生视频+YC+Foley音效Sound+Effect_2104029726410100737.json
hash: c7392ddb689b6361
coverage: 0.906977
learned_at: 2026-10-17 02:28:46
nodes: [JWInteger, PrimitiveInt, VHS_VideoCombine, VHS_SelectFilename, Any To Any, easy cleanGpuUsed, CR Prompt Text, BerniniPromptEnhancer, RHLLMChatNode, StringReplace, StringReplace, easy showAnything, UNETLoader, PathchSageAttentionKJ, UNETLoader, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, VAELoader, CLIPLoader, CLIPTextEncode, CLIPTextEncode, KSamplerAdvanced, KSamplerAdvanced, BerniniConditioning, VAEDecode, CreateVideo, easy cleanGpuUsed, GetVideoComponents, LoraLoaderModelOnly, MarkdownNote, LayerUtility: ImageScaleByAspectRatio V2, Qwen3_VQA, HunyuanVideoFoley, easy showAnything, easy cleanGpuUsed, VHS_VideoCombine, Text, LoraLoaderModelOnly, LoraLoaderModelOnly, SaveVideo, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 10, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/Images to Video+Bernini图生视频+YC+Foley音效Sound+Effect_2104029726410100737.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Images to Video+Bernini图生视频+YC+Foley音效Sound+Effect_2104029726410100737.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（43 个）：
- `JWInteger`
- `PrimitiveInt`
- `VHS_VideoCombine`
- `VHS_SelectFilename`
- `Any To Any`
- `easy cleanGpuUsed`
- `CR Prompt Text`
- `BerniniPromptEnhancer`
- `RHLLMChatNode`
- `StringReplace`
- `StringReplace`
- `easy showAnything`
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `BerniniConditioning`
- `VAEDecode` ★核心
- `CreateVideo`
- `easy cleanGpuUsed`
- `GetVideoComponents`
- `LoraLoaderModelOnly` ★核心
- `MarkdownNote`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Qwen3_VQA`
- `HunyuanVideoFoley`
- `easy showAnything`
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `Text`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SaveVideo`
- `LoadImage`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `10`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **91%**（39/43）

**有卡**：`JWInteger`、`VHS_VideoCombine`、`VHS_SelectFilename`、`Any To Any`、`easy cleanGpuUsed`、`CR Prompt Text`、`BerniniPromptEnhancer`、`RHLLMChatNode`、`StringReplace`、`UNETLoader`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`VAELoader`、`CLIPLoader`、`CLIPTextEncode`、`KSamplerAdvanced`、`BerniniConditioning`、`VAEDecode`、`CreateVideo`、`GetVideoComponents`、`LayerUtility: ImageScaleByAspectRatio V2`、`Qwen3_VQA`、`HunyuanVideoFoley`、`Text`、`SaveVideo`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced

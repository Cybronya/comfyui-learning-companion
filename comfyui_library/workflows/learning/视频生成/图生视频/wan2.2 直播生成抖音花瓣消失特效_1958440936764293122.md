---
key: 视频生成/图生视频/wan2.2 直播生成抖音花瓣消失特效_1958440936764293122.json
name: wan2.2 直播生成抖音花瓣消失特效_1958440936764293122.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2 直播生成抖音花瓣消失特效_1958440936764293122.json
hash: 80476ce670ef045b
coverage: 0.928571
learned_at: 2026-10-15 22:31:22
nodes: [UNETLoader, PathchSageAttentionKJ, CLIPLoader, CLIPTextEncode, VAELoader, CLIPTextEncode, PathchSageAttentionKJ, UNETLoader, TextCombinerSix, Wan22PromptSelector, Note, ShowText, RH_LLMAPI_NODE, ModelSamplingSD3, ModelSamplingSD3, WanImageToVideo, ImageResizeKJv2, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoadImage, VHS_VideoCombine, Text, Note, WanMoeKSampler, TrimVideoLatent, VAEDecode]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "uni_pc", "sampler_name": 1, "scheduler": 1, "seed": 0.9, "steps": "randomize"}
---

# 视频生成/图生视频/wan2.2 直播生成抖音花瓣消失特效_1958440936764293122.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1958440936764293122.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（28 个）：
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `CLIPTextEncode` ★核心
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `TextCombinerSix`
- `Wan22PromptSelector`
- `Note`
- `ShowText`
- `RH_LLMAPI_NODE`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `WanImageToVideo`
- `ImageResizeKJv2`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `VHS_VideoCombine`
- `Text`
- `Note`
- `WanMoeKSampler` ★核心
- `TrimVideoLatent`
- `VAEDecode` ★核心

## 关键参数

- `seed` = `0.9`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `uni_pc`

## 知识

覆盖率 **93%**（26/28）

**有卡**：`UNETLoader`、`PathchSageAttentionKJ`、`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`TextCombinerSix`、`Wan22PromptSelector`、`ShowText`、`RH_LLMAPI_NODE`、`ModelSamplingSD3`、`WanImageToVideo`、`ImageResizeKJv2`、`LoraLoaderModelOnly`、`LoadImage`、`VHS_VideoCombine`、`Text`、`WanMoeKSampler`、`TrimVideoLatent`、`VAEDecode`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、WanMoeKSampler

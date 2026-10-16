---
key: 视频生成/图生视频/Bernini+Prompt Relay视频编辑or多图参考_2068343750555955202.json
name: Bernini+Prompt Relay视频编辑or多图参考_2068343750555955202.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2068343750555955202.json
hash: 34c7fc837d63f954
coverage: 0.777778
learned_at: 2026-10-15 22:40:18
nodes: [VAELoader, UNETLoader, UNETLoader, PathchSageAttentionKJ, ImageResizeKJv2, LoraLoaderModelOnly, PathchSageAttentionKJ, LoraLoaderModelOnly, VAEDecode, KSamplerAdvanced, CLIPLoader, ImageResizeKJv2, Fast Groups Bypasser (rgthree), ComfySwitchNode, Note, PreviewAny, Bool, CLIPTextEncode, CLIPTextEncode, BatchImagesNode, LoadImage, Reroute, ImageResizeKJv2, KSamplerAdvanced, MarkdownNote, EmptyHunyuanLatentVideo, PreviewAny, BerniniPromptEnhancer, PrimitiveInt, PrimitiveInt, MaxNode, VRAM_Debug, ConditioningZeroOut, BerniniConditioning, PrimitiveInt, CreateVideo, SaveVideo, PromptRelayEncodeTimeline, LoadImage, ImageResizeKJv2, easy convertAnything, CreateVideo, RH_LLMAPI_NODE, PreviewAny, StringReplace, TTP_text_mix, StringReplace, LoadImage, PrimitiveInt, VHS_LoadVideo, PromptRelayEncodeTimeline, TextInput_, TextInput_, TTP_text_mix]
patterns: []
missing: []
parameters: {"cfg": 10, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/Bernini+Prompt Relay视频编辑or多图参考_2068343750555955202.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2068343750555955202.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（54 个）：
- `VAELoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `ImageResizeKJv2`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPLoader`
- `ImageResizeKJv2`
- `Fast Groups Bypasser (rgthree)`
- `ComfySwitchNode`
- `Note`
- `PreviewAny`
- `Bool`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `BatchImagesNode`
- `LoadImage`
- `Reroute`
- `ImageResizeKJv2`
- `KSamplerAdvanced` ★核心
- `MarkdownNote`
- `EmptyHunyuanLatentVideo`
- `PreviewAny`
- `BerniniPromptEnhancer`
- `PrimitiveInt`
- `PrimitiveInt`
- `MaxNode`
- `VRAM_Debug`
- `ConditioningZeroOut`
- `BerniniConditioning`
- `PrimitiveInt`
- `CreateVideo`
- `SaveVideo`
- `PromptRelayEncodeTimeline`
- `LoadImage`
- `ImageResizeKJv2`
- `easy convertAnything`
- `CreateVideo`
- `RH_LLMAPI_NODE`
- `PreviewAny`
- `StringReplace`
- `TTP_text_mix`
- `StringReplace`
- `LoadImage`
- `PrimitiveInt`
- `VHS_LoadVideo`
- `PromptRelayEncodeTimeline`
- `TextInput_`
- `TextInput_`
- `TTP_text_mix`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `10`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **78%**（42/54）

**有卡**：`VAELoader`、`UNETLoader`、`PathchSageAttentionKJ`、`ImageResizeKJv2`、`LoraLoaderModelOnly`、`VAEDecode`、`KSamplerAdvanced`、`CLIPLoader`、`Bool`、`CLIPTextEncode`、`BatchImagesNode`、`LoadImage`、`EmptyHunyuanLatentVideo`、`BerniniPromptEnhancer`、`MaxNode`、`VRAM_Debug`、`ConditioningZeroOut`、`BerniniConditioning`、`CreateVideo`、`SaveVideo`、`PromptRelayEncodeTimeline`、`easy convertAnything`、`RH_LLMAPI_NODE`、`StringReplace`、`TTP_text_mix`、`VHS_LoadVideo`、`TextInput_`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

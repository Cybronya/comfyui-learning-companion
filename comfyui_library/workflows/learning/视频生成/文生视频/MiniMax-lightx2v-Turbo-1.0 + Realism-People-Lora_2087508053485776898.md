---
key: 视频生成/文生视频/MiniMax-lightx2v-Turbo-1.0 + Realism-People-Lora_2087508053485776898.json
name: MiniMax-lightx2v-Turbo-1.0 + Realism-People-Lora_2087508053485776898
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MiniMax-lightx2v-Turbo-1.0 + Realism-People-Lora_2087508053485776898.json
hash: 3308d74521189e86
coverage: 0.9
learned_at: 2026-10-11 20:53:43
nodes: [MarkdownNote, ComfyMathExpression, CLIPLoader, VAELoader, VAELoader, RandomNoise, KSamplerSelect, BasicGuider, SamplerCustomAdvanced, Text Find and Replace, easy showAnything, KSamplerSelect, BasicGuider, RandomNoise, CreateVideo, BasicScheduler, KSamplerSelect, RandomNoise, BasicScheduler, CreateVideo, VAEDecode, SamplerCustomAdvanced, VAEDecode, KSamplerSelect, RandomNoise, SaveVideo, CreateVideo, BasicGuider, BasicScheduler, VAEDecode, VAEDecode, VAEDecodeAudio, SaveVideo, Seed (rgthree), ImageConcatMulti, SamplerCustomAdvanced, SaveVideo, SamplerCustomAdvanced, BasicScheduler, KSamplerSelect, SaveVideo, CreateVideo, BasicScheduler, VAEDecode, VAEDecodeAudio, SamplerCustomAdvanced, RandomNoise, BasicGuider, BasicGuider, KSamplerSelect, VAEDecodeAudio, CreateVideo, VAEDecode, SaveVideo, BasicGuider, SamplerCustomAdvanced, BasicScheduler, LoraLoaderModelOnly, MiniMaxH3ImageToVideo, UNETLoader, LoraLoaderModelOnly, RandomNoise, SaveVideo, ImageConcatMulti, Reroute, ImageConcatMulti, VAEDecodeAudio, VAEDecodeAudio, CreateVideo, VAEDecodeAudio, PreviewAudio, PreviewAudio, PreviewAudio, PrimitiveFloat, RH_LLMAPI_Pro_Node, MarkdownNote, CR Text, ImageConcatMulti, TextOverlay, TextOverlay, TextOverlay, TextOverlay, TextOverlay, TextOverlay, ResolutionSelector, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, VHS_VideoCombine, MarkdownNote]
patterns: []
missing: [CR Text, Text Find and Replace, Seed (rgthree)]
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `Text Find and Replace` 知识库中没有该节点类型的任何知识, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/MiniMax-lightx2v-Turbo-1.0 + Realism-People-Lora_2087508053485776898.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MiniMax-lightx2v-Turbo-1.0 + Realism-People-Lora_2087508053485776898.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（90 个）：
- `MarkdownNote`
- `ComfyMathExpression`
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `Text Find and Replace`
- `easy showAnything`
- `KSamplerSelect` ★核心
- `BasicGuider`
- `RandomNoise`
- `CreateVideo`
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `BasicScheduler`
- `CreateVideo`
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `KSamplerSelect` ★核心
- `RandomNoise`
- `SaveVideo`
- `CreateVideo`
- `BasicGuider`
- `BasicScheduler`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `SaveVideo`
- `Seed (rgthree)`
- `ImageConcatMulti`
- `SamplerCustomAdvanced` ★核心
- `SaveVideo`
- `SamplerCustomAdvanced` ★核心
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `SaveVideo`
- `CreateVideo`
- `BasicScheduler`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `BasicGuider`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `VAEDecodeAudio` ★核心
- `CreateVideo`
- `VAEDecode` ★核心
- `SaveVideo`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `BasicScheduler`
- `LoraLoaderModelOnly` ★核心
- `MiniMaxH3ImageToVideo`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `RandomNoise`
- `SaveVideo`
- `ImageConcatMulti`
- `Reroute`
- `ImageConcatMulti`
- `VAEDecodeAudio` ★核心
- `VAEDecodeAudio` ★核心
- `CreateVideo`
- `VAEDecodeAudio` ★核心
- `PreviewAudio`
- `PreviewAudio`
- `PreviewAudio`
- `PrimitiveFloat`
- `RH_LLMAPI_Pro_Node`
- `MarkdownNote`
- `CR Text`
- `ImageConcatMulti`
- `TextOverlay`
- `TextOverlay`
- `TextOverlay`
- `TextOverlay`
- `TextOverlay`
- `TextOverlay`
- `ResolutionSelector`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoCombine`
- `MarkdownNote`

## 知识

覆盖率 **90%**（81/90）

**有卡**：`ComfyMathExpression`、`CLIPLoader`、`VAELoader`、`RandomNoise`、`KSamplerSelect`、`BasicGuider`、`SamplerCustomAdvanced`、`CreateVideo`、`BasicScheduler`、`VAEDecode`、`SaveVideo`、`VAEDecodeAudio`、`ImageConcatMulti`、`LoraLoaderModelOnly`、`MiniMaxH3ImageToVideo`、`UNETLoader`、`PreviewAudio`、`RH_LLMAPI_Pro_Node`、`TextOverlay`、`ResolutionSelector`、`VHS_VideoCombine`

**缺卡**（3）：`CR Text`、`Text Find and Replace`、`Seed (rgthree)`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、UNETLoader、KSamplerSelect、SamplerCustomAdvanced

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Find and Replace` 知识库中没有该节点类型的任何知识
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明

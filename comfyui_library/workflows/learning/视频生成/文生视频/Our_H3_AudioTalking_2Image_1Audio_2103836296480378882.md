---
key: 视频生成/文生视频/Our_H3_AudioTalking_2Image_1Audio_2103836296480378882.json
name: Our_H3_AudioTalking_2Image_1Audio_2103836296480378882
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Our_H3_AudioTalking_2Image_1Audio_2103836296480378882.json
hash: fb34b2e917e888b9
coverage: 0.402597
learned_at: 2026-10-11 22:12:46
nodes: [SetNode, VAELoader, VAELoader, SetNode, SetNode, SetNode, SetNode, LoraLoaderModelOnly, CLIPLoader, Reroute, Reroute, GetNode, GetNode, GetNode, GetNode, VAEDecode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, MiniMaxH3ReferenceToVideo, SetNode, ComfyMathExpression, SetNode, SamplerCustomAdvanced, SetNode, BasicGuider, SetNode, SetNode, SetNode, VAEDecode, GetNode, LTXVConcatAVLatent, GetNode, MarkdownNote, SamplerCustomAdvanced, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVSeparateAVLatent, SetNode, Note, RandomNoise, KSamplerSelect, UNETLoader, SetNode, GetNode, SetNode, MiniMaxH3MemoryEfficientSageAttentionPatch, VHS_VideoCombine, LoraLoaderModelOnly, LoraLoaderModelOnly, BasicScheduler, SplitSigmas, VHS_VideoCombine, SetNode, MinimaxH3LatentUpscaler3D, Note, easy float, easy cleanGpuUsed, Note, Note, VRGDG_MiniMaxH3AudioDrive, SoundFlow_GetLength, LoadImage, LoadImage, LoadAudio, Note, ResolutionSelector, Text]
patterns: []
missing: [easy cleanGpuUsed, easy float]
discoveries: [次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy float` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/Our_H3_AudioTalking_2Image_1Audio_2103836296480378882.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Our_H3_AudioTalking_2Image_1Audio_2103836296480378882.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Other

**节点**（77 个）：
- `SetNode`
- `VAELoader`
- `VAELoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `Reroute`
- `Reroute`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `MiniMaxH3ReferenceToVideo`
- `SetNode`
- `ComfyMathExpression`
- `SetNode`
- `SamplerCustomAdvanced` ★核心
- `SetNode`
- `BasicGuider`
- `SetNode`
- `SetNode`
- `SetNode`
- `VAEDecode` ★核心
- `GetNode`
- `LTXVConcatAVLatent`
- `GetNode`
- `MarkdownNote`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `SetNode`
- `Note`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `UNETLoader` ★核心
- `SetNode`
- `GetNode`
- `SetNode`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `BasicScheduler`
- `SplitSigmas`
- `VHS_VideoCombine`
- `SetNode`
- `MinimaxH3LatentUpscaler3D`
- `Note`
- `easy float`
- `easy cleanGpuUsed`
- `Note`
- `Note`
- `VRGDG_MiniMaxH3AudioDrive`
- `SoundFlow_GetLength`
- `LoadImage`
- `LoadImage`
- `LoadAudio`
- `Note`
- `ResolutionSelector`
- `Text`

## 知识

覆盖率 **40%**（31/77）

**有卡**：`VAELoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAEDecode`、`MiniMaxH3ReferenceToVideo`、`ComfyMathExpression`、`SamplerCustomAdvanced`、`BasicGuider`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`RandomNoise`、`KSamplerSelect`、`UNETLoader`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`VHS_VideoCombine`、`BasicScheduler`、`SplitSigmas`、`MinimaxH3LatentUpscaler3D`、`VRGDG_MiniMaxH3AudioDrive`、`SoundFlow_GetLength`、`LoadImage`、`LoadAudio`、`ResolutionSelector`、`Text`

**缺卡**（2）：`easy cleanGpuUsed`、`easy float`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect

## 学习发现

- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy float` 知识库中没有该节点类型的任何知识

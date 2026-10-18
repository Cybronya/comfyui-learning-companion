---
key: 视频生成/图生视频/MiniMax-H3全栈式短剧生成V7.1原始版_2105117440979066882.json
name: MiniMax-H3全栈式短剧生成V7.1原始版_2105117440979066882
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMax-H3全栈式短剧生成V7.1原始版_2105117440979066882.json
hash: 8a8ee97385efeadf
coverage: 0.45098
learned_at: 2026-10-17 02:43:56
nodes: [SetNode, GetNode, GetNode, GetNode, GetNode, PrimitiveStringMultiline, GetNode, PrimitiveStringMultiline, GetNode, SetNode, SetNode, SetNode, GetNode, SetNode, PrimitiveFloat, SetNode, SetNode, MarkdownNote, ResolutionSelector, SetNode, SetNode, CLIPLoader, GetNode, GetNode, GetNode, GetNode, GetNode, ResolutionSelector, SetNode, SetNode, GetNode, GetNode, GetNode, PrimitiveInt, VHS_VideoCombine, KSamplerSelect, SetNode, TextGenerate, PrimitiveStringMultiline, GetNode, ManualSigmas, ManualSigmas, ManualSigmas, SetNode, SetNode, ModelAttentionBackend, MiniMaxChunkFeedForward, VAELoader, CLIPLoader, VAELoader, SetNode, SetNode, GetNode, PreviewImage, GetNode, GetNode, ComfyMathExpression, YuanAudioSplit, GetNode, PrimitiveNode, GetImage, GetImage, GetImage, SetNode, UNETLoader, BasicScheduler, MiniMaxH3MemoryEfficientSageAttentionPatch, UNETLoader, LoraLoaderModelOnly, MiniMaxLowVRAMAttention, LoraLoaderModelOnly, LoraLoaderBypassModelOnly, GetNode, RandomNoise, YuanMultiImage, YUAN_TXTJsonSwitch, SetNode, SetNode, SetNode, SetNode, GetNode, YuanAudioList, YUAN_TXTPreviewContent, GetNode, GetNode, ComfyMathExpression, GetNode, GetNode, GetNode, YuanTool, YUAN_TXTJsonExtractor, SamplerCustomAdvanced, RandomNoise, BasicGuider, KSamplerSelect, BasicScheduler, Yuan_H3Upscale3D, BasicGuider, SamplerCustomAdvanced, Yuan_H3MotionContext, Yuan_H3MotionContextTrim, Yuan_MiniMaxH3Video]
patterns: []
missing: []
---

# 视频生成/图生视频/MiniMax-H3全栈式短剧生成V7.1原始版_2105117440979066882.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMax-H3全栈式短剧生成V7.1原始版_2105117440979066882.json`

## 结构

**生成流程**：Model → Latent → Sampling → Process → Output → Other

**节点**（102 个）：
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `PrimitiveStringMultiline`
- `GetNode`
- `PrimitiveStringMultiline`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `PrimitiveFloat`
- `SetNode`
- `SetNode`
- `MarkdownNote`
- `ResolutionSelector`
- `SetNode`
- `SetNode`
- `CLIPLoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ResolutionSelector`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `PrimitiveInt`
- `VHS_VideoCombine`
- `KSamplerSelect` ★核心
- `SetNode`
- `TextGenerate`
- `PrimitiveStringMultiline`
- `GetNode`
- `ManualSigmas`
- `ManualSigmas`
- `ManualSigmas`
- `SetNode`
- `SetNode`
- `ModelAttentionBackend`
- `MiniMaxChunkFeedForward`
- `VAELoader`
- `CLIPLoader`
- `VAELoader`
- `SetNode`
- `SetNode`
- `GetNode`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `ComfyMathExpression`
- `YuanAudioSplit`
- `GetNode`
- `PrimitiveNode`
- `GetImage`
- `GetImage`
- `GetImage`
- `SetNode`
- `UNETLoader` ★核心
- `BasicScheduler`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `MiniMaxLowVRAMAttention`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderBypassModelOnly` ★核心
- `GetNode`
- `RandomNoise`
- `YuanMultiImage`
- `YUAN_TXTJsonSwitch`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `YuanAudioList`
- `YUAN_TXTPreviewContent`
- `GetNode`
- `GetNode`
- `ComfyMathExpression`
- `GetNode`
- `GetNode`
- `GetNode`
- `YuanTool`
- `YUAN_TXTJsonExtractor`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `Yuan_H3Upscale3D`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `Yuan_H3MotionContext`
- `Yuan_H3MotionContextTrim`
- `Yuan_MiniMaxH3Video`

## 知识

覆盖率 **45%**（46/102）

**有卡**：`ResolutionSelector`、`CLIPLoader`、`VHS_VideoCombine`、`KSamplerSelect`、`TextGenerate`、`ManualSigmas`、`ModelAttentionBackend`、`MiniMaxChunkFeedForward`、`VAELoader`、`ComfyMathExpression`、`YuanAudioSplit`、`GetImage`、`UNETLoader`、`BasicScheduler`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`LoraLoaderModelOnly`、`MiniMaxLowVRAMAttention`、`LoraLoaderBypassModelOnly`、`RandomNoise`、`YuanMultiImage`、`YUAN_TXTJsonSwitch`、`YuanAudioList`、`YUAN_TXTPreviewContent`、`YuanTool`、`YUAN_TXTJsonExtractor`、`SamplerCustomAdvanced`、`BasicGuider`、`Yuan_H3Upscale3D`、`Yuan_H3MotionContext`、`Yuan_H3MotionContextTrim`、`Yuan_MiniMaxH3Video`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、UNETLoader、KSamplerSelect、SamplerCustomAdvanced、LoraLoaderBypassModelOnly

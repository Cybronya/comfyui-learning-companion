---
key: 视频生成/图生视频/MiniMax-H3全栈式短剧生成V7.1自用Dasiwa_2095041265858605058.json
name: MiniMax-H3全栈式短剧生成V7.1自用Dasiwa_2095041265858605058
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMax-H3全栈式短剧生成V7.1自用Dasiwa_2095041265858605058.json
hash: 944631b3f33f0d54
coverage: 0.373737
learned_at: 2026-10-17 00:02:27
nodes: [SetNode, GetNode, GetNode, GetNode, GetNode, MarkdownNote, PrimitiveStringMultiline, GetNode, PrimitiveStringMultiline, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, SetNode, PrimitiveFloat, SetNode, SetNode, MarkdownNote, ResolutionSelector, SetNode, SetNode, GetNode, VAEDecodeAudio, YUAN_TXTJsonExtractor, GetNode, SamplerCustomAdvanced, GetNode, GetNode, GetNode, GetNode, ResolutionSelector, GetNode, YuanTool, SetNode, GetNode, GetNode, GetNode, YUAN_TXTParagraphSplitter, GetNode, GetNode, GetNode, PrimitiveInt, GetNode, VHS_VideoCombine, KSamplerSelect, SetNode, BasicGuider, RandomNoise, GetNode, GetNode, ManualSigmas, ManualSigmas, ManualSigmas, SetNode, SetNode, ModelAttentionBackend, MiniMaxChunkFeedForward, VAELoader, VAELoader, SetNode, SetNode, GetNode, PreviewImage, GetNode, GetNode, ComfyMathExpression, YuanAudioSplit, GetNode, Yuan_H3MotionContextLoadLatent, PrimitiveNode, Yuan_H3MotionContext, ComfyMathExpression, Yuan_MiniMaxH3Video, PrimitiveNode, GetImage, GetImage, GetImage, SetNode, YuanAudioList, SetNode, YUAN_TXTShotReplace, MiniMaxLowVRAMAttention, LoraLoaderBypassModelOnly, SetNode, SetNode, YuanMultiImage, PrimitiveStringMultiline, VAEDecode, ShowText|pysssss, PrimitiveStringMultiline, BasicScheduler, Yuan_H3MotionContextTrim, CLIPLoader, UNETLoader]
patterns: []
missing: []
---

# 视频生成/图生视频/MiniMax-H3全栈式短剧生成V7.1自用Dasiwa_2095041265858605058.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMax-H3全栈式短剧生成V7.1自用Dasiwa_2095041265858605058.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（99 个）：
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `MarkdownNote`
- `PrimitiveStringMultiline`
- `GetNode`
- `PrimitiveStringMultiline`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
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
- `GetNode`
- `VAEDecodeAudio` ★核心
- `YUAN_TXTJsonExtractor`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ResolutionSelector`
- `GetNode`
- `YuanTool`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `YUAN_TXTParagraphSplitter`
- `GetNode`
- `GetNode`
- `GetNode`
- `PrimitiveInt`
- `GetNode`
- `VHS_VideoCombine`
- `KSamplerSelect` ★核心
- `SetNode`
- `BasicGuider`
- `RandomNoise`
- `GetNode`
- `GetNode`
- `ManualSigmas`
- `ManualSigmas`
- `ManualSigmas`
- `SetNode`
- `SetNode`
- `ModelAttentionBackend`
- `MiniMaxChunkFeedForward`
- `VAELoader`
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
- `Yuan_H3MotionContextLoadLatent`
- `PrimitiveNode`
- `Yuan_H3MotionContext`
- `ComfyMathExpression`
- `Yuan_MiniMaxH3Video`
- `PrimitiveNode`
- `GetImage`
- `GetImage`
- `GetImage`
- `SetNode`
- `YuanAudioList`
- `SetNode`
- `YUAN_TXTShotReplace`
- `MiniMaxLowVRAMAttention`
- `LoraLoaderBypassModelOnly` ★核心
- `SetNode`
- `SetNode`
- `YuanMultiImage`
- `PrimitiveStringMultiline`
- `VAEDecode` ★核心
- `ShowText|pysssss`
- `PrimitiveStringMultiline`
- `BasicScheduler`
- `Yuan_H3MotionContextTrim`
- `CLIPLoader`
- `UNETLoader` ★核心

## 知识

覆盖率 **37%**（37/99）

**有卡**：`ResolutionSelector`、`VAEDecodeAudio`、`YUAN_TXTJsonExtractor`、`SamplerCustomAdvanced`、`YuanTool`、`YUAN_TXTParagraphSplitter`、`VHS_VideoCombine`、`KSamplerSelect`、`BasicGuider`、`RandomNoise`、`ManualSigmas`、`ModelAttentionBackend`、`MiniMaxChunkFeedForward`、`VAELoader`、`ComfyMathExpression`、`YuanAudioSplit`、`Yuan_H3MotionContextLoadLatent`、`Yuan_H3MotionContext`、`Yuan_MiniMaxH3Video`、`GetImage`、`YuanAudioList`、`YUAN_TXTShotReplace`、`MiniMaxLowVRAMAttention`、`LoraLoaderBypassModelOnly`、`YuanMultiImage`、`VAEDecode`、`BasicScheduler`、`Yuan_H3MotionContextTrim`、`CLIPLoader`、`UNETLoader`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、ResolutionSelector、UNETLoader、KSamplerSelect、SamplerCustomAdvanced、VAEDecodeAudio

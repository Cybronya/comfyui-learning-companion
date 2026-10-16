---
key: 视频生成/图生视频/MiniMax-H3全栈式短剧生成V4.2.2_2092157971756310530.json
name: MiniMax-H3全栈式短剧生成V4.2.2_2092157971756310530
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMax-H3全栈式短剧生成V4.2.2_2092157971756310530.json
hash: a5b06f5c9d3515de
coverage: 0.775862
learned_at: 2026-10-16 22:59:12
nodes: [YuanMultiImage, CLIPLoader, ModelAttentionBackend, MiniMaxChunkFeedForward, LoraLoaderModelOnly, PrimitiveBoolean, If ANY execute A else B, If ANY execute A else B, Int, Int, UNETLoader, Yuan_H3MotionContextLoadLatent, VAELoader, BasicGuider, BasicScheduler, KSamplerSelect, VAELoader, Yuan_H3MotionContextTrim, RandomNoise, Yuan_H3MotionContext, Yuan_MiniMaxH3Video, MiniMaxLowVRAMAttention, RandomNoise, SamplerCustomAdvanced, BasicGuider, KSamplerSelect, Yuan_RTXVideoUpscaleH3, BasicScheduler, Reroute, ResolutionSelector, ResolutionSelector, MathExpression|pysssss, ResolutionSelector, PrimitiveNode, SamplerCustomAdvanced, Reroute, Reroute, VAEDecode, VAEDecodeAudio, CreateVideo, SaveVideo, GetImage, PreviewImage, GetImage, PreviewImage, GetImage, YuanTool, YUAN_TXTJsonExtractor, easy showAnything, PreviewImage, YUAN_TXTShotReplace, PreviewImage, PrimitiveStringMultiline, PrimitiveStringMultiline, YUAN_TXTParagraphSplitter, easy showAnything, RH_LLMAPI_Pro_Node, PrimitiveInt]
patterns: []
missing: []
---

# 视频生成/图生视频/MiniMax-H3全栈式短剧生成V4.2.2_2092157971756310530.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMax-H3全栈式短剧生成V4.2.2_2092157971756310530.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（58 个）：
- `YuanMultiImage`
- `CLIPLoader`
- `ModelAttentionBackend`
- `MiniMaxChunkFeedForward`
- `LoraLoaderModelOnly` ★核心
- `PrimitiveBoolean`
- `If ANY execute A else B`
- `If ANY execute A else B`
- `Int`
- `Int`
- `UNETLoader` ★核心
- `Yuan_H3MotionContextLoadLatent`
- `VAELoader`
- `BasicGuider`
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `VAELoader`
- `Yuan_H3MotionContextTrim`
- `RandomNoise`
- `Yuan_H3MotionContext`
- `Yuan_MiniMaxH3Video`
- `MiniMaxLowVRAMAttention`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `BasicGuider`
- `KSamplerSelect` ★核心
- `Yuan_RTXVideoUpscaleH3`
- `BasicScheduler`
- `Reroute`
- `ResolutionSelector`
- `ResolutionSelector`
- `MathExpression|pysssss`
- `ResolutionSelector`
- `PrimitiveNode`
- `SamplerCustomAdvanced` ★核心
- `Reroute`
- `Reroute`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `CreateVideo`
- `SaveVideo`
- `GetImage`
- `PreviewImage`
- `GetImage`
- `PreviewImage`
- `GetImage`
- `YuanTool`
- `YUAN_TXTJsonExtractor`
- `easy showAnything`
- `PreviewImage`
- `YUAN_TXTShotReplace`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `YUAN_TXTParagraphSplitter`
- `easy showAnything`
- `RH_LLMAPI_Pro_Node`
- `PrimitiveInt`

## 知识

覆盖率 **78%**（45/58）

**有卡**：`YuanMultiImage`、`CLIPLoader`、`ModelAttentionBackend`、`MiniMaxChunkFeedForward`、`LoraLoaderModelOnly`、`PrimitiveBoolean`、`If ANY execute A else B`、`Int`、`UNETLoader`、`Yuan_H3MotionContextLoadLatent`、`VAELoader`、`BasicGuider`、`BasicScheduler`、`KSamplerSelect`、`Yuan_H3MotionContextTrim`、`RandomNoise`、`Yuan_H3MotionContext`、`Yuan_MiniMaxH3Video`、`MiniMaxLowVRAMAttention`、`SamplerCustomAdvanced`、`Yuan_RTXVideoUpscaleH3`、`ResolutionSelector`、`MathExpression|pysssss`、`VAEDecode`、`VAEDecodeAudio`、`CreateVideo`、`SaveVideo`、`GetImage`、`YuanTool`、`YUAN_TXTJsonExtractor`、`YUAN_TXTShotReplace`、`YUAN_TXTParagraphSplitter`、`RH_LLMAPI_Pro_Node`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、UNETLoader、KSamplerSelect、SamplerCustomAdvanced

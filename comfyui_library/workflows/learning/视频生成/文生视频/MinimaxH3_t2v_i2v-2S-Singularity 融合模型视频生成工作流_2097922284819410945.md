---
key: 视频生成/文生视频/MinimaxH3_t2v_i2v-2S-Singularity 融合模型视频生成工作流_2097922284819410945.json
name: MinimaxH3_t2v_i2v-2S-Singularity 融合模型视频生成工作流_2097922284819410945
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MinimaxH3_t2v_i2v-2S-Singularity 融合模型视频生成工作流_2097922284819410945.json
hash: ae726355646a1090
coverage: 0.666667
learned_at: 2026-10-15 22:46:44
nodes: [BasicGuider, GetNode, ComfyMathExpression, SetNode, PrimitiveFloat, SetNode, KSamplerSelect, SamplerCustomAdvanced, SamplerCustomAdvanced, ModelPatchTorchSettings, MiniMaxH3ImageToVideo, SetNode, SetNode, GetNode, GetNode, VAEDecode, GetNode, VAEDecodeAudio, GetNode, GetNode, GetNode, RandomNoise, VAEDecode, easy cleanGpuUsed, easy clearCacheAll, GetNode, MathExpression|pysssss, RandomNoise, BasicGuider, KSamplerSelect, SetNode, PrimitiveFloat, MiniMaxChunkFeedForward, PathchSageAttentionKJ, MiniMaxH3SigmaShift, MarkdownNote, ImageResizeKJv2, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, FrameInterpolate, SeedNode, UNETLoader, CLIPLoader, VAELoader, VAELoader, ImageResizeKJv2, PrimitiveStringMultiline, ResolutionSelector, PrimitiveFloat, SetNode, BasicScheduler, FrameInterpolationModelLoader, BasicScheduler, Note, LoraLoaderModelOnly, Reroute, MiniMaxH3MemoryEfficientSageAttentionPatch, VHS_VideoCombine, LoadImage, VHS_VideoCombine, LoadImage, DLSS5Settings, RH_DLSS5FrameInterpolation, DLSS5EnhanceImages, ApplyVDNH3Advanced, Note, Note]
patterns: []
missing: []
---

# 视频生成/文生视频/MinimaxH3_t2v_i2v-2S-Singularity 融合模型视频生成工作流_2097922284819410945.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MinimaxH3_t2v_i2v-2S-Singularity 融合模型视频生成工作流_2097922284819410945.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Other

**节点**（69 个）：
- `BasicGuider`
- `GetNode`
- `ComfyMathExpression`
- `SetNode`
- `PrimitiveFloat`
- `SetNode`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `ModelPatchTorchSettings`
- `MiniMaxH3ImageToVideo`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `VAEDecodeAudio` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `RandomNoise`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `GetNode`
- `MathExpression|pysssss`
- `RandomNoise`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `SetNode`
- `PrimitiveFloat`
- `MiniMaxChunkFeedForward`
- `PathchSageAttentionKJ`
- `MiniMaxH3SigmaShift`
- `MarkdownNote`
- `ImageResizeKJv2`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `FrameInterpolate`
- `SeedNode`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `ImageResizeKJv2`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `PrimitiveFloat`
- `SetNode`
- `BasicScheduler`
- `FrameInterpolationModelLoader`
- `BasicScheduler`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `Reroute`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `VHS_VideoCombine`
- `LoadImage`
- `VHS_VideoCombine`
- `LoadImage`
- `DLSS5Settings`
- `RH_DLSS5FrameInterpolation`
- `DLSS5EnhanceImages`
- `ApplyVDNH3Advanced`
- `Note`
- `Note`

## 知识

覆盖率 **67%**（46/69）

**有卡**：`BasicGuider`、`ComfyMathExpression`、`KSamplerSelect`、`SamplerCustomAdvanced`、`ModelPatchTorchSettings`、`MiniMaxH3ImageToVideo`、`VAEDecode`、`VAEDecodeAudio`、`RandomNoise`、`easy cleanGpuUsed`、`easy clearCacheAll`、`MathExpression|pysssss`、`MiniMaxChunkFeedForward`、`PathchSageAttentionKJ`、`MiniMaxH3SigmaShift`、`ImageResizeKJv2`、`LoraLoaderModelOnly`、`UNETLoader`、`FrameInterpolate`、`SeedNode`、`CLIPLoader`、`VAELoader`、`ResolutionSelector`、`BasicScheduler`、`FrameInterpolationModelLoader`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`VHS_VideoCombine`、`LoadImage`、`DLSS5Settings`、`RH_DLSS5FrameInterpolation`、`DLSS5EnhanceImages`、`ApplyVDNH3Advanced`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect

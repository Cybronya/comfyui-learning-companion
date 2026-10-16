---
key: 视频生成/图生视频/（音频驱动FL2VA-lightx2v1.1）MiniMax H3数字人加速版V1_2090641147021578241.json
name: （音频驱动FL2VA-lightx2v1.1）MiniMax H3数字人加速版V1_2090641147021578241
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/（音频驱动FL2VA-lightx2v1.1）MiniMax H3数字人加速版V1_2090641147021578241.json
hash: 2d0388b8cd39e4b5
coverage: 0.904762
learned_at: 2026-10-16 22:02:46
nodes: [CLIPLoader, BasicGuider, MarkdownNote, VAELoader, MiniMaxH3MemoryEfficientSageAttentionPatch, VAELoader, LoadImage, ModelAttentionBackend, ComfyMathExpression, PrimitiveFloat, SamplerCustomAdvanced, LoadAudio, MiniMaxH3DualClockSamplerT8, ResolutionSelector, CR Prompt Text, MiniMaxH3AudioConditioningT8, UNETLoader, MiniMaxH3AVDecodeT8, LoraLoaderBypassModelOnly, RandomNoise, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/（音频驱动FL2VA-lightx2v1.1）MiniMax H3数字人加速版V1_2090641147021578241.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/（音频驱动FL2VA-lightx2v1.1）MiniMax H3数字人加速版V1_2090641147021578241.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Other

**节点**（21 个）：
- `CLIPLoader`
- `BasicGuider`
- `MarkdownNote`
- `VAELoader`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `VAELoader`
- `LoadImage`
- `ModelAttentionBackend`
- `ComfyMathExpression`
- `PrimitiveFloat`
- `SamplerCustomAdvanced` ★核心
- `LoadAudio`
- `MiniMaxH3DualClockSamplerT8` ★核心
- `ResolutionSelector`
- `CR Prompt Text`
- `MiniMaxH3AudioConditioningT8`
- `UNETLoader` ★核心
- `MiniMaxH3AVDecodeT8`
- `LoraLoaderBypassModelOnly` ★核心
- `RandomNoise`
- `VHS_VideoCombine`

## 知识

覆盖率 **90%**（19/21）

**有卡**：`CLIPLoader`、`BasicGuider`、`VAELoader`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`LoadImage`、`ModelAttentionBackend`、`ComfyMathExpression`、`SamplerCustomAdvanced`、`LoadAudio`、`MiniMaxH3DualClockSamplerT8`、`ResolutionSelector`、`CR Prompt Text`、`MiniMaxH3AudioConditioningT8`、`UNETLoader`、`MiniMaxH3AVDecodeT8`、`LoraLoaderBypassModelOnly`、`RandomNoise`、`VHS_VideoCombine`

**用到的条目**：VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、SamplerCustomAdvanced、MiniMaxH3DualClockSamplerT8、MiniMaxH3AVDecodeT8

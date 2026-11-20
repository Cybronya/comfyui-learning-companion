---
key: 视频生成/图生视频/Pika MinimaxH3 FLEX无限时长全能参考+首尾帧  满血turbo四步保真融合_2116749269372854273.json
name: Pika MinimaxH3 FLEX无限时长全能参考+首尾帧  满血turbo四步保真融合_2116749269372854273
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Pika MinimaxH3 FLEX无限时长全能参考+首尾帧  满血turbo四步保真融合_2116749269372854273.json
hash: 72c98b9359b08af5
coverage: 0.805556
learned_at: 2026-11-02 19:18:23
nodes: [UNETLoader, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, CLIPLoader, VAELoader, VAELoader, MiniMaxH3SigmaShift, ModelAttentionBackend, BlockSparseAttention, ComfySwitchNode, LoadImage, LoadImage, LoadImage, MiniMaxH3ScheduledPictureReference, MiniMaxH3ScheduledPictureReference, MiniMaxH3ScheduledPictureReference, ResolutionSelector, PrimitiveFloat, ResolutionSelector, PrimitiveNode, MiniMaxH3ChainPlan, MiniMaxH3ChainScenePromptEditor, MiniMaxH3ChainLoopStart, MiniMaxH3ChainLoopEnd, MiniMaxH3ChainCurrent, MiniMaxH3ChainSegmentSave, MiniMaxH3ScheduledReferenceToVideo, Anything Everywhere3, SetNode, MiniMaxH3ImageToVideo, GetNode, AnySwitch, MiniMaxH3ChainContext, AnySwitch, BasicGuider, SamplerCustomAdvanced, RandomNoise, KSamplerSelect, BasicScheduler, VAEDecode, VAEDecodeAudio, GetNode, MiniMaxH3LoopTrim, LTXVSeparateAVLatent, ManualSigmas, MinimaxH3LatentUpscaler3D, BasicGuider, ManualSigmas, ManualSigmas, SamplerCustomAdvanced, VAEDecode, LTXVConcatAVLatent, BasicScheduler, VAEDecodeAudio, MiniMaxH3ImageToVideo, AnySwitch, Reroute, GetNode, AnySwitch, AnySwitch, Reroute, Reroute, MiniMaxH3ChainReview, MiniMaxH3ChainAssemble, Reroute, Reroute, Fast Bypasser (rgthree), Fast Groups Bypasser (rgthree), FastGroupsBypassSwitch, CreateVideo, SaveVideo]
patterns: []
missing: []
---

# 视频生成/图生视频/Pika MinimaxH3 FLEX无限时长全能参考+首尾帧  满血turbo四步保真融合_2116749269372854273.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Pika MinimaxH3 FLEX无限时长全能参考+首尾帧  满血turbo四步保真融合_2116749269372854273.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（72 个）：
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `BlockSparseAttention`
- `ComfySwitchNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `MiniMaxH3ScheduledPictureReference`
- `MiniMaxH3ScheduledPictureReference`
- `MiniMaxH3ScheduledPictureReference`
- `ResolutionSelector`
- `PrimitiveFloat`
- `ResolutionSelector`
- `PrimitiveNode`
- `MiniMaxH3ChainPlan`
- `MiniMaxH3ChainScenePromptEditor`
- `MiniMaxH3ChainLoopStart`
- `MiniMaxH3ChainLoopEnd`
- `MiniMaxH3ChainCurrent`
- `MiniMaxH3ChainSegmentSave`
- `MiniMaxH3ScheduledReferenceToVideo`
- `Anything Everywhere3`
- `SetNode`
- `MiniMaxH3ImageToVideo`
- `GetNode`
- `AnySwitch`
- `MiniMaxH3ChainContext`
- `AnySwitch`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `GetNode`
- `MiniMaxH3LoopTrim`
- `LTXVSeparateAVLatent`
- `ManualSigmas`
- `MinimaxH3LatentUpscaler3D`
- `BasicGuider`
- `ManualSigmas`
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `LTXVConcatAVLatent`
- `BasicScheduler`
- `VAEDecodeAudio` ★核心
- `MiniMaxH3ImageToVideo`
- `AnySwitch`
- `Reroute`
- `GetNode`
- `AnySwitch`
- `AnySwitch`
- `Reroute`
- `Reroute`
- `MiniMaxH3ChainReview`
- `MiniMaxH3ChainAssemble`
- `Reroute`
- `Reroute`
- `Fast Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `FastGroupsBypassSwitch`
- `CreateVideo`
- `SaveVideo`

## 知识

覆盖率 **81%**（58/72）

**有卡**：`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`MiniMaxH3SigmaShift`、`ModelAttentionBackend`、`BlockSparseAttention`、`LoadImage`、`MiniMaxH3ScheduledPictureReference`、`ResolutionSelector`、`MiniMaxH3ChainPlan`、`MiniMaxH3ChainScenePromptEditor`、`MiniMaxH3ChainLoopStart`、`MiniMaxH3ChainLoopEnd`、`MiniMaxH3ChainCurrent`、`MiniMaxH3ChainSegmentSave`、`MiniMaxH3ScheduledReferenceToVideo`、`MiniMaxH3ImageToVideo`、`AnySwitch`、`MiniMaxH3ChainContext`、`BasicGuider`、`SamplerCustomAdvanced`、`RandomNoise`、`KSamplerSelect`、`BasicScheduler`、`VAEDecode`、`VAEDecodeAudio`、`MiniMaxH3LoopTrim`、`LTXVSeparateAVLatent`、`ManualSigmas`、`MinimaxH3LatentUpscaler3D`、`LTXVConcatAVLatent`、`MiniMaxH3ChainReview`、`MiniMaxH3ChainAssemble`、`Fast Bypasser (rgthree)`、`FastGroupsBypassSwitch`、`CreateVideo`、`SaveVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect

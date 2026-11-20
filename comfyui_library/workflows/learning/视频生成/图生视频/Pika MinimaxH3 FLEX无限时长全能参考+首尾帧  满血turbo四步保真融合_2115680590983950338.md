---
key: 视频生成/图生视频/Pika MinimaxH3 FLEX无限时长全能参考+首尾帧  满血turbo四步保真融合_2115680590983950338.json
name: Pika MinimaxH3 FLEX无限时长全能参考+首尾帧  满血turbo四步保真融合_2115680590983950338
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Pika MinimaxH3 FLEX无限时长全能参考+首尾帧  满血turbo四步保真融合_2115680590983950338.json
hash: e20eaeab320e1aeb
coverage: 0.855072
learned_at: 2026-11-02 19:18:23
nodes: [Reroute, MiniMaxH3ChainLoopStart, Reroute, Reroute, BasicGuider, UNETLoader, ManualSigmas, ManualSigmas, LTXVConcatAVLatent, ModelAttentionBackend, MiniMaxH3SigmaShift, Reroute, Reroute, Reroute, VAELoader, ManualSigmas, RandomNoise, Reroute, MiniMaxH3ChainContext, BlockSparseAttention, BasicScheduler, Reroute, KSamplerSelect, SamplerCustomAdvanced, MiniMaxH3LoopTrim, AnySwitch, BasicScheduler, LTXVSeparateAVLatent, VAEDecode, VAEDecodeAudio, MiniMaxH3ChainLoopEnd, AnySwitch, AnySwitch, VAEDecode, VAEDecodeAudio, SamplerCustomAdvanced, MinimaxH3LatentUpscaler3D, PrimitiveFloat, CLIPLoader, VAELoader, AnySwitch, BasicGuider, MiniMaxH3ImageToVideo, MiniMaxH3ScheduledReferenceToVideo, MiniMaxH3ImageToVideo, ResolutionSelector, ResolutionSelector, MiniMaxH3ChainAssemble, MiniMaxH3ChainCurrent, MiniMaxH3ChainSegmentSave, MiniMaxH3ChainReview, AnySwitch, Fast Bypasser (rgthree), LoadImage, MiniMaxH3ScheduledPictureReference, MiniMaxH3ScheduledPictureReference, MiniMaxH3ScheduledPictureReference, Fast Bypasser (rgthree), MiniMaxH3ChainScenePromptEditor, LoadImage, MiniMaxH3ChainPlan, LoadImage, Fast Bypasser (rgthree), CreateVideo, SaveVideo, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, ComfySwitchNode]
patterns: []
missing: []
---

# 视频生成/图生视频/Pika MinimaxH3 FLEX无限时长全能参考+首尾帧  满血turbo四步保真融合_2115680590983950338.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Pika MinimaxH3 FLEX无限时长全能参考+首尾帧  满血turbo四步保真融合_2115680590983950338.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（69 个）：
- `Reroute`
- `MiniMaxH3ChainLoopStart`
- `Reroute`
- `Reroute`
- `BasicGuider`
- `UNETLoader` ★核心
- `ManualSigmas`
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `ModelAttentionBackend`
- `MiniMaxH3SigmaShift`
- `Reroute`
- `Reroute`
- `Reroute`
- `VAELoader`
- `ManualSigmas`
- `RandomNoise`
- `Reroute`
- `MiniMaxH3ChainContext`
- `BlockSparseAttention`
- `BasicScheduler`
- `Reroute`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3LoopTrim`
- `AnySwitch`
- `BasicScheduler`
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `MiniMaxH3ChainLoopEnd`
- `AnySwitch`
- `AnySwitch`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `SamplerCustomAdvanced` ★核心
- `MinimaxH3LatentUpscaler3D`
- `PrimitiveFloat`
- `CLIPLoader`
- `VAELoader`
- `AnySwitch`
- `BasicGuider`
- `MiniMaxH3ImageToVideo`
- `MiniMaxH3ScheduledReferenceToVideo`
- `MiniMaxH3ImageToVideo`
- `ResolutionSelector`
- `ResolutionSelector`
- `MiniMaxH3ChainAssemble`
- `MiniMaxH3ChainCurrent`
- `MiniMaxH3ChainSegmentSave`
- `MiniMaxH3ChainReview`
- `AnySwitch`
- `Fast Bypasser (rgthree)`
- `LoadImage`
- `MiniMaxH3ScheduledPictureReference`
- `MiniMaxH3ScheduledPictureReference`
- `MiniMaxH3ScheduledPictureReference`
- `Fast Bypasser (rgthree)`
- `MiniMaxH3ChainScenePromptEditor`
- `LoadImage`
- `MiniMaxH3ChainPlan`
- `LoadImage`
- `Fast Bypasser (rgthree)`
- `CreateVideo`
- `SaveVideo`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ComfySwitchNode`

## 知识

覆盖率 **86%**（59/69）

**有卡**：`MiniMaxH3ChainLoopStart`、`BasicGuider`、`UNETLoader`、`ManualSigmas`、`LTXVConcatAVLatent`、`ModelAttentionBackend`、`MiniMaxH3SigmaShift`、`VAELoader`、`RandomNoise`、`MiniMaxH3ChainContext`、`BlockSparseAttention`、`BasicScheduler`、`KSamplerSelect`、`SamplerCustomAdvanced`、`MiniMaxH3LoopTrim`、`AnySwitch`、`LTXVSeparateAVLatent`、`VAEDecode`、`VAEDecodeAudio`、`MiniMaxH3ChainLoopEnd`、`MinimaxH3LatentUpscaler3D`、`CLIPLoader`、`MiniMaxH3ImageToVideo`、`MiniMaxH3ScheduledReferenceToVideo`、`ResolutionSelector`、`MiniMaxH3ChainAssemble`、`MiniMaxH3ChainCurrent`、`MiniMaxH3ChainSegmentSave`、`MiniMaxH3ChainReview`、`Fast Bypasser (rgthree)`、`LoadImage`、`MiniMaxH3ScheduledPictureReference`、`MiniMaxH3ChainScenePromptEditor`、`MiniMaxH3ChainPlan`、`CreateVideo`、`SaveVideo`、`LoraLoaderModelOnly`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect

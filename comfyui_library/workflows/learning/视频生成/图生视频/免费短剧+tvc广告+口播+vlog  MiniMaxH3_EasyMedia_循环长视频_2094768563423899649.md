---
key: 视频生成/图生视频/免费短剧+tvc广告+口播+vlog  MiniMaxH3_EasyMedia_循环长视频_2094768563423899649.json
name: 免费短剧+tvc广告+口播+vlog  MiniMaxH3_EasyMedia_循环长视频_2094768563423899649
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/免费短剧+tvc广告+口播+vlog  MiniMaxH3_EasyMedia_循环长视频_2094768563423899649.json
hash: 1a2698a22bda7962
coverage: 0.608696
learned_at: 2026-10-17 00:02:58
nodes: [SetNode, SetNode, SetNode, SetNode, GetNode, Reroute, Reroute, Reroute, KSamplerSelect, GetNode, SamplerCustomAdvanced, RandomNoise, BasicGuider, Reroute, Reroute, Reroute, Reroute, VAEDecode, Reroute, MiniMaxH3ChainLoopEnd, GetNode, MiniMaxH3ChainContext, Reroute, Reroute, Reroute, MarkdownNote, 孤海注释, MiniMaxH3ChainSegmentSave, Reroute, VAEDecodeAudio, 孤海注释, GetNode, MiniMaxH3TaggedReferenceToVideo, GetNode, GetNode, LoadVideo, GetVideoComponents, MiniMaxH3TaggedVideoReference, 忽略多组孤海, 忽略多组孤海, MiniMaxH3TaggedAudioReference, MiniMaxH3TaggedAudioReference, Reroute, MiniMaxH3ChainRunManager, MiniMaxH3ChainReview, MiniMaxH3ChainLoopStart, 孤海注释, MiniMaxH3SigmaShift, CLIPLoader, VAELoader, VAELoader, UNETLoader, MiniMaxH3ChainCurrent, MiniMaxH3ChainAssemble, MiniMaxH3ChainPlanStudio, LoadImage, MiniMaxH3TaggedPictureReference, ResolutionSelector, LoadImage, MiniMaxH3TaggedPictureReference, MiniMaxH3ChainPlan, ModelAttentionBackend, LoraLoaderModelOnly, BasicScheduler, LoadAudio, LoraLoaderModelOnly, MiniMaxH3LoopTrim, SaveImage, MiniMaxH3ChainRichScenePromptEditor]
patterns: []
missing: []
---

# 视频生成/图生视频/免费短剧+tvc广告+口播+vlog  MiniMaxH3_EasyMedia_循环长视频_2094768563423899649.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/免费短剧+tvc广告+口播+vlog  MiniMaxH3_EasyMedia_循环长视频_2094768563423899649.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Output → Other

**节点**（69 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `Reroute`
- `Reroute`
- `Reroute`
- `KSamplerSelect` ★核心
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `BasicGuider`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `VAEDecode` ★核心
- `Reroute`
- `MiniMaxH3ChainLoopEnd`
- `GetNode`
- `MiniMaxH3ChainContext`
- `Reroute`
- `Reroute`
- `Reroute`
- `MarkdownNote`
- `孤海注释`
- `MiniMaxH3ChainSegmentSave`
- `Reroute`
- `VAEDecodeAudio` ★核心
- `孤海注释`
- `GetNode`
- `MiniMaxH3TaggedReferenceToVideo`
- `GetNode`
- `GetNode`
- `LoadVideo`
- `GetVideoComponents`
- `MiniMaxH3TaggedVideoReference`
- `忽略多组孤海`
- `忽略多组孤海`
- `MiniMaxH3TaggedAudioReference`
- `MiniMaxH3TaggedAudioReference`
- `Reroute`
- `MiniMaxH3ChainRunManager`
- `MiniMaxH3ChainReview`
- `MiniMaxH3ChainLoopStart`
- `孤海注释`
- `MiniMaxH3SigmaShift`
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `UNETLoader` ★核心
- `MiniMaxH3ChainCurrent`
- `MiniMaxH3ChainAssemble`
- `MiniMaxH3ChainPlanStudio`
- `LoadImage`
- `MiniMaxH3TaggedPictureReference`
- `ResolutionSelector`
- `LoadImage`
- `MiniMaxH3TaggedPictureReference`
- `MiniMaxH3ChainPlan`
- `ModelAttentionBackend`
- `LoraLoaderModelOnly` ★核心
- `BasicScheduler`
- `LoadAudio`
- `LoraLoaderModelOnly` ★核心
- `MiniMaxH3LoopTrim`
- `SaveImage`
- `MiniMaxH3ChainRichScenePromptEditor`

## 知识

覆盖率 **61%**（42/69）

**有卡**：`KSamplerSelect`、`SamplerCustomAdvanced`、`RandomNoise`、`BasicGuider`、`VAEDecode`、`MiniMaxH3ChainLoopEnd`、`MiniMaxH3ChainContext`、`MiniMaxH3ChainSegmentSave`、`VAEDecodeAudio`、`MiniMaxH3TaggedReferenceToVideo`、`LoadVideo`、`GetVideoComponents`、`MiniMaxH3TaggedVideoReference`、`忽略多组孤海`、`MiniMaxH3TaggedAudioReference`、`MiniMaxH3ChainRunManager`、`MiniMaxH3ChainReview`、`MiniMaxH3ChainLoopStart`、`MiniMaxH3SigmaShift`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`MiniMaxH3ChainCurrent`、`MiniMaxH3ChainAssemble`、`MiniMaxH3ChainPlanStudio`、`LoadImage`、`MiniMaxH3TaggedPictureReference`、`ResolutionSelector`、`MiniMaxH3ChainPlan`、`ModelAttentionBackend`、`LoraLoaderModelOnly`、`BasicScheduler`、`LoadAudio`、`MiniMaxH3LoopTrim`、`SaveImage`、`MiniMaxH3ChainRichScenePromptEditor`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect

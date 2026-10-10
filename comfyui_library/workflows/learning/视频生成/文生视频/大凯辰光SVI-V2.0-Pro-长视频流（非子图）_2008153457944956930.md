---
key: 视频生成/文生视频/大凯辰光SVI-V2.0-Pro-长视频流（非子图）_2008153457944956930.json
name: 大凯辰光SVI-V2.0-Pro-长视频流（非子图）_2008153457944956930
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/大凯辰光SVI-V2.0-Pro-长视频流（非子图）_2008153457944956930.json
hash: 1ab55172f987ce10
coverage: 0.529412
learned_at: 2026-10-10 23:12:17
nodes: [CLIPLoader, VAELoader, SplitSigmas, SetNode, SetNode, SetNode, ImageResizeKJv2, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, VAEEncode, GetNode, BasicScheduler, KSamplerSelect, SetNode, SetNode, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, DisableNoise, CLIPTextEncode, SamplerCustomAdvanced, CLIPTextEncode, VAEDecode, SamplerCustomAdvanced, WanImageToVideoSVIPro, RandomNoise, ScheduledCFGGuidance, ScheduledCFGGuidance, DisableNoise, ScheduledCFGGuidance, ScheduledCFGGuidance, RandomNoise, CLIPTextEncode, CLIPTextEncode, VAEDecode, SamplerCustomAdvanced, SamplerCustomAdvanced, ImageBatchExtendWithOverlap, WanImageToVideoSVIPro, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, ScheduledCFGGuidance, GetNode, GetNode, GetNode, GetNode, ScheduledCFGGuidance, SamplerCustomAdvanced, GetNode, GetNode, GetNode, DisableNoise, VAEDecode, CLIPTextEncode, GetNode, CLIPTextEncode, VHS_VideoCombine, VHS_VideoCombine, Reroute, SamplerCustomAdvanced, WanImageToVideoSVIPro, RandomNoise, Reroute, ImageBatchExtendWithOverlap, Reroute, Reroute, ScheduledCFGGuidance, GetNode, GetNode, GetNode, GetNode, ScheduledCFGGuidance, SamplerCustomAdvanced, GetNode, GetNode, GetNode, DisableNoise, VAEDecode, CLIPTextEncode, GetNode, CLIPTextEncode, VHS_VideoCombine, WanImageToVideoSVIPro, RandomNoise, Reroute, Reroute, ImageBatchExtendWithOverlap, SamplerCustomAdvanced, VHS_VideoCombine, Reroute, Reroute, ScheduledCFGGuidance, GetNode, GetNode, GetNode, GetNode, ScheduledCFGGuidance, SamplerCustomAdvanced, GetNode, GetNode, GetNode, DisableNoise, VAEDecode, CLIPTextEncode, GetNode, CLIPTextEncode, VHS_VideoCombine, WanImageToVideoSVIPro, RandomNoise, Reroute, Reroute, ImageBatchExtendWithOverlap, SamplerCustomAdvanced, VHS_VideoCombine, Reroute, Reroute, ScheduledCFGGuidance, GetNode, GetNode, GetNode, GetNode, ScheduledCFGGuidance, SamplerCustomAdvanced, GetNode, GetNode, GetNode, DisableNoise, VAEDecode, CLIPTextEncode, GetNode, CLIPTextEncode, VHS_VideoCombine, WanImageToVideoSVIPro, RandomNoise, Reroute, Reroute, ImageBatchExtendWithOverlap, SamplerCustomAdvanced, VHS_VideoCombine, Reroute, Reroute, ScheduledCFGGuidance, GetNode, GetNode, GetNode, GetNode, ScheduledCFGGuidance, SamplerCustomAdvanced, GetNode, GetNode, GetNode, DisableNoise, VAEDecode, CLIPTextEncode, GetNode, CLIPTextEncode, VHS_VideoCombine, WanImageToVideoSVIPro, RandomNoise, Reroute, ImageBatchExtendWithOverlap, SamplerCustomAdvanced, VHS_VideoCombine, Reroute, Reroute, Reroute, ScheduledCFGGuidance, GetNode, GetNode, GetNode, GetNode, ScheduledCFGGuidance, SamplerCustomAdvanced, GetNode, GetNode, GetNode, DisableNoise, VAEDecode, GetNode, CLIPTextEncode, VHS_VideoCombine, WanImageToVideoSVIPro, Reroute, ImageBatchExtendWithOverlap, SamplerCustomAdvanced, VHS_VideoCombine, Reroute, Reroute, Reroute, RandomNoise, CLIPTextEncode, Note, LoadImage, DiffusionModelLoaderKJ, DiffusionModelLoaderKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingSD3]
patterns: []
missing: []
---

# 视频生成/文生视频/大凯辰光SVI-V2.0-Pro-长视频流（非子图）_2008153457944956930.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/大凯辰光SVI-V2.0-Pro-长视频流（非子图）_2008153457944956930.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（221 个）：
- `CLIPLoader`
- `VAELoader`
- `SplitSigmas`
- `SetNode`
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `VAEEncode` ★核心
- `GetNode`
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `SetNode`
- `SetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `DisableNoise`
- `CLIPTextEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `WanImageToVideoSVIPro`
- `RandomNoise`
- `ScheduledCFGGuidance`
- `ScheduledCFGGuidance`
- `DisableNoise`
- `ScheduledCFGGuidance`
- `ScheduledCFGGuidance`
- `RandomNoise`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `ImageBatchExtendWithOverlap`
- `WanImageToVideoSVIPro`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `ScheduledCFGGuidance`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ScheduledCFGGuidance`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `DisableNoise`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Reroute`
- `SamplerCustomAdvanced` ★核心
- `WanImageToVideoSVIPro`
- `RandomNoise`
- `Reroute`
- `ImageBatchExtendWithOverlap`
- `Reroute`
- `Reroute`
- `ScheduledCFGGuidance`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ScheduledCFGGuidance`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `DisableNoise`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `WanImageToVideoSVIPro`
- `RandomNoise`
- `Reroute`
- `Reroute`
- `ImageBatchExtendWithOverlap`
- `SamplerCustomAdvanced` ★核心
- `VHS_VideoCombine`
- `Reroute`
- `Reroute`
- `ScheduledCFGGuidance`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ScheduledCFGGuidance`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `DisableNoise`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `WanImageToVideoSVIPro`
- `RandomNoise`
- `Reroute`
- `Reroute`
- `ImageBatchExtendWithOverlap`
- `SamplerCustomAdvanced` ★核心
- `VHS_VideoCombine`
- `Reroute`
- `Reroute`
- `ScheduledCFGGuidance`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ScheduledCFGGuidance`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `DisableNoise`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `WanImageToVideoSVIPro`
- `RandomNoise`
- `Reroute`
- `Reroute`
- `ImageBatchExtendWithOverlap`
- `SamplerCustomAdvanced` ★核心
- `VHS_VideoCombine`
- `Reroute`
- `Reroute`
- `ScheduledCFGGuidance`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ScheduledCFGGuidance`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `DisableNoise`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `WanImageToVideoSVIPro`
- `RandomNoise`
- `Reroute`
- `ImageBatchExtendWithOverlap`
- `SamplerCustomAdvanced` ★核心
- `VHS_VideoCombine`
- `Reroute`
- `Reroute`
- `Reroute`
- `ScheduledCFGGuidance`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ScheduledCFGGuidance`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `DisableNoise`
- `VAEDecode` ★核心
- `GetNode`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `WanImageToVideoSVIPro`
- `Reroute`
- `ImageBatchExtendWithOverlap`
- `SamplerCustomAdvanced` ★核心
- `VHS_VideoCombine`
- `Reroute`
- `Reroute`
- `Reroute`
- `RandomNoise`
- `CLIPTextEncode` ★核心
- `Note`
- `LoadImage`
- `DiffusionModelLoaderKJ`
- `DiffusionModelLoaderKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`

## 知识

覆盖率 **53%**（117/221）

**有卡**：`CLIPLoader`、`VAELoader`、`SplitSigmas`、`ImageResizeKJv2`、`VAEEncode`、`BasicScheduler`、`KSamplerSelect`、`VHS_VideoCombine`、`DisableNoise`、`CLIPTextEncode`、`SamplerCustomAdvanced`、`VAEDecode`、`WanImageToVideoSVIPro`、`RandomNoise`、`ScheduledCFGGuidance`、`ImageBatchExtendWithOverlap`、`LoadImage`、`DiffusionModelLoaderKJ`、`LoraLoaderModelOnly`、`ModelSamplingSD3`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerSelect、SamplerCustomAdvanced

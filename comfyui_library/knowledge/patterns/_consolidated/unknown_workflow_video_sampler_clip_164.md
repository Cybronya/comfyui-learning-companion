---
name: unknown_workflow_video_sampler_clip_164
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.541
common_nodes: [Any Switch (rgthree), AudioEncoderEncode, AudioEncoderLoader, AudioSeparation, CLIPLoader, CLIPTextEncode, DWPreprocessor, DeepTranslatorTextNode, DepthAnythingV2Preprocessor, Fast Groups Muter (rgthree), GetNode, ImageResizeKJ, ImageResizeKJv2, KSampler, LoadAudio, LoadImage, ModelSamplingSD3, Mute / Bypass Relay (rgthree), Mute / Bypass Repeater (rgthree), PathchSageAttentionKJ, PreviewAny, PrimitiveStringMultiline, SetNode, TorchCompileModel, TorchCompileModelWanVideoV2, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanSoundImageToVideo, easy int]
problems: []
missing: [Bookmark (rgthree), Label (rgthree), Mute / Bypass Relay (rgthree), Mute / Bypass Repeater (rgthree), Note Plus (mtb), easy int, easy seed]
members: [视频生成/图生视频/1960754743637413890.json, 视频生成/图生视频/1961620401896013826.json, 视频生成/文生视频/1960754743637413890.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_164

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/1960754743637413890.json、视频生成/图生视频/1961620401896013826.json、视频生成/文生视频/1960754743637413890.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：54%

## 共有节点

全部 3 个 workflow 都包含：
- `Any Switch (rgthree)`
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `AudioSeparation`
- `CLIPLoader`
- `CLIPTextEncode`
- `DWPreprocessor`
- `DeepTranslatorTextNode`
- `DepthAnythingV2Preprocessor`
- `Fast Groups Muter (rgthree)`
- `GetNode`
- `ImageResizeKJ`
- `ImageResizeKJv2`
- `KSampler`
- `LoadAudio`
- `LoadImage`
- `ModelSamplingSD3`
- `Mute / Bypass Relay (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `PathchSageAttentionKJ`
- `PreviewAny`
- `PrimitiveStringMultiline`
- `SetNode`
- `TorchCompileModel`
- `TorchCompileModelWanVideoV2`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanSoundImageToVideo`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `Bookmark (rgthree)` —— 2/3 个有
- `Label (rgthree)` —— 2/3 个有
- `Note Plus (mtb)` —— 2/3 个有
- `PrimitiveString` —— 2/3 个有
- `SaveAudioMP3` —— 2/3 个有
- `SaveAudioOpus` —— 2/3 个有
- `StringConcatenate` —— 2/3 个有
- `easy seed` —— 2/3 个有
- `ACE_ImageGetSize` —— 1/3 个有
- `AudioCrop` —— 1/3 个有
- `FrameSelector` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `ResizeLongestToNode` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 25 | 3 | 89% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 3 | 100% |
| 采样算法 | uni_pc | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 25，3 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：Bookmark (rgthree)、Label (rgthree)、Mute / Bypass Relay (rgthree)、Mute / Bypass Repeater (rgthree)、Note Plus (mtb)

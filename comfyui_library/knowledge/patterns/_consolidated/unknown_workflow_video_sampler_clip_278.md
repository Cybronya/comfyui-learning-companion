---
name: unknown_workflow_video_sampler_clip_278
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6465
common_nodes: [Any Switch (rgthree), AudioEncoderEncode, AudioEncoderLoader, AudioSeparation, CLIPLoader, CLIPTextEncode, DWPreprocessor, DeepTranslatorTextNode, DepthAnythingV2Preprocessor, Fast Groups Muter (rgthree), GetNode, ImageResizeKJ, ImageResizeKJv2, KSampler, LoadAudio, LoadImage, ModelSamplingSD3, Mute / Bypass Relay (rgthree), Mute / Bypass Repeater (rgthree), PathchSageAttentionKJ, PreviewAny, PrimitiveStringMultiline, SetNode, TorchCompileModel, TorchCompileModelWanVideoV2, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanSoundImageToVideo, easy int]
problems: []
missing: []
members: [视频生成/图生视频/🦖Wan2.2 S2V 声音驱动图片或视频！官方版_1961620401896013826.json, 视频生成/文生视频/Wan2.2 S2V 声音驱动视频！官方版 多合一工作流_1960754743637413890.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_278

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/🦖Wan2.2 S2V 声音驱动图片或视频！官方版_1961620401896013826.json、视频生成/文生视频/Wan2.2 S2V 声音驱动视频！官方版 多合一工作流_1960754743637413890.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：65%

## 共有节点

全部 2 个 workflow 都包含：
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
- `ACE_ImageGetSize` —— 1/2 个有
- `AudioCrop` —— 1/2 个有
- `Bookmark (rgthree)` —— 1/2 个有
- `FrameSelector` —— 1/2 个有
- `Label (rgthree)` —— 1/2 个有
- `Note Plus (mtb)` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `PrimitiveString` —— 1/2 个有
- `ResizeLongestToNode` —— 1/2 个有
- `SaveAudioMP3` —— 1/2 个有
- `SaveAudioOpus` —— 1/2 个有
- `StringConcatenate` —— 1/2 个有
- `easy seed` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 22.5 | - | 2 | 89% |
| Prompt 约束强度(CFG) | 6 | - | 2 | 100% |
| 采样算法 | uni_pc | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 22.5，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 6，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

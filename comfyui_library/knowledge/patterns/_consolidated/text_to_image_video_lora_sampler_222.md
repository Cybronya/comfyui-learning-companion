---
name: text_to_image_video_lora_sampler_222
type: Text To Image
frequency: 2
level: weak
coverage: 0.5945
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetNode, ImageResizeKJv2, JjkText, KSampler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3ImageToVideo, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, PT_H3ConcatAVLatent, PreviewImage, PrimitiveFloat, RandomNoise, ResolutionSelector, RunningHub Deepcleaner, SamplerCustomAdvanced, SetNode, Text, UNETLoader, VAEDecode, VAEEncode, VAEEncodeAudio, VAELoader, VHS_LoadVideo, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/Fenglairh MiniMax H3 官方版｜完整工作流集合最新加速_2097556019563028482.json, 视频生成/文生视频/超级多合一官方版V2文生图生视频｜MiniMax H3视频生成工作流_2088317993481760769.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_222

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/Fenglairh MiniMax H3 官方版｜完整工作流集合最新加速_2097556019563028482.json、视频生成/文生视频/超级多合一官方版V2文生图生视频｜MiniMax H3视频生成工作流_2088317993481760769.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：59%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `ImageResizeKJv2`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3ImageToVideo`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `PT_H3ConcatAVLatent`
- `PreviewImage`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `RunningHub Deepcleaner`
- `SamplerCustomAdvanced`
- `SetNode`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAEEncodeAudio`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `FL_Audio_BPM_Analyzer` —— 1/2 个有
- `FL_Audio_Drum_Detector` —— 1/2 个有
- `HAIGC_VideoLastFrame` —— 1/2 个有
- `JWFloatToString` —— 1/2 个有
- `LoadAudioUI` —— 1/2 个有
- `ModelAttentionBackend` —— 1/2 个有
- `PixaromaGroupSwitch` —— 1/2 个有
- `PreviewAny` —— 1/2 个有
- `Qwen3ASRLoader_DFT` —— 1/2 个有
- `Qwen3ASRTranscribe_DFT` —— 1/2 个有
- `RHLLMChatNode` —— 1/2 个有
- `RTXVideoSuperResolution` —— 1/2 个有
- `SaveImage` —— 1/2 个有
- `TextCombinerSix` —— 1/2 个有
- `TextCombinerTwo` —— 1/2 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | - | 2 | 100% |
| 高度 | 80 | - | 2 | 100% |
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 4.5 | - | 2 | 100% |
| 采样算法 | er_sde | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 80，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（3/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

---
name: text_to_image_video_lora_sampler_155
type: Text To Image
frequency: 4
level: strong
coverage: 0.53025
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetNode, ImageResizeKJv2, JjkText, KSampler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, PT_H3ConcatAVLatent, RandomNoise, ResolutionSelector, RunningHub Deepcleaner, SamplerCustomAdvanced, SetNode, Text, UNETLoader, VAEDecode, VAEEncode, VAEEncodeAudio, VAELoader, VHS_LoadVideo, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/Fenglairh MiniMax H3 官方版｜完整工作流集合最新加速_2097556019563028482.json, 视频生成/文生视频/MiniMax H3超级多合一工作流官方版V2文生视频图生视频持续优化_2088350962753826818.json, 视频生成/文生视频/多参全能整合｜MiniMax H3文生视频图生视频高速生成_2090141978154590210.json, 视频生成/文生视频/多参全能整合｜MiniMax H3文生视频图生视频高速生成_2090345152245223426.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_155

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/Fenglairh MiniMax H3 官方版｜完整工作流集合最新加速_2097556019563028482.json、视频生成/文生视频/MiniMax H3超级多合一工作流官方版V2文生视频图生视频持续优化_2088350962753826818.json、视频生成/文生视频/多参全能整合｜MiniMax H3文生视频图生视频高速生成_2090141978154590210.json、视频生成/文生视频/多参全能整合｜MiniMax H3文生视频图生视频高速生成_2090345152245223426.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：53%

## 共有节点

全部 4 个 workflow 都包含：
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
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `PT_H3ConcatAVLatent`
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
- `Int` —— 2/4 个有
- `JjkShowText` —— 2/4 个有
- `MiniMaxH3ImageToVideo` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `PrimitiveFloat` —— 2/4 个有
- `PrimitiveString` —— 2/4 个有
- `Dapao_LlamaH3Prompt` —— 1/4 个有
- `FL_Audio_BPM_Analyzer` —— 1/4 个有
- `FL_Audio_Drum_Detector` —— 1/4 个有
- `HAIGC_VideoLastFrame` —— 1/4 个有
- `JWFloatToString` —— 1/4 个有
- `LoadAudioUI` —— 1/4 个有
- `ModelAttentionBackend` —— 1/4 个有
- `PixaromaGroupSwitch` —— 1/4 个有
- `PreviewAny` —— 1/4 个有
- `Qwen3ASRLoader_DFT` —— 1/4 个有
- `Qwen3ASRTranscribe_DFT` —— 1/4 个有
- `RHLLMChatNode` —— 1/4 个有
- `RTXVideoSuperResolution` —— 1/4 个有
- `SaveImage` —— 1/4 个有
- `TextCombinerSix` —— 1/4 个有
- `TextCombinerTwo` —— 1/4 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足

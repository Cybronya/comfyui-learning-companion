---
name: text_to_image_video_upscale_latent_upscale_22
type: Text To Image
frequency: 3
level: strong
coverage: 0.910333
common_nodes: [AudioCrop, BasicGuider, Bjornulf_ShowFloat, CLIPLoader, CLIPTextEncode, CR Float To String, CR Prompt Text, CR Text, CR Text Concatenate, CR Text Replace, ComfyMathExpression, ConcatTextOfUtils, EmptyLatentImage, Float, GetNode, ImageBatchMultiV2, JjkText, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, MelBandRoFormerModelLoader, MelBandRoFormerSampler, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3LearnedLatentUpscaleT8Advanced, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3TwoPassDetailMixerT8Advanced, MiniMaxH3TwoPassLatentReconcileT8Advanced, ModelAttentionBackend, PreviewAny, PreviewAudio, PrimitiveFloat, PurgeVRAM_UTK, RH_GetAudioDuration, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, ShowAnything|Mie, SolAttnMiniMax, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy anythingIndexSwitch, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/动漫MV人物唱歌专用 视频生成处理工具_2100645683492638722.json, 数字人/数字人/动漫MV人物唱歌专用For anime MV｜数字人角色表演一条龙，视频成片直接发布_2100462340885012481.json, 数字人/数字人/极速数字人MV制作 小白友好高清多模态视频生成_2098859053823905793.json]
source: knowledge_consolidation
---

# text_to_image_video_upscale_latent_upscale_22

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（数字人/数字人/动漫MV人物唱歌专用 视频生成处理工具_2100645683492638722.json、数字人/数字人/动漫MV人物唱歌专用For anime MV｜数字人角色表演一条龙，视频成片直接发布_2100462340885012481.json、数字人/数字人/极速数字人MV制作 小白友好高清多模态视频生成_2098859053823905793.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 3 个 workflow 都包含：
- `AudioCrop`
- `BasicGuider`
- `Bjornulf_ShowFloat`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Float To String`
- `CR Prompt Text`
- `CR Text`
- `CR Text Concatenate`
- `CR Text Replace`
- `ComfyMathExpression`
- `ConcatTextOfUtils`
- `EmptyLatentImage`
- `Float`
- `GetNode`
- `ImageBatchMultiV2`
- `JjkText`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderBypassModelOnly`
- `LoraLoaderModelOnly`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3DualClockSamplerT8`
- `MiniMaxH3LearnedLatentUpscaleT8Advanced`
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3TwoPassDetailMixerT8Advanced`
- `MiniMaxH3TwoPassLatentReconcileT8Advanced`
- `ModelAttentionBackend`
- `PreviewAny`
- `PreviewAudio`
- `PrimitiveFloat`
- `PurgeVRAM_UTK`
- `RH_GetAudioDuration`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `ShowAnything|Mie`
- `SolAttnMiniMax`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy anythingIndexSwitch`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LoadVideo` —— 2/3 个有
- `PrimitiveStringMultiline` —— 2/3 个有
- `SaveImage` —— 2/3 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 2/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足

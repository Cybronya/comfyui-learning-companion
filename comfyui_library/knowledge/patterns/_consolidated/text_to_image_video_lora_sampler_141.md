---
name: text_to_image_video_lora_sampler_141
type: Text To Image
frequency: 4
level: strong
coverage: 0.90275
common_nodes: [AudioCrop, BasicGuider, Bjornulf_ShowFloat, CLIPLoader, CLIPTextEncode, CR Float To String, CR Text, CR Text Concatenate, CR Text Replace, EmptyLatentImage, GetNode, ImageBatchMultiV2, JjkText, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoraLoaderModelOnly, MelBandRoFormerModelLoader, MelBandRoFormerSampler, MiniMaxH3MemoryEfficientSageAttentionPatch, ModelAttentionBackend, PreviewAny, PreviewAudio, PrimitiveFloat, RH_GetAudioDuration, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, ShowAnything|Mie, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/MiniMax H3数字歌手字节4步，最高质量完美版_2111279715519655937.json, 数字人/数字人/动漫MV人物唱歌专用 视频生成处理工具_2100645683492638722.json, 数字人/数字人/动漫MV人物唱歌专用For anime MV｜数字人角色表演一条龙，视频成片直接发布_2100462340885012481.json, 数字人/数字人/极速数字人MV制作 小白友好高清多模态视频生成_2098859053823905793.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_141

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（数字人/数字人/MiniMax H3数字歌手字节4步，最高质量完美版_2111279715519655937.json、数字人/数字人/动漫MV人物唱歌专用 视频生成处理工具_2100645683492638722.json、数字人/数字人/动漫MV人物唱歌专用For anime MV｜数字人角色表演一条龙，视频成片直接发布_2100462340885012481.json、数字人/数字人/极速数字人MV制作 小白友好高清多模态视频生成_2098859053823905793.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 4 个 workflow 都包含：
- `AudioCrop`
- `BasicGuider`
- `Bjornulf_ShowFloat`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Float To String`
- `CR Text`
- `CR Text Concatenate`
- `CR Text Replace`
- `EmptyLatentImage`
- `GetNode`
- `ImageBatchMultiV2`
- `JjkText`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `ModelAttentionBackend`
- `PreviewAny`
- `PreviewAudio`
- `PrimitiveFloat`
- `RH_GetAudioDuration`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `ShowAnything|Mie`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 3/4 个有
- `ComfyMathExpression` —— 3/4 个有
- `ConcatTextOfUtils` —— 3/4 个有
- `Float` —— 3/4 个有
- `LoraLoaderBypassModelOnly` —— 3/4 个有
- `MiniMaxH3AVDecodeT8` —— 3/4 个有
- `MiniMaxH3AudioConditioningT8` —— 3/4 个有
- `MiniMaxH3DualClockSamplerT8` —— 3/4 个有
- `MiniMaxH3LearnedLatentUpscaleT8Advanced` —— 3/4 个有
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced` —— 3/4 个有
- `MiniMaxH3TwoPassDetailMixerT8Advanced` —— 3/4 个有
- `MiniMaxH3TwoPassLatentReconcileT8Advanced` —— 3/4 个有
- `PurgeVRAM_UTK` —— 3/4 个有
- `SaveImage` —— 3/4 个有
- `SolAttnMiniMax` —— 3/4 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 3/4 个有
- `easy anythingIndexSwitch` —— 3/4 个有
- `LoadVideo` —— 2/4 个有
- `PrimitiveStringMultiline` —— 2/4 个有
- `BasicScheduler` —— 1/4 个有
- `Bjornulf_ShowInt` —— 1/4 个有
- `Int` —— 1/4 个有
- `KSamplerSelect` —— 1/4 个有
- `MathExpression|pysssss` —— 1/4 个有
- `MiniMaxH3ReferenceToVideo` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足

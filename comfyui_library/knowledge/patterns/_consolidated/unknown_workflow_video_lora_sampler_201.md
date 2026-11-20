---
name: unknown_workflow_video_lora_sampler_201
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.7332
common_nodes: [BasicScheduler, CLIPLoader, CR Float To String, CR Text, CR Text Concatenate, CR Text Replace, ComfyMathExpression, ComfyNumberConvert, ConditioningZeroOut, ImageBatchMultiV2, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MelBandRoFormerModelLoader, MelBandRoFormerSampler, MiniMaxChunkFeedForward, MiniMaxH3ReferenceToVideo, MiniMaxLowVRAMAttention, ModelAttentionBackend, ModelPreviewOverrideKJ, PreviewAny, PreviewAudio, PrimitiveStringMultiline, ResolutionSelector, SelfLiftAvatarH3Sampler, ShowAnything|Mie, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: []
missing: []
members: [图片生成/图生图/MV_数字人_最高质量+中等质量1分钟MV_数字人(selflift)_2113455986445996034.json, 图片生成/图生图/全新_Selflift+商用MV工作流+12种组合可选。完美数字人20260916版_2113463501913157634.json, 数字人/数字人/MV 数字人 最高质量+中等质量1分钟MV_数字人(selflift)_2102990042653356034.json, 数字人/数字人/MV 数字人-唱歌 说唱 口播 虚拟主播  minmaxh3 一分钟MV_数字人(selflift)_2111794578809507842.json, 数字人/数字人/MV-数字人-高质量版+中等质量1分钟MV_数字人-最新版_2104865906382958594.json, 视频生成/图生视频/MV 数字人 最高质量版+中等质量1分钟MV_数字人_2102990042653356034.json, 视频生成/图生视频/MV-数字人-高质量版+中等质量1分钟MV_数字人-最新版_2104938995259109378.json, 视频生成/图生视频/MV_数字人_最高质量版_-MMH3_Selflift_2105590721473507329.json, 视频生成/图生视频/MV_数字人_最高质量版_-MMH3_Selflift_2108379925534298113.json, 视频生成/图生视频/全新 Selflift+商用MV工作流+12种组合可选。完美数字人20260916版_2099750134669201409.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_201

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/MV_数字人_最高质量+中等质量1分钟MV_数字人(selflift)_2113455986445996034.json、图片生成/图生图/全新_Selflift+商用MV工作流+12种组合可选。完美数字人20260916版_2113463501913157634.json、数字人/数字人/MV 数字人 最高质量+中等质量1分钟MV_数字人(selflift)_2102990042653356034.json、数字人/数字人/MV 数字人-唱歌 说唱 口播 虚拟主播  minmaxh3 一分钟MV_数字人(selflift)_2111794578809507842.json、数字人/数字人/MV-数字人-高质量版+中等质量1分钟MV_数字人-最新版_2104865906382958594.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：73%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CR Float To String`
- `CR Text`
- `CR Text Concatenate`
- `CR Text Replace`
- `ComfyMathExpression`
- `ComfyNumberConvert`
- `ConditioningZeroOut`
- `ImageBatchMultiV2`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PreviewAny`
- `PreviewAudio`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `SelfLiftAvatarH3Sampler`
- `ShowAnything|Mie`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `LTXVSeparateAVLatent` —— 9/10 个有
- `LTXVAudioVAEEncode` —— 8/10 个有
- `LTXVConcatAVLatent` —— 8/10 个有
- `LoadAudio` —— 8/10 个有
- `SetLatentNoiseMask` —— 8/10 个有
- `SolidMask` —— 8/10 个有
- `SoundFlow_GetLength` —— 8/10 个有
- `JWStringToFloat` —— 6/10 个有
- `TrimAudioDuration` —— 6/10 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 3/10 个有
- `AudioCrop` —— 2/10 个有
- `EmptyImage` —— 2/10 个有
- `Fast Groups Bypasser (rgthree)` —— 2/10 个有
- `GetNode` —— 2/10 个有
- `Int` —— 2/10 个有
- `LoadAudioUI` —— 2/10 个有
- `PreviewImage` —— 2/10 个有
- `PurgeVRAM_UTK` —— 2/10 个有
- `RH_Translator` —— 2/10 个有
- `SetNode` —— 2/10 个有
- `忽略多组孤海` —— 2/10 个有
- `TextInput_` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

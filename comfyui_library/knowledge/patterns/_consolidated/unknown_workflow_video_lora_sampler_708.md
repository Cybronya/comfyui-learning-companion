---
name: unknown_workflow_video_lora_sampler_708
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.56525
common_nodes: [AudioConcat, BasicGuider, BlockSparseAttention, CLIPLoader, CM_FloatToInt, ColorTransfer, ComfyMathExpression, ComfySwitchNode, CreateVideo, EmptyAudio, Float, GetNode, GetVideoComponents, ImageAddNoise, ImageBatchMulti, ImageFromBatch, Int, JjkText, KSamplerSelect, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVSeparateAVLatent, Label (rgthree), LoadAudio, LoadImage, LoadVideo, LoraLoaderModelOnly, ManualSigmas, MemoryManager, MiniMaxH3AddGuide, MiniMaxH3PromptEnhancerT8, MiniMaxH3ReferenceToVideo, ModelAttentionBackend, ModelPreviewOverrideKJ, PixaromaDropdown, PreviewAny, PreviewAudio, RH_IndexTTS25_Loader, RH_IndexTTS25_Synthesize, RandomNoise, RepeatImageBatch, ResizeShortestToNode, ResolutionSelector, SamplerCustomAdvanced, SetLatentNoiseMask, SetNode, SolidMask, StringMergeNode, StringToNumber, TrimAudioDuration, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_GetImageCount, VHS_LoadVideo, VHS_VideoCombine, VideoFrameSample, VideoTemporalCrop, 忽略多组孤海]
problems: []
missing: []
members: [数字人/数字人/MinimaxH3综合工作流 数字人 人物替换 动作迁移 长视频断点续接_2113201744183390210.json, 数字人/数字人/MinimaxH3综合工作流V2 精准边缘识别 多人替换 复杂镜头跟踪 长视频断点续接_2116248553747206146.json, 数字人/数字人/MinimaxH3综合工作流_数字人_人物替换_动作迁移_长视频断点续接_2116693553027043329.json, 视频生成/视频生视频/MinimaxH3综合工作流 数字人 人物替换 动作迁移 长视频断点续接_2113201744183390210.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_708

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（数字人/数字人/MinimaxH3综合工作流 数字人 人物替换 动作迁移 长视频断点续接_2113201744183390210.json、数字人/数字人/MinimaxH3综合工作流V2 精准边缘识别 多人替换 复杂镜头跟踪 长视频断点续接_2116248553747206146.json、数字人/数字人/MinimaxH3综合工作流_数字人_人物替换_动作迁移_长视频断点续接_2116693553027043329.json、视频生成/视频生视频/MinimaxH3综合工作流 数字人 人物替换 动作迁移 长视频断点续接_2113201744183390210.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：57%

## 共有节点

全部 4 个 workflow 都包含：
- `AudioConcat`
- `BasicGuider`
- `BlockSparseAttention`
- `CLIPLoader`
- `CM_FloatToInt`
- `ColorTransfer`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `CreateVideo`
- `EmptyAudio`
- `Float`
- `GetNode`
- `GetVideoComponents`
- `ImageAddNoise`
- `ImageBatchMulti`
- `ImageFromBatch`
- `Int`
- `JjkText`
- `KSamplerSelect`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `Label (rgthree)`
- `LoadAudio`
- `LoadImage`
- `LoadVideo`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MemoryManager`
- `MiniMaxH3AddGuide`
- `MiniMaxH3PromptEnhancerT8`
- `MiniMaxH3ReferenceToVideo`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PixaromaDropdown`
- `PreviewAny`
- `PreviewAudio`
- `RH_IndexTTS25_Loader`
- `RH_IndexTTS25_Synthesize`
- `RandomNoise`
- `RepeatImageBatch`
- `ResizeShortestToNode`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `SetNode`
- `SolidMask`
- `StringMergeNode`
- `StringToNumber`
- `TrimAudioDuration`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_GetImageCount`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VideoFrameSample`
- `VideoTemporalCrop`
- `忽略多组孤海`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 1/4 个有
- `CheckpointLoaderSimple` —— 1/4 个有
- `EmptyImage` —— 1/4 个有
- `GetImageSize` —— 1/4 个有
- `GrowMask` —— 1/4 个有
- `ImageCompositeMasked` —— 1/4 个有
- `MaskCompositeYC` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `PrimitiveInt` —— 1/4 个有
- `SAM3_TrackPreview` —— 1/4 个有
- `SAM3_TrackToMask` —— 1/4 个有
- `SAM3_VideoTrack` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

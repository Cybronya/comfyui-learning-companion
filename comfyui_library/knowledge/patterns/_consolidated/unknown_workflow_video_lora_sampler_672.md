---
name: unknown_workflow_video_lora_sampler_672
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.43225
common_nodes: [AddLabel, BasicScheduler, CFGGuider, CLIPLoader, ComfyMathExpression, ComfyNumberConvert, ComfySwitchNode, CreateVideo, EmptyAudio, EmptyMiniMaxH3LatentAV, GetImageSize, GetNode, ImageConcatMulti, ImageResizeKJv2, KSamplerSelect, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3AddGuide, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, MiniMaxLowVRAMAttention, ModelAttentionBackend, ModelPreviewOverrideKJ, PreviewAny, PrimitiveFloat, PrimitiveInt, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, SetNode, SolAttnPatch, SomethingToString, StringConcatenate, TextGenerate, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideoFFmpeg, VHS_VideoCombine, VHS_VideoInfo]
problems: []
missing: []
members: [平台全量/MinimaxH3全能参考动作迁移+高清放大_2117665280808804353.json, 平台全量/minimax_动作迁移_2113827513460940801.json, 视频生成/图生视频/MiniMax H3 风格参考视频风格迁移_2099000699609767937.json, 视频生成/图生视频/MinimaxH3视频角色替换+lms放大_2110649907953627137.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_672

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/MinimaxH3全能参考动作迁移+高清放大_2117665280808804353.json、平台全量/minimax_动作迁移_2113827513460940801.json、视频生成/图生视频/MiniMax H3 风格参考视频风格迁移_2099000699609767937.json、视频生成/图生视频/MinimaxH3视频角色替换+lms放大_2110649907953627137.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：43%

## 共有节点

全部 4 个 workflow 都包含：
- `AddLabel`
- `BasicScheduler`
- `CFGGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `ComfyNumberConvert`
- `ComfySwitchNode`
- `CreateVideo`
- `EmptyAudio`
- `EmptyMiniMaxH3LatentAV`
- `GetImageSize`
- `GetNode`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3AddGuide`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PreviewAny`
- `PrimitiveFloat`
- `PrimitiveInt`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `SetNode`
- `SolAttnPatch`
- `SomethingToString`
- `StringConcatenate`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideoFFmpeg`
- `VHS_VideoCombine`
- `VHS_VideoInfo`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 3/4 个有
- `ImageFromBatch` —— 3/4 个有
- `LTXVConcatAVLatent` —— 3/4 个有
- `ManualSigmas` —— 3/4 个有
- `MinimaxH3LatentUpscaler3D` —— 3/4 个有
- `PrimitiveBoolean` —— 3/4 个有
- `PrimitiveStringMultiline` —— 3/4 个有
- `ResizeImageMaskNode` —— 3/4 个有
- `VAEDecodeAudio` —— 3/4 个有
- `BatchImagesNode` —— 2/4 个有
- `StringReplace` —— 2/4 个有
- `VHS_SelectEveryNthImage` —— 2/4 个有
- `CLIPTextEncode` —— 1/4 个有
- `DualCLIPLoader` —— 1/4 个有
- `GetImageRangeFromBatch` —— 1/4 个有
- `GetImageSize+` —— 1/4 个有
- `GetVideoComponents` —— 1/4 个有
- `Int` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

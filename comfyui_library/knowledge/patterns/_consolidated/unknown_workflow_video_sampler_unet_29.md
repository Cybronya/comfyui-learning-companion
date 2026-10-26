---
name: unknown_workflow_video_sampler_unet_29
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.7061
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, CreateVideo, ImageResizeKJv2, LoadAudio, LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, StringFunction|pysssss, UNETLoader, VAELoader, VHS_LoadVideo, VHS_VideoCombine, easy clearCacheAll, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/Minimax H3_全能参考提示词自动反推_2085332365689319426.json, 视频生成/图生视频/加速lora高质开源MiniMax+H3+RE2VA开源版-多图参考生视频_2084144233992253441.json, 视频生成/图生视频/加速版-MiniMax H3 -多参考生视频-提示词自动优化-EasyCache+sag_2084987956389044226.json, 视频生成/图生视频/加速版-MiniMax H3 -多参考生视频-提示词自动优化_2085190964104228865.json, 视频生成/图生视频/高质量双采样Minimax H3高清修复-加速-优秀的一致性_2086079440601313281.json, 视频生成/文生视频/Minimax H3二采重绘，超强一致性！_2087874789624078338.json, 视频生成/文生视频/Minimax H3目前最优方案_2086647576996171777.json, 视频生成/文生视频/Minimax双采高清人脸工作流（自动提示词+最新加速lora）_2088225624673574914.json, 视频生成/文生视频/minimax H3-FL2VA单模型_int8_高清重绘_9图3视频3音频版 (1)_2089990413913518082.json, 视频生成/文生视频/开源H3二次采样 2K高清 (清晰度升级版）_2088273350861869058.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_29

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/Minimax H3_全能参考提示词自动反推_2085332365689319426.json、视频生成/图生视频/加速lora高质开源MiniMax+H3+RE2VA开源版-多图参考生视频_2084144233992253441.json、视频生成/图生视频/加速版-MiniMax H3 -多参考生视频-提示词自动优化-EasyCache+sag_2084987956389044226.json、视频生成/图生视频/加速版-MiniMax H3 -多参考生视频-提示词自动优化_2085190964104228865.json、视频生成/图生视频/高质量双采样Minimax H3高清修复-加速-优秀的一致性_2086079440601313281.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：71%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `ImageResizeKJv2`
- `LoadAudio`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `StringFunction|pysssss`
- `UNETLoader`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `easy clearCacheAll`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 9/10 个有
- `EasyCache` —— 9/10 个有
- `Fast Groups Bypasser (rgthree)` —— 9/10 个有
- `KSamplerSelect` —— 9/10 个有
- `RHLLMChatNode` —— 9/10 个有
- `VAEDecode` —— 9/10 个有
- `VAEDecodeAudio` —— 9/10 个有
- `LoraLoaderBypassModelOnly` —— 7/10 个有
- `PathchSageAttentionKJ` —— 7/10 个有
- `AudioCrop` —— 6/10 个有
- `INTConstant` —— 6/10 个有
- `PT_H3ConcatAVLatent` —— 6/10 个有
- `VAEEncode` —— 6/10 个有
- `VAEEncodeAudio` —— 6/10 个有
- `GetNode` —— 5/10 个有
- `ResizeShortestToNode` —— 5/10 个有
- `SetNode` —— 5/10 个有
- `GetImageRangeFromBatch` —— 4/10 个有
- `Label (rgthree)` —— 4/10 个有
- `CR Text` —— 3/10 个有
- `LoraLoaderModelOnly` —— 3/10 个有
- `ModelAttentionBackend` —— 3/10 个有
- `孤海注释` —— 3/10 个有
- `MiniMaxH3BlockCacheT8` —— 2/10 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/10 个有
- `VHS_VideoInfoLoaded` —— 2/10 个有
- `Any Switch (rgthree)` —— 1/10 个有
- `LoadVideo` —— 1/10 个有
- `MiniMaxH3AVDecodeT8` —— 1/10 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 1/10 个有
- `PreviewAny` —— 1/10 个有
- `SaveVideo` —— 1/10 个有
- `SolAttnPatch` —— 1/10 个有
- `Text Multiline` —— 1/10 个有
- `TrimAudioDuration` —— 1/10 个有
- `UniBlockSwap` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

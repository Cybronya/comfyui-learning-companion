---
name: unknown_workflow_video_sampler_unet_42
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.720429
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, CreateVideo, ImageResizeKJv2, LoadAudio, LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RHLLMChatNode, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, StringFunction|pysssss, UNETLoader, VAELoader, VHS_LoadVideo, VHS_VideoCombine, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/Minimax H3_全能参考提示词自动反推_2085332365689319426.json, 视频生成/图生视频/加速lora高质开源MiniMax+H3+RE2VA开源版-多图参考生视频_2084144233992253441.json, 视频生成/图生视频/加速版-MiniMax H3 -多参考生视频-提示词自动优化-EasyCache+sag_2084987956389044226.json, 视频生成/图生视频/加速版-MiniMax H3 -多参考生视频-提示词自动优化_2085190964104228865.json, 视频生成/图生视频/高质量双采样Minimax H3高清修复-加速-优秀的一致性_2086079440601313281.json, 视频生成/文生视频/MiniMax+H3多合一加速工作流，提示词优化，二采放大，多参，图生，文生，首尾帧_2087914357572325377.json, 视频生成/文生视频/Minimax H3目前最优方案_2086647576996171777.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_42

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/Minimax H3_全能参考提示词自动反推_2085332365689319426.json、视频生成/图生视频/加速lora高质开源MiniMax+H3+RE2VA开源版-多图参考生视频_2084144233992253441.json、视频生成/图生视频/加速版-MiniMax H3 -多参考生视频-提示词自动优化-EasyCache+sag_2084987956389044226.json、视频生成/图生视频/加速版-MiniMax H3 -多参考生视频-提示词自动优化_2085190964104228865.json、视频生成/图生视频/高质量双采样Minimax H3高清修复-加速-优秀的一致性_2086079440601313281.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：72%

## 共有节点

全部 7 个 workflow 都包含：
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
- `RHLLMChatNode`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `StringFunction|pysssss`
- `UNETLoader`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 6/7 个有
- `Fast Groups Bypasser (rgthree)` —— 6/7 个有
- `KSamplerSelect` —— 6/7 个有
- `PathchSageAttentionKJ` —— 6/7 个有
- `VAEDecode` —— 6/7 个有
- `VAEDecodeAudio` —— 6/7 个有
- `easy clearCacheAll` —— 6/7 个有
- `EasyCache` —— 5/7 个有
- `AudioCrop` —— 4/7 个有
- `GetImageRangeFromBatch` —— 4/7 个有
- `Label (rgthree)` —— 4/7 个有
- `CR Text` —— 3/7 个有
- `GetNode` —— 3/7 个有
- `LoraLoaderBypassModelOnly` —— 3/7 个有
- `PT_H3ConcatAVLatent` —— 3/7 个有
- `SetNode` —— 3/7 个有
- `VAEEncode` —— 3/7 个有
- `VAEEncodeAudio` —— 3/7 个有
- `孤海注释` —— 3/7 个有
- `INTConstant` —— 2/7 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/7 个有
- `ResizeShortestToNode` —— 2/7 个有
- `VHS_VideoInfoLoaded` —— 2/7 个有
- `AILab_ImageStitch` —— 1/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/7 个有
- `LayerUtility: PurgeVRAM V2` —— 1/7 个有
- `LoraLoaderModelOnly` —— 1/7 个有
- `MiniMaxH3AVDecodeT8` —— 1/7 个有
- `MiniMaxH3BlockCacheT8` —— 1/7 个有
- `MiniMaxH3ImageToVideo` —— 1/7 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 1/7 个有
- `ModelAttentionBackend` —— 1/7 个有
- `PreviewAny` —— 1/7 个有
- `Text Multiline` —— 1/7 个有
- `llama_cpp_instruct_adv` —— 1/7 个有
- `llama_cpp_model_loader` —— 1/7 个有
- `llama_cpp_parameters` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

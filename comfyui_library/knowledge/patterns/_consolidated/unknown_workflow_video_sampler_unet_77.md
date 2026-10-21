---
name: unknown_workflow_video_sampler_unet_77
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.869333
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, CreateVideo, EasyCache, ImageResizeKJv2, LoadAudio, LoadImage, MiniMaxH3ReferenceToVideo, PathchSageAttentionKJ, PrimitiveFloat, PrimitiveStringMultiline, RHLLMChatNode, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, StringFunction|pysssss, UNETLoader, VAELoader, VHS_LoadVideo, VHS_VideoCombine, easy clearCacheAll, easy showAnything]
problems: []
missing: []
members: [视频生成/文生视频/Minimax_h3_多参生视频+自动提示词优化+light2V加速lora0.1版本_2085875294937903106.json, 视频生成/文生视频/Minimax_h3_多参生视频+自动提示词优化+light2V加速lora0.1版本_2085894326038650882.json, 视频生成/文生视频/【MiniMax H3】数字人 多图参考 提示词自动反推工作流_2084586291085275138.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_77

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/Minimax_h3_多参生视频+自动提示词优化+light2V加速lora0.1版本_2085875294937903106.json、视频生成/文生视频/Minimax_h3_多参生视频+自动提示词优化+light2V加速lora0.1版本_2085894326038650882.json、视频生成/文生视频/【MiniMax H3】数字人 多图参考 提示词自动反推工作流_2084586291085275138.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `EasyCache`
- `ImageResizeKJv2`
- `LoadAudio`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `PathchSageAttentionKJ`
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
- `easy clearCacheAll`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `GetImageRangeFromBatch` —— 2/3 个有
- `LoraLoaderBypassModelOnly` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `MiniMaxH3AVDecodeT8` —— 2/3 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/3 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 2/3 个有
- `AudioCrop` —— 1/3 个有
- `BasicScheduler` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `KSamplerSelect` —— 1/3 个有
- `Label (rgthree)` —— 1/3 个有
- `VAEDecode` —— 1/3 个有
- `VAEDecodeAudio` —— 1/3 个有
- `VHS_VideoInfoLoaded` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

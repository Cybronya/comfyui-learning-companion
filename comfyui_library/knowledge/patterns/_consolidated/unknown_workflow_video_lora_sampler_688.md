---
name: unknown_workflow_video_lora_sampler_688
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.466667
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, GetNode, KSamplerSelect, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3ReferenceToVideo, MiniMaxLowVRAMAttention, ModelAttentionBackend, ModelPreviewOverrideKJ, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/1-Aiden-MiniMax-H3-疯狂测试工作流！！！！_2093054855547015170.json, 视频生成/文生视频/H3全能参考短剧工作流_2108172108395278338.json, 视频生成/文生视频/H3长视频衔接（尾帧22帧锚点）_2108174255279140865.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_688

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/1-Aiden-MiniMax-H3-疯狂测试工作流！！！！_2093054855547015170.json、视频生成/文生视频/H3全能参考短剧工作流_2108172108395278338.json、视频生成/文生视频/H3长视频衔接（尾帧22帧锚点）_2108174255279140865.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：47%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `GetNode`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 2/3 个有
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `VHS_LoadVideo` —— 2/3 个有
- `AudioCrop` —— 1/3 个有
- `GetImageRangeFromBatch` —— 1/3 个有
- `InversionDemoLazyIndexSwitch` —— 1/3 个有
- `LTXVConcatAVLatent` —— 1/3 个有
- `LTXVSeparateAVLatent` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `MiniMaxH3AddGuide` —— 1/3 个有
- `MiniMaxH3SigmaShift` —— 1/3 个有
- `MinimaxH3LatentUpscaler3D` —— 1/3 个有
- `Seed (rgthree)` —— 1/3 个有
- `SplitSigmas` —— 1/3 个有
- `TrimAudioDuration` —— 1/3 个有
- `easy int` —— 1/3 个有
- `easy positive` —— 1/3 个有
- `孤海注释` —— 1/3 个有
- `忽略多组孤海` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

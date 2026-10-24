---
name: unknown_workflow_lora_sampler_unet_88
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.761
common_nodes: [BasicGuider, CLIPLoader, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3SigmaShift, ModelAttentionBackend, ModelPreviewOverrideKJ, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax H3全能插件+双采1080p高清（8步加速）_2090022090694021122.json, 视频生成/文生视频/MiniMax H3全能插件+音频设计_2097244728222896129.json, 视频生成/文生视频/MiniMax H3去除人物油腻（单采高质量加速版）_2092133541474816001.json, 视频生成/文生视频/MiniMax H3增强画面电影感_2092881815047598082.json, 视频生成/文生视频/MiniMax H3新版8步768p加速（单采高质量）_2094009829802205186.json, 视频生成/文生视频/MiniMax-H3 fl2v单模型二采无编解码放大_2093393143118000129.json, 视频生成/文生视频/MiniMax-H3 极限复杂大动态与人脸去油腻工作流_2096278728602112001.json, 视频生成/文生视频/啊癫 minimaxh3极速版二采潜空间直接放大（去油版）_2093957991434379265.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_88

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3全能插件+双采1080p高清（8步加速）_2090022090694021122.json、视频生成/文生视频/MiniMax H3全能插件+音频设计_2097244728222896129.json、视频生成/文生视频/MiniMax H3去除人物油腻（单采高质量加速版）_2092133541474816001.json、视频生成/文生视频/MiniMax H3增强画面电影感_2092881815047598082.json、视频生成/文生视频/MiniMax H3新版8步768p加速（单采高质量）_2094009829802205186.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：76%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 7/8 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 7/8 个有
- `Label (rgthree)` —— 6/8 个有
- `VHS_VideoCombine` —— 6/8 个有
- `LTXVConcatAVLatent` —— 5/8 个有
- `LTXVSeparateAVLatent` —— 5/8 个有
- `LoadImage` —— 5/8 个有
- `MiniMaxH3Unified` —— 5/8 个有
- `MinimaxH3LatentUpscaler3D` —— 5/8 个有
- `SplitSigmas` —— 5/8 个有
- `ComfyMathExpression` —— 4/8 个有
- `CreateVideo` —— 3/8 个有
- `H3SigmaRefiner` —— 3/8 个有
- `MiniMaxH3ReferenceToVideo` —— 3/8 个有
- `SaveVideo` —— 3/8 个有
- `GetNode` —— 2/8 个有
- `ManualSigmas` —— 2/8 个有
- `SetNode` —— 2/8 个有
- `ComfySwitchNode` —— 1/8 个有
- `ConditioningZeroOut` —— 1/8 个有
- `ExtendIntermediateSigmas` —— 1/8 个有
- `Fast Groups Bypasser (rgthree)` —— 1/8 个有
- `LoadAudio` —— 1/8 个有
- `MiniMaxChunkFeedForward` —— 1/8 个有
- `MiniMaxH3ImageToVideo` —— 1/8 个有
- `UniBlockSwap` —— 1/8 个有
- `VRAM_Debug` —— 1/8 个有
- `布尔孤海` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

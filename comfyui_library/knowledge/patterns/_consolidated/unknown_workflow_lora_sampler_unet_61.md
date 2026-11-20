---
name: unknown_workflow_lora_sampler_unet_61
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.859182
common_nodes: [BasicScheduler, CLIPLoader, KSamplerSelect, LoraLoaderModelOnly, ModelAttentionBackend, ResolutionSelector, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Mini MAX-H3加速版图生视频1080p_2114685347656454146.json, 视频生成/图生视频/MiniMax H3 导演skill+双采2k直出_2106288951286915073.json, 视频生成/图生视频/MiniMax-H3-导演skill-双采2k直出.json, 视频生成/文生视频/MiniMax H3 导演skill+双采2k直出_2103795804296273922.json, 视频生成/文生视频/MiniMax H3全能插件+音频设计_2097244728222896129.json, 视频生成/文生视频/MiniMax H3去除人物油腻（单采高质量加速版）_2092133541474816001.json, 视频生成/文生视频/MiniMax H3增强画面电影感_2092881815047598082.json, 视频生成/文生视频/MiniMax H3新版8步768p加速（单采高质量）_2094009829802205186.json, 视频生成/文生视频/MiniMax_H3_REF2VA-Upscale 双采样视频生成工作流_2092581047509807105.json, 视频生成/文生视频/Minimax H3 多参数视频生成 768p 加速 LoRA 两步生成_2095762977566846977.json, 视频生成/文生视频/minimax h3综合型工作流第一人称，男友视角_2108015047955013633.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_61

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/Mini MAX-H3加速版图生视频1080p_2114685347656454146.json、视频生成/图生视频/MiniMax H3 导演skill+双采2k直出_2106288951286915073.json、视频生成/图生视频/MiniMax-H3-导演skill-双采2k直出.json、视频生成/文生视频/MiniMax H3 导演skill+双采2k直出_2103795804296273922.json、视频生成/文生视频/MiniMax H3全能插件+音频设计_2097244728222896129.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `ModelAttentionBackend`
- `ResolutionSelector`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 10/11 个有
- `MiniMaxH3SigmaShift` —— 10/11 个有
- `PrimitiveFloat` —— 10/11 个有
- `PrimitiveStringMultiline` —— 10/11 个有
- `LoadImage` —— 9/11 个有
- `ModelPreviewOverrideKJ` —— 9/11 个有
- `ComfyMathExpression` —— 8/11 个有
- `Label (rgthree)` —— 8/11 个有
- `MiniMaxH3ReferenceToVideo` —— 8/11 个有
- `VHS_VideoCombine` —— 8/11 个有
- `BasicGuider` —— 7/11 个有
- `MiniMaxH3Unified` —— 7/11 个有
- `RandomNoise` —— 7/11 个有
- `SamplerCustomAdvanced` —— 7/11 个有
- `H3SigmaRefiner` —— 5/11 个有
- `LTXVSeparateAVLatent` —— 5/11 个有
- `ConditioningZeroOut` —— 4/11 个有
- `Fast Groups Bypasser (rgthree)` —— 4/11 个有
- `LTXVConcatAVLatent` —— 4/11 个有
- `MinimaxH3LatentUpscaler3D` —— 4/11 个有
- `SelfLiftH3Sampler` —— 4/11 个有
- `CreateVideo` —— 3/11 个有
- `SaveVideo` —— 3/11 个有
- `SplitSigmas` —— 3/11 个有
- `ExtendIntermediateSigmas` —— 1/11 个有
- `Float` —— 1/11 个有
- `GetVideoComponents` —— 1/11 个有
- `LoadVideo` —— 1/11 个有
- `ManualSigmas` —— 1/11 个有
- `MiniMaxH3ChunkFeedForwardT8Advanced` —— 1/11 个有
- `MiniMaxH3SemanticBridgeApplyT8` —— 1/11 个有
- `MiniMaxH3SemanticBridgeConfigT8` —— 1/11 个有
- `SolAttnMiniMax` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

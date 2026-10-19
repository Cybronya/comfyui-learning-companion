---
name: unknown_workflow_video_upscale_latent_upscale_69
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8532
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, Label (rgthree), MiniMaxH3SigmaShift, MinimaxH3LatentUpscaler3D, ModelAttentionBackend, ModelPreviewOverrideKJ, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SplitSigmas, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/H3全能工作台+1080p高清+8步加速+提示词优化_2098420190462701570.json, 视频生成/图生视频/H3多参视频生成+Qwen3.8全自动撰写H3提示词_2095738490674827265.json, 视频生成/图生视频/H3（人物替换）参考视频生成+Qwen3.8视频提示词反推_2095682870034653186.json, 视频生成/文生视频/MiniMax H3全能插件+双采1080p高清（8步加速）_2090022090694021122.json, 视频生成/文生视频/MiniMax H3全能插件+音频设计_2097244728222896129.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_69

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/H3全能工作台+1080p高清+8步加速+提示词优化_2098420190462701570.json、视频生成/图生视频/H3多参视频生成+Qwen3.8全自动撰写H3提示词_2095738490674827265.json、视频生成/图生视频/H3（人物替换）参考视频生成+Qwen3.8视频提示词反推_2095682870034653186.json、视频生成/文生视频/MiniMax H3全能插件+双采1080p高清（8步加速）_2090022090694021122.json、视频生成/文生视频/MiniMax H3全能插件+音频设计_2097244728222896129.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `Label (rgthree)`
- `MiniMaxH3SigmaShift`
- `MinimaxH3LatentUpscaler3D`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 4/5 个有
- `ComfyMathExpression` —— 3/5 个有
- `H3SigmaRefiner` —— 3/5 个有
- `LoraLoaderModelOnly` —— 3/5 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/5 个有
- `MiniMaxH3PromptEnhancerT8` —— 3/5 个有
- `MiniMaxH3ReferenceToVideo` —— 3/5 个有
- `MiniMaxH3Unified` —— 3/5 个有
- `PreviewAny` —— 3/5 个有
- `PrimitiveStringMultiline` —— 3/5 个有
- `easy showAnything` —— 3/5 个有
- `ExtendIntermediateSigmas` —— 2/5 个有
- `Float to Int` —— 2/5 个有
- `ManualSigmas` —— 2/5 个有
- `MuyeTextEditOutput` —— 2/5 个有
- `SaveImage` —— 2/5 个有
- `ShellAgentPluginOutputText` —— 2/5 个有
- `CR Prompt Text` —— 1/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `ImageResizeKJv2` —— 1/5 个有
- `LoadVideo` —— 1/5 个有
- `RH_Translator` —— 1/5 个有
- `VHS_LoadVideo` —— 1/5 个有
- `easy saveText` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

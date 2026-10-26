---
name: unknown_workflow_video_upscale_latent_upscale_62
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.711167
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MinimaxH3LatentUpscaler3D, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SplitSigmas, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/H3全能工作台+1080p高清+8步加速+提示词优化_2098420190462701570.json, 视频生成/图生视频/MiniMax H3 多图参考+二采+高清放大+去噪点+两倍提速_2090100666210537473.json, 视频生成/图生视频/MiniMax H3五分钟生成1080p高清（可视化全模态高清输出）_2093962334623584257.json, 视频生成/图生视频/MiniMax H3全能参考，二采放大_2092138431697735681.json, 视频生成/图生视频/MiniMax H3全能插件+音频设计_2104837330120036354.json, 视频生成/图生视频/MinimaxH3 图生视频极速版_2093989563374071810.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_62

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/H3全能工作台+1080p高清+8步加速+提示词优化_2098420190462701570.json、视频生成/图生视频/MiniMax H3 多图参考+二采+高清放大+去噪点+两倍提速_2090100666210537473.json、视频生成/图生视频/MiniMax H3五分钟生成1080p高清（可视化全模态高清输出）_2093962334623584257.json、视频生成/图生视频/MiniMax H3全能参考，二采放大_2092138431697735681.json、视频生成/图生视频/MiniMax H3全能插件+音频设计_2104837330120036354.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：71%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MinimaxH3LatentUpscaler3D`
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
- `H3SigmaRefiner` —— 5/6 个有
- `LoadImage` —— 5/6 个有
- `MiniMaxH3SigmaShift` —— 5/6 个有
- `ModelAttentionBackend` —— 5/6 个有
- `ComfyMathExpression` —— 4/6 个有
- `MiniMaxH3ReferenceToVideo` —— 4/6 个有
- `ModelPreviewOverrideKJ` —— 4/6 个有
- `MiniMaxH3Unified` —— 3/6 个有
- `PrimitiveStringMultiline` —— 3/6 个有
- `CR Prompt Text` —— 2/6 个有
- `ExtendIntermediateSigmas` —— 2/6 个有
- `Fast Groups Bypasser (rgthree)` —— 2/6 个有
- `GetNode` —— 2/6 个有
- `Label (rgthree)` —— 2/6 个有
- `SaveImage` —— 2/6 个有
- `SetNode` —— 2/6 个有
- `easy showAnything` —— 2/6 个有
- `GetVideoComponents` —— 1/6 个有
- `MiniMaxH3HybridArtifactBuilderT8Advanced` —— 1/6 个有
- `MiniMaxH3HybridModelLoaderT8Advanced` —— 1/6 个有
- `MiniMaxH3HybridPairInspectorT8Advanced` —— 1/6 个有
- `MiniMaxH3PromptEnhancerT8` —— 1/6 个有
- `PreviewAny` —— 1/6 个有
- `RH_Translator` —— 1/6 个有
- `Vignette` —— 1/6 个有
- `easy saveText` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

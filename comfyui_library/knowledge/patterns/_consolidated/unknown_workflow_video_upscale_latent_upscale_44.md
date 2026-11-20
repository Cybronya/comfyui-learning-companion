---
name: unknown_workflow_video_upscale_latent_upscale_44
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.885
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, H3SigmaRefiner, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MinimaxH3LatentUpscaler3D, RandomNoise, SamplerCustomAdvanced, SplitSigmas, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/H3 Easy 工作台+双采样+提示词增强_2096870281045434370.json, 视频生成/图生视频/H3全能工作台+1080p高清+8步加速+提示词优化_2098420190462701570.json, 视频生成/图生视频/H3最强去油+双采样+提示词全自动优化_2096561381649772545.json, 视频生成/图生视频/MINIMAX-H3开源 最强去油全模式精简流+独立双采样_2095453807462412289.json, 视频生成/图生视频/MINIMAX-H3开源 最强去油全模式精简流+独立双采样_2095464911093714946.json, 视频生成/图生视频/最强去油全模式精简流+独立双采样 MINIMAXH3_2095036845418700801.json, 视频生成/图生视频/最强去油全模式精简流+独立双采样_MINIMAXH3_2095322121126891521.json, 视频生成/图生视频/最强去油全模式精简流+独立双采样_MINIMAXH3_2095425902569152514.json, 视频生成/文生视频/MiniMax H3全能插件+双采1080p高清（8步加速）_2090022090694021122.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_44

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/H3 Easy 工作台+双采样+提示词增强_2096870281045434370.json、视频生成/图生视频/H3全能工作台+1080p高清+8步加速+提示词优化_2098420190462701570.json、视频生成/图生视频/H3最强去油+双采样+提示词全自动优化_2096561381649772545.json、视频生成/图生视频/MINIMAX-H3开源 最强去油全模式精简流+独立双采样_2095453807462412289.json、视频生成/图生视频/MINIMAX-H3开源 最强去油全模式精简流+独立双采样_2095464911093714946.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `H3SigmaRefiner`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MinimaxH3LatentUpscaler3D`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 8/9 个有
- `Fast Groups Bypasser (rgthree)` —— 7/9 个有
- `LoadAudio` —— 7/9 个有
- `MiniMaxH3Easy` —— 7/9 个有
- `MiniMaxH3EasyModelAdapter` —— 7/9 个有
- `MiniMaxH3EasyOutput` —— 7/9 个有
- `MiniMaxH3EasySecondPassConditioning` —— 7/9 个有
- `VHS_LoadVideo` —— 7/9 个有
- `Label (rgthree)` —— 4/9 个有
- `CR Prompt Text` —— 3/9 个有
- `MiniMaxH3PromptEnhancerT8` —— 3/9 个有
- `PreviewAny` —— 3/9 个有
- `RH_Translator` —— 3/9 个有
- `easy saveText` —— 3/9 个有
- `easy showAnything` —— 3/9 个有
- `ExtendIntermediateSigmas` —— 2/9 个有
- `Int` —— 2/9 个有
- `MiniMaxH3SigmaShift` —— 2/9 个有
- `MiniMaxH3Unified` —— 2/9 个有
- `ModelAttentionBackend` —— 2/9 个有
- `ModelPreviewOverrideKJ` —— 2/9 个有
- `PrimitiveFloat` —— 2/9 个有
- `ResolutionSelector` —— 2/9 个有
- `PrimitiveStringMultiline` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

---
name: unknown_workflow_lora_sampler_unet_34
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.776846
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, H3SigmaRefiner, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3SigmaShift, ModelAttentionBackend, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SplitSigmas, UNETLoader, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/1.MinimaxH3双采样V2版本（自用修改布局）！_2089749289575731202.json, 视频生成/图生视频/MiniMax H3五分钟生成1080p高清（可视化全模态高清输出）_2093962334623584257.json, 视频生成/图生视频/MiniMax H3全能插件+双采1080p高清（8步加速）8-30_2093712107018743809.json, 视频生成/图生视频/MiniMax H3全能插件+双采1080p高清（8步加速）8-30_2093741169816723457.json, 视频生成/图生视频/MiniMax H3全能插件+音频设计_2104837330120036354.json, 视频生成/图生视频/MiniMaxH3+lightx2v加速不油版-单双采_2084916996847792130.json, 视频生成/图生视频/MiniMax_H3_双采样潜空间放大直出1080p_2096948674386550786.json, 视频生成/图生视频/MiniMax_H3全能插件+音频设计_2102927188453584898.json, 视频生成/图生视频/MiniMax_H3全能插件+音频设计_2103670916667494401.json, 视频生成/图生视频/MiniMax_H3全能插件+音频设计_2104845055516299265.json, 视频生成/图生视频/Minimax H3全能多模态--二采放大（加速+sigma强化）工作流_2092164749025964033.json, 视频生成/图生视频/MinimaxH3 图生视频极速版_2093989563374071810.json, 视频生成/图生视频/二采-10s(768P→1080p) Minimax多参生视频_2090054499200225281.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_34

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/文生图/1.MinimaxH3双采样V2版本（自用修改布局）！_2089749289575731202.json、视频生成/图生视频/MiniMax H3五分钟生成1080p高清（可视化全模态高清输出）_2093962334623584257.json、视频生成/图生视频/MiniMax H3全能插件+双采1080p高清（8步加速）8-30_2093712107018743809.json、视频生成/图生视频/MiniMax H3全能插件+双采1080p高清（8步加速）8-30_2093741169816723457.json、视频生成/图生视频/MiniMax H3全能插件+音频设计_2104837330120036354.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 13 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `H3SigmaRefiner`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SplitSigmas`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `MinimaxH3LatentUpscaler3D` —— 12/13 个有
- `PrimitiveFloat` —— 12/13 个有
- `PrimitiveStringMultiline` —— 12/13 个有
- `ModelPreviewOverrideKJ` —— 11/13 个有
- `VAEDecode` —— 11/13 个有
- `VAEDecodeAudio` —— 11/13 个有
- `VHS_VideoCombine` —— 10/13 个有
- `ComfyMathExpression` —— 9/13 个有
- `LoadImage` —— 9/13 个有
- `MiniMaxH3ReferenceToVideo` —— 9/13 个有
- `MiniMaxH3Unified` —— 8/13 个有
- `Fast Groups Bypasser (rgthree)` —— 7/13 个有
- `SolAttnMiniMax` —— 6/13 个有
- `Label (rgthree)` —— 5/13 个有
- `GetNode` —— 4/13 个有
- `SetNode` —— 4/13 个有
- `CreateVideo` —— 3/13 个有
- `ExtendIntermediateSigmas` —— 3/13 个有
- `LoraLoaderBypassModelOnly` —— 3/13 个有
- `SaveVideo` —— 3/13 个有
- `GetVideoComponents` —— 2/13 个有
- `LoadAudio` —— 2/13 个有
- `MiniMaxH3AVDecodeT8` —— 2/13 个有
- `MiniMaxH3HybridArtifactBuilderT8Advanced` —— 2/13 个有
- `MiniMaxH3HybridModelLoaderT8Advanced` —— 2/13 个有
- `MiniMaxH3HybridPairInspectorT8Advanced` —— 2/13 个有
- `SaveImage` —— 2/13 个有
- `CR Text` —— 1/13 个有
- `JWStringToFloat` —— 1/13 个有
- `LayerUtility: PurgeVRAM V2` —— 1/13 个有
- `LoadVideo` —— 1/13 个有
- `MiniMaxH3BlockCacheT8` —— 1/13 个有
- `MiniMaxH3HybridLoader` —— 1/13 个有
- `MiniMaxH3TurboLoRA` —— 1/13 个有
- `MiniMaxH3VRAMPolicyT8Advanced` —— 1/13 个有
- `MinimaxH3LatentUpscalerNode3D` —— 1/13 个有
- `Vignette` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

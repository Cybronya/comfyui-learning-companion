---
name: unknown_workflow_sampler_unet_vae_40
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.756077
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3 图生视频 首尾帧视频 二采 加速版_2104858491864313857.json, 视频生成/图生视频/MiniMax H3 图生视频_首尾帧 加速版_2084297892575145985.json, 视频生成/图生视频/MiniMax H3 多图参考+二采+高清放大+去噪点+两倍提速_2090100666210537473.json, 视频生成/图生视频/MiniMax H3全能插件+音频设计_2104837330120036354.json, 视频生成/图生视频/MiniMax H3图生视频动作面部优化工作流_2089680420211347458.json, 视频生成/图生视频/MiniMaxH3+lightx2v加速不油版-单双采_2084916996847792130.json, 视频生成/图生视频/MiniMax_H3全能插件+音频设计_2102927188453584898.json, 视频生成/图生视频/MiniMax_H3全能插件+音频设计_2103670916667494401.json, 视频生成/图生视频/MiniMax_H3全能插件+音频设计_2104845055516299265.json, 视频生成/图生视频/Minimax H3开源 小脸不崩！打斗不糊！H3 sigma强化+潜空间放大工作流_2089663075422130178.json, 视频生成/图生视频/Minimax H3开源 小脸不崩！打斗不糊！H3 sigma强化+潜空间放大工作流_2089687254284455937.json, 视频生成/图生视频/MinimaxH3 图生视频极速版_2093989563374071810.json, 视频生成/图生视频/二采-10s(768P→1080p) Minimax多参生视频_2090054499200225281.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_40

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3 图生视频 首尾帧视频 二采 加速版_2104858491864313857.json、视频生成/图生视频/MiniMax H3 图生视频_首尾帧 加速版_2084297892575145985.json、视频生成/图生视频/MiniMax H3 多图参考+二采+高清放大+去噪点+两倍提速_2090100666210537473.json、视频生成/图生视频/MiniMax H3全能插件+音频设计_2104837330120036354.json、视频生成/图生视频/MiniMax H3图生视频动作面部优化工作流_2089680420211347458.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：76%

## 共有节点

全部 13 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LTXVConcatAVLatent` —— 12/13 个有
- `LTXVSeparateAVLatent` —— 12/13 个有
- `LoraLoaderModelOnly` —— 12/13 个有
- `SplitSigmas` —— 12/13 个有
- `H3SigmaRefiner` —— 11/13 个有
- `MiniMaxH3ReferenceToVideo` —— 11/13 个有
- `MiniMaxH3SigmaShift` —— 11/13 个有
- `ModelAttentionBackend` —— 11/13 个有
- `PrimitiveStringMultiline` —— 11/13 个有
- `MinimaxH3LatentUpscaler3D` —— 8/13 个有
- `ModelPreviewOverrideKJ` —— 8/13 个有
- `VHS_VideoCombine` —— 7/13 个有
- `CreateVideo` —— 6/13 个有
- `SaveVideo` —— 6/13 个有
- `Fast Groups Bypasser (rgthree)` —— 5/13 个有
- `GetNode` —— 4/13 个有
- `MiniMaxH3Unified` —— 4/13 个有
- `MinimaxH3LatentUpscalerNode3D` —— 4/13 个有
- `SetNode` —— 4/13 个有
- `SolAttnMiniMax` —— 4/13 个有
- `SaveImage` —— 3/13 个有
- `Label (rgthree)` —— 2/13 个有
- `MiniMaxH3HybridArtifactBuilderT8Advanced` —— 2/13 个有
- `MiniMaxH3HybridModelLoaderT8Advanced` —— 2/13 个有
- `MiniMaxH3HybridPairInspectorT8Advanced` —— 2/13 个有
- `MiniMaxH3ImageToVideo` —— 2/13 个有
- `easy showAnything` —— 2/13 个有
- `DiffusionModelLoaderKJ` —— 1/13 个有
- `ExtendIntermediateSigmas` —— 1/13 个有
- `GetVideoComponents` —— 1/13 个有
- `LoadAudio` —— 1/13 个有
- `LoraLoaderBypassModelOnly` —— 1/13 个有
- `MiniMaxH3BlockCacheT8` —— 1/13 个有
- `MiniMaxH3HybridLoader` —— 1/13 个有
- `MiniMaxH3TurboLoRA` —— 1/13 个有
- `MiniMaxH3VRAMPolicyT8Advanced` —— 1/13 个有
- `Vignette` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

---
name: unknown_workflow_upscale_latent_upscale_sampler_8
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.881
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, MiniMaxH3SigmaShift, MinimaxH3LatentUpscaler3D, ModelAttentionBackend, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SplitSigmas, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/H3-R2V 分镜故事板（一键全自动生成视频）_2094235413853589505.json, 视频生成/图生视频/H3全栈式短剧 自动生成二次采样 h3 i2v fastH3 trim latent upscale_2110526500184354818.json, 视频生成/图生视频/H3参考模式_10步+3步Latent Upscaler_2090620971345596417.json, 视频生成/图生视频/MiniMax FastH3 v2全能参考高清放大VSA加速生成_2099780057341456385.json, 视频生成/图生视频/MiniMax H3 图生视频 首尾帧视频 二采 加速版_2104858491864313857.json, 视频生成/图生视频/MiniMax H3 首尾帧3步快速生成+2采放大_2099689978258345985.json, 视频生成/图生视频/MiniMax H3 首尾帧3步快速生成_2100766250199773186.json, 视频生成/图生视频/MiniMax-H3 ref2va单模型二采无编解码放大_2093541824198701058.json, 视频生成/图生视频/h3-二阶+sigma+latent_2096577454994448385.json, 视频生成/文生视频/h3-二阶采样（sigma插值+latent放大）_2090487702180417538.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_sampler_8

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/H3-R2V 分镜故事板（一键全自动生成视频）_2094235413853589505.json、视频生成/图生视频/H3全栈式短剧 自动生成二次采样 h3 i2v fastH3 trim latent upscale_2110526500184354818.json、视频生成/图生视频/H3参考模式_10步+3步Latent Upscaler_2090620971345596417.json、视频生成/图生视频/MiniMax FastH3 v2全能参考高清放大VSA加速生成_2099780057341456385.json、视频生成/图生视频/MiniMax H3 图生视频 首尾帧视频 二采 加速版_2104858491864313857.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `MiniMaxH3SigmaShift`
- `MinimaxH3LatentUpscaler3D`
- `ModelAttentionBackend`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `VHS_VideoCombine` —— 9/10 个有
- `CreateVideo` —— 8/10 个有
- `ModelPreviewOverrideKJ` —— 8/10 个有
- `SaveVideo` —— 8/10 个有
- `LoraLoaderModelOnly` —— 7/10 个有
- `ManualSigmas` —— 7/10 个有
- `PrimitiveStringMultiline` —— 7/10 个有
- `MiniMaxH3ReferenceToVideo` —— 6/10 个有
- `MiniMaxH3ImageToVideo` —— 4/10 个有
- `CR Text` —— 3/10 个有
- `ExtendIntermediateSigmas` —— 3/10 个有
- `Fast Groups Muter (rgthree)` —— 3/10 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/10 个有
- `RH_LLMAPI_Pro_Node` —— 3/10 个有
- `easy showAnything` —— 3/10 个有
- `BlockSparseAttention` —— 2/10 个有
- `Fast Groups Bypasser (rgthree)` —— 2/10 个有
- `GetImageSize` —— 2/10 个有
- `ImageConcatMulti` —— 2/10 个有
- `ImageResizeKJv2` —— 2/10 个有
- `PixaromaDuration` —— 2/10 个有
- `SolAttnMiniMax` —— 2/10 个有
- `TextOverlay` —— 2/10 个有
- `DeepTranslatorTextNode` —— 1/10 个有
- `MiniMaxH3HybridLoader` —— 1/10 个有
- `PixaromaSizes` —— 1/10 个有
- `RH_RhartImageV1OfficialEdit` —— 1/10 个有
- `SaveImage` —— 1/10 个有
- `ShowText|pysssss` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

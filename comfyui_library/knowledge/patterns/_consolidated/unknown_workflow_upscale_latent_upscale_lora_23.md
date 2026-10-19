---
name: unknown_workflow_upscale_latent_upscale_lora_23
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.7508
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MinimaxH3LatentUpscaler3D, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/1.MinimaxH3双采样V2版本（自用修改布局）！_2089749289575731202.json, 视频生成/图生视频/MiniMax H3五分钟生成1080p高清（可视化全模态高清输出）_2093962334623584257.json, 视频生成/图生视频/MiniMax H3全能参考，二采放大_2092138431697735681.json, 视频生成/图生视频/MiniMax H3全能插件+双采1080p高清（8步加速）8-30_2093712107018743809.json, 视频生成/图生视频/MiniMax H3全能插件+双采1080p高清（8步加速）8-30_2093741169816723457.json, 视频生成/图生视频/MiniMax_H3_二次采样+放大文戏工作流_2096179690426949633.json, 视频生成/图生视频/MiniMax_H3_二次采样+放大武器对决工作流_2096593027769913345.json, 视频生成/图生视频/MiniMax_H3_二次采样+放大武戏工作流_2096227914462355458.json, 视频生成/图生视频/h3-二阶+sigma+latent_2096577454994448385.json, 视频生成/文生视频/h3-二阶采样（sigma插值+latent放大）_2090487702180417538.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_23

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/1.MinimaxH3双采样V2版本（自用修改布局）！_2089749289575731202.json、视频生成/图生视频/MiniMax H3五分钟生成1080p高清（可视化全模态高清输出）_2093962334623584257.json、视频生成/图生视频/MiniMax H3全能参考，二采放大_2092138431697735681.json、视频生成/图生视频/MiniMax H3全能插件+双采1080p高清（8步加速）8-30_2093712107018743809.json、视频生成/图生视频/MiniMax H3全能插件+双采1080p高清（8步加速）8-30_2093741169816723457.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MinimaxH3LatentUpscaler3D`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveFloat` —— 9/10 个有
- `MiniMaxH3SigmaShift` —— 8/10 个有
- `ModelAttentionBackend` —— 8/10 个有
- `SplitSigmas` —— 8/10 个有
- `VAEDecode` —— 8/10 个有
- `VAEDecodeAudio` —— 8/10 个有
- `ExtendIntermediateSigmas` —— 7/10 个有
- `ModelPreviewOverrideKJ` —— 7/10 个有
- `VHS_VideoCombine` —— 7/10 个有
- `ComfyMathExpression` —— 6/10 个有
- `LoadImage` —— 6/10 个有
- `MiniMaxH3ReferenceToVideo` —— 6/10 个有
- `CreateVideo` —— 5/10 个有
- `H3SigmaRefiner` —— 5/10 个有
- `SaveVideo` —— 5/10 个有
- `SolAttnMiniMax` —— 5/10 个有
- `CR Prompt Text` —— 4/10 个有
- `GetNode` —— 4/10 个有
- `MiniMaxH3Unified` —— 4/10 个有
- `SetNode` —— 4/10 个有
- `CR Text` —— 3/10 个有
- `Fast Groups Bypasser (rgthree)` —— 3/10 个有
- `PrimitiveStringMultiline` —— 3/10 个有
- `孤海注释` —— 3/10 个有
- `GetImageSize` —— 2/10 个有
- `ImageConcatMulti` —— 2/10 个有
- `ImageResizeKJv2` —— 2/10 个有
- `Label (rgthree)` —— 2/10 个有
- `LoraLoaderBypassModelOnly` —— 2/10 个有
- `MiniMaxH3AVDecodeT8` —— 2/10 个有
- `RH_LLMAPI_Pro_Node` —— 2/10 个有
- `SplitSigmasDenoise` —— 2/10 个有
- `TextOverlay` —— 2/10 个有
- `easy cleanGpuUsed` —— 2/10 个有
- `easy showAnything` —— 2/10 个有
- `DeepTranslatorTextNode` —— 1/10 个有
- `JWStringToFloat` —— 1/10 个有
- `MiniMaxH3HybridLoader` —— 1/10 个有
- `StringConcatenate` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

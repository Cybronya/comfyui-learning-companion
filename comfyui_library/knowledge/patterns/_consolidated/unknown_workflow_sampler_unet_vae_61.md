---
name: unknown_workflow_sampler_unet_vae_61
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8537
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3 图生视频高质量加速版_2084173235788275713.json, 视频生成/图生视频/MiniMax H3开源 稳定加速版 全能参考加速版本 支持自定义音频_2091103432185827330.json, 视频生成/图生视频/MiniMax H3开源 稳定加速版 全能参考加速版本 支持自定义音频_2091128219092213762.json, 视频生成/图生视频/MiniMax H3稳定加速版（全能参考加速版本支持自定义音频）_2088836712364601345.json, 视频生成/图生视频/MiniMax H3稳定加速版（全能参考加速版本支持自定义音频）_2092061440717967361.json, 视频生成/图生视频/MiniMax H3稳定加速版（整合打斗和脸部修复lora）_2090765284436176898.json, 视频生成/图生视频/MiniMaxH3_KeyFarmes_X2（二关键帧）视频生成工作流_2094650229818748929.json, 视频生成/图生视频/MiniMaxH3_KeyFarmes_X4（四关键帧）视频生成工作流_2094650342708436993.json, 视频生成/图生视频/MinimaxH3开源版-全能多参支持视频参考-标准_加速集合版_2087030186406662145.json, 视频生成/文生视频/MiNiMaxH3全能参考_2087801246601277442.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_61

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3 图生视频高质量加速版_2084173235788275713.json、视频生成/图生视频/MiniMax H3开源 稳定加速版 全能参考加速版本 支持自定义音频_2091103432185827330.json、视频生成/图生视频/MiniMax H3开源 稳定加速版 全能参考加速版本 支持自定义音频_2091128219092213762.json、视频生成/图生视频/MiniMax H3稳定加速版（全能参考加速版本支持自定义音频）_2088836712364601345.json、视频生成/图生视频/MiniMax H3稳定加速版（全能参考加速版本支持自定义音频）_2092061440717967361.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 9/10 个有
- `PrimitiveFloat` —— 9/10 个有
- `PrimitiveStringMultiline` —— 9/10 个有
- `SaveVideo` —— 9/10 个有
- `LoraLoaderBypassModelOnly` —— 8/10 个有
- `MiniMaxH3AudioConditioningT8` —— 8/10 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 8/10 个有
- `VHS_VideoCombine` —— 8/10 个有
- `LoadAudio` —— 7/10 个有
- `MiniMaxH3DualClockSamplerT8` —— 6/10 个有
- `MiniMaxH3ReferenceToVideo` —— 4/10 个有
- `Label (rgthree)` —— 3/10 个有
- `LoraLoaderModelOnly` —— 3/10 个有
- `MiniMaxH3AVDecodeT8` —— 3/10 个有
- `ModelAttentionBackend` —— 3/10 个有
- `AudioCrop` —— 2/10 个有
- `MiniMaxH3AddGuide` —— 2/10 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 2/10 个有
- `VHS_LoadVideo` —— 2/10 个有
- `easy cleanGpuUsed` —— 2/10 个有
- `忽略多组孤海` —— 2/10 个有
- `LayerUtility: TextBox` —— 1/10 个有
- `MiniMaxH3ImageToVideo` —— 1/10 个有
- `PrimitiveInt` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

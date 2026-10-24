---
name: text_to_image_upscale_latent_upscale_lora_2
type: Text To Image
frequency: 14
level: strong
coverage: 0.737786
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MinimaxH3LatentUpscaler3D, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MinimaxH3全能参考高清放大｜9图12素材去噪加放大_2111315771795267585.json, 视频生成/图生视频/MinimaxH3动作迁移+人物替换二合一｜图生视频完美优化版_2110680462313218050.json, 视频生成/图生视频/MinimaxH3双模双采hybird+remix｜双加速实验工作流_2094864494676762625.json, 视频生成/图生视频/Ref2VA多参生视频进阶版 MiniMax H3服装展示图生视频_2104344870545608706.json, 视频生成/图生视频/Singularity最强一致性 Minimax H3多参考双采生视频多比例版_2104776734221627394.json, 视频生成/图生视频/Singularity最强一致性 Minimax H3多参考双采生视频标准版_2104646935444549633.json, 视频生成/图生视频/Singularity最强一致性 Minimax H3多参考双采视频生成_2098283807588839426.json, 视频生成/图生视频/Singularity最强一致性多参考双采生视频处理工具_2101743307100610561.json, 视频生成/图生视频/hybird+remix双模双采｜MinimaxH3双加速实验生成_2095055333248032769.json, 视频生成/图生视频/双模双采hybird+remix｜MinimaxH3图生视频双larry加速_2093078463535210498.json, 视频生成/图生视频/双模双采加速｜MinimaxH3 hybrid+remix双larry工作流_2093241754479845378.json, 视频生成/图生视频/双模双采小脸不崩｜Minimax H3高动态不崩脸视频_2093486007596437506.json, 视频生成/图生视频/双模双采资源面板短剧助手 MiniMax H3 全能参考生成视频_2094255084355022849.json, 视频生成/图生视频/同模双采动态修复工作流｜H3图生视频画质增强生成_2097104202756608002.json]
source: knowledge_consolidation
---

# text_to_image_upscale_latent_upscale_lora_2

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/图生视频/MinimaxH3全能参考高清放大｜9图12素材去噪加放大_2111315771795267585.json、视频生成/图生视频/MinimaxH3动作迁移+人物替换二合一｜图生视频完美优化版_2110680462313218050.json、视频生成/图生视频/MinimaxH3双模双采hybird+remix｜双加速实验工作流_2094864494676762625.json、视频生成/图生视频/Ref2VA多参生视频进阶版 MiniMax H3服装展示图生视频_2104344870545608706.json、视频生成/图生视频/Singularity最强一致性 Minimax H3多参考双采生视频多比例版_2104776734221627394.json…）

- **类型**：Text To Image
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：74%

## 共有节点

全部 14 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `MinimaxH3LatentUpscaler3D`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 13/14 个有
- `PrimitiveFloat` —— 13/14 个有
- `ResolutionSelector` —— 13/14 个有
- `SplitSigmas` —— 13/14 个有
- `VHS_VideoCombine` —— 12/14 个有
- `ModelAttentionBackend` —— 11/14 个有
- `LoadAudio` —— 10/14 个有
- `GetNode` —— 9/14 个有
- `SetNode` —— 9/14 个有
- `H3SigmaRefiner` —— 8/14 个有
- `MiniMaxH3SigmaShift` —— 7/14 个有
- `ModelPreviewOverrideKJ` —— 7/14 个有
- `easy cleanGpuUsed` —— 7/14 个有
- `PrimitiveStringMultiline` —— 6/14 个有
- `SaveImage` —— 6/14 个有
- `Text` —— 6/14 个有
- `VHS_LoadVideo` —— 6/14 个有
- `easy float` —— 6/14 个有
- `MiniMaxH3TurboLoRA` —— 5/14 个有
- `Seed (rgthree)` —— 5/14 个有
- `ShellAgentPluginVideoCombineEncrypt` —— 5/14 个有
- `SolAttnMiniMax` —— 5/14 个有
- `Lora Loader Stack (rgthree)` —— 4/14 个有
- `MiniMaxLowVRAMAttention` —— 4/14 个有
- `CreateVideo` —— 2/14 个有
- `LoraLoaderBypassModelOnly` —— 2/14 个有
- `SaveVideo` —— 2/14 个有
- `easy int` —— 2/14 个有
- `Anything Everywhere` —— 1/14 个有
- `Anything Everywhere3` —— 1/14 个有
- `CR Prompt Text` —— 1/14 个有
- `DF_Integer` —— 1/14 个有
- `MiniMaxH3MediaLoaderFantastic` —— 1/14 个有
- `MiniMaxH3ReferenceSplitter` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 14 | 100% |
| 高度 | 80 | 80 - 80 | 14 | 100% |
| 采样步数 | 4 | 4 - 4 | 14 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 14 | 100% |
| 采样算法 | er_sde | - | 14 | 100% |
| 调度器 | beta | - | 14 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，14 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，14 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，14 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，14 个样本，一致性 100%
- 调度器 最常用 beta，14 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 高发问题（14/14 个样本）：Steps较低可能导致细节不足

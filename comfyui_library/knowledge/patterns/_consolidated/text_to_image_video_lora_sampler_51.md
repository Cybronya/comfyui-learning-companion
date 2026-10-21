---
name: text_to_image_video_lora_sampler_51
type: Text To Image
frequency: 13
level: strong
coverage: 0.888846
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoraLoaderModelOnly, MiniMaxH3SigmaShift, ModelAttentionBackend, ModelPreviewOverrideKJ, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SplitSigmas, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/Qwen3.8全自动写提示词｜H3多参视频生成省心流_2096267936318185473.json, 视频生成/图生视频/Singularity真实人物双采流｜角色一致性高保真_2098716861327298562.json, 视频生成/图生视频/minimax h3 i2v Latent Upscaler｜图生视频潜空间放大_2092084924617674753.json, 视频生成/图生视频/minimax h3 i2v Latent Upscaler｜图生视频潜空间放大_2092377938405707778.json, 视频生成/图生视频/minimax h3 r2v Latent Upscaler｜图生视频二采放大_2092058189146710017.json, 视频生成/图生视频/minimax_h3_r2v复杂镜头运动｜视频生视频运镜_2095302998342848513.json, 视频生成/图生视频/minmax潜空间放大姿势迁移｜图生视频新玩法_2097908550017306625.json, 视频生成/图生视频/r2v故事板分镜生成｜minimax_h3图生视频直出_2092737402887561218.json, 视频生成/图生视频/五分钟1080p高清 MiniMax H3 可视化全模态输出_2094229426480439297.json, 视频生成/图生视频/五分钟1080p高清生成｜MiniMax H3全模态可视化视频_2094576638112657410.json, 视频生成/图生视频/五分钟出1080p高清｜MiniMax H3全模态可视化视频_2094351180242710529.json, 视频生成/图生视频/参考视频人物替换｜Qwen3.8反推提示词H3视频生成_2096280706988204034.json, 视频生成/文生视频/全能插件双采1080p｜MiniMax H3 8步加速高清视频_2090562080675033089.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_51

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/Qwen3.8全自动写提示词｜H3多参视频生成省心流_2096267936318185473.json、视频生成/图生视频/Singularity真实人物双采流｜角色一致性高保真_2098716861327298562.json、视频生成/图生视频/minimax h3 i2v Latent Upscaler｜图生视频潜空间放大_2092084924617674753.json、视频生成/图生视频/minimax h3 i2v Latent Upscaler｜图生视频潜空间放大_2092377938405707778.json、视频生成/图生视频/minimax h3 r2v Latent Upscaler｜图生视频二采放大_2092058189146710017.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 13 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly`
- `MiniMaxH3SigmaShift`
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
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `MinimaxH3LatentUpscaler3D` —— 12/13 个有
- `PrimitiveStringMultiline` —— 12/13 个有
- `ComfyMathExpression` —— 9/13 个有
- `LoadImage` —— 9/13 个有
- `ManualSigmas` —— 8/13 个有
- `MiniMaxH3ReferenceToVideo` —— 7/13 个有
- `H3SigmaRefiner` —— 5/13 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/13 个有
- `ExtendIntermediateSigmas` —— 4/13 个有
- `ImageResizeKJv2` —— 4/13 个有
- `MiniMaxH3Unified` —— 4/13 个有
- `Label (rgthree)` —— 3/13 个有
- `SaveImage` —— 3/13 个有
- `Float to Int` —— 2/13 个有
- `MiniMaxH3ImageToVideo` —— 2/13 个有
- `MiniMaxH3PromptEnhancerT8` —— 2/13 个有
- `MuyeTextEditOutput` —— 2/13 个有
- `PreviewAny` —— 2/13 个有
- `ShellAgentPluginOutputText` —— 2/13 个有
- `VHS_LoadVideo` —— 2/13 个有
- `easy showAnything` —— 2/13 个有
- `LoadVideo` —— 1/13 个有
- `MiniMaxH3TurboLoRA` —— 1/13 个有
- `MinimaxH3LatentUpscalerNode3D` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 13 | 100% |
| 高度 | 80 | 80 - 80 | 13 | 100% |
| 采样步数 | 4 | 4 - 4 | 13 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 13 | 100% |
| 采样算法 | er_sde | - | 13 | 100% |
| 调度器 | beta | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，13 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，13 个样本，一致性 100%
- 调度器 最常用 beta，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 高发问题（15/13 个样本）：Steps较低可能导致细节不足

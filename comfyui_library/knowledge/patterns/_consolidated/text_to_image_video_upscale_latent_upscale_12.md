---
name: text_to_image_video_upscale_latent_upscale_12
type: Text To Image
frequency: 6
level: strong
coverage: 0.679
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MinimaxH3LatentUpscaler3D, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SplitSigmas, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, easy float, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/MiniMax H3批量素材图生成｜支持文生图图生图工作流_2097442419775201281.json, 视频生成/文生视频/MiniMax+H3多参考生视频｜9图片3视频3音频任意混搭｜多角色锁定_2101896037253337090.json, 视频生成/文生视频/Minimax H3全能导演台｜短剧分镜丝滑衔接生成_2094862928741756929.json, 视频生成/文生视频/Singularity模型双采放大 视频图片超分辨率增强_2098863700953362434.json, 视频生成/文生视频/台词优化正反打镜头Singularity双采放大｜文生视频视频生视频对话戏更带感_2100457358244798465.json, 视频生成/文生视频/台词优化正反打镜头Singularity模型双采放大处理_2100644227557445634.json]
source: knowledge_consolidation
---

# text_to_image_video_upscale_latent_upscale_12

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3批量素材图生成｜支持文生图图生图工作流_2097442419775201281.json、视频生成/文生视频/MiniMax+H3多参考生视频｜9图片3视频3音频任意混搭｜多角色锁定_2101896037253337090.json、视频生成/文生视频/Minimax H3全能导演台｜短剧分镜丝滑衔接生成_2094862928741756929.json、视频生成/文生视频/Singularity模型双采放大 视频图片超分辨率增强_2098863700953362434.json、视频生成/文生视频/台词优化正反打镜头Singularity双采放大｜文生视频视频生视频对话戏更带感_2100457358244798465.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：68%

## 共有节点

全部 6 个 workflow 都包含：
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
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
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
- `easy float`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 5/6 个有
- `LoadAudio` —— 5/6 个有
- `SetNode` —— 5/6 个有
- `VHS_LoadVideo` —— 5/6 个有
- `BlockSparseAttention` —— 3/6 个有
- `DisableNoise` —— 3/6 个有
- `ExtendIntermediateSigmas` —— 3/6 个有
- `Lora Loader Stack (rgthree)` —— 3/6 个有
- `MiniMaxChunkFeedForward` —— 3/6 个有
- `MiniMaxLowVRAMAttention` —— 3/6 个有
- `ModelAttentionBackend` —— 3/6 个有
- `PrimitiveStringMultiline` —— 3/6 个有
- `SaveImage` —— 3/6 个有
- `Text` —— 2/6 个有
- `ExtractStoryboards_xuhuan1024` —— 1/6 个有
- `PrimitiveBoolean` —— 1/6 个有
- `Text Multiline` —— 1/6 个有
- `VRAM_Debug` —— 1/6 个有
- `ZML_AnyTypeSwitch` —— 1/6 个有
- `llama_cpp_instruct_adv` —— 1/6 个有
- `llama_cpp_model_loader` —— 1/6 个有
- `llama_cpp_parameters` —— 1/6 个有
- `忽略多组孤海` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足

---
name: text_to_image_upscale_latent_upscale_lora_3
type: Text To Image
frequency: 10
level: strong
coverage: 0.612
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, GetNode, JjkText, KSampler, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, MinimaxH3LatentUpscaler3D, ModelAttentionBackend, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, SplitSigmas, UNETLoader, VAEDecode, VAELoader, easy float, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/MINImax-H3单人音乐MV制作｜文生视频音乐生成_2094927265846091778.json, 视频生成/文生视频/MiniMax H3 二采加速｜多参考图生视频效率翻倍实用工作流_2097500273798369281.json, 视频生成/文生视频/MiniMax H3二采去油不爆音加速工作流，文生视频图生视频制作级方案_2103555034809192449.json, 视频生成/文生视频/MiniMax H3二采去油不爆音加速工作流｜视频生视频不糊脸，音画同步更高级_2100506185672781826.json, 视频生成/文生视频/Singularity模型双采放大 视频图片超分辨率增强_2098863700953362434.json, 视频生成/文生视频/minimaxH3混合模型sigma强化｜潜空间放大高清直出_2094545098968227842.json, 视频生成/文生视频/sigma强化不油腻混合模型｜minimaxH3潜空间放大高清直出_2094790731905986562.json, 视频生成/文生视频/单人音乐MV制作｜MINImax-H3三模视频生成工作流_2095106732040220673.json, 视频生成/文生视频/台词优化正反打镜头Singularity双采放大｜文生视频视频生视频对话戏更带感_2100457358244798465.json, 视频生成/文生视频/台词优化正反打镜头Singularity模型双采放大处理_2100644227557445634.json]
source: knowledge_consolidation
---

# text_to_image_upscale_latent_upscale_lora_3

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/文生视频/MINImax-H3单人音乐MV制作｜文生视频音乐生成_2094927265846091778.json、视频生成/文生视频/MiniMax H3 二采加速｜多参考图生视频效率翻倍实用工作流_2097500273798369281.json、视频生成/文生视频/MiniMax H3二采去油不爆音加速工作流，文生视频图生视频制作级方案_2103555034809192449.json、视频生成/文生视频/MiniMax H3二采去油不爆音加速工作流｜视频生视频不糊脸，音画同步更高级_2100506185672781826.json、视频生成/文生视频/Singularity模型双采放大 视频图片超分辨率增强_2098863700953362434.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：61%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `GetNode`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `MinimaxH3LatentUpscaler3D`
- `ModelAttentionBackend`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy float`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 8/10 个有
- `VAEDecodeAudio` —— 8/10 个有
- `CreateVideo` —— 7/10 个有
- `Fast Groups Bypasser (rgthree)` —— 7/10 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 7/10 个有
- `PrimitiveStringMultiline` —— 7/10 个有
- `SaveVideo` —— 7/10 个有
- `MiniMaxChunkFeedForward` —— 6/10 个有
- `MiniMaxLowVRAMAttention` —— 6/10 个有
- `VHS_LoadVideo` —— 6/10 个有
- `H3SigmaRefiner` —— 4/10 个有
- `INTConstant` —— 4/10 个有
- `ModelPreviewOverrideKJ` —— 4/10 个有
- `ResizeShortestToNode` —— 4/10 个有
- `SolAttnMiniMax` —— 4/10 个有
- `BlockSparseAttention` —— 3/10 个有
- `DisableNoise` —— 3/10 个有
- `ExtendIntermediateSigmas` —— 3/10 个有
- `Lora Loader Stack (rgthree)` —— 3/10 个有
- `MiniMaxH3TurboSampler` —— 3/10 个有
- `SaveImage` —— 3/10 个有
- `Text` —— 3/10 个有
- `VHS_VideoCombine` —— 3/10 个有
- `MuyeTextEditOutput` —— 2/10 个有
- `PreviewAudio` —— 2/10 个有
- `RHLLMChatNode` —— 2/10 个有
- `SoundFlow_GetLength` —— 2/10 个有
- `TrimAudioDuration` —— 2/10 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 2/10 个有
- `easy showAnything` —— 2/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 10 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 10 | 100% |
| 采样算法 | er_sde | - | 10 | 100% |
| 调度器 | beta | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| 宽度 | 80 | 80 - 80 | 10 | 100% |
| 高度 | 80 | 80 - 80 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足

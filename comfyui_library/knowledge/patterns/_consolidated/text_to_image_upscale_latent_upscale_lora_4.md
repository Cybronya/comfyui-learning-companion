---
name: text_to_image_upscale_latent_upscale_lora_4
type: Text To Image
frequency: 9
level: strong
coverage: 0.749
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MinimaxH3LatentUpscaler3D, ModelAttentionBackend, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/MINIMAX H3能文能武双采工作流，文生视频视频生视频图生视频方案_2106850207001563138.json, 视频生成/文生视频/MiniMax H3双模双采高清1080P 4MP一键切换处理工作流_2101753484373745665.json, 视频生成/文生视频/MiniMax H3双模双采高清工作流｜1080P与4MP一键档位切换_2097119187176083458.json, 视频生成/文生视频/Minimax H3浅空间二次放大｜优化小脸和打斗文生视频_2092075828388651010.json, 视频生成/文生视频/Minimax H3浅空间二次放大｜优化小脸和打斗文生视频_2092385604226076674.json, 视频生成/文生视频/Singularity模型双采放大 视频图片超分辨率增强_2098863700953362434.json, 视频生成/文生视频/台词优化正反打镜头Singularity双采放大｜文生视频视频生视频对话戏更带感_2100457358244798465.json, 视频生成/文生视频/台词优化正反打镜头Singularity模型双采放大处理_2100644227557445634.json, 视频生成/文生视频/极速版二采潜空间直接放大 minimaxh3 去油画质提升_2094233661909585921.json]
source: knowledge_consolidation
---

# text_to_image_upscale_latent_upscale_lora_4

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/文生视频/MINIMAX H3能文能武双采工作流，文生视频视频生视频图生视频方案_2106850207001563138.json、视频生成/文生视频/MiniMax H3双模双采高清1080P 4MP一键切换处理工作流_2101753484373745665.json、视频生成/文生视频/MiniMax H3双模双采高清工作流｜1080P与4MP一键档位切换_2097119187176083458.json、视频生成/文生视频/Minimax H3浅空间二次放大｜优化小脸和打斗文生视频_2092075828388651010.json、视频生成/文生视频/Minimax H3浅空间二次放大｜优化小脸和打斗文生视频_2092385604226076674.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 9 个 workflow 都包含：
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
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MinimaxH3LatentUpscaler3D`
- `ModelAttentionBackend`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 8/9 个有
- `PrimitiveFloat` —— 8/9 个有
- `SplitSigmas` —— 8/9 个有
- `GetNode` —— 7/9 个有
- `MiniMaxLowVRAMAttention` —— 7/9 个有
- `SetNode` —— 7/9 个有
- `LoadImage` —— 6/9 个有
- `MiniMaxH3ReferenceToVideo` —— 6/9 个有
- `PrimitiveStringMultiline` —— 6/9 个有
- `ResolutionSelector` —— 6/9 个有
- `VHS_VideoCombine` —— 6/9 个有
- `CreateVideo` —— 5/9 个有
- `H3SigmaRefiner` —— 5/9 个有
- `MiniMaxH3SigmaShift` —— 5/9 个有
- `ModelPreviewOverrideKJ` —— 5/9 个有
- `SaveImage` —— 5/9 个有
- `SaveVideo` —— 5/9 个有
- `ExtendIntermediateSigmas` —— 4/9 个有
- `LoadAudio` —— 4/9 个有
- `easy cleanGpuUsed` —— 4/9 个有
- `BlockSparseAttention` —— 3/9 个有
- `DisableNoise` —— 3/9 个有
- `Lora Loader Stack (rgthree)` —— 3/9 个有
- `MiniMaxChunkFeedForward` —— 3/9 个有
- `MiniMaxH3IntegrationAdapterGH` —— 3/9 个有
- `MiniMaxH3IntegrationGH` —— 3/9 个有
- `VHS_LoadVideo` —— 3/9 个有
- `easy float` —— 3/9 个有
- `easy ifElse` —— 3/9 个有
- `GoohaiMinimaxH3TiledSampler` —— 2/9 个有
- `FlashVSRNode` —— 1/9 个有
- `easy anythingIndexSwitch` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | beta | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 80 | 80 - 80 | 9 | 100% |
| 高度 | 80 | 80 - 80 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高发问题（10/9 个样本）：Steps较低可能导致细节不足

---
name: text_to_image_lora_sampler_clip_280
type: Text To Image
frequency: 8
level: strong
coverage: 0.782875
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3SigmaShift, ModelAttentionBackend, ModelPreviewOverrideKJ, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/全能插件双采1080p｜MiniMax H3 8步加速高清视频_2090562080675033089.json, 视频生成/文生视频/单采高质量加速版｜MiniMax H3去除人物油腻处理_2092550530987020289.json, 视频生成/文生视频/双采样V2版｜MinimaxH3文生图生视频全能高速生成_2089771004057972737.json, 视频生成/文生视频/双采样V2版｜MinimaxH3文生图生视频角色表演_2091658421383815170.json, 视频生成/文生视频/双采样高清提速V2｜MinimaxH3音画同步角色表演_2091828773837697025.json, 视频生成/文生视频/小脸不崩运动不糊｜H3高清优化版文生图生视频_2089773922295304193.json, 视频生成/文生视频/智能提示词优化｜海螺minimaxH3加速双采样高清放大工作流_2089801693700648962.json, 视频生成/文生视频/混合模型sigma强化潜空间放大｜minimaxH3高清直出不油腻_2091282726027616257.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_280

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/文生视频/全能插件双采1080p｜MiniMax H3 8步加速高清视频_2090562080675033089.json、视频生成/文生视频/单采高质量加速版｜MiniMax H3去除人物油腻处理_2092550530987020289.json、视频生成/文生视频/双采样V2版｜MinimaxH3文生图生视频全能高速生成_2089771004057972737.json、视频生成/文生视频/双采样V2版｜MinimaxH3文生图生视频角色表演_2091658421383815170.json、视频生成/文生视频/双采样高清提速V2｜MinimaxH3音画同步角色表演_2091828773837697025.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `H3SigmaRefiner` —— 7/8 个有
- `LTXVConcatAVLatent` —— 7/8 个有
- `LTXVSeparateAVLatent` —— 7/8 个有
- `SplitSigmas` —— 7/8 个有
- `SolAttnMiniMax` —— 6/8 个有
- `VHS_VideoCombine` —— 6/8 个有
- `MiniMaxH3Unified` —— 5/8 个有
- `PrimitiveFloat` —— 5/8 个有
- `VAEDecodeAudio` —— 5/8 个有
- `CR Text` —— 4/8 个有
- `Label (rgthree)` —— 4/8 个有
- `MinimaxH3LatentUpscalerNode3D` —— 4/8 个有
- `PrimitiveStringMultiline` —— 4/8 个有
- `ComfyMathExpression` —— 3/8 个有
- `Fast Groups Bypasser (rgthree)` —— 3/8 个有
- `GetNode` —— 3/8 个有
- `LoadImage` —— 3/8 个有
- `MiniMaxH3AVDecodeT8` —— 3/8 个有
- `MiniMaxH3ReferenceToVideo` —— 3/8 个有
- `MinimaxH3LatentUpscaler3D` —— 3/8 个有
- `SetNode` —— 3/8 个有
- `CreateVideo` —— 2/8 个有
- `SaveVideo` —— 2/8 个有
- `ExtendIntermediateSigmas` —— 1/8 个有
- `INTConstant` —— 1/8 个有
- `MuyeTextEditOutput` —— 1/8 个有
- `PathchSageAttentionKJ` —— 1/8 个有
- `ResizeShortestToNode` —— 1/8 个有
- `ShowText|pysssss` —— 1/8 个有
- `StariAI-MiniMaxH3-Skill` —— 1/8 个有
- `easy float` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 80 | 80 - 80 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足

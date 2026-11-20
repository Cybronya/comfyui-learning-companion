---
name: text_to_image_video_lora_sampler_45
type: Text To Image
frequency: 17
level: strong
coverage: 0.912294
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3Unified, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/Minimax双采全功能视频工作流｜文生视频图生视频视频生视频三合一_2088696202564038657.json, 视频生成/文生视频/h3 4步二采视频生成 文生视频加速高质量出片_2094239404528324609.json, 视频生成/文生视频/h3 8步二采视频生成 文生视频二采加速放大出片_2094240878670995457.json, 视频生成/文生视频/h3 8步单采视频替换生成 文生视频快速高质量出片_2094226586693357570.json, 视频生成/文生视频/h3八步二采视频｜文生图生视频生视频三模输出_2094358128707063810.json, 视频生成/文生视频/h3四步二采视频｜三模加速一键生成工作流_2094356687963648002.json, 视频生成/文生视频/lightx2V加速版V3｜MinimaxH3全功能三模工作流_2092579297893642242.json, 视频生成/文生视频/全功能加速工作流V3｜MinimaxH3 lightx2V加速版_2092331681079451649.json, 视频生成/文生视频/全功能双采二选一｜Minimax文生视频图生视频视频生视频_2089019399863889922.json, 视频生成/文生视频/全能插件双采1080p｜MiniMax H3 8步加速高清视频_2090562080675033089.json, 视频生成/文生视频/单采高质量加速版｜MiniMax H3去除人物油腻处理_2092550530987020289.json, 视频生成/文生视频/双采样V2版本｜MinimaxH3拳打LTX脚踢WAN三模生成_2092580801660674049.json, 视频生成/文生视频/双采样V2版｜MinimaxH3文生图生视频全能高速生成_2089771004057972737.json, 视频生成/文生视频/双采样V2版｜MinimaxH3文生图生视频角色表演_2091658421383815170.json, 视频生成/文生视频/双采样高清提速V2｜MinimaxH3音画同步角色表演_2091828773837697025.json, 视频生成/文生视频/拳打LTX脚踢WAN三模｜MinimaxH3双采样V2版本生成_2092698320908152834.json, 视频生成/文生视频/拳打LTX脚踢WAN｜MinimaxH3双采样V2版本生成_2092333106131980289.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_45

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（视频生成/文生视频/Minimax双采全功能视频工作流｜文生视频图生视频视频生视频三合一_2088696202564038657.json、视频生成/文生视频/h3 4步二采视频生成 文生视频加速高质量出片_2094239404528324609.json、视频生成/文生视频/h3 8步二采视频生成 文生视频二采加速放大出片_2094240878670995457.json、视频生成/文生视频/h3 8步单采视频替换生成 文生视频快速高质量出片_2094226586693357570.json、视频生成/文生视频/h3八步二采视频｜文生图生视频生视频三模输出_2094358128707063810.json…）

- **类型**：Text To Image
- **样本数**：17
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 17 个 workflow 都包含：
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
- `MiniMaxH3Unified`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 15/17 个有
- `MiniMaxH3AVDecodeT8` —— 15/17 个有
- `ModelAttentionBackend` —— 15/17 个有
- `ModelPreviewOverrideKJ` —— 15/17 个有
- `H3SigmaRefiner` —— 13/17 个有
- `LTXVConcatAVLatent` —— 11/17 个有
- `LTXVSeparateAVLatent` —— 11/17 个有
- `SplitSigmas` —— 11/17 个有
- `MiniMaxH3SigmaShift` —— 10/17 个有
- `MinimaxH3LatentUpscaler3D` —— 9/17 个有
- `Fast Groups Bypasser (rgthree)` —— 8/17 个有
- `SolAttnMiniMax` —— 6/17 个有
- `Label (rgthree)` —— 3/17 个有
- `ImageResizeKJv2` —— 2/17 个有
- `LoadImage` —— 2/17 个有
- `MinimaxH3LatentUpscalerNode3D` —— 2/17 个有
- `PT_H3ConcatAVLatent` —— 2/17 个有
- `PathchSageAttentionKJ` —— 2/17 个有
- `PrimitiveFloat` —— 2/17 个有
- `PrimitiveStringMultiline` —— 2/17 个有
- `VAEDecodeAudio` —— 2/17 个有
- `VAEEncode` —— 2/17 个有
- `easy clearCacheAll` —— 2/17 个有
- `ExtendIntermediateSigmas` —— 1/17 个有
- `MuyeTextEditOutput` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 17 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 17 | 100% |
| 采样算法 | er_sde | - | 17 | 100% |
| 调度器 | beta | - | 17 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 17 | 100% |
| 宽度 | 80 | 80 - 80 | 17 | 100% |
| 高度 | 80 | 80 - 80 | 17 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，17 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，17 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，17 个样本，一致性 100%
- 调度器 最常用 beta，17 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，17 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，17 个样本，取值集中（一致性 100%）
- 高发问题（18/17 个样本）：Steps较低可能导致细节不足

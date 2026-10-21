---
name: text_to_image_lora_sampler_clip_60
type: Text To Image
frequency: 14
level: strong
coverage: 0.918714
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, ModelPreviewOverrideKJ, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/h3 8步二采视频生成 文生视频二采加速放大出片_2094240878670995457.json, 视频生成/文生视频/h3 8步单采视频替换生成 文生视频快速高质量出片_2094226586693357570.json, 视频生成/文生视频/h3八步二采视频｜文生图生视频生视频三模输出_2094358128707063810.json, 视频生成/文生视频/h3四步二采视频｜三模加速一键生成工作流_2094356687963648002.json, 视频生成/文生视频/lightx2V加速版V3｜MinimaxH3全功能三模工作流_2092579297893642242.json, 视频生成/文生视频/二采潜空间放大极简版｜MinimaxH3文生图生视频_2091597395741204481.json, 视频生成/文生视频/全功能加速工作流V3｜MinimaxH3 lightx2V加速版_2092331681079451649.json, 视频生成/文生视频/双采样V2版本｜MinimaxH3拳打LTX脚踢WAN三模生成_2092580801660674049.json, 视频生成/文生视频/双采样V2版｜MinimaxH3文生图生视频全能高速生成_2089771004057972737.json, 视频生成/文生视频/双采样V2版｜MinimaxH3文生图生视频角色表演_2091658421383815170.json, 视频生成/文生视频/双采样高清提速V2｜MinimaxH3音画同步角色表演_2091828773837697025.json, 视频生成/文生视频/拳打LTX脚踢WAN三模｜MinimaxH3双采样V2版本生成_2092698320908152834.json, 视频生成/文生视频/拳打LTX脚踢WAN｜MinimaxH3双采样V2版本生成_2092333106131980289.json, 视频生成/文生视频/极简节点二采放大｜那颗星星MinimaxH3潜空间强化_2091769005567725569.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_60

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/文生视频/h3 8步二采视频生成 文生视频二采加速放大出片_2094240878670995457.json、视频生成/文生视频/h3 8步单采视频替换生成 文生视频快速高质量出片_2094226586693357570.json、视频生成/文生视频/h3八步二采视频｜文生图生视频生视频三模输出_2094358128707063810.json、视频生成/文生视频/h3四步二采视频｜三模加速一键生成工作流_2094356687963648002.json、视频生成/文生视频/lightx2V加速版V3｜MinimaxH3全功能三模工作流_2092579297893642242.json…）

- **类型**：Text To Image
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 14 个 workflow 都包含：
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
- `ModelPreviewOverrideKJ`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `H3SigmaRefiner` —— 13/14 个有
- `CR Text` —— 12/14 个有
- `MiniMaxH3AVDecodeT8` —— 12/14 个有
- `MiniMaxH3Unified` —— 12/14 个有
- `ModelAttentionBackend` —— 12/14 个有
- `ResolutionSelector` —— 12/14 个有
- `VHS_VideoCombine` —— 12/14 个有
- `LTXVConcatAVLatent` —— 11/14 个有
- `LTXVSeparateAVLatent` —— 11/14 个有
- `SplitSigmas` —— 11/14 个有
- `MinimaxH3LatentUpscaler3D` —— 10/14 个有
- `MiniMaxH3SigmaShift` —— 9/14 个有
- `SolAttnMiniMax` —— 8/14 个有
- `Fast Groups Bypasser (rgthree)` —— 6/14 个有
- `LoadImage` —— 3/14 个有
- `CreateVideo` —— 2/14 个有
- `GetLatentSizeAndCount` —— 2/14 个有
- `MiniMaxH3Easy` —— 2/14 个有
- `MiniMaxH3EasyModelAdapter` —— 2/14 个有
- `MiniMaxH3EasyOutput` —— 2/14 个有
- `MiniMaxH3EasySecondPassConditioning` —— 2/14 个有
- `PathchSageAttentionKJ` —— 2/14 个有
- `SaveVideo` —— 2/14 个有
- `VAEDecodeAudio` —— 2/14 个有
- `Label (rgthree)` —— 1/14 个有
- `MinimaxH3LatentUpscalerNode3D` —— 1/14 个有
- `MuyeTextEditOutput` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 14 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 14 | 100% |
| 采样算法 | er_sde | - | 14 | 100% |
| 调度器 | beta | - | 14 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |
| 宽度 | 80 | 80 - 80 | 14 | 100% |
| 高度 | 80 | 80 - 80 | 14 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，14 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，14 个样本，一致性 100%
- 调度器 最常用 beta，14 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，14 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，14 个样本，取值集中（一致性 100%）
- 高发问题（15/14 个样本）：Steps较低可能导致细节不足

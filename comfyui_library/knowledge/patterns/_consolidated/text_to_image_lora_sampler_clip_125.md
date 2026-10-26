---
name: text_to_image_lora_sampler_clip_125
type: Text To Image
frequency: 13
level: strong
coverage: 0.918846
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/h3 4步二采视频生成 文生视频加速高质量出片_2094239404528324609.json, 视频生成/文生视频/h3 8步二采视频生成 文生视频二采加速放大出片_2094240878670995457.json, 视频生成/文生视频/h3 8步单采视频替换生成 文生视频快速高质量出片_2094226586693357570.json, 视频生成/文生视频/h3八步二采视频｜文生图生视频生视频三模输出_2094358128707063810.json, 视频生成/文生视频/h3四步二采视频｜三模加速一键生成工作流_2094356687963648002.json, 视频生成/文生视频/lightx2V加速版V3｜MinimaxH3全功能三模工作流_2092579297893642242.json, 视频生成/文生视频/二采潜空间放大极简版｜MinimaxH3文生图生视频_2091597395741204481.json, 视频生成/文生视频/全功能加速工作流V3｜MinimaxH3 lightx2V加速版_2092331681079451649.json, 视频生成/文生视频/去油全模式精简流｜MINIMAXH3独立双采样生成_2095128913096822786.json, 视频生成/文生视频/双采样V2版本｜MinimaxH3拳打LTX脚踢WAN三模生成_2092580801660674049.json, 视频生成/文生视频/拳打LTX脚踢WAN三模｜MinimaxH3双采样V2版本生成_2092698320908152834.json, 视频生成/文生视频/拳打LTX脚踢WAN｜MinimaxH3双采样V2版本生成_2092333106131980289.json, 视频生成/文生视频/极简节点二采放大｜那颗星星MinimaxH3潜空间强化_2091769005567725569.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_125

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/文生视频/h3 4步二采视频生成 文生视频加速高质量出片_2094239404528324609.json、视频生成/文生视频/h3 8步二采视频生成 文生视频二采加速放大出片_2094240878670995457.json、视频生成/文生视频/h3 8步单采视频替换生成 文生视频快速高质量出片_2094226586693357570.json、视频生成/文生视频/h3八步二采视频｜文生图生视频生视频三模输出_2094358128707063810.json、视频生成/文生视频/h3四步二采视频｜三模加速一键生成工作流_2094356687963648002.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：92%

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
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `H3SigmaRefiner` —— 12/13 个有
- `ModelPreviewOverrideKJ` —— 12/13 个有
- `VHS_VideoCombine` —— 11/13 个有
- `CR Text` —— 10/13 个有
- `LTXVConcatAVLatent` —— 10/13 个有
- `LTXVSeparateAVLatent` —— 10/13 个有
- `MiniMaxH3AVDecodeT8` —— 10/13 个有
- `MiniMaxH3Unified` —— 10/13 个有
- `MinimaxH3LatentUpscaler3D` —— 10/13 个有
- `ModelAttentionBackend` —— 10/13 个有
- `ResolutionSelector` —— 10/13 个有
- `SplitSigmas` —— 10/13 个有
- `MiniMaxH3SigmaShift` —— 7/13 个有
- `Fast Groups Bypasser (rgthree)` —— 6/13 个有
- `SolAttnMiniMax` —— 5/13 个有
- `LoadImage` —— 4/13 个有
- `MiniMaxH3Easy` —— 3/13 个有
- `MiniMaxH3EasyModelAdapter` —— 3/13 个有
- `MiniMaxH3EasyOutput` —— 3/13 个有
- `MiniMaxH3EasySecondPassConditioning` —— 3/13 个有
- `VAEDecodeAudio` —— 3/13 个有
- `CreateVideo` —— 2/13 个有
- `GetLatentSizeAndCount` —— 2/13 个有
- `PathchSageAttentionKJ` —— 2/13 个有
- `SaveVideo` —— 2/13 个有
- `LoadAudio` —— 1/13 个有
- `VHS_LoadVideo` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 13 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 13 | 100% |
| 采样算法 | er_sde | - | 13 | 100% |
| 调度器 | beta | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |
| 宽度 | 80 | 80 - 80 | 13 | 100% |
| 高度 | 80 | 80 - 80 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，13 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，13 个样本，一致性 100%
- 调度器 最常用 beta，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高发问题（14/13 个样本）：Steps较低可能导致细节不足

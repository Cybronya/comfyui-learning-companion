---
name: text_to_image_video_lora_sampler_88
type: Text To Image
frequency: 9
level: strong
coverage: 0.682444
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/Fastvideo H3快速文生视频｜ComfyUI加速生成_2095222013941080065.json, 视频生成/文生视频/H3 氛围感短视频｜文生视频图生视频双双在线_2096866829003218946.json, 视频生成/文生视频/H3全能参考漫剧工作流，文生视频视频生视频图生视频方案_2107191447593246721.json, 视频生成/文生视频/H3全能参考漫剧工作流，文生视频视频生视频图生视频方案_2107333167064637441.json, 视频生成/文生视频/H3全能参考漫剧工作流，文生视频视频生视频图生视频方案_2107444165738057730.json, 视频生成/文生视频/H3全能参考漫剧工作流，文生视频视频生视频图生视频方案_2107958839365689345.json, 视频生成/文生视频/MiniMax H3多参考工作流｜全接口开放内部开发版_2095279663810695169.json, 视频生成/文生视频/六宫格生视频｜minimax h3文生图生视频生成_2093790080652627970.json, 视频生成/文生视频/六宫格生视频｜minimax h3文生图生视频直出_2093456500986568705.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_88

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/文生视频/Fastvideo H3快速文生视频｜ComfyUI加速生成_2095222013941080065.json、视频生成/文生视频/H3 氛围感短视频｜文生视频图生视频双双在线_2096866829003218946.json、视频生成/文生视频/H3全能参考漫剧工作流，文生视频视频生视频图生视频方案_2107191447593246721.json、视频生成/文生视频/H3全能参考漫剧工作流，文生视频视频生视频图生视频方案_2107333167064637441.json、视频生成/文生视频/H3全能参考漫剧工作流，文生视频视频生视频图生视频方案_2107444165738057730.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：68%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 8/9 个有
- `LoadImage` —— 8/9 个有
- `MiniMaxH3ReferenceToVideo` —— 8/9 个有
- `SetNode` —— 8/9 个有
- `ModelAttentionBackend` —— 7/9 个有
- `ModelPreviewOverrideKJ` —— 7/9 个有
- `PrimitiveStringMultiline` —— 7/9 个有
- `孤海注释` —— 7/9 个有
- `Fast Groups Bypasser (rgthree)` —— 6/9 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 6/9 个有
- `LoadAudio` —— 5/9 个有
- `ManualSigmas` —— 5/9 个有
- `BlockSparseAttention` —— 4/9 个有
- `MiniMaxH3SemanticBridgeApplyT8` —— 4/9 个有
- `MiniMaxH3SemanticBridgeConfigT8` —— 4/9 个有
- `MiniMaxH3SigmaShift` —— 4/9 个有
- `SaveImage` —— 4/9 个有
- `EmptyImage` —— 3/9 个有
- `PreviewImage` —— 3/9 个有
- `CR Prompt Text` —— 2/9 个有
- `PathchSageAttentionKJ` —— 2/9 个有
- `MiniMaxH3ImageToVideo` —— 1/9 个有
- `StringConcatenate` —— 1/9 个有
- `VHS_LoadVideo` —— 1/9 个有

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

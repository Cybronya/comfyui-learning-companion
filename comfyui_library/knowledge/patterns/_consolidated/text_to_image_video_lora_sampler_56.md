---
name: text_to_image_video_lora_sampler_56
type: Text To Image
frequency: 12
level: strong
coverage: 0.890917
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/Minimax H3多参单图版注意力再加速工作流，图生视频高效处理方案_2107945151611105282.json, 视频生成/图生视频/Minimax h3高一致性故事多分镜图处理 漫画分镜批量生成_2104667473604866050.json, 视频生成/图生视频/Minimax h3高一致性故事多分镜图处理 漫画分镜批量生成_2105069400066969601.json, 视频生成/图生视频/Minimax h3高一致性故事多分镜图处理 漫画分镜批量生成_2105401727510990850.json, 视频生成/图生视频/Seedance2.5图生视频工作流｜首尾帧4K长视频生成_2097830170391572482.json, 视频生成/图生视频/minimax_h3多参单图版注意力再加速｜批量出片提速实测有感_2111284144385908737.json, 视频生成/图生视频/三图multi_ref参考生成｜minimax h3 i2v视频_2094928789578014722.json, 视频生成/图生视频/三图参考生视频｜multi_ref_minimax_h3_i2v生成_2095108277595099138.json, 视频生成/图生视频/故事多分镜图处理工作流｜Minimax h3图生图分镜生成_2096719495321710593.json, 视频生成/图生视频/竖屏640p H3官流无lora12步 视频生成官方最佳方案_2109698060283629570.json, 视频生成/文生视频/H3 氛围感短视频｜文生视频图生视频双双在线_2096866829003218946.json, 视频生成/文生视频/氛围感短视频生成｜H3文生视频光影情绪渲染_2096675059892047874.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_56

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/Minimax H3多参单图版注意力再加速工作流，图生视频高效处理方案_2107945151611105282.json、视频生成/图生视频/Minimax h3高一致性故事多分镜图处理 漫画分镜批量生成_2104667473604866050.json、视频生成/图生视频/Minimax h3高一致性故事多分镜图处理 漫画分镜批量生成_2105069400066969601.json、视频生成/图生视频/Minimax h3高一致性故事多分镜图处理 漫画分镜批量生成_2105401727510990850.json、视频生成/图生视频/Seedance2.5图生视频工作流｜首尾帧4K长视频生成_2097830170391572482.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 12 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 10/12 个有
- `MiniMaxH3ReferenceToVideo` —— 10/12 个有
- `ModelAttentionBackend` —— 10/12 个有
- `SaveImage` —— 7/12 个有
- `ManualSigmas` —— 5/12 个有
- `ModelPreviewOverrideKJ` —— 5/12 个有
- `CreateVideo` —— 4/12 个有
- `Fast Groups Bypasser (rgthree)` —— 4/12 个有
- `GetImagesFromBatchIndexed` —— 4/12 个有
- `GetVideoComponents` —— 4/12 个有
- `MiniMaxLowVRAMAttention` —— 3/12 个有
- `PathchSageAttentionKJ` —— 3/12 个有
- `LayerUtility: PurgeVRAM V2` —— 2/12 个有
- `MiniMaxH3AudioConditioningT8` —— 2/12 个有
- `MiniMaxH3ChunkFeedForwardT8Advanced` —— 2/12 个有
- `PainterVRAM` —— 2/12 个有
- `SolAttnPatch` —— 2/12 个有
- `YK_LoadImageFromURL` —— 2/12 个有
- `BlockSparseAttention` —— 1/12 个有
- `MiniMaxChunkFeedForward` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 12 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 12 | 100% |
| 采样算法 | er_sde | - | 12 | 100% |
| 调度器 | beta | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |
| 宽度 | 80 | 80 - 80 | 12 | 100% |
| 高度 | 80 | 80 - 80 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，12 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，12 个样本，一致性 100%
- 调度器 最常用 beta，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高发问题（15/12 个样本）：Steps较低可能导致细节不足

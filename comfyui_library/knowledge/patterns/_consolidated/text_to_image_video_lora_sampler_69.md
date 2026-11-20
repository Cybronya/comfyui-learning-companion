---
name: text_to_image_video_lora_sampler_69
type: Text To Image
frequency: 12
level: strong
coverage: 0.8095
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/Minimax H3多参单图版注意力再加速工作流，图生视频高效处理方案_2107945151611105282.json, 视频生成/图生视频/Minimax H3完美人物替换 图生视频换人方案_2110363954835976194.json, 视频生成/图生视频/MinimaxH3多参音视频生成开源版（9图3视频3音频）ENGENG_2087124578177998850.json, 视频生成/图生视频/Seedance2.5图生视频工作流｜首尾帧4K长视频生成_2097830170391572482.json, 视频生成/图生视频/api竖屏540p坤坤H3官流｜图生视频轻量出片工作流_2108371168330866690.json, 视频生成/图生视频/api竖屏768p坤坤H3官流｜高清图生视频出片工作流_2108380600238428161.json, 视频生成/图生视频/minimax_h3多参单图版注意力再加速｜批量出片提速实测有感_2111284144385908737.json, 视频生成/图生视频/三图multi_ref参考生成｜minimax h3 i2v视频_2094928789578014722.json, 视频生成/图生视频/三图参考生视频｜multi_ref_minimax_h3_i2v生成_2095108277595099138.json, 视频生成/图生视频/最强单采V2加特林版，10步极速战斗特效出片_2111231473561989122.json, 视频生成/图生视频/最强单采双重显存优化 30秒直出高质量视频处理工具_2114053245072138241.json, 视频生成/图生视频/最强单采双重显存优化1.0｜画质30秒直出流省显存_2113903837118554114.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_69

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/Minimax H3多参单图版注意力再加速工作流，图生视频高效处理方案_2107945151611105282.json、视频生成/图生视频/Minimax H3完美人物替换 图生视频换人方案_2110363954835976194.json、视频生成/图生视频/MinimaxH3多参音视频生成开源版（9图3视频3音频）ENGENG_2087124578177998850.json、视频生成/图生视频/Seedance2.5图生视频工作流｜首尾帧4K长视频生成_2097830170391572482.json、视频生成/图生视频/api竖屏540p坤坤H3官流｜图生视频轻量出片工作流_2108371168330866690.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：81%

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
- `ModelAttentionBackend` —— 9/12 个有
- `ManualSigmas` —— 8/12 个有
- `ModelPreviewOverrideKJ` —— 8/12 个有
- `LoadAudio` —— 7/12 个有
- `BlockSparseAttention` —— 6/12 个有
- `SaveImage` —— 5/12 个有
- `VHS_LoadVideo` —— 5/12 个有
- `MiniMaxH3ChunkFeedForwardT8Advanced` —— 4/12 个有
- `PathchSageAttentionKJ` —— 4/12 个有
- `GetNode` —— 3/12 个有
- `MiniMaxLowVRAMAttention` —— 3/12 个有
- `PainterVRAM` —— 3/12 个有
- `SetNode` —— 3/12 个有
- `LayerUtility: PurgeVRAM V2` —— 2/12 个有
- `MiniMaxH3AudioConditioningT8` —— 2/12 个有
- `MiniMaxH3LowVRAMAttentionT8Advanced` —— 2/12 个有
- `SolAttnPatch` —— 2/12 个有
- `YK_LoadImageFromURL` —— 2/12 个有
- `CR Prompt Text` —— 1/12 个有
- `MiniMaxChunkFeedForward` —— 1/12 个有
- `PreviewAny` —— 1/12 个有
- `RH_LLMAPI_Pro_Node` —— 1/12 个有

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
| Steps较低可能导致细节不足 | 12/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，12 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，12 个样本，一致性 100%
- 调度器 最常用 beta，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高发问题（12/12 个样本）：Steps较低可能导致细节不足

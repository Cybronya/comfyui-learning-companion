---
name: text_to_image_video_lora_sampler_94
type: Text To Image
frequency: 9
level: strong
coverage: 0.754778
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, ModelAttentionBackend, ModelPreviewOverrideKJ, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3多参分镜硬控流，空间人物一致性分镜制作短剧漫剧图生视频_2103531675861995521.json, 视频生成/图生视频/MiniMax H3多参短剧批量专用90角色场景道具视频处理工具_2101729336322781185.json, 视频生成/图生视频/MiniMax H3电影质感LoRA V2 电影感文生视频图生视频处理工具_2112981849206247426.json, 视频生成/图生视频/Minimax H3多参单图版注意力再加速工作流，图生视频高效处理方案_2107945151611105282.json, 视频生成/图生视频/Minimax H3完美人物替换 图生视频换人方案_2110363954835976194.json, 视频生成/图生视频/minimax_h3多参单图版注意力再加速｜批量出片提速实测有感_2111284144385908737.json, 视频生成/图生视频/最强单采V2加特林版，10步极速战斗特效出片_2111231473561989122.json, 视频生成/图生视频/最强单采双重显存优化 30秒直出高质量视频处理工具_2114053245072138241.json, 视频生成/图生视频/最强单采双重显存优化1.0｜画质30秒直出流省显存_2113903837118554114.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_94

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3多参分镜硬控流，空间人物一致性分镜制作短剧漫剧图生视频_2103531675861995521.json、视频生成/图生视频/MiniMax H3多参短剧批量专用90角色场景道具视频处理工具_2101729336322781185.json、视频生成/图生视频/MiniMax H3电影质感LoRA V2 电影感文生视频图生视频处理工具_2112981849206247426.json、视频生成/图生视频/Minimax H3多参单图版注意力再加速工作流，图生视频高效处理方案_2107945151611105282.json、视频生成/图生视频/Minimax H3完美人物替换 图生视频换人方案_2110363954835976194.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
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
- `LoadImage` —— 8/9 个有
- `ManualSigmas` —— 8/9 个有
- `SaveImage` —— 7/9 个有
- `BasicScheduler` —— 6/9 个有
- `LoadAudio` —— 6/9 个有
- `BlockSparseAttention` —— 5/9 个有
- `MiniMaxH3ReferenceToVideo` —— 5/9 个有
- `VHS_LoadVideo` —— 5/9 个有
- `GetNode` —— 4/9 个有
- `LayerUtility: PurgeVRAM V2` —— 4/9 个有
- `MiniMaxH3ChunkFeedForwardT8Advanced` —— 4/9 个有
- `MiniMaxLowVRAMAttention` —— 4/9 个有
- `SetNode` —— 4/9 个有
- `MiniMaxChunkFeedForward` —— 2/9 个有
- `MiniMaxH3AudioConditioningT8` —— 2/9 个有
- `MiniMaxH3LowVRAMAttentionT8Advanced` —— 2/9 个有
- `SolAttnPatch` —— 2/9 个有
- `ki_MiniMaxH3ReferenceToVideo` —— 2/9 个有
- `CR Prompt Text` —— 1/9 个有
- `ExtendIntermediateSigmas` —— 1/9 个有
- `MiniMaxH3TurboSampler` —— 1/9 个有
- `PathchSageAttentionKJ` —— 1/9 个有
- `PreviewAny` —— 1/9 个有
- `PreviewImage` —— 1/9 个有
- `RH_LLMAPI_Pro_Node` —— 1/9 个有
- `ki_宫格拼图高阶版` —— 1/9 个有

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
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足

---
name: text_to_image_lora_sampler_clip_514
type: Text To Image
frequency: 4
level: strong
coverage: 0.71275
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, ModelAttentionBackend, ModelPreviewOverrideKJ, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3多参分镜硬控流，空间人物一致性分镜制作短剧漫剧图生视频_2103531675861995521.json, 视频生成/图生视频/MiniMax H3多参短剧批量专用90角色场景道具视频处理工具_2101729336322781185.json, 视频生成/图生视频/MiniMax H3电影质感LoRA V2 电影感文生视频图生视频处理工具_2112981849206247426.json, 视频生成/图生视频/MiniMax-H3高速大动态，无劣化抗形变模糊文生视频_2111233041338298369.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_514

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3多参分镜硬控流，空间人物一致性分镜制作短剧漫剧图生视频_2103531675861995521.json、视频生成/图生视频/MiniMax H3多参短剧批量专用90角色场景道具视频处理工具_2101729336322781185.json、视频生成/图生视频/MiniMax H3电影质感LoRA V2 电影感文生视频图生视频处理工具_2112981849206247426.json、视频生成/图生视频/MiniMax-H3高速大动态，无劣化抗形变模糊文生视频_2111233041338298369.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：71%

## 共有节点

全部 4 个 workflow 都包含：
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
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 3/4 个有
- `LoadImage` —— 3/4 个有
- `ManualSigmas` —— 3/4 个有
- `MiniMaxChunkFeedForward` —— 3/4 个有
- `MiniMaxLowVRAMAttention` —— 3/4 个有
- `VHS_VideoCombine` —— 3/4 个有
- `BasicScheduler` —— 2/4 个有
- `BlockSparseAttention` —— 2/4 个有
- `GetNode` —— 2/4 个有
- `LayerUtility: PurgeVRAM V2` —— 2/4 个有
- `MiniMaxH3ReferenceToVideo` —— 2/4 个有
- `SetNode` —— 2/4 个有
- `VHS_LoadVideo` —— 2/4 个有
- `ki_MiniMaxH3ReferenceToVideo` —— 2/4 个有
- `CreateVideo` —— 1/4 个有
- `ExtendIntermediateSigmas` —— 1/4 个有
- `Fast Bypasser (rgthree)` —— 1/4 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/4 个有
- `MiniMaxH3SemanticBridgeApplyT8` —— 1/4 个有
- `MiniMaxH3SemanticBridgeConfigT8` —— 1/4 个有
- `MiniMaxH3SigmaShift` —— 1/4 个有
- `MiniMaxH3TurboSampler` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `PrimitiveBoolean` —— 1/4 个有
- `SaveVideo` —— 1/4 个有
- `SplitSigmas` —— 1/4 个有
- `VRAM_Debug` —— 1/4 个有
- `easy ifElse` —— 1/4 个有
- `ki_宫格拼图高阶版` —— 1/4 个有
- `布尔孤海` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足

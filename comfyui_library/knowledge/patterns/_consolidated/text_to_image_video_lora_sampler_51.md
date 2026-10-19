---
name: text_to_image_video_lora_sampler_51
type: Text To Image
frequency: 13
level: strong
coverage: 0.899077
common_nodes: [CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3多参分镜硬控流，空间人物一致性分镜制作短剧漫剧图生视频_2103531675861995521.json, 视频生成/图生视频/MiniMax H3多参短剧批量专用90角色场景道具视频处理工具_2101729336322781185.json, 视频生成/图生视频/MiniMax H3超燃角色PV制作｜人物特效美少女_2095264146601365505.json, 视频生成/图生视频/Minimax H3 高动态打斗模型｜更稳更有冲击力_2096914596027260929.json, 视频生成/图生视频/Minimax H3三图参考无参考音｜图生视频多图参考_2089732304192237570.json, 视频生成/图生视频/Minimax H3多参单图版注意力再加速工作流，图生视频高效处理方案_2107945151611105282.json, 视频生成/图生视频/minimax_h3多参单图版注意力再加速｜批量出片提速实测有感_2111284144385908737.json, 视频生成/图生视频/双图参考+1参考音｜Minimax H3批量管理系统api用_2094010898447945730.json, 视频生成/图生视频/双图参考+2参考音｜Minimax H3音画同参图生视频生成_2089444909353889793.json, 视频生成/图生视频/双图参考加参考音｜Minimax H3批量管理系统API版_2093778584715481089.json, 视频生成/文生视频/H3多图参考加速工作流 单采不油腻不破音_2099563905008889858.json, 视频生成/文生视频/MiniMax H3多图参考加速工作流 单采不油腻不破音_2099185147278090242.json, 视频生成/文生视频/Minimax_H3多图参考加速版｜文图视频都能喂，出视频又快又稳_2099527126897745922.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_51

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3多参分镜硬控流，空间人物一致性分镜制作短剧漫剧图生视频_2103531675861995521.json、视频生成/图生视频/MiniMax H3多参短剧批量专用90角色场景道具视频处理工具_2101729336322781185.json、视频生成/图生视频/MiniMax H3超燃角色PV制作｜人物特效美少女_2095264146601365505.json、视频生成/图生视频/Minimax H3 高动态打斗模型｜更稳更有冲击力_2096914596027260929.json、视频生成/图生视频/Minimax H3三图参考无参考音｜图生视频多图参考_2089732304192237570.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
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
- `LoadImage` —— 12/13 个有
- `BasicScheduler` —— 11/13 个有
- `BasicGuider` —— 10/13 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 9/13 个有
- `MiniMaxH3ReferenceToVideo` —— 9/13 个有
- `MiniMaxH3SigmaShift` —— 9/13 个有
- `ModelAttentionBackend` —— 9/13 个有
- `LoadAudio` —— 7/13 个有
- `ModelPreviewOverrideKJ` —— 6/13 个有
- `SaveImage` —— 5/13 个有
- `SolAttnPatch` —— 5/13 个有
- `INTConstant` —— 4/13 个有
- `LayerUtility: PurgeVRAM V2` —— 4/13 个有
- `MiniMaxH3TurboSampler` —— 4/13 个有
- `MiniMaxLowVRAMAttention` —— 4/13 个有
- `CFGGuider` —— 3/13 个有
- `ConditioningZeroOut` —— 3/13 个有
- `H3AudioRefineSampler` —— 3/13 个有
- `H3FrozenVideoCache` —— 3/13 个有
- `ManualSigmas` —— 3/13 个有
- `MiniMaxChunkFeedForward` —— 2/13 个有
- `MiniMaxH3AudioConditioningT8` —— 2/13 个有
- `MiniMaxH3ChunkFeedForwardT8Advanced` —— 2/13 个有
- `ki_MiniMaxH3ReferenceToVideo` —— 2/13 个有
- `ExtendIntermediateSigmas` —— 1/13 个有
- `PathchSageAttentionKJ` —— 1/13 个有
- `PreviewImage` —— 1/13 个有
- `ki_宫格拼图高阶版` —— 1/13 个有

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
| Steps较低可能导致细节不足 | 13/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，13 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，13 个样本，一致性 100%
- 调度器 最常用 beta，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高发问题（13/13 个样本）：Steps较低可能导致细节不足

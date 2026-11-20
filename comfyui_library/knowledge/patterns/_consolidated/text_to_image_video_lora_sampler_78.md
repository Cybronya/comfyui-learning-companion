---
name: text_to_image_video_lora_sampler_78
type: Text To Image
frequency: 10
level: strong
coverage: 0.7756
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, CR Text, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3Unified, MiniMaxLowVRAMAttention, ModelAttentionBackend, ModelPreviewOverrideKJ, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3导演台多模 4K直出视频生成处理工具_2113399209385881601.json, 视频生成/图生视频/MiniMax H3文生视频直出4K超清画质，LoRA去油化+统一插件+渐进式采样一步到位_2114405475897921537.json, 视频生成/图生视频/Minimax H3直出4K去油化LoRA｜统一插件自提升渐进式采样工作流_2114163521184423938.json, 视频生成/图生视频/MinimaxH3自定义sigma参数工作流，文生视频视频生视频全能_2110448826346729474.json, 视频生成/图生视频/MinimaxH3超快数字人 数字人口播方案_2109739061270368258.json, 视频生成/文生视频/1002海螺H3三采极致高分辨率｜最长20秒放大到4K出片_2106269806440837121.json, 视频生成/文生视频/MiniMax H3单采双采视频生成处理工作流_2101002133435928578.json, 视频生成/文生视频/文戏不油三采极致高分辨率工作流，文生视频视频生视频图生视频方案_2105713741986881538.json, 视频生成/文生视频/文戏不油腻｜三采极致高分辨率工作流 让文生视频画质再上一层楼_2105476192806723585.json, 视频生成/文生视频/海螺H3三采极致高分辨率工作流最长20秒放大到4K，文生视频图生视频_2106458890740260866.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_78

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3导演台多模 4K直出视频生成处理工具_2113399209385881601.json、视频生成/图生视频/MiniMax H3文生视频直出4K超清画质，LoRA去油化+统一插件+渐进式采样一步到位_2114405475897921537.json、视频生成/图生视频/Minimax H3直出4K去油化LoRA｜统一插件自提升渐进式采样工作流_2114163521184423938.json、视频生成/图生视频/MinimaxH3自定义sigma参数工作流，文生视频视频生视频全能_2110448826346729474.json、视频生成/图生视频/MinimaxH3超快数字人 数字人口播方案_2109739061270368258.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3Unified`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
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
- `ConditioningZeroOut` —— 9/10 个有
- `Fast Groups Bypasser (rgthree)` —— 9/10 个有
- `H3SigmaRefiner` —— 9/10 个有
- `PreviewImage` —— 9/10 个有
- `VAEDecodeAudio` —— 9/10 个有
- `VHS_SelectImages` —— 9/10 个有
- `Any Switch (rgthree)` —— 8/10 个有
- `Fast Muter (rgthree)` —— 8/10 个有
- `GetNode` —— 8/10 个有
- `MemoryCleaner` —— 8/10 个有
- `RH_DLSS5Enhance` —— 8/10 个有
- `SelfLiftH3Sampler` —— 8/10 个有
- `SetNode` —— 8/10 个有
- `SaveImage` —— 7/10 个有
- `FlashVSRInitPipe` —— 5/10 个有
- `FlashVSRNodeAdv` —— 5/10 个有
- `INTConstant` —— 5/10 个有
- `LTXVSeparateAVLatent` —— 5/10 个有
- `MiniMaxH3VAEDecodeFast` —— 5/10 个有
- `VOSR2ModelLoader` —— 5/10 个有
- `VOSR2Upscale` —— 5/10 个有
- `BlockSparseAttention` —— 1/10 个有
- `ManualSigmas` —— 1/10 个有
- `MiniMaxH3AVDecodeT8` —— 1/10 个有
- `SelfLiftAvatarH3Sampler` —— 1/10 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 10 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 10 | 100% |
| 采样算法 | er_sde | - | 10 | 100% |
| 调度器 | beta | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| 宽度 | 80 | 80 - 80 | 10 | 100% |
| 高度 | 80 | 80 - 80 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足

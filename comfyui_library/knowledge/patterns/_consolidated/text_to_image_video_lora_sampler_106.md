---
name: text_to_image_video_lora_sampler_106
type: Text To Image
frequency: 7
level: strong
coverage: 0.780286
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, CR Text, ConditioningZeroOut, EmptyLatentImage, Fast Groups Bypasser (rgthree), H3SigmaRefiner, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3Unified, MiniMaxLowVRAMAttention, ModelAttentionBackend, ModelPreviewOverrideKJ, PreviewImage, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_SelectImages, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MinimaxH3超快数字人 数字人口播方案_2109739061270368258.json, 视频生成/文生视频/1002海螺H3三采极致高分辨率｜最长20秒放大到4K出片_2106269806440837121.json, 视频生成/文生视频/MiniMax H3单采双采视频生成处理工作流_2101002133435928578.json, 视频生成/文生视频/minimaxH3单采双采工作流｜文生视频图生视频样样通_2100759046625259522.json, 视频生成/文生视频/文戏不油三采极致高分辨率工作流，文生视频视频生视频图生视频方案_2105713741986881538.json, 视频生成/文生视频/文戏不油腻｜三采极致高分辨率工作流 让文生视频画质再上一层楼_2105476192806723585.json, 视频生成/文生视频/海螺H3三采极致高分辨率工作流最长20秒放大到4K，文生视频图生视频_2106458890740260866.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_106

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/MinimaxH3超快数字人 数字人口播方案_2109739061270368258.json、视频生成/文生视频/1002海螺H3三采极致高分辨率｜最长20秒放大到4K出片_2106269806440837121.json、视频生成/文生视频/MiniMax H3单采双采视频生成处理工作流_2101002133435928578.json、视频生成/文生视频/minimaxH3单采双采工作流｜文生视频图生视频样样通_2100759046625259522.json、视频生成/文生视频/文戏不油三采极致高分辨率工作流，文生视频视频生视频图生视频方案_2105713741986881538.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `H3SigmaRefiner`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3Unified`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PreviewImage`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_SelectImages`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `SelfLiftH3Sampler` —— 6/7 个有
- `VAEDecodeAudio` —— 6/7 个有
- `Any Switch (rgthree)` —— 5/7 个有
- `Fast Muter (rgthree)` —— 5/7 个有
- `FlashVSRInitPipe` —— 5/7 个有
- `FlashVSRNodeAdv` —— 5/7 个有
- `GetNode` —— 5/7 个有
- `INTConstant` —— 5/7 个有
- `LTXVSeparateAVLatent` —— 5/7 个有
- `MemoryCleaner` —— 5/7 个有
- `MiniMaxH3VAEDecodeFast` —— 5/7 个有
- `RH_DLSS5Enhance` —— 5/7 个有
- `SetNode` —— 5/7 个有
- `VOSR2ModelLoader` —— 5/7 个有
- `VOSR2Upscale` —— 5/7 个有
- `SaveImage` —— 4/7 个有
- `MiniMaxH3AVDecodeT8` —— 2/7 个有
- `SelfLiftAvatarH3Sampler` —— 1/7 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足

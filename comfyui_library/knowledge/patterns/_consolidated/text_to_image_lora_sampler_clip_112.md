---
name: text_to_image_lora_sampler_clip_112
type: Text To Image
frequency: 10
level: strong
coverage: 0.7737
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3ImageToVideo, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MinimaxH3图生视频指定音乐-高清视频生成工作流_2087398733066625026.json, 视频生成/图生视频/MinimaxH3海螺4步lightx2v加速lora-多重提速转场运镜图生视频_2087374035620556802.json, 视频生成/图生视频/T2V文生视频加速流AITUDOU MiniMax H3图生视频工作流_2088399160956510209.json, 视频生成/图生视频/T2V文生视频加速流｜AITUDOU-MiniMax H3图生视频工作流_2088378615552634882.json, 视频生成/图生视频/i2v加速版直出｜Minimax H3文生图生视频场景特效_2092740361742536706.json, 视频生成/图生视频/minimaxH3开源版首尾帧｜8step加速图生视频_2095261239302774785.json, 视频生成/文生视频/2108095483951538177.json, 视频生成/文生视频/MiniMax h3 4步lora2加速版｜文生图生视频直出_2092366496205987842.json, 视频生成/文生视频/人物角色文生视频｜MiniMax+H3角色设计一键生成_2094312279473999874.json, 视频生成/文生视频/开源文生视频｜MiniMax-H3战斗特效角色设计生成_2094797659730169857.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_112

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/MinimaxH3图生视频指定音乐-高清视频生成工作流_2087398733066625026.json、视频生成/图生视频/MinimaxH3海螺4步lightx2v加速lora-多重提速转场运镜图生视频_2087374035620556802.json、视频生成/图生视频/T2V文生视频加速流AITUDOU MiniMax H3图生视频工作流_2088399160956510209.json、视频生成/图生视频/T2V文生视频加速流｜AITUDOU-MiniMax H3图生视频工作流_2088378615552634882.json、视频生成/图生视频/i2v加速版直出｜Minimax H3文生图生视频场景特效_2092740361742536706.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 10 个 workflow 都包含：
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
- `MiniMaxH3ImageToVideo`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 9/10 个有
- `LoadImage` —— 6/10 个有
- `Text` —— 6/10 个有
- `VHS_VideoCombine` —— 6/10 个有
- `GetNode` —— 5/10 个有
- `SetNode` —— 5/10 个有
- `CreateVideo` —— 4/10 个有
- `ModelAttentionBackend` —— 4/10 个有
- `SaveVideo` —— 4/10 个有
- `VHS_LoadVideoFFmpeg` —— 2/10 个有
- `1hew_AudioDuration` —— 1/10 个有
- `AudioMerge` —— 1/10 个有
- `Bjornulf_ShowFloat` —— 1/10 个有
- `Fast Groups Bypasser (rgthree)` —— 1/10 个有
- `Label (rgthree)` —— 1/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/10 个有
- `LoadVideoUI` —— 1/10 个有
- `MiniMaxH3BlockCacheT8` —— 1/10 个有
- `RHHiddenNodes` —— 1/10 个有
- `SaveVideoRGBA` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 10 | 100% |
| 高度 | 80 | 80 - 80 | 10 | 100% |
| 采样步数 | 4 | 4 - 4 | 10 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 10 | 100% |
| 采样算法 | er_sde | - | 10 | 100% |
| 调度器 | beta | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足

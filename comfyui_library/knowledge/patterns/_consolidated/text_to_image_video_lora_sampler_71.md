---
name: text_to_image_video_lora_sampler_71
type: Text To Image
frequency: 10
level: strong
coverage: 0.8315
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, Text, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MinimaxH3图生视频指定音乐-高清视频生成工作流_2087398733066625026.json, 视频生成/图生视频/T2V文生视频加速流AITUDOU MiniMax H3图生视频工作流_2088399160956510209.json, 视频生成/图生视频/T2V文生视频加速流｜AITUDOU-MiniMax H3图生视频工作流_2088378615552634882.json, 视频生成/图生视频/T2首尾帧官方指南｜MInimaxH3提示词自动扩写生成_2094777866826371074.json, 视频生成/图生视频/T3官方指南首尾帧｜MInimaxH3提示词自动扩写分镜_2095062492773961730.json, 视频生成/图生视频/T7官方指南首尾帧｜MInimaxH3提示词自动扩写分镜出图_2094772557869309953.json, 视频生成/图生视频/T8全参官方指南｜minimaxh3扩展提示词角色一致性生视频_2094463893199482882.json, 视频生成/图生视频/官方提示词指南自动扩写T1｜MInimaxH3首尾帧图生视频_2095791903588569089.json, 视频生成/图生视频/提示词指南自动扩写T7｜MinimaxH3首尾帧分镜出图_2091166611460939778.json, 视频生成/图生视频/美好的夏天｜图生视频把夏日照片变成会动的回忆短片_2097543142554820609.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_71

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/MinimaxH3图生视频指定音乐-高清视频生成工作流_2087398733066625026.json、视频生成/图生视频/T2V文生视频加速流AITUDOU MiniMax H3图生视频工作流_2088399160956510209.json、视频生成/图生视频/T2V文生视频加速流｜AITUDOU-MiniMax H3图生视频工作流_2088378615552634882.json、视频生成/图生视频/T2首尾帧官方指南｜MInimaxH3提示词自动扩写生成_2094777866826371074.json、视频生成/图生视频/T3官方指南首尾帧｜MInimaxH3提示词自动扩写分镜_2095062492773961730.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：83%

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
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3ImageToVideo` —— 9/10 个有
- `LoadImage` —— 8/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/10 个有
- `RHHiddenNodes` —— 7/10 个有
- `easy showAnything` —— 6/10 个有
- `ImageResizeKJv2` —— 5/10 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/10 个有
- `ResolutionSelector` —— 3/10 个有
- `GetNode` —— 2/10 个有
- `MiniMaxH3BlockCacheT8` —— 2/10 个有
- `RH_Captioner` —— 2/10 个有
- `SetNode` —— 2/10 个有
- `1hew_AudioDuration` —— 1/10 个有
- `AudioMerge` —— 1/10 个有
- `Bjornulf_ShowFloat` —— 1/10 个有
- `ImageConcatenateMulti_UTK` —— 1/10 个有
- `LoadVideoUI` —— 1/10 个有
- `PreviewImage` —— 1/10 个有
- `SaveVideoRGBA` —— 1/10 个有
- `TextConcatenate_UTK` —— 1/10 个有
- `easy MiniMaxH3ReferenceToVideoBridge` —— 1/10 个有

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

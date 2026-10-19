---
name: text_to_image_video_lora_sampler_31
type: Text To Image
frequency: 17
level: strong
coverage: 0.803
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3ImageToVideo, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, Text, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MinimaxH3图生视频指定音乐-高清视频生成工作流_2087398733066625026.json, 视频生成/图生视频/T2V文生视频加速流AITUDOU MiniMax H3图生视频工作流_2088399160956510209.json, 视频生成/图生视频/T2V文生视频加速流｜AITUDOU-MiniMax H3图生视频工作流_2088378615552634882.json, 视频生成/图生视频/T2首尾帧官方指南｜MInimaxH3提示词自动扩写生成_2094777866826371074.json, 视频生成/图生视频/T3官方指南首尾帧｜MInimaxH3提示词自动扩写分镜_2095062492773961730.json, 视频生成/图生视频/T7官方指南首尾帧｜MInimaxH3提示词自动扩写分镜出图_2094772557869309953.json, 视频生成/图生视频/T8官方指南首尾帧｜MInimaxH3提示词自动扩写出图_2095070966761213953.json, 视频生成/图生视频/人物微表情变化｜图生视频捕捉眨眼抿嘴 细节拉满_2097850526296797185.json, 视频生成/图生视频/人物表情变化动作生成｜图生视频形象动态演绎工作流_2097536720039399426.json, 视频生成/图生视频/人物表情变化动作｜图生视频让静态人像笑起来动起来_2097522798133596161.json, 视频生成/图生视频/官方提示词指南自动扩写T1｜MInimaxH3首尾帧图生视频_2095791903588569089.json, 视频生成/图生视频/提示词指南自动扩写T7｜MinimaxH3首尾帧分镜出图_2091166611460939778.json, 视频生成/图生视频/美好的夏天｜图生视频把夏日照片变成会动的回忆短片_2097543142554820609.json, 视频生成/文生视频/2108095483951538177.json, 视频生成/文生视频/人物角色文生视频｜MiniMax+H3角色设计一键生成_2094312279473999874.json, 视频生成/文生视频/开源文生视频｜MiniMax-H3战斗特效角色设计生成_2094797659730169857.json, 视频生成/文生视频/文生视频 MiniMax H3 可设时长分辨率比例快速出片_2094174814998192130.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_31

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（视频生成/图生视频/MinimaxH3图生视频指定音乐-高清视频生成工作流_2087398733066625026.json、视频生成/图生视频/T2V文生视频加速流AITUDOU MiniMax H3图生视频工作流_2088399160956510209.json、视频生成/图生视频/T2V文生视频加速流｜AITUDOU-MiniMax H3图生视频工作流_2088378615552634882.json、视频生成/图生视频/T2首尾帧官方指南｜MInimaxH3提示词自动扩写生成_2094777866826371074.json、视频生成/图生视频/T3官方指南首尾帧｜MInimaxH3提示词自动扩写分镜_2095062492773961730.json…）

- **类型**：Text To Image
- **样本数**：17
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 17 个 workflow 都包含：
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
- `LoadImage` —— 12/17 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 11/17 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 11/17 个有
- `easy showAnything` —— 10/17 个有
- `RHHiddenNodes` —— 7/17 个有
- `GetNode` —— 6/17 个有
- `ImageResizeKJv2` —— 6/17 个有
- `ResolutionSelector` —— 6/17 个有
- `SetNode` —— 6/17 个有
- `MiniMaxH3BlockCacheT8` —— 5/17 个有
- `RH_Captioner` —— 5/17 个有
- `ModelAttentionBackend` —— 4/17 个有
- `TextConcatenate_UTK` —— 4/17 个有
- `VHS_LoadVideoFFmpeg` —— 3/17 个有
- `1hew_AudioDuration` —— 1/17 个有
- `AudioMerge` —— 1/17 个有
- `Bjornulf_ShowFloat` —— 1/17 个有
- `LoadVideoUI` —— 1/17 个有
- `SaveImage` —— 1/17 个有
- `SaveVideoRGBA` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 17 | 100% |
| 高度 | 80 | 80 - 80 | 17 | 100% |
| 采样步数 | 4 | 4 - 4 | 17 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 17 | 100% |
| 采样算法 | er_sde | - | 17 | 100% |
| 调度器 | beta | - | 17 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 17 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，17 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，17 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，17 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，17 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，17 个样本，一致性 100%
- 调度器 最常用 beta，17 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 高发问题（17/17 个样本）：Steps较低可能导致细节不足

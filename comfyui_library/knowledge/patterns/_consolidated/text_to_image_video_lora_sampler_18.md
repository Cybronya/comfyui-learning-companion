---
name: text_to_image_video_lora_sampler_18
type: Text To Image
frequency: 23
level: strong
coverage: 0.877087
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: [LayerUtility: ImageScaleByAspectRatio V2]
members: [视频生成/图生视频/I2V lora加速｜MiniMax H3首帧图生视频3分40秒_2091174539307872258.json, 视频生成/图生视频/MInimaxH3首尾帧T3指南｜官方提示词自动扩写，分镜出图更对味_2099427468598923266.json, 视频生成/图生视频/MInimaxH3首尾帧官方提示词指南T7版｜自动扩写保角色一致性｜分镜出图_2099115888204140545.json, 视频生成/图生视频/MInimaxH3首尾帧官方提示词指南T8升级版｜自动扩写分镜一致出片_2099117086592290817.json, 视频生成/图生视频/MInimaxH3首尾帧官方提示词指南_自动扩写T2分镜更稳_2106263717989150721.json, 视频生成/图生视频/MInimaxH3首尾帧官方提示词指南自动扩写_2086206535667109889.json, 视频生成/图生视频/MInimaxH3首尾帧官方提示词指南｜自动扩写T3分镜出图_2106974045374869506.json, 视频生成/图生视频/MiniMax H3 I2V图生视频｜Fused ACC八步极速出片_2097147575894888449.json, 视频生成/图生视频/MiniMax H3首尾帧参考生成 官方提示词自动扩写T2_2098110557789446146.json, 视频生成/图生视频/MiniMaxH3首尾帧提示词指南T7｜自动扩写分镜出图_2094493855881187329.json, 视频生成/图生视频/MiniMaxH3首尾帧自动扩写｜官方提示词指南T1_2095564089794846721.json, 视频生成/图生视频/Minimax h3超级加速多图参考生视频 快速出片方案_2109357930280734721.json, 视频生成/图生视频/T2首尾帧官方指南｜MInimaxH3提示词自动扩写生成_2094777866826371074.json, 视频生成/图生视频/T3官方指南首尾帧｜MInimaxH3提示词自动扩写分镜_2095062492773961730.json, 视频生成/图生视频/T7官方指南首尾帧｜MInimaxH3提示词自动扩写分镜出图_2094772557869309953.json, 视频生成/图生视频/T8官方指南首尾帧｜MInimaxH3提示词自动扩写出图_2095070966761213953.json, 视频生成/图生视频/人物微表情变化｜图生视频捕捉眨眼抿嘴 细节拉满_2097850526296797185.json, 视频生成/图生视频/人物表情变化动作生成｜图生视频形象动态演绎工作流_2097536720039399426.json, 视频生成/图生视频/人物表情变化动作｜图生视频让静态人像笑起来动起来_2097522798133596161.json, 视频生成/图生视频/古装美女扮相图生视频｜古风人像一键动起来_2098703419811909633.json, 视频生成/图生视频/官方提示词指南自动扩写T1｜MInimaxH3首尾帧图生视频_2095791903588569089.json, 视频生成/图生视频/提示词指南自动扩写T7｜MinimaxH3首尾帧分镜出图_2091166611460939778.json, 视频生成/图生视频/美好的夏天｜图生视频把夏日照片变成会动的回忆短片_2097543142554820609.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_18

> 由 `engine/knowledge_consolidation` 从 23 个 workflow 归纳得出（视频生成/图生视频/I2V lora加速｜MiniMax H3首帧图生视频3分40秒_2091174539307872258.json、视频生成/图生视频/MInimaxH3首尾帧T3指南｜官方提示词自动扩写，分镜出图更对味_2099427468598923266.json、视频生成/图生视频/MInimaxH3首尾帧官方提示词指南T7版｜自动扩写保角色一致性｜分镜出图_2099115888204140545.json、视频生成/图生视频/MInimaxH3首尾帧官方提示词指南T8升级版｜自动扩写分镜一致出片_2099117086592290817.json、视频生成/图生视频/MInimaxH3首尾帧官方提示词指南_自动扩写T2分镜更稳_2106263717989150721.json…）

- **类型**：Text To Image
- **样本数**：23
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 23 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
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
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3ImageToVideo` —— 22/23 个有
- `Text` —— 21/23 个有
- `easy showAnything` —— 20/23 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 19/23 个有
- `ImageResizeKJv2` —— 15/23 个有
- `RHHiddenNodes` —— 14/23 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 8/23 个有
- `RH_Captioner` —— 8/23 个有
- `TextConcatenate_UTK` —— 6/23 个有
- `MiniMaxH3BlockCacheT8` —— 4/23 个有
- `ResolutionSelector` —— 3/23 个有
- `SaveImage` —— 3/23 个有
- `PrimitiveStringMultiline` —— 2/23 个有
- `EnhancedLoadDiffusionModel` —— 1/23 个有
- `GetNode` —— 1/23 个有
- `LoraLoaderBypassModelOnly` —— 1/23 个有
- `MiniMaxChunkFeedForward` —— 1/23 个有
- `MiniMaxH3ReferenceToVideo` —— 1/23 个有
- `MiniMaxLowVRAMAttention` —— 1/23 个有
- `PainterVRAM` —— 1/23 个有
- `SetNode` —— 1/23 个有
- `SolAttnPatch` —— 1/23 个有
- `ZNGB_ResizeImage` —— 1/23 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 23 | 100% |
| 高度 | 80 | 80 - 80 | 23 | 100% |
| 采样步数 | 4 | 4 - 4 | 23 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 23 | 100% |
| 采样算法 | er_sde | - | 23 | 100% |
| 调度器 | beta | - | 23 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 23 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 23/23 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，23 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，23 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，23 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，23 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，23 个样本，一致性 100%
- 调度器 最常用 beta，23 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，23 个样本，取值集中（一致性 100%）
- 高发问题（23/23 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2

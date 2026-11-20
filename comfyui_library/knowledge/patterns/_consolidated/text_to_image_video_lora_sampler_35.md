---
name: text_to_image_video_lora_sampler_35
type: Text To Image
frequency: 18
level: strong
coverage: 0.856667
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ImageToVideo, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/H3首尾帧官方提示词指南自动扩写 角色一致性分镜生成_2098819339918073857.json, 视频生成/图生视频/H3首尾帧官方提示词指南自动扩写 角色一致性分镜生成_2098820909527293953.json, 视频生成/图生视频/H3首尾帧官方提示词指南自动扩写 角色一致性分镜生成_2099181667595407361.json, 视频生成/图生视频/H3首尾帧官方提示词指南自动扩写 角色一致性分镜生成_2099549898831126529.json, 视频生成/图生视频/I2V lora加速｜MiniMax H3首帧图生视频3分40秒_2091174539307872258.json, 视频生成/图生视频/MInimaxH3首尾帧T3指南｜官方提示词自动扩写，分镜出图更对味_2099427468598923266.json, 视频生成/图生视频/MInimaxH3首尾帧官方提示词指南T7版｜自动扩写保角色一致性｜分镜出图_2099115888204140545.json, 视频生成/图生视频/MInimaxH3首尾帧官方提示词指南T8升级版｜自动扩写分镜一致出片_2099117086592290817.json, 视频生成/图生视频/MInimaxH3首尾帧官方提示词指南自动扩写_2086206535667109889.json, 视频生成/图生视频/MInimaxH3首尾帧官方提示词指南｜自动扩写T2分镜更稳_2106263717989150721.json, 视频生成/图生视频/MInimaxH3首尾帧官方提示词指南｜自动扩写T3分镜出图_2106974045374869506.json, 视频生成/图生视频/MiniMax H3 I2V图生视频｜Fused ACC八步极速出片_2097147575894888449.json, 视频生成/图生视频/MiniMax H3图生视频fastH3基础版 trim加速快速直出_2110253662495928321.json, 视频生成/图生视频/MiniMax H3图生视频fastH3基础版 trim加速快速直出_2110368880341377026.json, 视频生成/图生视频/MiniMax H3首尾帧参考生成 官方提示词自动扩写T2_2098110557789446146.json, 视频生成/图生视频/MiniMaxH3首尾帧提示词指南T7｜自动扩写分镜出图_2094493855881187329.json, 视频生成/图生视频/MiniMaxH3首尾帧自动扩写｜官方提示词指南T1_2095564089794846721.json, 视频生成/图生视频/minimax h3 i2v fastH3 contextmotion longvideo 图生视频_2105127145923244034.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_35

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（视频生成/图生视频/H3首尾帧官方提示词指南自动扩写 角色一致性分镜生成_2098819339918073857.json、视频生成/图生视频/H3首尾帧官方提示词指南自动扩写 角色一致性分镜生成_2098820909527293953.json、视频生成/图生视频/H3首尾帧官方提示词指南自动扩写 角色一致性分镜生成_2099181667595407361.json、视频生成/图生视频/H3首尾帧官方提示词指南自动扩写 角色一致性分镜生成_2099549898831126529.json、视频生成/图生视频/I2V lora加速｜MiniMax H3首帧图生视频3分40秒_2091174539307872258.json…）

- **类型**：Text To Image
- **样本数**：18
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 18 个 workflow 都包含：
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
- `MiniMaxH3ImageToVideo`
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
- `Text` —— 14/18 个有
- `ImageResizeKJv2` —— 13/18 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 13/18 个有
- `easy showAnything` —— 13/18 个有
- `RHHiddenNodes` —— 12/18 个有
- `SaveImage` —— 8/18 个有
- `PrimitiveStringMultiline` —— 4/18 个有
- `ResolutionSelector` —— 4/18 个有
- `SetNode` —— 4/18 个有
- `BlockSparseAttention` —— 3/18 个有
- `MiniMaxH3SigmaShift` —— 3/18 个有
- `ModelAttentionBackend` —— 3/18 个有
- `GetNode` —— 2/18 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/18 个有
- `RH_Captioner` —— 2/18 个有
- `MiniMaxChunkFeedForward` —— 1/18 个有
- `MiniMaxH3MotionContext` —— 1/18 个有
- `MiniMaxH3MotionContextChain` —— 1/18 个有
- `MiniMaxH3MotionContextLoadLatent` —— 1/18 个有
- `MiniMaxH3MotionContextSaveLatent` —— 1/18 个有
- `MiniMaxH3MotionContextTrim` —— 1/18 个有
- `MiniMaxLowVRAMAttention` —— 1/18 个有
- `SolAttnPatch` —— 1/18 个有
- `TextConcatenate_UTK` —— 1/18 个有
- `ZNGB_ResizeImage` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 18 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 18 | 100% |
| 采样算法 | er_sde | - | 18 | 100% |
| 调度器 | beta | - | 18 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 18 | 100% |
| 宽度 | 80 | 80 - 80 | 18 | 100% |
| 高度 | 80 | 80 - 80 | 18 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/18 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，18 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，18 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，18 个样本，一致性 100%
- 调度器 最常用 beta，18 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，18 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，18 个样本，取值集中（一致性 100%）
- 高发问题（18/18 个样本）：Steps较低可能导致细节不足

---
name: text_to_image_video_lora_sampler_28
type: Text To Image
frequency: 16
level: strong
coverage: 0.656062
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, GetNode, ImageResizeKJv2, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy clearCacheAll, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/Lightx2v+8步加速官模｜双模型双采样单图自动反推提词_2089395917622439937.json, 视频生成/图生视频/Minimax H3二采重绘效率流｜秒变清晰不丢一致性，出片效率起飞_2099519441183789057.json, 视频生成/图生视频/MinimaxH3全能参考提示词自动反推版！ENGENG开源视频模型真神！！_2087149888927780865.json, 视频生成/图生视频/MinimaxH3双采样音频驱动数字人单人版V1.0｜图生视频数字人_2090068073612144642.json, 视频生成/图生视频/单模型无编解码二采放大｜Minimax H3全能参考自动反推提示词 13 浏览 0 点赞 0 收藏_2092299427519225857.json, 视频生成/图生视频/双采高清人脸视频生成｜Minimax自动提示词加最新加速lora_2090470050162630658.json, 视频生成/文生视频/0823修复横屏12秒｜万象+rh双模型二采放大视频_2091772010216124417.json, 视频生成/文生视频/0823修复竖屏12秒｜万象+rh双模型二采放大_2091770489449570306.json, 视频生成/文生视频/Minimax H3双模二采｜文生视频图生视频视频生视频全能出片_2088728994442203137.json, 视频生成/文生视频/万象rh双模型二采放大｜0823修复横屏12秒文生视频_2091600249746972673.json, 视频生成/文生视频/万象rh双模型二采放大｜0823修复竖屏12秒文生视频_2091598794503839745.json, 视频生成/文生视频/双模二采玩法｜Minimax H3文生图生视频再采样_2089071865905115138.json, 视频生成/文生视频/双模型二采+潜空间放大｜MinimaxH3自动提示词人脸修复视频_2090226427131154433.json, 视频生成/文生视频/双模型二采参考生视频｜万象+rh横屏16_9时长12秒_2090554080665104386.json, 视频生成/文生视频/双模型二采参考生视频｜万象+rh横屏16_9时长12秒_2090857572986343426.json, 视频生成/文生视频/双模型二采放大提示词反推｜0823修复文生视频直出_2091603200427253762.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_28

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（视频生成/图生视频/Lightx2v+8步加速官模｜双模型双采样单图自动反推提词_2089395917622439937.json、视频生成/图生视频/Minimax H3二采重绘效率流｜秒变清晰不丢一致性，出片效率起飞_2099519441183789057.json、视频生成/图生视频/MinimaxH3全能参考提示词自动反推版！ENGENG开源视频模型真神！！_2087149888927780865.json、视频生成/图生视频/MinimaxH3双采样音频驱动数字人单人版V1.0｜图生视频数字人_2090068073612144642.json、视频生成/图生视频/单模型无编解码二采放大｜Minimax H3全能参考自动反推提示词 13 浏览 0 点赞 0 收藏_2092299427519225857.json…）

- **类型**：Text To Image
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：66%

## 共有节点

全部 16 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `GetNode`
- `ImageResizeKJv2`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy clearCacheAll`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 15/16 个有
- `INTConstant` —— 15/16 个有
- `LoadAudio` —— 15/16 个有
- `ModelAttentionBackend` —— 15/16 个有
- `PrimitiveStringMultiline` —— 15/16 个有
- `VAEDecodeAudio` —— 15/16 个有
- `CreateVideo` —— 14/16 个有
- `LoraLoaderBypassModelOnly` —— 14/16 个有
- `ResizeShortestToNode` —— 14/16 个有
- `VHS_LoadVideo` —— 14/16 个有
- `孤海注释` —— 14/16 个有
- `EasyCache` —— 12/16 个有
- `LTXVConcatAVLatent` —— 9/16 个有
- `LTXVSeparateAVLatent` —— 9/16 个有
- `StringFunction|pysssss` —— 9/16 个有
- `TrimAudioDuration` —— 9/16 个有
- `easy showAnything` —— 9/16 个有
- `RHLLMChatNode` —— 8/16 个有
- `AudioCrop` —— 6/16 个有
- `Label (rgthree)` —— 6/16 个有
- `MinimaxH3LatentUpscaler3D` —— 6/16 个有
- `PT_H3ConcatAVLatent` —— 6/16 个有
- `VAEEncode` —— 6/16 个有
- `VAEEncodeAudio` —— 6/16 个有
- `LoadVideo` —— 4/16 个有
- `CR Text` —— 3/16 个有
- `GetImageRangeFromBatch` —— 3/16 个有
- `MinimaxH3LatentUpscalerNode3D` —— 3/16 个有
- `CR Text Concatenate` —— 2/16 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/16 个有
- `CR Prompt Text` —— 1/16 个有
- `ExtendIntermediateSigmas` —— 1/16 个有
- `FastGroupsBypassSwitch` —— 1/16 个有
- `H3SigmaRefiner` —— 1/16 个有
- `PathchSageAttentionKJ` —— 1/16 个有
- `PreviewAudio` —— 1/16 个有
- `RH_LLMAPI_Pro_Node` —— 1/16 个有
- `SoundFlow_GetLength` —— 1/16 个有
- `SplitSigmas` —— 1/16 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 1/16 个有
- `easy cleanGpuUsed` —— 1/16 个有
- `easy promptConcat` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 16 | 100% |
| 高度 | 80 | 80 - 80 | 16 | 100% |
| 采样步数 | 4 | 4 - 4 | 16 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 16 | 100% |
| 采样算法 | er_sde | - | 16 | 100% |
| 调度器 | beta | - | 16 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 16 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，16 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，16 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，16 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，16 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，16 个样本，一致性 100%
- 调度器 最常用 beta，16 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 高发问题（16/16 个样本）：Steps较低可能导致细节不足

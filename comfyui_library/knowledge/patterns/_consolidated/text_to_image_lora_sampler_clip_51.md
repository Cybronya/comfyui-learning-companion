---
name: text_to_image_lora_sampler_clip_51
type: Text To Image
frequency: 17
level: strong
coverage: 0.666588
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLatentImage, Fast Groups Bypasser (rgthree), INTConstant, ImageResizeKJv2, JjkText, KSampler, KSamplerSelect, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_LoadVideo, easy clearCacheAll, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax-H3全功能疾速多参高清二采加速｜角色一致性视频生视频图生视频_2089701921434193922.json, 视频生成/图生视频/Minimax H3二采重绘效率流｜秒变清晰不丢一致性，出片效率起飞_2099519441183789057.json, 视频生成/图生视频/MinimaxH3全能参考提示词自动反推版！ENGENG开源视频模型真神！！_2087149888927780865.json, 视频生成/图生视频/单模型无编解码二采放大｜Minimax H3全能参考自动反推提示词 13 浏览 0 点赞 0 收藏_2092299427519225857.json, 视频生成/图生视频/双采高清人脸视频生成｜Minimax自动提示词加最新加速lora_2090470050162630658.json, 视频生成/图生视频/多参二采加速｜minimax-h3全功能疾速高清 鸭鸭图私密版直出_2089425542838841345.json, 视频生成/文生视频/0823修复横屏12秒｜万象+rh双模型二采放大视频_2091772010216124417.json, 视频生成/文生视频/0823修复竖屏12秒｜万象+rh双模型二采放大_2091770489449570306.json, 视频生成/文生视频/MiniMax H3 FL2VA单模型int8高清重绘｜9图3视频3音频文生视频_2090459732577439745.json, 视频生成/文生视频/Minimax H3双模二采｜文生视频图生视频视频生视频全能出片_2088728994442203137.json, 视频生成/文生视频/万象rh双模型二采放大｜0823修复横屏12秒文生视频_2091600249746972673.json, 视频生成/文生视频/万象rh双模型二采放大｜0823修复竖屏12秒文生视频_2091598794503839745.json, 视频生成/文生视频/双模二采玩法｜Minimax H3文生图生视频再采样_2089071865905115138.json, 视频生成/文生视频/双模型二采+潜空间放大｜MinimaxH3自动提示词人脸修复视频_2090226427131154433.json, 视频生成/文生视频/双模型二采参考生视频｜万象+rh横屏16_9时长12秒_2090554080665104386.json, 视频生成/文生视频/双模型二采参考生视频｜万象+rh横屏16_9时长12秒_2090857572986343426.json, 视频生成/文生视频/双模型二采放大提示词反推｜0823修复文生视频直出_2091603200427253762.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_51

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（视频生成/图生视频/MiniMax-H3全功能疾速多参高清二采加速｜角色一致性视频生视频图生视频_2089701921434193922.json、视频生成/图生视频/Minimax H3二采重绘效率流｜秒变清晰不丢一致性，出片效率起飞_2099519441183789057.json、视频生成/图生视频/MinimaxH3全能参考提示词自动反推版！ENGENG开源视频模型真神！！_2087149888927780865.json、视频生成/图生视频/单模型无编解码二采放大｜Minimax H3全能参考自动反推提示词 13 浏览 0 点赞 0 收藏_2092299427519225857.json、视频生成/图生视频/双采高清人脸视频生成｜Minimax自动提示词加最新加速lora_2090470050162630658.json…）

- **类型**：Text To Image
- **样本数**：17
- **可信度**：强结论
- **平均知识覆盖**：67%

## 共有节点

全部 17 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `INTConstant`
- `ImageResizeKJv2`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_LoadVideo`
- `easy clearCacheAll`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 16/17 个有
- `ResizeShortestToNode` —— 16/17 个有
- `SetNode` —— 16/17 个有
- `EasyCache` —— 15/17 个有
- `VHS_VideoCombine` —— 15/17 个有
- `孤海注释` —— 15/17 个有
- `LoraLoaderBypassModelOnly` —— 13/17 个有
- `ModelAttentionBackend` —— 13/17 个有
- `TrimAudioDuration` —— 11/17 个有
- `LTXVConcatAVLatent` —— 9/17 个有
- `LTXVSeparateAVLatent` —— 9/17 个有
- `RHLLMChatNode` —— 9/17 个有
- `StringFunction|pysssss` —— 9/17 个有
- `easy showAnything` —— 9/17 个有
- `PT_H3ConcatAVLatent` —— 7/17 个有
- `VAEEncode` —— 7/17 个有
- `VAEEncodeAudio` —— 7/17 个有
- `Label (rgthree)` —— 6/17 个有
- `MinimaxH3LatentUpscaler3D` —— 6/17 个有
- `AudioCrop` —— 5/17 个有
- `LoadVideo` —— 4/17 个有
- `PathchSageAttentionKJ` —— 4/17 个有
- `GetImageRangeFromBatch` —— 3/17 个有
- `MinimaxH3LatentUpscalerNode3D` —— 3/17 个有
- `SaveVideo` —— 3/17 个有
- `CR Text` —— 2/17 个有
- `CR Text Concatenate` —— 2/17 个有
- `DuckHideNode` —— 2/17 个有
- `HAIGC_SaveImagesToZip` —— 2/17 个有
- `SaveImage` —— 2/17 个有
- `easy imageSize` —— 2/17 个有
- `Any Switch (rgthree)` —— 1/17 个有
- `MiniMaxH3BlockCacheT8` —— 1/17 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/17 个有
- `SolAttnPatch` —— 1/17 个有
- `SplitSigmas` —— 1/17 个有
- `UniBlockSwap` —— 1/17 个有
- `easy cleanGpuUsed` —— 1/17 个有

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

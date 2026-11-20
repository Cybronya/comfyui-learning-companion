---
name: text_to_image_lora_sampler_clip_47
type: Text To Image
frequency: 20
level: strong
coverage: 0.78135
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/minimaxH3多图生成视频ENGENG_2087121643830333442.json, 视频生成/图生视频/minimaxH3开源版首尾帧｜8step加速图生视频_2095261239302774785.json, 视频生成/图生视频/minimax_h3_turbo_v4_step600_ema图生视频加速模型_2105146341893693442.json, 视频生成/图生视频/minimax双图参考生视频｜两张图搞定人物场景视频_2111131778227462145.json, 视频生成/图生视频/r2v参考生视频带TTS｜h3图生视频v2直出_2093853858853376001.json, 视频生成/图生视频/step600_ema_kitchen_attn｜图生视频专业增强模型工作流_2113888199780163585.json, 视频生成/图生视频/v2.0多参双采样图影音｜minimax h3电影感大片生成_2094317653564420098.json, 视频生成/图生视频/去除ai感全能参考｜minimax h3转场运镜图生视频_2093435277451812865.json, 视频生成/图生视频/去除ai感转场运镜｜minimax h3全能参考图生视频_2093764750915231745.json, 视频生成/图生视频/多参双采样图影音电影感大片 minimax h3 v2.0视频制作_2094183296849768450.json, 视频生成/图生视频/极致电影质感｜Minimax-H3转场运镜图生视频_2093229463424299009.json, 视频生成/图生视频/电影级视频多参版v1.0｜minimax H3制作工作流_2093475759825440770.json, 视频生成/图生视频/电影质感极致呈现｜Minimax-H3运镜转场图生视频_2093071322497769473.json, 视频生成/文生视频/H3电影质感正式版 真实电影摄影级视频生成_2099921435648155650.json, 视频生成/文生视频/MiniMax H3真实电影质感｜高质量视频生成_2095284422009507842.json, 视频生成/文生视频/MiniMax H3远景模糊人脸修复视频生成处理工具_2101368651281682433.json, 视频生成/文生视频/电影质感视频｜MiniMax H3正式版，文生图生视频都高级_2099918951735185409.json, 视频生成/文生视频/远景模糊人脸修复利器｜MiniMax_H3视频增强_2101179629947146242.json, 视频生成/视频生视频/MiniMax H3电影质感正式版工作流，真实质感文生视频视频生视频图生视频_2106462021058383874.json, 视频生成/视频生视频/MiniMax H3电影质感正式版｜文生视频图生视频大片感_2106274377644994562.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_47

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（视频生成/图生视频/minimaxH3多图生成视频ENGENG_2087121643830333442.json、视频生成/图生视频/minimaxH3开源版首尾帧｜8step加速图生视频_2095261239302774785.json、视频生成/图生视频/minimax_h3_turbo_v4_step600_ema图生视频加速模型_2105146341893693442.json、视频生成/图生视频/minimax双图参考生视频｜两张图搞定人物场景视频_2111131778227462145.json、视频生成/图生视频/r2v参考生视频带TTS｜h3图生视频v2直出_2093853858853376001.json…）

- **类型**：Text To Image
- **样本数**：20
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 20 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 19/20 个有
- `MiniMaxH3ReferenceToVideo` —— 19/20 个有
- `PrimitiveFloat` —— 19/20 个有
- `ResolutionSelector` —— 19/20 个有
- `LoadAudio` —— 17/20 个有
- `PrimitiveStringMultiline` —— 17/20 个有
- `PathchSageAttentionKJ` —— 15/20 个有
- `VHS_LoadVideo` —— 15/20 个有
- `MiniMaxH3BlockCacheT8` —— 14/20 个有
- `easy anythingIndexSwitch` —— 14/20 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 13/20 个有
- `MiniMaxH3ImageToVideo` —— 12/20 个有
- `H3SigmaRefiner` —— 9/20 个有
- `easy cleanGpuUsed` —— 8/20 个有
- `DisableNoise` —— 7/20 个有
- `Fast Groups Bypasser (rgthree)` —— 7/20 个有
- `H3LatentUpscaleByJingchen573` —— 7/20 个有
- `LTXVConcatAVLatent` —— 7/20 个有
- `LTXVSeparateAVLatent` —— 7/20 个有
- `MinimaxH3LatentUpscaler3D` —— 7/20 个有
- `SplitSigmas` —— 7/20 个有
- `easy showAnything` —— 7/20 个有
- `GetNode` —— 5/20 个有
- `PrimitiveInt` —— 5/20 个有
- `SetNode` —— 5/20 个有
- `Fast Groups Muter (rgthree)` —— 4/20 个有
- `FastGroupsBypassSwitch` —— 4/20 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/20 个有
- `SaveImage` —— 3/20 个有
- `ExtendIntermediateSigmas` —— 2/20 个有
- `H3FaceStitch` —— 2/20 个有
- `H3FaceTrackCrop` —— 2/20 个有
- `H3InjectVideoLatent` —— 2/20 个有
- `H3PerFrameDenoise` —— 2/20 个有
- `LoraLoaderBypassModelOnly` —— 2/20 个有
- `MiniMaxH3NativeAudioLock` —— 2/20 个有
- `MmuuaiGroupBypass` —— 2/20 个有
- `MuyeTextEditOutput` —— 2/20 个有
- `EmptyAudio` —— 1/20 个有
- `MiniMaxChunkFeedForward` —— 1/20 个有
- `MiniMaxH3SigmaShift` —— 1/20 个有
- `MiniMaxH3TurboLoRA` —— 1/20 个有
- `ModelAttentionBackend` —— 1/20 个有
- `ShowText|pysssss` —— 1/20 个有
- `Text` —— 1/20 个有
- `easy mathInt` —— 1/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 20 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 20 | 100% |
| 采样算法 | er_sde | - | 20 | 100% |
| 调度器 | beta | - | 20 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 20 | 100% |
| 宽度 | 80 | 80 - 80 | 20 | 100% |
| 高度 | 80 | 80 - 80 | 20 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 20/20 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，20 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，20 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，20 个样本，一致性 100%
- 调度器 最常用 beta，20 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，20 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，20 个样本，取值集中（一致性 100%）
- 高发问题（20/20 个样本）：Steps较低可能导致细节不足

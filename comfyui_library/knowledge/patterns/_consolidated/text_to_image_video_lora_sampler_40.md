---
name: text_to_image_video_lora_sampler_40
type: Text To Image
frequency: 17
level: strong
coverage: 0.818118
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, CR Prompt Text, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3MemoryEfficientSageAttentionPatch, ModelAttentionBackend, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SolAttnMiniMax, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/MiniMax H3双采全能V2｜文戏自然武戏动感强｜文生视频均衡出片_2104755900853604353.json, 图片生成/图生图/MiniMax_H3人物替换LoRA版工作流，视频生视频人物替换处理工具_2114992792735936514.json, 图片生成/图生图/MiniMax_H3视频复刻数字人｜换人换产品文案不换原声保留_2114993472179630081.json, 图片生成/图生图/MiniMax_H3音频驱动数字人多人对话｜加速版长视频处理工具_2114993807048658945.json, 视频生成/图生视频/(Hybird+VBVR逻辑强化-长视频-均衡版)MiniMax H3双采生视频｜文生图生双支持_2114264692993646594.json, 视频生成/图生视频/H3 POV视角720P超采样版工作流，图生视频第一人称视角创作方案_2106905984181563394.json, 视频生成/图生视频/H3-POV第一人称视角｜720p超采样图生视频_2106607588157771778.json, 视频生成/图生视频/H3_POV视角720P超采样版工作流，图生视频第一人称视角创作方案_2108378553988501505.json, 视频生成/图生视频/H3双采全能V4参考生视频_VBVR逻辑强化文武戏兼顾，长视频高清直出_2114408880754221058.json, 视频生成/图生视频/MiniMax H3全能参考9图3音频｜HyperVae 2X高清画质输出_2111077634724679682.json, 视频生成/图生视频/MiniMax H3双采V3语义桥｜文戏不油武戏动态强_2106606073850454017.json, 视频生成/图生视频/MiniMax H3双采全能V3语义桥 文戏自然武戏动态强长视频_2110355426595401730.json, 视频生成/图生视频/MiniMax H3双采全能V4-VBVR逻辑强化版｜图生视频长视频高清直出文戏武戏都拿捏_2114167141531475969.json, 视频生成/图生视频/MiniMax H3双采全能工作流V3语义桥，文戏不油武戏动态强参考生视频_2106823219750727681.json, 视频生成/文生视频/H3双采全能V4_VBVR逻辑强化文戏不油武戏动态强，文生视频长视频高清直出_2114407376332873729.json, 视频生成/文生视频/MiniMax H3双采全能V4-VBVR逻辑强化｜文戏不油武戏动态强参考生视频长视频直出_2114165525571006465.json, 视频生成/文生视频/MiniMax H3双采全能工作流V3语义桥文生视频版，长视频高清直出方案_2106998489740828674.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_40

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/图生图/MiniMax H3双采全能V2｜文戏自然武戏动感强｜文生视频均衡出片_2104755900853604353.json、图片生成/图生图/MiniMax_H3人物替换LoRA版工作流，视频生视频人物替换处理工具_2114992792735936514.json、图片生成/图生图/MiniMax_H3视频复刻数字人｜换人换产品文案不换原声保留_2114993472179630081.json、图片生成/图生图/MiniMax_H3音频驱动数字人多人对话｜加速版长视频处理工具_2114993807048658945.json、视频生成/图生视频/(Hybird+VBVR逻辑强化-长视频-均衡版)MiniMax H3双采生视频｜文生图生双支持_2114264692993646594.json…）

- **类型**：Text To Image
- **样本数**：17
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 17 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderBypassModelOnly`
- `LoraLoaderModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3DualClockSamplerT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `ModelAttentionBackend`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SolAttnMiniMax`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 16/17 个有
- `PrimitiveFloat` —— 16/17 个有
- `MiniMaxH3LearnedLatentUpscaleT8Advanced` —— 15/17 个有
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced` —— 15/17 个有
- `MiniMaxH3TwoPassDetailMixerT8Advanced` —— 15/17 个有
- `MiniMaxH3TwoPassLatentReconcileT8Advanced` —— 15/17 个有
- `Float` —— 14/17 个有
- `MiniMaxH3SemanticBridgeApplyT8` —— 14/17 个有
- `MiniMaxH3SemanticBridgeConfigT8` —— 14/17 个有
- `MiniMaxH3ChunkFeedForwardT8Advanced` —— 13/17 个有
- `RunningHub Deepcleaner` —— 13/17 个有
- `easy anythingIndexSwitch` —— 13/17 个有
- `easy cleanGpuUsed` —— 13/17 个有
- `孤海注释` —— 13/17 个有
- `SaveImage` —— 10/17 个有
- `Astra` —— 9/17 个有
- `CreateVideo` —— 9/17 个有
- `Fast Groups Bypasser (rgthree)` —— 9/17 个有
- `GetNode` —— 9/17 个有
- `MiniMaxH3HyperVAE2xLoaderEXPT8` —— 9/17 个有
- `SaveVideo` —— 9/17 个有
- `SetNode` —— 9/17 个有
- `ImpactFloat` —— 8/17 个有
- `Int` —— 8/17 个有
- `SimpleMath+` —— 8/17 个有
- `BlockSparseAttention` —— 4/17 个有
- `PreviewImage` —— 4/17 个有
- `GetImageSize` —— 3/17 个有
- `ImageCrop` —— 3/17 个有
- `ImageScale` —— 3/17 个有
- `LoadAudio` —— 3/17 个有
- `MiniMaxH3ActivationChunkT8Advanced` —— 3/17 个有
- `LoadVideo` —— 2/17 个有
- `VHS_LoadVideo` —— 2/17 个有
- `EmptyImage` —— 1/17 个有
- `GetVideoComponents` —— 1/17 个有
- `ImageResizeKJv2` —— 1/17 个有
- `JWStringToFloat` —— 1/17 个有
- `MiniMaxH3OutputTrimT8` —— 1/17 个有
- `SaveAudio` —— 1/17 个有
- `Video Slice` —— 1/17 个有
- `Vignette` —— 1/17 个有

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
| Steps较低可能导致细节不足 | 18/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，17 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，17 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，17 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，17 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，17 个样本，一致性 100%
- 调度器 最常用 beta，17 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 高发问题（18/17 个样本）：Steps较低可能导致细节不足

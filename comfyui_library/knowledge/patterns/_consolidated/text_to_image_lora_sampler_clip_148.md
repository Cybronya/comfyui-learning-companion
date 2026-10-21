---
name: text_to_image_lora_sampler_clip_148
type: Text To Image
frequency: 8
level: strong
coverage: 0.846375
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/H3 FACE REFINE面部重绘修复崩脸｜图生视频画质修复_2090410678174707713.json, 视频生成/图生视频/H3 LightX2V二采高清参考图生视频视频生视频_2088216027187474434.json, 视频生成/图生视频/H3开源9宫视图片Minimax图生视频EasyCache+Sage Attention KJ加速_2086421628958892033.json, 视频生成/图生视频/MINIMAX-H3文戏利器｜多图参考生视频手动版API调用_2105106295446663170.json, 视频生成/图生视频/MiniMax-H3全功能疾速多参高清二采加速｜角色一致性视频生视频图生视频_2089701921434193922.json, 视频生成/图生视频/多参二采加速｜minimax-h3全功能疾速高清 鸭鸭图私密版直出_2089425542838841345.json, 视频生成/图生视频/多图参考角色一致｜MINIMAX-H3图生视频视频生视频直出_2093757341844983809.json, 视频生成/文生视频/MiniMax H3 FL2VA单模型int8高清重绘｜9图3视频3音频文生视频_2090459732577439745.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_148

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/H3 FACE REFINE面部重绘修复崩脸｜图生视频画质修复_2090410678174707713.json、视频生成/图生视频/H3 LightX2V二采高清参考图生视频视频生视频_2088216027187474434.json、视频生成/图生视频/H3开源9宫视图片Minimax图生视频EasyCache+Sage Attention KJ加速_2086421628958892033.json、视频生成/图生视频/MINIMAX-H3文戏利器｜多图参考生视频手动版API调用_2105106295446663170.json、视频生成/图生视频/MiniMax-H3全功能疾速多参高清二采加速｜角色一致性视频生视频图生视频_2089701921434193922.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 8 个 workflow 都包含：
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
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 7/8 个有
- `CreateVideo` —— 6/8 个有
- `ImageResizeKJv2` —— 6/8 个有
- `LoadAudio` —— 6/8 个有
- `PT_H3ConcatAVLatent` —— 6/8 个有
- `SaveVideo` —— 6/8 个有
- `VAEEncode` —— 6/8 个有
- `VAEEncodeAudio` —— 6/8 个有
- `INTConstant` —— 5/8 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/8 个有
- `EasyCache` —— 4/8 个有
- `PathchSageAttentionKJ` —— 4/8 个有
- `VHS_LoadVideo` —— 4/8 个有
- `Fast Groups Bypasser (rgthree)` —— 3/8 个有
- `LoraLoaderBypassModelOnly` —— 3/8 个有
- `VHS_VideoCombine` —— 3/8 个有
- `easy clearCacheAll` —— 3/8 个有
- `DuckHideNode` —— 2/8 个有
- `ExtendIntermediateSigmas` —— 2/8 个有
- `GetNode` —— 2/8 个有
- `H3SigmaRefiner` —— 2/8 个有
- `HAIGC_SaveImagesToZip` —— 2/8 个有
- `MiniMaxH3AVDecodeT8` —— 2/8 个有
- `ResizeShortestToNode` —— 2/8 个有
- `SaveImage` —— 2/8 个有
- `SetNode` —— 2/8 个有
- `TrimAudioDuration` —— 2/8 个有
- `easy imageSize` —— 2/8 个有
- `Any Switch (rgthree)` —— 1/8 个有
- `H3FaceStitch` —— 1/8 个有
- `H3FaceTrackCrop` —— 1/8 个有
- `H3InjectVideoLatent` —— 1/8 个有
- `H3PerFrameDenoise` —— 1/8 个有
- `MiniMaxH3BlockCacheT8` —— 1/8 个有
- `MiniMaxH3NativeAudioLock` —— 1/8 个有
- `RHLLMChatNode` —— 1/8 个有
- `SolAttnPatch` —— 1/8 个有
- `StringFunction|pysssss` —— 1/8 个有
- `UniBlockSwap` —— 1/8 个有
- `easy showAnything` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足

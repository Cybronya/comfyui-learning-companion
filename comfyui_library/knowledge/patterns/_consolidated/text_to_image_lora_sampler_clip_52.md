---
name: text_to_image_lora_sampler_clip_52
type: Text To Image
frequency: 18
level: strong
coverage: 0.860667
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3MemoryEfficientSageAttentionPatch, ModelAttentionBackend, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/MiniMax H3双采全能V2｜文戏自然武戏动感强｜文生视频均衡出片_2104755900853604353.json, 图片生成/图生图/双时钟8步高质量极速图生视频V2｜Minimax图生图工作流_2088157021035126785.json, 图片生成/文生图/Minimax H3快速版短剧漫剧创意文生视频｜新加速LORA提效_2111290931298263042.json, 数字人/数字人/MiniMax H3视频复刻数字人视频换人换产品换文案替换原语音，图生视频方案_2107160853769449474.json, 数字人/数字人/MiniMax H3视频复刻数字人视频换人换产品文案不换保持原语音，图生视频方案_2107159320273178626.json, 数字人/数字人/MiniMax H3视频复刻数字人｜换人换产品文案不换原声保留_2106922727604056065.json, 数字人/数字人/MiniMax H3视频复刻数字人｜视频换人换产品换文案语音替换_2106924252430684161.json, 数字人/数字人/MiniMax H3音频驱动数字人多人对话加速版长视频处理工具，数字人生成方案_2107223547927162882.json, 数字人/数字人/MiniMax H3音频驱动数字人多人对话｜加速版长视频处理工具_2106925731669438465.json, 数字人/数字人/加速版单采参考生视频｜MiniMax H3长视频直出_2105482904137719809.json, 视频生成/图生视频/3段合成双时钟双采｜T8公共参考Lantent Upscaler加速_2093837736695386114.json, 视频生成/图生视频/5段合成双采加速｜T8公共参考Lantent Upscaler超真实_2093818227938914306.json, 视频生成/图生视频/BUNNY_H3高动态双采放大｜FL2VA_REF2VA专属｜打斗图生视频专用_2101851538271588353.json, 视频生成/图生视频/Eros Beta4电影感加速｜Minimax H3 Upscaler参考生视频_2095125881621663746.json, 视频生成/图生视频/H3高动态双采放大，图生视频高清增强分辨率提升工作流_2103273133582147585.json, 视频生成/图生视频/MINIMAX H3多参二采新玩法9图3音混合参考生成视频工作流，图生视频处理方案_2108329037356683266.json, 视频生成/图生视频/MINIMAX-H3多参二采新玩法｜9图3音混合参考生成视频_2107978172766711810.json, 视频生成/图生视频/MINIMAX-H3最强工作流｜图生视频高质量全能生成_2097040443535089666.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_52

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（图片生成/图生图/MiniMax H3双采全能V2｜文戏自然武戏动感强｜文生视频均衡出片_2104755900853604353.json、图片生成/图生图/双时钟8步高质量极速图生视频V2｜Minimax图生图工作流_2088157021035126785.json、图片生成/文生图/Minimax H3快速版短剧漫剧创意文生视频｜新加速LORA提效_2111290931298263042.json、数字人/数字人/MiniMax H3视频复刻数字人视频换人换产品换文案替换原语音，图生视频方案_2107160853769449474.json、数字人/数字人/MiniMax H3视频复刻数字人视频换人换产品文案不换保持原语音，图生视频方案_2107159320273178626.json…）

- **类型**：Text To Image
- **样本数**：18
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 18 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderBypassModelOnly`
- `LoraLoaderModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3DualClockSamplerT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `ModelAttentionBackend`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 17/18 个有
- `CR Prompt Text` —— 16/18 个有
- `SolAttnMiniMax` —— 16/18 个有
- `VHS_VideoCombine` —— 16/18 个有
- `孤海注释` —— 16/18 个有
- `LoadAudio` —— 11/18 个有
- `MiniMaxH3LearnedLatentUpscaleT8Advanced` —— 9/18 个有
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced` —— 9/18 个有
- `MiniMaxH3TwoPassDetailMixerT8Advanced` —— 9/18 个有
- `MiniMaxH3TwoPassLatentReconcileT8Advanced` —— 9/18 个有
- `SaveImage` —— 8/18 个有
- `GetNode` —— 4/18 个有
- `SetNode` —— 4/18 个有
- `VHS_LoadVideo` —— 4/18 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/18 个有
- `PreviewImage` —— 3/18 个有
- `AudioConcat` —— 2/18 个有
- `CreateVideo` —— 2/18 个有
- `Fast Groups Bypasser (rgthree)` —— 2/18 个有
- `ImageBatch` —— 2/18 个有
- `MiniMaxH3MotionContext` —— 2/18 个有
- `MiniMaxH3MotionContextTrim` —— 2/18 个有
- `PrimitiveStringMultiline` —— 2/18 个有
- `SaveVideo` —— 2/18 个有
- `ConditioningZeroOut` —— 1/18 个有
- `Float` —— 1/18 个有
- `Florence2ModelLoader` —— 1/18 个有
- `Florence2Run` —— 1/18 个有
- `Image Comparer (rgthree)` —— 1/18 个有
- `ModelPreviewOverrideKJ` —— 1/18 个有
- `SeedVR2LoadDiTModel` —— 1/18 个有
- `SeedVR2LoadVAEModel` —— 1/18 个有
- `SeedVR2VideoUpscaler` —— 1/18 个有
- `VAEEncode` —— 1/18 个有
- `Vignette` —— 1/18 个有
- `easy int` —— 1/18 个有
- `easy showAnything` —— 1/18 个有
- `忽略多组孤海` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 18 | 100% |
| 高度 | 80 | 80 - 80 | 18 | 100% |
| 采样步数 | 4 | 4 - 4 | 18 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 18 | 100% |
| 采样算法 | er_sde | - | 18 | 100% |
| 调度器 | beta | - | 18 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 18 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 22/18 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，18 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，18 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，18 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，18 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，18 个样本，一致性 100%
- 调度器 最常用 beta，18 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 高发问题（22/18 个样本）：Steps较低可能导致细节不足

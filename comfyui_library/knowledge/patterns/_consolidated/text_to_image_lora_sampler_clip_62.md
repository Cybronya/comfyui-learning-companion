---
name: text_to_image_lora_sampler_clip_62
type: Text To Image
frequency: 18
level: strong
coverage: 0.917833
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/Ref2VA参考视频动作迁移｜MiniMax_H3视频生视频生成_2093993310472986625.json, 平台全量/Scail2动作迁移真人卡通背景替换视频处理工具_2102467348744724482.json, 平台全量/参考视频驱动动作迁移 MiniMax_H3 Ref2VA视频生视频工作流_2094022196468477954.json, 平台全量/参考视频驱动动作迁移 MiniMax_H3 Ref2VA视频生视频工作流_2097101419143843841.json, 平台全量/要上传的9-MV-H3-1_2089108591226740738.json, 数字人/数字人/MiniMax H3视频复刻数字人视频换人换产品换文案替换原语音，图生视频方案_2107160853769449474.json, 数字人/数字人/MiniMax H3视频复刻数字人视频换人换产品文案不换保持原语音，图生视频方案_2107159320273178626.json, 数字人/数字人/MiniMax H3视频复刻数字人｜换人换产品文案不换原声保留_2106922727604056065.json, 数字人/数字人/MiniMax H3视频复刻数字人｜视频换人换产品换文案语音替换_2106924252430684161.json, 数字人/数字人/MiniMax H3音频驱动数字人多人对话加速版长视频处理工具，数字人生成方案_2107223547927162882.json, 数字人/数字人/MiniMax H3音频驱动数字人多人对话｜加速版长视频处理工具_2106925731669438465.json, 数字人/数字人/加速版单采参考生视频｜MiniMax H3长视频直出_2105482904137719809.json, 视频生成/图生视频/3段合成双时钟双采｜T8公共参考Lantent Upscaler加速_2093837736695386114.json, 视频生成/图生视频/5段合成双采加速｜T8公共参考Lantent Upscaler超真实_2093818227938914306.json, 视频生成/图生视频/BUNNY_H3高动态双采放大｜FL2VA_REF2VA专属｜打斗图生视频专用_2101851538271588353.json, 视频生成/图生视频/Eros Beta4电影感加速｜Minimax H3 Upscaler参考生视频_2095125881621663746.json, 视频生成/图生视频/H3 720P文戏均衡画质加强工作流，图生视频高质量文戏创作工具_2106163296528330753.json, 视频生成/图生视频/H3高动态双采放大，图生视频高清增强分辨率提升工作流_2103273133582147585.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_62

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（平台全量/Ref2VA参考视频动作迁移｜MiniMax_H3视频生视频生成_2093993310472986625.json、平台全量/Scail2动作迁移真人卡通背景替换视频处理工具_2102467348744724482.json、平台全量/参考视频驱动动作迁移 MiniMax_H3 Ref2VA视频生视频工作流_2094022196468477954.json、平台全量/参考视频驱动动作迁移 MiniMax_H3 Ref2VA视频生视频工作流_2097101419143843841.json、平台全量/要上传的9-MV-H3-1_2089108591226740738.json…）

- **类型**：Text To Image
- **样本数**：18
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 18 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3AVDecodeT8` —— 17/18 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 17/18 个有
- `孤海注释` —— 17/18 个有
- `MiniMaxH3AudioConditioningT8` —— 16/18 个有
- `VHS_VideoCombine` —— 16/18 个有
- `CR Prompt Text` —— 15/18 个有
- `LoraLoaderBypassModelOnly` —— 14/18 个有
- `MiniMaxH3DualClockSamplerT8` —— 14/18 个有
- `ModelAttentionBackend` —— 14/18 个有
- `SolAttnMiniMax` —— 13/18 个有
- `LoadAudio` —— 8/18 个有
- `VHS_LoadVideo` —— 8/18 个有
- `SaveImage` —— 7/18 个有
- `MiniMaxH3LearnedLatentUpscaleT8Advanced` —— 6/18 个有
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced` —— 6/18 个有
- `MiniMaxH3TwoPassDetailMixerT8Advanced` —— 6/18 个有
- `MiniMaxH3TwoPassLatentReconcileT8Advanced` —— 6/18 个有
- `BasicScheduler` —— 4/18 个有
- `KSamplerSelect` —— 4/18 个有
- `AudioConcat` —— 2/18 个有
- `CreateVideo` —— 2/18 个有
- `ImageBatch` —— 2/18 个有
- `MiniMaxH3MotionContext` —— 2/18 个有
- `MiniMaxH3MotionContextTrim` —— 2/18 个有
- `MiniMaxH3ReferenceToVideo` —— 2/18 个有
- `PrimitiveStringMultiline` —— 2/18 个有
- `SaveVideo` —— 2/18 个有
- `CR Text` —— 1/18 个有
- `GetImageSize` —— 1/18 个有
- `ImageCrop` —— 1/18 个有
- `ImageScale` —— 1/18 个有
- `MiniMaxH3ChunkFeedForwardT8Advanced` —— 1/18 个有
- `MiniMaxH3SigmaShift` —— 1/18 个有
- `ModelPreviewOverrideKJ` —— 1/18 个有
- `PathchSageAttentionKJ` —— 1/18 个有
- `easy cleanGpuUsed` —— 1/18 个有

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
| Steps较低可能导致细节不足 | 20/18 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，18 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，18 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，18 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，18 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，18 个样本，一致性 100%
- 调度器 最常用 beta，18 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 高发问题（20/18 个样本）：Steps较低可能导致细节不足

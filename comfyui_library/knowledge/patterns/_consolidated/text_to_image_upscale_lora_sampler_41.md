---
name: text_to_image_upscale_lora_sampler_41
type: Text To Image
frequency: 6
level: strong
coverage: 0.871667
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, GetImage, If ANY execute A else B, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxLowVRAMAttention, ModelAttentionBackend, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, YUAN_TXTJsonExtractor, YUAN_TXTParagraphSplitter, YUAN_TXTShotReplace, YuanMultiImage, YuanTool, Yuan_H3MotionContext, Yuan_H3MotionContextLoadLatent, Yuan_H3MotionContextTrim, Yuan_MiniMaxH3Video, Yuan_RTXVideoUpscaleH3, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/全栈式短剧生成V4.2.2｜MiniMax-H3图生视频制作_2092600480978530306.json, 视频生成/图生视频/全栈式短剧生成｜MiniMax-H3一分钟直出图生视频_2091615876062736386.json, 视频生成/图生视频/短剧直出1分钟｜MiniMax-H3全栈式生成V4.2.2图生视频_2092602046498299905.json, 视频生成/文生视频/全栈式短剧生成 MiniMax-H3 V4.2.3直出一分钟全节点注释_2094181672697810945.json, 视频生成/文生视频/全栈式短剧生成V4.2.2｜MiniMax-H3一分钟直出全节点注释_2091311737495707649.json, 视频生成/文生视频/短剧版本直出1分钟｜MiniMax-H3全栈式生成V4.2.3注释版_2096271170562772993.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_41

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/全栈式短剧生成V4.2.2｜MiniMax-H3图生视频制作_2092600480978530306.json、视频生成/图生视频/全栈式短剧生成｜MiniMax-H3一分钟直出图生视频_2091615876062736386.json、视频生成/图生视频/短剧直出1分钟｜MiniMax-H3全栈式生成V4.2.2图生视频_2092602046498299905.json、视频生成/文生视频/全栈式短剧生成 MiniMax-H3 V4.2.3直出一分钟全节点注释_2094181672697810945.json、视频生成/文生视频/全栈式短剧生成V4.2.2｜MiniMax-H3一分钟直出全节点注释_2091311737495707649.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `GetImage`
- `If ANY execute A else B`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `YUAN_TXTJsonExtractor`
- `YUAN_TXTParagraphSplitter`
- `YUAN_TXTShotReplace`
- `YuanMultiImage`
- `YuanTool`
- `Yuan_H3MotionContext`
- `Yuan_H3MotionContextLoadLatent`
- `Yuan_H3MotionContextTrim`
- `Yuan_MiniMaxH3Video`
- `Yuan_RTXVideoUpscaleH3`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `AudioConcat` —— 5/6 个有
- `EmptyAudio` —— 5/6 个有
- `Int` —— 5/6 个有
- `PreviewImage` —— 5/6 个有
- `VHS_VideoCombine` —— 5/6 个有
- `easy batchAnything` —— 5/6 个有
- `easy forLoopEnd` —— 5/6 个有
- `easy forLoopStart` —— 5/6 个有
- `easy isNone` —— 5/6 个有
- `ComfyMathExpression` —— 3/6 个有
- `CreateVideo` —— 3/6 个有
- `MathExpression|pysssss` —— 3/6 个有
- `PrimitiveFloat` —— 3/6 个有
- `SaveVideo` —— 3/6 个有
- `ShowText|pysssss` —— 3/6 个有
- `YuanPrimitive` —— 3/6 个有
- `easy mathInt` —— 3/6 个有
- `easy showAnything` —— 3/6 个有
- `LoadImage` —— 2/6 个有
- `PrimitiveBoolean` —— 2/6 个有
- `PrimitiveInt` —— 2/6 个有
- `RH_LLMAPI_Pro_Node` —— 2/6 个有
- `CM_IntUnaryOperation` —— 1/6 个有
- `DisTorchPurgeVRAMV2` —— 1/6 个有
- `MultiMergeVideos` —— 1/6 个有
- `easy cleanGpuUsed` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足

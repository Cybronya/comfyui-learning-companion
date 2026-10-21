---
name: text_to_image_video_lora_sampler_77
type: Text To Image
frequency: 9
level: strong
coverage: 0.645111
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, GetImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxLowVRAMAttention, ModelAttentionBackend, PreviewImage, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, ShowText|pysssss, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, YUAN_TXTJsonExtractor, YUAN_TXTParagraphSplitter, YuanMultiImage, YuanTool, Yuan_H3MotionContext, Yuan_H3MotionContextLoadLatent, Yuan_H3MotionContextTrim, Yuan_MiniMaxH3Video, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3全栈式短剧视频生成V4.2图生视频工作流_2088289186230128641.json, 视频生成/图生视频/MiniMax-H3全站式短剧｜图生视频分镜生成一站式_2089439572085264386.json, 视频生成/图生视频/Skill双阶段版V7.2｜MiniMax-H3全栈式短剧生成_2094024013784903681.json, 视频生成/图生视频/全栈式短剧生成V5.2｜MiniMax-H3图生视频直出_2089837999159857153.json, 视频生成/图生视频/全栈式短剧生成V7.1｜MiniMax-H3自用图生视频_2095119621128019969.json, 视频生成/图生视频/全栈式短剧生成V7.2｜MiniMax-H3 Skill双阶段版_2093802392323190785.json, 视频生成/文生视频/MiniMax-H3全栈式短剧V4.2.1｜循环直出一集全节点注释修复版_2089388164245975042.json, 视频生成/文生视频/全栈短剧生成｜MiniMax H3 V4.2.1 循环直出整集 全节点注释版_2089332705229107201.json, 视频生成/文生视频/全节点注释版｜MiniMax H3 V4.2.1全栈短剧生成循环直出整集_2089428387751354369.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_77

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3全栈式短剧视频生成V4.2图生视频工作流_2088289186230128641.json、视频生成/图生视频/MiniMax-H3全站式短剧｜图生视频分镜生成一站式_2089439572085264386.json、视频生成/图生视频/Skill双阶段版V7.2｜MiniMax-H3全栈式短剧生成_2094024013784903681.json、视频生成/图生视频/全栈式短剧生成V5.2｜MiniMax-H3图生视频直出_2089837999159857153.json、视频生成/图生视频/全栈式短剧生成V7.1｜MiniMax-H3自用图生视频_2095119621128019969.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：65%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `GetImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `PreviewImage`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `YUAN_TXTJsonExtractor`
- `YUAN_TXTParagraphSplitter`
- `YuanMultiImage`
- `YuanTool`
- `Yuan_H3MotionContext`
- `Yuan_H3MotionContextLoadLatent`
- `Yuan_H3MotionContextTrim`
- `Yuan_MiniMaxH3Video`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `StringConcatenate` —— 7/9 个有
- `GetNode` —— 6/9 个有
- `PrimitiveInt` —— 6/9 个有
- `SetNode` —— 6/9 个有
- `Yuan_RTXVideoUpscaleH3` —— 6/9 个有
- `ComfySwitchNode` —— 5/9 个有
- `INTConstant` —— 5/9 个有
- `PrimitiveBoolean` —— 5/9 个有
- `RegexExtract` —— 5/9 个有
- `StringReplace` —— 5/9 个有
- `YUAN_TXTAppearanceOrder` —— 5/9 个有
- `YUAN_TXTListNumber` —— 5/9 个有
- `YUAN_TXTReplace` —— 5/9 个有
- `ResolutionSelector` —— 4/9 个有
- `YUAN_TXTShotReplace` —— 4/9 个有
- `AudioConcat` —— 3/9 个有
- `EmptyAudio` —— 3/9 个有
- `If ANY execute A else B` —— 3/9 个有
- `LoraLoaderBypassModelOnly` —— 3/9 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/9 个有
- `SimpleMath+` —— 3/9 个有
- `YuanAudioList` —— 3/9 个有
- `YuanAudioSplit` —— 3/9 个有
- `easy batchAnything` —— 3/9 个有
- `easy forLoopEnd` —— 3/9 个有
- `easy forLoopStart` —— 3/9 个有
- `easy isNone` —— 3/9 个有
- `LoadImage` —— 2/9 个有
- `TextGenerate` —— 2/9 个有
- `Yuan_H3Upscale3D` —— 2/9 个有
- `ManualSigmas` —— 1/9 个有
- `YuanPrimitive` —— 1/9 个有
- `easy cleanGpuUsed` —— 1/9 个有
- `easy clearCacheAll` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | beta | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 80 | 80 - 80 | 9 | 100% |
| 高度 | 80 | 80 - 80 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高发问题（10/9 个样本）：Steps较低可能导致细节不足

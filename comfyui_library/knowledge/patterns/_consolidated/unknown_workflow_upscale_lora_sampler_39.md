---
name: unknown_workflow_upscale_lora_sampler_39
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.642833
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, GetImage, If ANY execute A else B, KSamplerSelect, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxLowVRAMAttention, ModelAttentionBackend, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, YUAN_TXTJsonExtractor, YUAN_TXTParagraphSplitter, YUAN_TXTShotReplace, YuanMultiImage, YuanTool, Yuan_H3MotionContext, Yuan_H3MotionContextLoadLatent, Yuan_H3MotionContextTrim, Yuan_MiniMaxH3Video, Yuan_RTXVideoUpscaleH3]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax-H3全栈式短剧生成V4.2.2 短剧版本直出1分钟_2091886599092133889.json, 视频生成/图生视频/MiniMax-H3全栈式短剧生成V4.2.2_2092157971756310530.json, 视频生成/图生视频/全栈式短剧生成｜MiniMax-H3一分钟直出_2091350303965794305.json, 视频生成/文生视频/MiniMax-H3全栈式短剧生成V4.2.2（短剧版本直出1分钟）+全节点注释_2097626909663383553.json, 视频生成/文生视频/MiniMax-H3全栈式短剧生成V4.2.2（短剧版本直出1分钟）+全节点注释_2104462985950486530.json, 视频生成/文生视频/🔥AIGC大赛🔥MiniMax-H3全栈式短剧生成V4.2.2（短剧版本直出1分钟）+全节点注释_2097297028450709506.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_39

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/MiniMax-H3全栈式短剧生成V4.2.2 短剧版本直出1分钟_2091886599092133889.json、视频生成/图生视频/MiniMax-H3全栈式短剧生成V4.2.2_2092157971756310530.json、视频生成/图生视频/全栈式短剧生成｜MiniMax-H3一分钟直出_2091350303965794305.json、视频生成/文生视频/MiniMax-H3全栈式短剧生成V4.2.2（短剧版本直出1分钟）+全节点注释_2097626909663383553.json、视频生成/文生视频/MiniMax-H3全栈式短剧生成V4.2.2（短剧版本直出1分钟）+全节点注释_2104462985950486530.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：64%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `GetImage`
- `If ANY execute A else B`
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
- `PrimitiveBoolean` —— 2/6 个有
- `PrimitiveInt` —— 2/6 个有
- `RH_LLMAPI_Pro_Node` —— 2/6 个有
- `CM_IntUnaryOperation` —— 1/6 个有
- `DisTorchPurgeVRAMV2` —— 1/6 个有
- `LoadImage` —— 1/6 个有
- `MultiMergeVideos` —— 1/6 个有
- `easy cleanGpuUsed` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

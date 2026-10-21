---
name: unknown_workflow_video_sampler_clip_105
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.749
common_nodes: [CFGGuider, CLIPTextEncode, DualCLIPLoaderGGUF, EmptyLTXVLatentVideo, GetNode, KSamplerSelect, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVScheduler, LTXVSeparateAVLatent, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SetNode, UnetLoaderGGUF, VAEDecodeTiled, VAELoader, VHS_VideoCombine, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/2012026599562022913.json, 视频生成/图生视频/2011768781089017858.json, 视频生成/图生视频/2021585038990647298.json, 视频生成/图生视频/2012344262502912001.json, 视频生成/文生视频/LTX-2 GGUF量化版-文生视频-直接生成带音频的视频-低显存-速度贼快-自动提示词_2012014023218302977.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_105

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/2012026599562022913.json、视频生成/图生视频/2011768781089017858.json、视频生成/图生视频/2021585038990647298.json、视频生成/图生视频/2012344262502912001.json、视频生成/文生视频/LTX-2 GGUF量化版-文生视频-直接生成带音频的视频-低显存-速度贼快-自动提示词_2012014023218302977.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `DualCLIPLoaderGGUF`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `UnetLoaderGGUF`
- `VAEDecodeTiled`
- `VAELoader`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `LTXVImgToVideoInplace` —— 4/5 个有
- `LTXVPreprocess` —— 4/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/5 个有
- `LoadImage` —— 4/5 个有
- `easy showAnything` —— 4/5 个有
- `INTConstant` —— 3/5 个有
- `Int` —— 3/5 个有
- `JWInteger` —— 3/5 个有
- `PreviewImage` —— 3/5 个有
- `AddLabel` —— 2/5 个有
- `CR Prompt Text` —— 2/5 个有
- `RH_LLMAPI_Pro_Node` —— 2/5 个有
- `SimpleMath+` —— 2/5 个有
- `easy anythingIndexSwitch` —— 2/5 个有
- `GetImageSize` —— 1/5 个有
- `Label (rgthree)` —— 1/5 个有
- `MathExpression|pysssss` —— 1/5 个有
- `Qwen3_VQA` —— 1/5 个有
- `SomethingToString` —— 1/5 个有
- `Split String` —— 1/5 个有
- `TextPreview` —— 1/5 个有
- `easy int` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 5 | 100% |
| 高度 | 25 | 25 - 25 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，5 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，5 个样本，取值集中（一致性 100%）

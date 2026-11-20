---
name: unknown_workflow_sampler_clip_unet_285
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.771
common_nodes: [CFGGuider, CLIPTextEncode, DualCLIPLoaderGGUF, EmptyLTXVLatentVideo, GetNode, INTConstant, KSamplerSelect, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVScheduler, LTXVSeparateAVLatent, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SetNode, UnetLoaderGGUF, VAEDecodeTiled, VAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/反推提示词/65wenshengtukuaikuai_2052625123169062913.json, 视频生成/图生视频/LTX-2 GGUF量化版-图生视频-直接生成带音频的视频-低显存-速度贼快-自动提示词_2012026599562022913.json, 视频生成/图生视频/LTX-2 GGUF量化版图生视频_2011768781089017858.json, 视频生成/文生视频/LTX-2 GGUF量化版-文生视频-直接生成带音频的视频-低显存-速度贼快-自动提示词_2012014023218302977.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_285

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/反推提示词/65wenshengtukuaikuai_2052625123169062913.json、视频生成/图生视频/LTX-2 GGUF量化版-图生视频-直接生成带音频的视频-低显存-速度贼快-自动提示词_2012026599562022913.json、视频生成/图生视频/LTX-2 GGUF量化版图生视频_2011768781089017858.json、视频生成/文生视频/LTX-2 GGUF量化版-文生视频-直接生成带音频的视频-低显存-速度贼快-自动提示词_2012014023218302977.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `DualCLIPLoaderGGUF`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `INTConstant`
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
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 3/4 个有
- `Int` —— 3/4 个有
- `SimpleMath+` —— 3/4 个有
- `VHS_VideoCombine` —— 3/4 个有
- `easy anythingIndexSwitch` —— 3/4 个有
- `AddLabel` —— 2/4 个有
- `JWInteger` —— 2/4 个有
- `LTXVImgToVideoInplace` —— 2/4 个有
- `LTXVPreprocess` —— 2/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `LoadImage` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `RH_LLMAPI_Pro_Node` —— 2/4 个有
- `easy showAnything` —— 2/4 个有
- `CreateVideo` —— 1/4 个有
- `Label (rgthree)` —— 1/4 个有
- `RH_LLMAPI_NODE` —— 1/4 个有
- `RTXVideoSuperResolution` —— 1/4 个有
- `SaveVideo` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 4 | 100% |
| 高度 | 25 | 25 - 25 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，4 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，4 个样本，取值集中（一致性 100%）

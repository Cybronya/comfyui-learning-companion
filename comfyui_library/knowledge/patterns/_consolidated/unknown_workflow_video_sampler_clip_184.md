---
name: unknown_workflow_video_sampler_clip_184
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.822
common_nodes: [CFGGuider, CLIPTextEncode, CR Float To Integer, DualCLIPLoader, EmptyLTXVLatentVideo, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LoadImage, ManualSigmas, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SimpleMath+, TTResolutionSelector, UNETLoader, VAEDecodeTiled, VAELoader, VAELoaderKJ, VHS_VideoCombine, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/SFStudio 四宫格 I2V 分帧注入引擎_2078305256244596737.json, 视频生成/文生视频/LTX2.3_四宫格漫剧视频_2064675254458474498.json, 视频生成/文生视频/最强漫剧生成LTX-2.3（四宫格V2.0-单采光速版）_2041148096977047554.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_184

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/SFStudio 四宫格 I2V 分帧注入引擎_2078305256244596737.json、视频生成/文生视频/LTX2.3_四宫格漫剧视频_2064675254458474498.json、视频生成/文生视频/最强漫剧生成LTX-2.3（四宫格V2.0-单采光速版）_2041148096977047554.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CR Float To Integer`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `ManualSigmas`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SimpleMath+`
- `TTResolutionSelector`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `GuHaiAutoImageSplit` —— 2/3 个有
- `INTConstant` —— 2/3 个有
- `ImageFromBatch+` —— 2/3 个有
- `ImageResizeKJv2` —— 2/3 个有
- `LTXVAddGuideMulti` —— 2/3 个有
- `LatentUpscaleModelLoader` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `RH_LLMAPI_Pro_Node` —— 2/3 个有
- `Text` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `GetNode` —— 1/3 个有
- `JWStringToInteger` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `ParseJsonNode` —— 1/3 个有
- `RHHiddenNodes` —— 1/3 个有
- `SetNode` —— 1/3 个有
- `StringConstantMultiline` —— 1/3 个有
- `TD_LTXVAddGuideFromGrid` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 3 | 100% |
| 高度 | 25 | 25 - 25 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，3 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，3 个样本，取值集中（一致性 100%）

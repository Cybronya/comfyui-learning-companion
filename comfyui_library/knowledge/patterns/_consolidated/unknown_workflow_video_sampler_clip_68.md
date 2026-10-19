---
name: unknown_workflow_video_sampler_clip_68
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.553625
common_nodes: [CFGGuider, CLIPTextEncode, CR Float To Integer, DualCLIPLoader, EmptyLTXVLatentVideo, GetNode, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LoadImage, ManualSigmas, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SetNode, SimpleMath+, UNETLoader, VAEDecodeTiled, VAELoader, VAELoaderKJ, VHS_VideoCombine, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/2068875713587007490.json, 视频生成/图生视频/2068905830182899714.json, 视频生成/图生视频/2069697861658435586.json, 视频生成/图生视频/2069688707870978050.json, 视频生成/图生视频/2067017376826216450.json, 视频生成/图生视频/2069616746276937729.json, 视频生成/图生视频/2043556476085604353.json, 视频生成/图生视频/2041885580006526978.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_68

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/2068875713587007490.json、视频生成/图生视频/2068905830182899714.json、视频生成/图生视频/2069697861658435586.json、视频生成/图生视频/2069688707870978050.json、视频生成/图生视频/2067017376826216450.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：55%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CR Float To Integer`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetNode`
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
- `SetNode`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `LatentUpscaleModelLoader` —— 7/8 个有
- `TTResolutionSelector` —— 6/8 个有
- `JWString` —— 5/8 个有
- `ParseJsonNode` —— 5/8 个有
- `ShowText|pysssss` —— 5/8 个有
- `TD_LTXVAddGuideFromGrid` —— 5/8 个有
- `INTConstant` —— 3/8 个有
- `ImageFromBatch+` —— 3/8 个有
- `LTXVAddGuideMulti` —— 3/8 个有
- `LoraLoaderModelOnly` —— 3/8 个有
- `Text` —— 3/8 个有
- `Any To Any` —— 2/8 个有
- `BatchCount+` —— 2/8 个有
- `Fast Groups Bypasser (rgthree)` —— 2/8 个有
- `ImageResize+` —— 2/8 个有
- `Int` —— 2/8 个有
- `LTXVImgToVideoInplace` —— 2/8 个有
- `LTXVLatentUpsampler` —— 2/8 个有
- `Make Image Batch` —— 2/8 个有
- `MathExpression|pysssss` —— 2/8 个有
- `easy imageSize` —— 2/8 个有
- `ImageResizeKJv2` —— 1/8 个有
- `JWStringToInteger` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 8 | 100% |
| 高度 | 25 | 25 - 25 | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，8 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，8 个样本，取值集中（一致性 100%）

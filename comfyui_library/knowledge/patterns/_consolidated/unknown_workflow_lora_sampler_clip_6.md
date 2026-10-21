---
name: unknown_workflow_lora_sampler_clip_6
type: Unknown Workflow
frequency: 36
level: strong
coverage: 0.879556
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, SaveVideo, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/2039676993360367617.json, 视频生成/图生视频/2064178415359586305.json, 视频生成/图生视频/2065262381550358529.json, 视频生成/图生视频/LTX2.3++图生视频++视频生成+++最强开源_2087381685796167681.json, 视频生成/图生视频/2066688936931581953.json, 视频生成/图生视频/2067242779092279297.json, 视频生成/图生视频/2053006358177427458.json, 视频生成/图生视频/2060944466294431746.json, 视频生成/图生视频/2061066676938039297.json, 视频生成/图生视频/2062109335618146305.json, 视频生成/图生视频/2067149449188691969.json, 视频生成/图生视频/2067162980319588354.json, 视频生成/图生视频/2029780080481800193.json, 视频生成/图生视频/2052313394044256257.json, 视频生成/图生视频/2031218459471777794.json, 视频生成/图生视频/2039156073621360641.json, 视频生成/图生视频/2052027748742377473.json, 视频生成/图生视频/2067422892773695490.json, 视频生成/图生视频/2068906684529078274.json, 视频生成/图生视频/2077342354540945409.json, 视频生成/图生视频/2078064960806154242.json, 视频生成/图生视频/2079234685774950401.json, 视频生成/图生视频/2078120653017931778.json, 视频生成/图生视频/2056776482755792897.json, 视频生成/图生视频/2066084809260224514.json, 视频生成/图生视频/2052310440121774082.json, 视频生成/图生视频/2054804192941887490.json, 视频生成/图生视频/2053075212203241473.json, 视频生成/图生视频/2054046453240213506.json, 视频生成/图生视频/2052313640908406785.json, 视频生成/图生视频/2033776498380906497.json, 视频生成/图生视频/2044666108304691201.json, 视频生成/图生视频/2031918270768484353.json, 视频生成/图生视频/2031324375839940609.json, 视频生成/图生视频/2032023650970378241.json, 视频生成/图生视频/2032091629703663617.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_6

> 由 `engine/knowledge_consolidation` 从 36 个 workflow 归纳得出（视频生成/图生视频/2039676993360367617.json、视频生成/图生视频/2064178415359586305.json、视频生成/图生视频/2065262381550358529.json、视频生成/图生视频/LTX2.3++图生视频++视频生成+++最强开源_2087381685796167681.json、视频生成/图生视频/2066688936931581953.json…）

- **类型**：Unknown Workflow
- **样本数**：36
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 36 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplace`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 35/36 个有
- `GetImageSize` —— 35/36 个有
- `ImageScaleBy` —— 35/36 个有
- `LTXVCropGuides` —— 35/36 个有
- `LTXVLatentUpsampler` —— 35/36 个有
- `LatentUpscaleModelLoader` —— 35/36 个有
- `LTXVScheduler` —— 34/36 个有
- `KSampler` —— 33/36 个有
- `PrimitiveInt` —— 32/36 个有
- `Int` —— 26/36 个有
- `RH_LLMAPI_Pro_Node` —— 26/36 个有
- `easy showAnything` —— 26/36 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 25/36 个有
- `MathExpression|pysssss` —— 23/36 个有
- `CR Prompt Text` —— 22/36 个有
- `easy float` —— 22/36 个有
- `easy int` —— 22/36 个有
- `DualCLIPLoader` —— 16/36 个有
- `LTXVPreprocess` —— 16/36 个有
- `PreviewAny` —— 16/36 个有
- `TextGenerateLTX2Prompt` —— 16/36 个有
- `ResizeImagesByLongerEdge` —— 14/36 个有
- `ResizeImageMaskNode` —— 12/36 个有
- `Fast Groups Bypasser (rgthree)` —— 6/36 个有
- `CR Text` —— 4/36 个有
- `SimpleMath+` —— 4/36 个有
- `ImpactConditionalBranch` —— 3/36 个有
- `ImpactInt` —— 3/36 个有
- `LTXVChunkFeedForward` —— 3/36 个有
- `ModelPatchTorchSettings` —— 3/36 个有
- `PathchSageAttentionKJ` —— 3/36 个有
- `Switch any [Crystools]` —— 3/36 个有
- `ManualSigmas` —— 2/36 个有
- `Text` —— 2/36 个有
- `CM_FloatToInt` —— 1/36 个有
- `INTConstant` —— 1/36 个有
- `ImageResizeKJv2` —— 1/36 个有
- `LTXVFirstLastFrameControl_TTP` —— 1/36 个有
- `PreviewImage` —— 1/36 个有
- `PrimitiveFloat` —— 1/36 个有
- `SeargeIntegerMath` —— 1/36 个有
- `easy convertAnything` —— 1/36 个有
- `easy getNode` —— 1/36 个有
- `easy imageConcat` —— 1/36 个有
- `easy setNode` —— 1/36 个有
- `ttN int` —— 1/36 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 36 | 100% |
| 高度 | 25 | 24 - 25 | 36 | 99% |
| 采样步数 | 4 | 4 - 6 | 33 | 92% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 33 | 100% |
| 采样算法 | euler | - | 33 | 100% |
| 调度器 | simple | - | 33 | 100% |
| 重绘幅度 | 0.35 | 0.35 - 0.35 | 33 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 33/36 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，36 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 24 - 25，36 个样本，取值集中（一致性 99%）
- 采样步数 中位数 4，观测区间 4 - 6，33 个样本，取值集中（一致性 92%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，33 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，33 个样本，一致性 100%
- 调度器 最常用 simple，33 个样本，一致性 100%
- 重绘幅度 中位数 0.35，观测区间 0.35 - 0.35，33 个样本，取值集中（一致性 100%）
- 高发问题（33/36 个样本）：Steps较低可能导致细节不足

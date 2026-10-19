---
name: unknown_workflow_upscale_latent_upscale_lora_4
type: Unknown Workflow
frequency: 32
level: strong
coverage: 0.870406
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, ImageScaleBy, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/2053006358177427458.json, 视频生成/图生视频/2060944466294431746.json, 视频生成/图生视频/2061066676938039297.json, 视频生成/图生视频/2062109335618146305.json, 视频生成/图生视频/2067149449188691969.json, 视频生成/图生视频/2067162980319588354.json, 视频生成/图生视频/2052313394044256257.json, 视频生成/图生视频/2031218459471777794.json, 视频生成/图生视频/2039156073621360641.json, 视频生成/图生视频/2052027748742377473.json, 视频生成/图生视频/2067422892773695490.json, 视频生成/图生视频/2068906684529078274.json, 视频生成/图生视频/2077342354540945409.json, 视频生成/图生视频/2078064960806154242.json, 视频生成/图生视频/2079234685774950401.json, 视频生成/图生视频/2078120653017931778.json, 视频生成/图生视频/2056776482755792897.json, 视频生成/图生视频/2066084809260224514.json, 视频生成/图生视频/2052310440121774082.json, 视频生成/图生视频/2054804192941887490.json, 视频生成/图生视频/2053075212203241473.json, 视频生成/图生视频/2054046453240213506.json, 视频生成/图生视频/2052313640908406785.json, 视频生成/图生视频/2033776498380906497.json, 视频生成/图生视频/2044666108304691201.json, 视频生成/图生视频/2031918270768484353.json, 视频生成/图生视频/2056932845310009346.json, 视频生成/图生视频/2070027759010795521.json, 视频生成/图生视频/2031324375839940609.json, 视频生成/图生视频/2032023650970378241.json, 视频生成/图生视频/2032091629703663617.json, 视频生成/文生视频/🐱LTX2.3图生视频工作流_2030298909729361921.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_4

> 由 `engine/knowledge_consolidation` 从 32 个 workflow 归纳得出（视频生成/图生视频/2053006358177427458.json、视频生成/图生视频/2060944466294431746.json、视频生成/图生视频/2061066676938039297.json、视频生成/图生视频/2062109335618146305.json、视频生成/图生视频/2067149449188691969.json…）

- **类型**：Unknown Workflow
- **样本数**：32
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 32 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyImage`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `ImageScaleBy`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 31/32 个有
- `SaveVideo` —— 31/32 个有
- `KSampler` —— 30/32 个有
- `LTXVScheduler` —— 30/32 个有
- `PrimitiveInt` —— 28/32 个有
- `RH_LLMAPI_Pro_Node` —— 27/32 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 26/32 个有
- `easy showAnything` —— 26/32 个有
- `Int` —— 24/32 个有
- `MathExpression|pysssss` —— 23/32 个有
- `CR Prompt Text` —— 22/32 个有
- `easy float` —— 22/32 个有
- `easy int` —— 22/32 个有
- `PreviewAny` —— 13/32 个有
- `DualCLIPLoader` —— 12/32 个有
- `LTXVPreprocess` —— 12/32 个有
- `TextGenerateLTX2Prompt` —— 12/32 个有
- `ResizeImagesByLongerEdge` —— 11/32 个有
- `ResizeImageMaskNode` —— 8/32 个有
- `Fast Groups Bypasser (rgthree)` —— 6/32 个有
- `CR Text` —— 5/32 个有
- `LTXVChunkFeedForward` —— 4/32 个有
- `ModelPatchTorchSettings` —— 4/32 个有
- `PathchSageAttentionKJ` —— 4/32 个有
- `SimpleMath+` —— 4/32 个有
- `ImpactConditionalBranch` —— 3/32 个有
- `ImpactInt` —— 3/32 个有
- `Switch any [Crystools]` —— 3/32 个有
- `CM_FloatToInt` —— 2/32 个有
- `INTConstant` —— 2/32 个有
- `ManualSigmas` —— 2/32 个有
- `PrimitiveFloat` —— 2/32 个有
- `LTXVFirstLastFrameControl_TTP` —— 1/32 个有
- `LTXVImgToVideoConditionOnly` —— 1/32 个有
- `PreviewImage` —— 1/32 个有
- `PrimitiveBoolean` —— 1/32 个有
- `Text` —— 1/32 个有
- `VHS_VideoCombine` —— 1/32 个有
- `easy convertAnything` —— 1/32 个有
- `easy getNode` —— 1/32 个有
- `easy imageConcat` —— 1/32 个有
- `easy setNode` —— 1/32 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 6 | 30 | 91% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 30 | 100% |
| 采样算法 | euler | - | 30 | 100% |
| 调度器 | simple | - | 30 | 100% |
| 重绘幅度 | 0.35 | 0.35 - 0.35 | 30 | 100% |
| 宽度 | 97 | 97 - 97 | 32 | 100% |
| 高度 | 25 | 25 - 25 | 32 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 30/32 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 6，30 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，30 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，30 个样本，一致性 100%
- 调度器 最常用 simple，30 个样本，一致性 100%
- 重绘幅度 中位数 0.35，观测区间 0.35 - 0.35，30 个样本，取值集中（一致性 100%）
- 宽度 中位数 97，观测区间 97 - 97，32 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，32 个样本，取值集中（一致性 100%）
- 高发问题（30/32 个样本）：Steps较低可能导致细节不足

---
name: unknown_workflow_video_upscale_latent_upscale_69
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.788
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, ImageScaleBy, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, ManualSigmas, RandomNoise, SamplerCustomAdvanced, VAEDecodeTiled, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/YZ金鱼-LTX-2 文生视频_2009514987760394241.json, 视频生成/文生视频/[1月] 音画同步_ASMR LTX2文生视频_2009296819603382274.json, 视频生成/文生视频/ltx2文生视频（运行非常稳定，时长可调，运行速度很快）_2008912681826263041.json, 视频生成/文生视频/video_ltx2_t2v_unpack_2008579148603723778.json, 视频生成/文生视频/很强的文生视频-LTXV2.0你就是导演_2008866865359097857.json, 视频生成/文生视频/音画同步 LTX2.0 文生视频【蒸馏  48G】_2008562261769592834.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_69

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/文生视频/YZ金鱼-LTX-2 文生视频_2009514987760394241.json、视频生成/文生视频/[1月] 音画同步_ASMR LTX2文生视频_2009296819603382274.json、视频生成/文生视频/ltx2文生视频（运行非常稳定，时长可调，运行速度很快）_2008912681826263041.json、视频生成/文生视频/video_ltx2_t2v_unpack_2008579148603723778.json、视频生成/文生视频/很强的文生视频-LTXV2.0你就是导演_2008866865359097857.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 6 个 workflow 都包含：
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
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsampler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LTXVCropGuides` —— 5/6 个有
- `LTXVScheduler` —— 5/6 个有
- `PrimitiveFloat` —— 4/6 个有
- `PrimitiveInt` —— 4/6 个有
- `SimpleMath+` —— 3/6 个有
- `CR Text` —— 2/6 个有
- `GetNode` —— 2/6 个有
- `LoadImage` —— 2/6 个有
- `SetNode` —— 2/6 个有
- `INTConstant` —— 1/6 个有
- `Int` —— 1/6 个有
- `JWInteger` —— 1/6 个有
- `LayerUtility: PurgeVRAM V2` —— 1/6 个有
- `MathExpression|pysssss` —— 1/6 个有
- `MemoryCleaner` —— 1/6 个有
- `Primitive integer [Crystools]` —— 1/6 个有
- `PrimitiveStringMultiline` —— 1/6 个有
- `Qwen3_VQA_Plus` —— 1/6 个有
- `ShowText|pysssss` —— 1/6 个有
- `TextInput_` —— 1/6 个有
- `VAEDecode` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 121 | 6 | 91% |
| 高度 | 25 | 25 - 25 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 121，6 个样本，取值集中（一致性 91%）
- 高度 中位数 25，观测区间 25 - 25，6 个样本，取值集中（一致性 100%）

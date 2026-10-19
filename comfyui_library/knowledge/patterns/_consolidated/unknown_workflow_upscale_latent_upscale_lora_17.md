---
name: unknown_workflow_upscale_latent_upscale_lora_17
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.69425
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, ImageScaleBy, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, ManualSigmas, PrimitiveFloat, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, VAEDecodeTiled]
problems: []
missing: []
members: [视频生成/文生视频/AA--音画同步视频-LTX2.0文生视频+放大+插帧_2008918263912206338.json, 视频生成/文生视频/LH-DMT-LTX2.0-003.文生视频工作流_2016312568960258049.json, 视频生成/文生视频/LH-DMT-LTX2.0-004.自动扩写文生视频_2016319047557718017.json, 视频生成/文生视频/LH-DMT-LTX2.0-011.开源视频新秀LTX2.0！【文生视频】_2016324432947580929.json, 视频生成/文生视频/LTX2.0多模态大模型-全自动16秒生成-文生视频工作流低配版_2009173213447725058.json, 视频生成/文生视频/LTX2.0多模态大模型-全自动16秒生成-文生视频工作流高配版_2008523919015288834.json, 视频生成/文生视频/LTX2.0多模态大模型-文生视频工作流低配极速生产力版（超15秒）_2011047880521420802.json, 视频生成/文生视频/LTX2.0多模态大模型-文生视频自动提示词工作流_2008854964008914945.json, 视频生成/文生视频/LTX2.0多模态大模型16秒生文生视频工作流_2010893175543570433.json, 视频生成/文生视频/ltx-2文生视频数字人视频快速生成长视频生成ltx2快速生成长视频_2011497494135447554.json, 视频生成/文生视频/音画同步LTX2.0自动优化提示词16秒生成-文生视频_2009286685955198978.json, 视频生成/文生视频/颠覆想象力：LTX2.0多模态文生视频自动优化提示词工作流自动加音效_2015594786417287170.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_17

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/文生视频/AA--音画同步视频-LTX2.0文生视频+放大+插帧_2008918263912206338.json、视频生成/文生视频/LH-DMT-LTX2.0-003.文生视频工作流_2016312568960258049.json、视频生成/文生视频/LH-DMT-LTX2.0-004.自动扩写文生视频_2016319047557718017.json、视频生成/文生视频/LH-DMT-LTX2.0-011.开源视频新秀LTX2.0！【文生视频】_2016324432947580929.json、视频生成/文生视频/LTX2.0多模态大模型-全自动16秒生成-文生视频工作流低配版_2009173213447725058.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：69%

## 共有节点

全部 12 个 workflow 都包含：
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
- `LTXVLatentUpsampler`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveFloat`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`

**可变部分**（部分 workflow 才有）：
- `VHS_VideoCombine` —— 11/12 个有
- `Fast Groups Bypasser (rgthree)` —— 9/12 个有
- `JoinStrings` —— 9/12 个有
- `ShowText|pysssss` —— 9/12 个有
- `easy showAnything` —— 9/12 个有
- `Int` —— 8/12 个有
- `MemoryCleaner` —— 8/12 个有
- `Qwen3_VQA` —— 8/12 个有
- `TextInput_` —— 8/12 个有
- `SimpleMath+` —— 3/12 个有
- `CR Text` —— 2/12 个有
- `CreateVideo` —— 2/12 个有
- `INTConstant` —— 2/12 个有
- `SaveVideo` —— 2/12 个有
- `VAEDecode` —— 2/12 个有
- `CM_FloatBinaryOperation` —— 1/12 个有
- `CM_IntToFloat` —— 1/12 个有
- `FlashVSRNode` —— 1/12 个有
- `JWInteger` —— 1/12 个有
- `LoadImage` —— 1/12 个有
- `Qwen3VL_Advanced` —— 1/12 个有
- `RIFE VFI` —— 1/12 个有
- `SomethingToString` —— 1/12 个有
- `VHS_LoadVideo` —— 1/12 个有
- `VHS_VideoInfo` —— 1/12 个有
- `easy cleanGpuUsed` —— 1/12 个有
- `easy int` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 12 | 100% |
| 高度 | 25 | 25 - 25 | 12 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，12 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，12 个样本，取值集中（一致性 100%）

---
name: unknown_workflow_upscale_latent_upscale_lora_34
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.8351
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, ImageScaleBy, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, ManualSigmas, PrimitiveFloat, PrimitiveInt, RandomNoise, SamplerCustomAdvanced]
problems: []
missing: []
members: [视频生成/文生视频/NVFP4非蒸馏高质量LXT2镜头控制文生视频_2009643822036291585.json, 视频生成/文生视频/ltx2.3文生视频工作流-官方版_2055854688318304257.json, 视频生成/文生视频/ltx2文生视频（运行非常稳定，时长可调，运行速度很快）_2008912681826263041.json, 视频生成/文生视频/video_ltx2_3_t2v文生视频_2032300523310813186.json, 视频生成/文生视频/video_ltx2_t2v_unpack_2008579148603723778.json, 视频生成/文生视频/video_ltx2_t2v文生视频fp8_2011810389457117185.json, 视频生成/文生视频/内置sd2.0，原生4K 文生视频工作流_2046658693634199553.json, 视频生成/文生视频/大凯辰光-LTX-2_T2V_Full-拆分子图版-文生视频工作流_2009155872034922497.json, 视频生成/文生视频/用LTX-2大模型轻松制作搞笑祝福视频，ComfyUI工作流教程来啦！_2010631084064641025.json, 视频生成/文生视频/非蒸馏高质量LXT2镜头控制文生视频_2009183975582994433.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_34

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/文生视频/NVFP4非蒸馏高质量LXT2镜头控制文生视频_2009643822036291585.json、视频生成/文生视频/ltx2.3文生视频工作流-官方版_2055854688318304257.json、视频生成/文生视频/ltx2文生视频（运行非常稳定，时长可调，运行速度很快）_2008912681826263041.json、视频生成/文生视频/video_ltx2_3_t2v文生视频_2032300523310813186.json、视频生成/文生视频/video_ltx2_t2v_unpack_2008579148603723778.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 10 个 workflow 都包含：
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
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveFloat`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 8/10 个有
- `SaveVideo` —— 8/10 个有
- `LTXVCropGuides` —— 7/10 个有
- `VAEDecodeTiled` —— 7/10 个有
- `VAEDecode` —— 4/10 个有
- `CM_FloatToInt` —— 3/10 个有
- `LTXVSpatioTemporalTiledVAEDecode` —— 3/10 个有
- `PrimitiveStringMultiline` —— 3/10 个有
- `Fast Groups Bypasser (rgthree)` —— 2/10 个有
- `VHS_VideoCombine` —— 2/10 个有
- `DeepTranslatorTextNode` —— 1/10 个有
- `GetNode` —— 1/10 个有
- `Label (rgthree)` —— 1/10 个有
- `PreviewAny` —— 1/10 个有
- `SetNode` —— 1/10 个有
- `ShowText|pysssss` —— 1/10 个有
- `Text Multiline` —— 1/10 个有
- `TextGenerateLTX2Prompt` —— 1/10 个有
- `easy cleanGpuUsed` —— 1/10 个有
- `easy clearCacheAll` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 121 | 10 | 89% |
| 高度 | 25 | 25 - 25 | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 121，10 个样本，取值集中（一致性 89%）
- 高度 中位数 25，观测区间 25 - 25，10 个样本，取值集中（一致性 100%）

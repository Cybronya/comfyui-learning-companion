---
name: unknown_workflow_upscale_latent_upscale_lora_47
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.855125
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, CreateVideo, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, ImageScaleBy, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, ManualSigmas, PrimitiveFloat, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SaveVideo]
problems: []
missing: []
members: [视频生成/文生视频/NVFP4非蒸馏高质量LXT2镜头控制图生视频_2009643815291854849.json, 视频生成/文生视频/NVFP4非蒸馏高质量LXT2镜头控制文生视频_2009643822036291585.json, 视频生成/文生视频/ltx2.3文生视频工作流-官方版_2055854688318304257.json, 视频生成/文生视频/video_ltx2_t2v文生视频fp8_2011810389457117185.json, 视频生成/文生视频/内置sd2.0，原生4K 文生视频工作流_2046658693634199553.json, 视频生成/文生视频/大凯辰光-LTX-2_T2V_Full-拆分子图版-文生视频工作流_2009155872034922497.json, 视频生成/文生视频/非蒸馏高质量LXT2镜头控制图生视频_2009191002166267905.json, 视频生成/文生视频/非蒸馏高质量LXT2镜头控制文生视频_2009183975582994433.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_47

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/文生视频/NVFP4非蒸馏高质量LXT2镜头控制图生视频_2009643815291854849.json、视频生成/文生视频/NVFP4非蒸馏高质量LXT2镜头控制文生视频_2009643822036291585.json、视频生成/文生视频/ltx2.3文生视频工作流-官方版_2055854688318304257.json、视频生成/文生视频/video_ltx2_t2v文生视频fp8_2011810389457117185.json、视频生成/文生视频/内置sd2.0，原生4K 文生视频工作流_2046658693634199553.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `CreateVideo`
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
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `CM_FloatToInt` —— 5/8 个有
- `LTXVSpatioTemporalTiledVAEDecode` —— 5/8 个有
- `PrimitiveStringMultiline` —— 5/8 个有
- `Fast Groups Bypasser (rgthree)` —— 4/8 个有
- `LTXVCropGuides` —— 3/8 个有
- `VAEDecodeTiled` —— 3/8 个有
- `ImpactExecutionOrderController` —— 2/8 个有
- `LTXVImgToVideoInplace` —— 2/8 个有
- `LTXVPreprocess` —— 2/8 个有
- `LoadImage` —— 2/8 个有
- `ResizeImagesByLongerEdge` —— 2/8 个有
- `VAEDecode` —— 2/8 个有
- `DeepTranslatorTextNode` —— 1/8 个有
- `GetNode` —— 1/8 个有
- `SetNode` —— 1/8 个有
- `ShowText|pysssss` —— 1/8 个有
- `Text Multiline` —— 1/8 个有
- `easy cleanGpuUsed` —— 1/8 个有
- `easy clearCacheAll` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 121 | 97 - 121 | 8 | 90% |
| 高度 | 25 | 25 - 25 | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 121，观测区间 97 - 121，8 个样本，取值集中（一致性 90%）
- 高度 中位数 25，观测区间 25 - 25，8 个样本，取值集中（一致性 100%）

---
name: unknown_workflow_lora_sampler_clip_23
type: Unknown Workflow
frequency: 13
level: strong
coverage: 0.812308
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, ComfyMathExpression, CreateVideo, EmptyLTXVLatentVideo, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVPreprocess, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, ManualSigmas, RandomNoise, SamplerCustomAdvanced, SaveVideo]
problems: []
missing: []
members: [图片生成/文生图/首尾帧ltx2_3_style_transition+全节点注释_2057807645574254594.json, 视频生成/图生视频/6-LTX 2.3 (FLF) 首尾帧 Start and End Frame_2053476061249323010.json, 视频生成/图生视频/7-LTX2.3_首尾帧 视频工作流_2038606312925306881.json, 视频生成/图生视频/HS-template_ltx2_3_style_transition_2042083663428460545.json, 视频生成/图生视频/LTX 2.3 三种机甲变身(lora) 流_2041514210315735041.json, 视频生成/图生视频/LTX 2.3 变身特效（亦诚视觉原创）_2041734587340038146.json, 视频生成/图生视频/LTX 2.3 多图引导生视频_2082120324979716097.json, 视频生成/图生视频/LTX 2.3 紫色生物机甲变身(lora)_2038207302813097986.json, 视频生成/图生视频/LTX 2.3 首尾帧_2031685383376867330.json, 视频生成/图生视频/LTX 2.3 首尾帧生成视频-调用版_2031928343846723586.json, 视频生成/图生视频/LTX 2.3图生视频_文生视频工作流_2030540846281527298.json, 视频生成/图生视频/LTX 2.3图生视频高清增强版_2075950096994361345.json, 视频生成/图生视频/音画同步图生视频高清版_2081658308183814145.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_23

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/文生图/首尾帧ltx2_3_style_transition+全节点注释_2057807645574254594.json、视频生成/图生视频/6-LTX 2.3 (FLF) 首尾帧 Start and End Frame_2053476061249323010.json、视频生成/图生视频/7-LTX2.3_首尾帧 视频工作流_2038606312925306881.json、视频生成/图生视频/HS-template_ltx2_3_style_transition_2042083663428460545.json、视频生成/图生视频/LTX 2.3 三种机甲变身(lora) 流_2041514210315735041.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 13 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `PrimitiveInt` —— 12/13 个有
- `VAEDecodeTiled` —— 12/13 个有
- `KSamplerSelect` —— 11/13 个有
- `LTXVLatentUpsampler` —— 11/13 个有
- `LatentUpscaleModelLoader` —— 11/13 个有
- `Int` —— 10/13 个有
- `LTXVImgToVideoInplace` —— 10/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 10/13 个有
- `ResizeImageMaskNode` —— 10/13 个有
- `ResizeImagesByLongerEdge` —— 10/13 个有
- `LayerUtility: PurgeVRAM V2` —— 9/13 个有
- `PrimitiveBoolean` —— 9/13 个有
- `PrimitiveStringMultiline` —— 8/13 个有
- `Float` —— 4/13 个有
- `LTXVImgToVideoInplaceKJ` —— 4/13 个有
- `MathExpression|pysssss` —— 4/13 个有
- `ImageResizeKJv2` —— 3/13 个有
- `YC_textReplaceNode` —— 3/13 个有
- `GetImageSize` —— 2/13 个有
- `LTXTiledSampler` —— 2/13 个有
- `LTXVAddGuide` —— 2/13 个有
- `LTXVFirstLastFrameControl_TTP` —— 2/13 个有
- `LTXVLatentUpsamplerTiled` —— 2/13 个有
- `LTXVMiddleFrame_TTP` —— 2/13 个有
- `LayerUtility: TextBox` —— 2/13 个有
- `SamplerEulerAncestral` —— 2/13 个有
- `easy cleanGpuUsed` —— 2/13 个有
- `easy mathInt` —— 2/13 个有
- `ImageResizeKJ` —— 1/13 个有
- `LTXVAddGuideMulti` —— 1/13 个有
- `PreviewImage` —— 1/13 个有
- `SimpleMath+` —— 1/13 个有
- `VAEDecode` —— 1/13 个有
- `YC_ShowText` —— 1/13 个有
- `YC_SingleTextNode` —— 1/13 个有
- `easy clearCacheAll` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 13 | 100% |
| 高度 | 25 | 25 - 25 | 13 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，13 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，13 个样本，取值集中（一致性 100%）

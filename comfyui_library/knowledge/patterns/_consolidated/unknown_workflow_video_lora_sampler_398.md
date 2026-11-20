---
name: unknown_workflow_video_lora_sampler_398
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.958667
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyLTXVLatentVideo, GetImageSize, KSamplerSelect, LTXAVTextEncoderLoader, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVPreprocess, LTXVSeparateAVLatent, LoraLoaderModelOnly, ManualSigmas, PrimitiveBoolean, RandomNoise, SamplerCustomAdvanced, VAEDecodeTiled, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [数字人/数字人/无痕视频扩图 视频编辑 LTX2.3_2042587548962263042.json, 数字人/数字人/视频扩图  视频编辑 LTX 2.3_2042574837587120129.json, 视频生成/图生视频/LTX-2.3 视频动作迁移_2041045547859054594.json, 视频生成/文生视频/01_v2v_Video_Edit_视频编辑_RH_APP_2053497184217247746.json, 视频生成/文生视频/LTX2.3 电影级全向外扩视频工作流_2053375516647931906.json, 视频生成/文生视频/视频扩展3.0｜OmniNFT+Relay+蒸馏1.1｜竖屏扩宽_2058327114209910786.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_398

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（数字人/数字人/无痕视频扩图 视频编辑 LTX2.3_2042587548962263042.json、数字人/数字人/视频扩图  视频编辑 LTX 2.3_2042574837587120129.json、视频生成/图生视频/LTX-2.3 视频动作迁移_2041045547859054594.json、视频生成/文生视频/01_v2v_Video_Edit_视频编辑_RH_APP_2053497184217247746.json、视频生成/文生视频/LTX2.3 电影级全向外扩视频工作流_2053375516647931906.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXAddVideoICLoRAGuide`
- `LTXICLoRALoaderModelOnly`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoConditionOnly`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveBoolean`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CM_FloatToInt` —— 5/6 个有
- `Color Correct (mtb)` —— 5/6 个有
- `Int` —— 5/6 个有
- `Switch image [Crystools]` —— 5/6 个有
- `VHS_VideoInfo` —— 5/6 个有
- `ImageConcanate` —— 4/6 个有
- `ImageResizeKJv2` —— 4/6 个有
- `LoadImage` —— 4/6 个有
- `GemmaAPITextEncode` —— 3/6 个有
- `GetImageSize+` —— 3/6 个有
- `ImagePadKJ` —— 3/6 个有
- `LTXVAudioVAEDecode` —— 3/6 个有
- `PrimitiveString` —— 3/6 个有
- `Text` —— 3/6 个有
- `EmptyImage` —— 2/6 个有
- `LTX2SamplingPreviewOverride` —— 2/6 个有
- `ResizeAndPadImage` —— 2/6 个有
- `ResizeImageMaskNode` —— 2/6 个有
- `Float` —— 1/6 个有
- `FluxResolutionNode` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `SDPoseOODLoader` —— 1/6 个有
- `SDPoseOODProcessor` —— 1/6 个有
- `YOLOModelLoader` —— 1/6 个有
- `easy cleanGpuUsed` —— 1/6 个有
- `easy showAnything` —— 1/6 个有
- `image_scale_pixel_v2` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 6 | 100% |
| 高度 | 25 | 24 - 25 | 6 | 98% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，6 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 24 - 25，6 个样本，取值集中（一致性 98%）

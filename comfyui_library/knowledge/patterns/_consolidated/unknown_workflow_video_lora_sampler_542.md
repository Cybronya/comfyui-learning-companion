---
name: unknown_workflow_video_lora_sampler_542
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.9495
common_nodes: [CFGGuider, CLIPTextEncode, CM_FloatToInt, CheckpointLoaderSimple, EmptyLTXVLatentVideo, GemmaAPITextEncode, GetImageSize, KSamplerSelect, LTXAVTextEncoderLoader, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVPreprocess, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveBoolean, PrimitiveString, RandomNoise, SamplerCustomAdvanced, VAEDecodeTiled, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/01_v2v_Video_Edit_视频编辑_RH_APP_2053497184217247746.json, 视频生成/文生视频/LTX 2.3 IC-LoRA 视频上色工作流（手动提示）_2035643489333022722.json, 视频生成/文生视频/LTX2.3 电影级全向外扩视频工作流_2053375516647931906.json, 视频生成/文生视频/视频扩展3.0｜OmniNFT+Relay+蒸馏1.1｜竖屏扩宽_2058327114209910786.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_542

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/01_v2v_Video_Edit_视频编辑_RH_APP_2053497184217247746.json、视频生成/文生视频/LTX 2.3 IC-LoRA 视频上色工作流（手动提示）_2035643489333022722.json、视频生成/文生视频/LTX2.3 电影级全向外扩视频工作流_2053375516647931906.json、视频生成/文生视频/视频扩展3.0｜OmniNFT+Relay+蒸馏1.1｜竖屏扩宽_2058327114209910786.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CM_FloatToInt`
- `CheckpointLoaderSimple`
- `EmptyLTXVLatentVideo`
- `GemmaAPITextEncode`
- `GetImageSize`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXAddVideoICLoRAGuide`
- `LTXICLoRALoaderModelOnly`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoConditionOnly`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveBoolean`
- `PrimitiveString`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `Color Correct (mtb)` —— 3/4 个有
- `GetImageSize+` —— 3/4 个有
- `ImageConcanate` —— 3/4 个有
- `ImageResizeKJv2` —— 3/4 个有
- `Int` —— 3/4 个有
- `Switch image [Crystools]` —— 3/4 个有
- `VHS_VideoInfo` —— 3/4 个有
- `ResizeAndPadImage` —— 2/4 个有
- `image_scale_pixel_v2` —— 2/4 个有
- `CannyEdgePreprocessor` —— 1/4 个有
- `CreateVideo` —— 1/4 个有
- `DWPreprocessor` —— 1/4 个有
- `DepthCrafter` —— 1/4 个有
- `DownloadAndLoadDepthCrafterModel` —— 1/4 个有
- `Float` —— 1/4 个有
- `FluxResolutionNode` —— 1/4 个有
- `ImagePadKJ` —— 1/4 个有
- `Image_Resize_longsize` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `ResizeImageMaskNode` —— 1/4 个有
- `SaveVideo` —— 1/4 个有
- `SimpleMath+` —— 1/4 个有
- `VHS_VideoInfoLoaded` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 4 | 100% |
| 高度 | 25 | 25 - 25 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，4 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，4 个样本，取值集中（一致性 100%）

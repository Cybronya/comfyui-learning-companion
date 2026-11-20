---
name: unknown_workflow_lora_sampler_clip_25
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.838917
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, ComfyMathExpression, CreateVideo, EmptyLTXVLatentVideo, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVPreprocess, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SaveVideo]
problems: []
missing: []
members: [图片生成/文生图/首尾帧ltx2_3_style_transition+全节点注释_2057807645574254594.json, 视频生成/图生视频/6-LTX 2.3 (FLF) 首尾帧 Start and End Frame_2053476061249323010.json, 视频生成/图生视频/7-LTX 2.3（音频转视频）Image + Audio to Video_2053481289776414721.json, 视频生成/图生视频/Heishen-video_ltx2_3_id_lora_2041874975627415554.json, 视频生成/图生视频/LTX-2.3-Image Audio to Video-distilled-lora-1.1_2044225142284357633.json, 视频生成/图生视频/LTX-2.3图生视频，声画同步_2035291558307700737.json, 视频生成/图生视频/LTX-2.3高动态MV无限时长，一张图一段音频一键生成。_2037366573874290689.json, 视频生成/图生视频/LTX2.3 图 + 音频数字人对口型_2043593704170070018.json, 视频生成/图生视频/LTX2.3-图像音频生视频，口型同步_2031297244112101377.json, 视频生成/图生视频/LTX2.3-数字人（支持双人对话）_2031346405217935361.json, 视频生成/图生视频/LTX2.3_数字人口播_v1.0_（mv数字人）_2054790441681342465.json, 视频生成/图生视频/LTX2.3_数字人口播_v1.1_（自定义音频_图像生视频）_2054484478025838593.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_25

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/首尾帧ltx2_3_style_transition+全节点注释_2057807645574254594.json、视频生成/图生视频/6-LTX 2.3 (FLF) 首尾帧 Start and End Frame_2053476061249323010.json、视频生成/图生视频/7-LTX 2.3（音频转视频）Image + Audio to Video_2053481289776414721.json、视频生成/图生视频/Heishen-video_ltx2_3_id_lora_2041874975627415554.json、视频生成/图生视频/LTX-2.3-Image Audio to Video-distilled-lora-1.1_2044225142284357633.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 12 个 workflow 都包含：
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
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `KSamplerSelect` —— 11/12 个有
- `LTXVLatentUpsampler` —— 11/12 个有
- `LatentUpscaleModelLoader` —— 11/12 个有
- `ResizeImagesByLongerEdge` —— 11/12 个有
- `LTXVImgToVideoInplace` —— 10/12 个有
- `LoadAudio` —— 10/12 个有
- `SolidMask` —— 10/12 个有
- `VAEDecodeTiled` —— 10/12 个有
- `LTXVAudioVAEEncode` —— 9/12 个有
- `PrimitiveFloat` —— 9/12 个有
- `PrimitiveStringMultiline` —— 9/12 个有
- `SetLatentNoiseMask` —— 9/12 个有
- `PrimitiveBoolean` —— 8/12 个有
- `ResizeImageMaskNode` —— 8/12 个有
- `TrimAudioDuration` —— 8/12 个有
- `easy cleanGpuUsed` —— 5/12 个有
- `PreviewAny` —— 4/12 个有
- `LTXVEmptyLatentAudio` —— 3/12 个有
- `LoraLoader` —— 3/12 个有
- `TextGenerateLTX2Prompt` —— 3/12 个有
- `GetImageSize` —— 2/12 个有
- `ImageResizeKJv2` —— 2/12 个有
- `SimpleMath+` —— 2/12 个有
- `SoundFlow_GetLength` —— 2/12 个有
- `VAEDecode` —— 2/12 个有
- `easy clearCacheAll` —— 2/12 个有
- `AudioCrop` —— 1/12 个有
- `ImageResize+` —— 1/12 个有
- `LTXVAddGuide` —— 1/12 个有
- `LTXVImgToVideoInplaceKJ` —— 1/12 个有
- `LTXVReferenceAudio` —— 1/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/12 个有
- `Qwen3ASRLoader_DFT` —— 1/12 个有
- `Qwen3ASRTranscribe_DFT` —— 1/12 个有
- `RecordAudio` —— 1/12 个有
- `SamplerEulerAncestral` —— 1/12 个有
- `StringConcatenate` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 3 | 100% |
| 高度 | 25 | 25 - 25 | 3 | 100% |
| LoRA 模型强度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，3 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，3 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）

---
name: unknown_workflow_video_lora_sampler_569
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.95425
common_nodes: [AudioCropProcessUTK, CFGGuider, CLIPTextEncode, CR Text, CheckpointLoaderSimple, DualCLIPLoader, EmptyLTXVLatentVideo, JWInteger, KSamplerSelect, LTX2SamplingPreviewOverride, LTXVAudioVAEEncode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVPreprocess, LTXVSeparateAVLatent, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoraLoaderModelOnly, ManualSigmas, MathExpression|pysssss, PathchSageAttentionKJ, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SetLatentNoiseMask, SolidMask, TrimAudioDuration, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine, easy float]
problems: []
missing: []
members: [视频生成/图生视频/WH-AI-Studio-LTX2.3数字人_2049324232944914434.json, 视频生成/图生视频/ltx2.3数字人-图生视频_2029926925103276034.json, 视频生成/图生视频/ltx2.3数字人-图生视频无字幕_2069715609595760642.json, 视频生成/文生视频/ltx2.3-文_图生视频-数字人-整合版_2031260976904933377.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_569

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/WH-AI-Studio-LTX2.3数字人_2049324232944914434.json、视频生成/图生视频/ltx2.3数字人-图生视频_2029926925103276034.json、视频生成/图生视频/ltx2.3数字人-图生视频无字幕_2069715609595760642.json、视频生成/文生视频/ltx2.3-文_图生视频-数字人-整合版_2031260976904933377.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 4 个 workflow 都包含：
- `AudioCropProcessUTK`
- `CFGGuider`
- `CLIPTextEncode`
- `CR Text`
- `CheckpointLoaderSimple`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `JWInteger`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTXVAudioVAEEncode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MathExpression|pysssss`
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `SolidMask`
- `TrimAudioDuration`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `easy float`

**可变部分**（部分 workflow 才有）：
- `CR Text Concatenate` —— 3/4 个有
- `LTXVImgToVideoInplace` —— 3/4 个有
- `LayerUtility: PurgeVRAM V2` —— 3/4 个有
- `NormalizeAudioLoudness` —— 3/4 个有
- `PreviewAny` —— 3/4 个有
- `RH_LLMAPI_NODE` —— 3/4 个有
- `RTXVideoSuperResolution` —— 3/4 个有
- `AudioSeparation` —— 2/4 个有
- `LTXVLatentUpsampler` —— 2/4 个有
- `LatentUpscaleModelLoader` —— 2/4 个有
- `LazySwitch1way` —— 2/4 个有
- `RH_LLMAPI_Pro_Node` —— 2/4 个有
- `VAELoader` —— 2/4 个有
- `WhisperSTT` —— 2/4 个有
- `easy compare` —— 2/4 个有
- `AudioInfoNode` —— 1/4 个有
- `Bjornulf_IfElse` —— 1/4 个有
- `CM_FloatToInt` —— 1/4 个有
- `ComfySwitchNode` —— 1/4 个有
- `Float` —— 1/4 个有
- `ImageFromBatch+` —— 1/4 个有
- `ImpactSwitch` —— 1/4 个有
- `JWStringToFloat` —— 1/4 个有
- `LTX2_NAG` —— 1/4 个有
- `LTXVAudioVAEDecode` —— 1/4 个有
- `LTXVEmptyLatentAudio` —— 1/4 个有
- `LTXVImgToVideoInplaceKJ` —— 1/4 个有
- `PrimitiveBoolean` —— 1/4 个有
- `RH_RhartTextG3ProPreviewImageToText` —— 1/4 个有
- `ShowAnything|Mie` —— 1/4 个有
- `easy convertAnything` —— 1/4 个有
- `easy int` —— 1/4 个有
- `ttN concat` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 93 | - | 1 | 100% |
| 高度 | 20 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

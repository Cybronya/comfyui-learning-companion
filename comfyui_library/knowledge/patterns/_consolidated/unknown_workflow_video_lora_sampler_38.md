---
name: unknown_workflow_video_lora_sampler_38
type: Unknown Workflow
frequency: 25
level: strong
coverage: 0.71456
common_nodes: [CFGGuider, CLIPTextEncode, ComfyMathExpression, DualCLIPLoader, EmptyLTXVLatentVideo, KSamplerSelect, LTX2_NAG, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, ManualSigmas, PathchSageAttentionKJ, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/LTX2.3 MSR V2 +自定义声音_2067070674216251394.json, 视频生成/图生视频/LTX2.3 MSR V2 单采-改版-无需上传背景图+自定义音频_2076688428426682370.json, 视频生成/图生视频/LTX2.3 MSR V2 单采-改版-无需上传背景图_2076687501544218626.json, 视频生成/图生视频/LTX2.3 MSR V2 单采升级版+自定义语音_2076686212194193410.json, 视频生成/图生视频/LTX2.3 MSR V2 单采升级版_2076685195511685122.json, 视频生成/图生视频/LTX2.3 MSR V2 参考生视频_2067070625793003522.json, 视频生成/图生视频/LTX2.3 MSR V2 双采+ Customer Audio_2076574537289920514.json, 视频生成/图生视频/LTX2.3 MSR V2 双采_2076575617784569858.json, 视频生成/图生视频/LTX2.3 MSR V2 双采改版-无需上传背景图+自定义音频_2076690587205586945.json, 视频生成/图生视频/LTX2.3 MSR V2 双采改版-无需上传背景图_2076689573417144322.json, 视频生成/图生视频/LTX2.3 MSR V2 双采改版_2083450850885853185.json, 视频生成/图生视频/LTX2.3 MSR V2_2077624792404021250.json, 视频生成/图生视频/LTX2.3 MSR-V2 漫剧工作流_2078684359644762113.json, 视频生成/图生视频/LTX2.3-MSR-V2-多图参考-单采版+自定义语音_2078456447851130881.json, 视频生成/图生视频/LTX2.3-MSR-V2-多图参考-单采版_2077979824391544834.json, 视频生成/图生视频/LTX2.3-MSR-V2-多图参考-双采版+自定义语音-电商带货版_2078651399650504705.json, 视频生成/图生视频/LTX2.3-MSR-V2-多图参考-双采版+自定义语音_2078456551601434625.json, 视频生成/图生视频/LTX2.3-MSR-V2-多图参考-双采版-自动提示词 V2 版_2081280741002006529.json, 视频生成/图生视频/LTX2.3-MSR-V2-多图参考-双采版-自动提示词 V2 版_2081351747490111490.json, 视频生成/图生视频/LTX2.3-MSR-V2-多图参考-双采版-自动提示词_2078828097239080962.json, 视频生成/图生视频/LTX2.3-MSR-V2-多图参考-双采版-自动提示词_2078833439343726593.json, 视频生成/图生视频/LTX2.3-MSR-V2-多图参考-双采版-自动提示词_2078835671065784322.json, 视频生成/图生视频/LTX2.3-MSR-V2-多图参考-双采版_2077960603951525890.json, 视频生成/图生视频/LTX2.3-MSR-V2-多图参考自成视频-提示词自动_双采版_高清放大_2079917333656719361.json, 视频生成/图生视频/LTX2.3MSR-V2_2077234968824205313.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_38

> 由 `engine/knowledge_consolidation` 从 25 个 workflow 归纳得出（视频生成/图生视频/LTX2.3 MSR V2 +自定义声音_2067070674216251394.json、视频生成/图生视频/LTX2.3 MSR V2 单采-改版-无需上传背景图+自定义音频_2076688428426682370.json、视频生成/图生视频/LTX2.3 MSR V2 单采-改版-无需上传背景图_2076687501544218626.json、视频生成/图生视频/LTX2.3 MSR V2 单采升级版+自定义语音_2076686212194193410.json、视频生成/图生视频/LTX2.3 MSR V2 单采升级版_2076685195511685122.json…）

- **类型**：Unknown Workflow
- **样本数**：25
- **可信度**：强结论
- **平均知识覆盖**：71%

## 共有节点

全部 25 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTX2_NAG`
- `LTXAddVideoICLoRAGuide`
- `LTXICLoRALoaderModelOnly`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PathchSageAttentionKJ`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: PurgeVRAM` —— 24/25 个有
- `PrimitiveStringMultiline` —— 24/25 个有
- `UNETLoader` —— 24/25 个有
- `PrimitiveInt` —— 23/25 个有
- `RTXVideoSuperResolution` —— 22/25 个有
- `LiconMSR` —— 20/25 个有
- `FrameInterpolate` —— 19/25 个有
- `FrameInterpolationModelLoader` —— 19/25 个有
- `GetNode` —— 19/25 个有
- `SetNode` —— 19/25 个有
- `LTXVLatentUpsampler` —— 17/25 个有
- `LatentUpscaleModelLoader` —— 17/25 个有
- `LTXVEmptyLatentAudio` —— 16/25 个有
- `LTXVAddGuideMulti` —— 15/25 个有
- `Label (rgthree)` —— 14/25 个有
- `孤海注释` —— 11/25 个有
- `LTXVAudioVAEEncode` —— 9/25 个有
- `LoadAudio` —— 9/25 个有
- `PromptRelayEncode` —— 9/25 个有
- `SetLatentNoiseMask` —— 9/25 个有
- `SolidMask` —— 9/25 个有
- `TrimAudioDuration` —— 9/25 个有
- `MelBandRoFormerModelLoader` —— 8/25 个有
- `MelBandRoFormerSampler` —— 8/25 个有
- `BatchImagesNode` —— 6/25 个有
- `RepeatImageBatch` —— 6/25 个有
- `PreviewAudio` —— 5/25 个有
- `LTXTiledSampler` —— 4/25 个有
- `Int` —— 3/25 个有
- `CR Prompt Text` —— 1/25 个有
- `ImageOnlyCheckpointLoader` —— 1/25 个有
- `PromptRelayEncodeTimeline` —— 1/25 个有
- `RHHiddenNodes` —— 1/25 个有
- `RHLLMChatNode` —— 1/25 个有
- `Text` —— 1/25 个有
- `easy showAnything` —— 1/25 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 16 | 100% |
| 高度 | 44 | 44 - 44 | 16 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，16 个样本，取值集中（一致性 100%）
- 高度 中位数 44，观测区间 44 - 44，16 个样本，取值集中（一致性 100%）

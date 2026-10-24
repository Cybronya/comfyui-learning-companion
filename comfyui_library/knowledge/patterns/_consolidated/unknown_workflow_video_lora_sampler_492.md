---
name: unknown_workflow_video_lora_sampler_492
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.71
common_nodes: [AddLabel, CFGGuider, CLIPTextEncode, DualCLIPLoader, EmptyLTXVLatentVideo, GetImageSizeAndCount, ImageConcanate, ImageResizeKJv2, KSamplerSelect, LTX2SamplingPreviewOverride, LTX2_NAG, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVAudioVAEDecode, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVPreprocess, LTXVSeparateAVLatent, LoadImage, ManualSigmas, ModelPatchTorchSettings, PathchSageAttentionKJ, RandomNoise, SamplerCustomAdvanced, Seed (rgthree), SimpleCalculatorKJ, UNETLoader, VAEDecode, VAELoader, VAELoaderKJ, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/LTX2.3 图生视频｜+参考视频运镜（仅参考运镜）  IC LoRA_2042074773987008513.json, 视频生成/图生视频/LTX2.3 图生视频｜+参考视频运镜（仅参考运镜）  IC LoRA_2046118754756595713.json, 视频生成/图生视频/LTX2.3运镜参考不限时长_2072521435817537538.json, 视频生成/图生视频/ltx2.3-ic-lora-cameraman_2072140620956790785.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_492

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/LTX2.3 图生视频｜+参考视频运镜（仅参考运镜）  IC LoRA_2042074773987008513.json、视频生成/图生视频/LTX2.3 图生视频｜+参考视频运镜（仅参考运镜）  IC LoRA_2046118754756595713.json、视频生成/图生视频/LTX2.3运镜参考不限时长_2072521435817537538.json、视频生成/图生视频/ltx2.3-ic-lora-cameraman_2072140620956790785.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：71%

## 共有节点

全部 4 个 workflow 都包含：
- `AddLabel`
- `CFGGuider`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetImageSizeAndCount`
- `ImageConcanate`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `LTXAddVideoICLoRAGuide`
- `LTXICLoRALoaderModelOnly`
- `LTXVAudioVAEDecode`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoConditionOnly`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `ManualSigmas`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `Seed (rgthree)`
- `SimpleCalculatorKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `FL_FloatToInt` —— 2/4 个有
- `FloatConstant` —— 2/4 个有
- `GetNode` —— 2/4 个有
- `INTConstant` —— 2/4 个有
- `LTX2MemoryEfficientSageAttentionPatch` —— 2/4 个有
- `LTXVLatentUpsampler` —— 2/4 个有
- `LatentUpscaleModelLoader` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `MemoryCleaner` —— 2/4 个有
- `PrimitiveFloat` —— 2/4 个有
- `PrimitiveInt` —— 2/4 个有
- `ReverseImageBatch` —— 2/4 个有
- `SetNode` —— 2/4 个有
- `TextBox1` —— 2/4 个有
- `easy cleanGpuUsed` —— 2/4 个有
- `easy showAnything` —— 2/4 个有
- `CR Text Concatenate` —— 1/4 个有
- `LTXVContextWindows` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `PrimitiveStringMultiline` —— 1/4 个有
- `RH_Captioner` —— 1/4 个有
- `RH_Translator` —— 1/4 个有
- `easy convertAnything` —— 1/4 个有

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

---
name: unknown_workflow_video_lora_sampler_30
type: Unknown Workflow
frequency: 25
level: moderate
coverage: 0.91144
common_nodes: [BasicScheduler, CLIPTextEncode, ConditioningZeroOut, DF_Int_to_Float, DualCLIPLoader, EmptyLTXVLatentVideo, ImageResizeKJv2, Int, KSamplerSelect, LTX2SamplingPreviewOverride, LTX2_NAG, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, PrimitiveInt, SamplerCustom, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VAELoaderKJ, VHS_VideoCombine, VisualizeSigmasKJ]
problems: []
missing: []
members: [数字人/数字人/LTX2.3脱口秀一键制作_2087497245485780994.json, 视频生成/图生视频/2057094606336118785.json, 视频生成/图生视频/2081970099841495042.json, 视频生成/图生视频/2082088616767086594.json, 视频生成/图生视频/2070813395804319745.json, 视频生成/图生视频/2071195369723224066.json, 视频生成/图生视频/2076994911257317377.json, 视频生成/图生视频/LTX2.3极速文_图生视频脱口秀爆款工作流_2083129366271315970.json, 视频生成/图生视频/LTX2.3极速文_图生视频脱口秀爆款工作流_2083162929670737922.json, 视频生成/图生视频/LTX2.3极速文_图生视频脱口秀爆款工作流_2095825968475758593.json, 视频生成/图生视频/LTX2.3极速文_图生视频脱口秀爆款工作流_2095831915289993217.json, 视频生成/图生视频/LTX2.3极速文_图生视频脱口秀爆款工作流_2103436354901340161.json, 视频生成/图生视频/LTX2.3极速文_图生视频脱口秀爆款工作流_2103452178303250433.json, 视频生成/图生视频/LTX2.3极速文_图生视频脱口秀爆款工作流_2111305228783013889.json, 视频生成/图生视频/2050899507684098050.json, 视频生成/图生视频/2069653521200402433.json, 视频生成/图生视频/2070743071674945537.json, 视频生成/图生视频/2072940595001249794.json, 视频生成/图生视频/脱口秀爆款-LTX2.3极速文_图生视频工作流_2074485641030750209.json, 视频生成/文生视频/LTX2.3-OmniNFT-RL-Lora 文_图生视频_2057113427591647233.json, 视频生成/文生视频/LTX2.3-亲子对话-文生视频工作流--搞笑视频_2083450669406711809.json, 视频生成/文生视频/LTX2.3极速-文_图生视频_2048020134731718657.json, 视频生成/文生视频/LTX2.3极速-文_图生视频_可选放大_2048719748099219457.json, 视频生成/文生视频/LTX2.3脱口秀一键制作_2043887479178141698.json, 视频生成/文生视频/LTX不出字幕单图参考_无压缩参考_2049840291389157378.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_30

> 由 `engine/knowledge_consolidation` 从 25 个 workflow 归纳得出（数字人/数字人/LTX2.3脱口秀一键制作_2087497245485780994.json、视频生成/图生视频/2057094606336118785.json、视频生成/图生视频/2081970099841495042.json、视频生成/图生视频/2082088616767086594.json、视频生成/图生视频/2070813395804319745.json…）

- **类型**：Unknown Workflow
- **样本数**：25
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 25 个 workflow 都包含：
- `BasicScheduler`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DF_Int_to_Float`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `ImageResizeKJv2`
- `Int`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PrimitiveInt`
- `SamplerCustom`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `VisualizeSigmasKJ`

**可变部分**（部分 workflow 才有）：
- `LTXVImgToVideoConditionOnly` —— 23/25 个有
- `LTXVPreprocess` —— 23/25 个有
- `PrimitiveBoolean` —— 23/25 个有
- `VRAMReserver` —— 23/25 个有
- `easy getNode` —— 23/25 个有
- `easy setNode` —— 23/25 个有
- `CFGGuider` —— 22/25 个有
- `LTXVLatentUpsampler` —— 22/25 个有
- `LatentUpscaleModelLoader` —— 22/25 个有
- `ManualSigmas` —— 22/25 个有
- `RandomNoise` —— 22/25 个有
- `SamplerCustomAdvanced` —— 22/25 个有
- `LTXVImgToVideoInplace` —— 21/25 个有
- `Fast Groups Bypasser (rgthree)` —— 20/25 个有
- `LTXVCropGuides` —— 20/25 个有
- `GetNode` —— 2/25 个有
- `LTXVImgToVideoInplaceKJ` —— 2/25 个有
- `MathExpression|pysssss` —— 2/25 个有
- `MuyeTextEditOutput` —— 2/25 个有
- `PreviewAny` —— 2/25 个有
- `SetNode` —— 2/25 个有
- `CR Prompt Text` —— 1/25 个有
- `PromptRelayEncodeTimeline` —— 1/25 个有
- `Text` —— 1/25 个有
- `easy positive` —— 1/25 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 305 | 25 | 50% |
| 高度 | 25 | 24 - 25 | 25 | 99% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 305，25 个样本
- 高度 中位数 25，观测区间 24 - 25，25 个样本，取值集中（一致性 99%）

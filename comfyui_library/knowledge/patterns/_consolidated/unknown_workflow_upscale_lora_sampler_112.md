---
name: unknown_workflow_upscale_lora_sampler_112
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.822
common_nodes: [AILab_ImagePreview, BasicScheduler, CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, DetailDaemonGraphSigmasNode, DetailDaemonSamplerNode, EmptyLatentImage, Image Comparer (rgthree), KSamplerSelect, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, SaveImage, Seed (rgthree), SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader, VRAMReserver, easy int]
problems: []
missing: []
members: [图片生成/文生图/Lora训练_Z-Image-i2L_2019993856825102337.json, 图片生成/文生图/图片生成_Z-Image-Turbo_Detail-Daemon_增加细节_去除竖纹_2013923317299810306.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_112

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Lora训练_Z-Image-i2L_2019993856825102337.json、图片生成/文生图/图片生成_Z-Image-Turbo_Detail-Daemon_增加细节_去除竖纹_2013923317299810306.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 2 个 workflow 都包含：
- `AILab_ImagePreview`
- `BasicScheduler`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DetailDaemonGraphSigmasNode`
- `DetailDaemonSamplerNode`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `Seed (rgthree)`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VRAMReserver`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `BiRefNetRMBG` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `ImageBatchMulti` —— 1/2 个有
- `ImageResizeKJv2` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `PreviewAny` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `RunningHub_ZImageI2L_Loader` —— 1/2 个有
- `RunningHub_ZImageI2L_LoraGenerator` —— 1/2 个有
- `RunningHub_ZImageI2L_Saver` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `StringConcatenate` —— 1/2 个有
- `WD14Tagger|pysssss` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | - | 2 | 100% |
| 高度 | 512 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

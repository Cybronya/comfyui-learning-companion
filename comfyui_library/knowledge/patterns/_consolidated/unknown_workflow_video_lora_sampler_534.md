---
name: unknown_workflow_video_lora_sampler_534
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.90075
common_nodes: [1hew_StringJoinMulti, AnyBooleanSwitch, CFGGuider, CLIPLoader, CLIPTextEncode, DownloadAndLoadGIMMVFIModel, EmptyFlux2LatentImage, Fast Groups Bypasser (rgthree), Flux2Scheduler, GIMMVFI_interpolate, GetImageSize, INTConstant, ImageConcatMulti, ImageScaleToTotalPixels, ImpactControlBridge, ImpactNeg, Int, KSamplerAdvanced, KSamplerSelect, Logic Comparison AND, LoraLoaderModelOnly, ModelSamplingSD3, PainterVRAM, PathchSageAttentionKJ, PreviewAny, PrimitiveBoolean, PrimitiveInt, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SimpleMath+, Text Multiline, UNETLoader, VAEDecode, VAEEncode, VAELoader, VHS_VideoCombine, WanImageToVideo, ZML_AnyTypeSwitchFive, easy ifElse, workflow>load image01, workflow>load image02, workflow>load image03]
problems: []
missing: []
members: [视频生成/图生视频/2027331216810184706.json, 视频生成/图生视频/2039915994931531777.json, 视频生成/图生视频/2040088399033405441.json, 视频生成/文生视频/AI换装丨Flux2-Klein＋Wan2.2丨换装试穿·转身视频_2099769122765758466.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_534

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/2027331216810184706.json、视频生成/图生视频/2039915994931531777.json、视频生成/图生视频/2040088399033405441.json、视频生成/文生视频/AI换装丨Flux2-Klein＋Wan2.2丨换装试穿·转身视频_2099769122765758466.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 4 个 workflow 都包含：
- `1hew_StringJoinMulti`
- `AnyBooleanSwitch`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `DownloadAndLoadGIMMVFIModel`
- `EmptyFlux2LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Flux2Scheduler`
- `GIMMVFI_interpolate`
- `GetImageSize`
- `INTConstant`
- `ImageConcatMulti`
- `ImageScaleToTotalPixels`
- `ImpactControlBridge`
- `ImpactNeg`
- `Int`
- `KSamplerAdvanced`
- `KSamplerSelect`
- `Logic Comparison AND`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PainterVRAM`
- `PathchSageAttentionKJ`
- `PreviewAny`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SimpleMath+`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`
- `ZML_AnyTypeSwitchFive`
- `easy ifElse`
- `workflow>load image01`
- `workflow>load image02`
- `workflow>load image03`

**可变部分**（部分 workflow 才有）：
- `TT_img_enc_v2` —— 1/4 个有
- `TextBox` —— 1/4 个有
- `Textbox` —— 1/4 个有
- `ZML_SwitchOutput` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 4 | 100% |
| Prompt 约束强度(CFG) | 12 | 4 - 12 | 4 | 65% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | euler | - | 4 | 100% |
| 重绘幅度 | simple | - | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，4 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 12，观测区间 4 - 12，4 个样本
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，4 个样本，一致性 100%
- 重绘幅度 最常用 simple，4 个样本，一致性 100%

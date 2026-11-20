---
name: unknown_workflow_video_sampler_8
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.945
common_nodes: [LoadWanVideoT5TextEncoder, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddFlashVSRInput, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoExtraModelSelect, WanVideoFlashVSRDecoderLoader, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode]
problems: []
missing: []
members: [平台全量/(KJ版)Wan FlashVSR视频模糊变高清V1_1980932757046083586.json, 平台全量/007.其他-功能风格007.FlashVSR视频高清放大_2035408088685092866.json, 平台全量/03-17-01-WAN2.1-视频放大-FlashVSR_1992616873007312897.json, 平台全量/8-03.FlashVSR视频高清化工作流-好用_1992411531159687169.json, 平台全量/Charlie工作流_2079765261464461313.json, 平台全量/Flash VSR视频高清放大(KJ Wan)-无伪影_1982375598792294401.json, 平台全量/FlashVSR 视频快速修复高清化_1980518485581283330.json, 平台全量/FlashVSR 视频超清_1980575347118919682.json, 平台全量/FlashVSR视频快速修复高清化【全自动版】_1980173197142298625.json, 平台全量/FlashVSR视频高清化_1979571792933195777.json, 平台全量/FlashVSR视频高清化工作流01_1980678216677507073.json, 平台全量/FlashVSR视频高清化工作流_1978558470179934210.json, 平台全量/FlashVSR视频高清化工作流_1987190396440784897.json, 平台全量/kijiai版-FlashVSR视频高清化工作流_1979187013129768962.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_8

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（平台全量/(KJ版)Wan FlashVSR视频模糊变高清V1_1980932757046083586.json、平台全量/007.其他-功能风格007.FlashVSR视频高清放大_2035408088685092866.json、平台全量/03-17-01-WAN2.1-视频放大-FlashVSR_1992616873007312897.json、平台全量/8-03.FlashVSR视频高清化工作流-好用_1992411531159687169.json、平台全量/Charlie工作流_2079765261464461313.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 14 个 workflow 都包含：
- `LoadWanVideoT5TextEncoder`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAddFlashVSRInput`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoExtraModelSelect`
- `WanVideoFlashVSRDecoderLoader`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`

**可变部分**（部分 workflow 才有）：
- `ImageConcatMulti` —— 13/14 个有
- `GetImageSizeAndCount` —— 12/14 个有
- `ImageResizeKJv2` —— 11/14 个有
- `WanVideoTorchCompileSettings` —— 10/14 个有
- `VHS_VideoInfoLoaded` —— 6/14 个有
- `VHS_VideoInfo` —— 4/14 个有
- `ColorMatch` —— 3/14 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/14 个有
- `Fast Groups Bypasser (rgthree)` —— 1/14 个有
- `ImageBlur` —— 1/14 个有
- `JWInteger` —— 1/14 个有
- `Note Plus (mtb)` —— 1/14 个有
- `PrimitiveFloat` —— 1/14 个有
- `PrimitiveInt` —— 1/14 个有
- `WanVideoBlockSwap` —— 1/14 个有
- `WanVideoEnhanceAVideo` —— 1/14 个有
- `WanVideoSLG` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

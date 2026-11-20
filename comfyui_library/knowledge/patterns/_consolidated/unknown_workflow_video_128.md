---
name: unknown_workflow_video_128
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.465
common_nodes: [Fast Bypasser (rgthree), GetNode, ImageScaleToTotalPixels, Int, MathExpression_UTK, Mute / Bypass Repeater (rgthree), PreviewImage, RIFE VFI, SeedVR2, SeedVR2BlockSwap, SeedVR2ExtraArgs, SetNode, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoSource, easy showAnything]
problems: []
missing: []
members: [平台全量/3.0最新视频高清放大+补帧_2066124873759551489.json, 平台全量/SeedVR2 7B视频超分＋补帧｜一键拯救老视频 音画同步_2060180598379081729.json, 平台全量/SeedVR2+GIMM 视频高清放大+补帧_2049727921593524226.json]
source: knowledge_consolidation
---

# unknown_workflow_video_128

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/3.0最新视频高清放大+补帧_2066124873759551489.json、平台全量/SeedVR2 7B视频超分＋补帧｜一键拯救老视频 音画同步_2060180598379081729.json、平台全量/SeedVR2+GIMM 视频高清放大+补帧_2049727921593524226.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：46%

## 共有节点

全部 3 个 workflow 都包含：
- `Fast Bypasser (rgthree)`
- `GetNode`
- `ImageScaleToTotalPixels`
- `Int`
- `MathExpression_UTK`
- `Mute / Bypass Repeater (rgthree)`
- `PreviewImage`
- `RIFE VFI`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoSource`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 2/3 个有
- `CLIPTextEncode` —— 1/3 个有
- `CheckpointLoaderSimple` —— 1/3 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/3 个有
- `GIMMVFI_interpolate` —— 1/3 个有
- `Text` —— 1/3 个有
- `TextInput_` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

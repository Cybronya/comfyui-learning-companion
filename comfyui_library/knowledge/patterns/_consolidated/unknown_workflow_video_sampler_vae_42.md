---
name: unknown_workflow_video_sampler_vae_42
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.593
common_nodes: [GetNode, LoadWanVideoT5TextEncoder, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader, easy int, easy positive]
problems: []
missing: []
members: [图片生成/图生图/Wan Vace 14B  视频扩图工作流_1923647335333548033.json, 平台全量/GTP4O-荧光吉卜力风格_1932409629588779010.json, 平台全量/WAN视频风格转绘_1936768347985858562.json, 平台全量/WAN视频风格转绘_1937318918589456385.json, 平台全量/Wan2.1 VACE风格视频转绘_1948583334376013825.json, 平台全量/Wan2.1 吉卜力风格视频转绘_2030899997117521922.json, 平台全量/wan 吉卜力风格视频转绘_1919217770158817281.json, 平台全量/视频外扩_1933061319216205825.json, 视频生成/图生视频/VACE Controlnet控制视频_1913722846840061953.json, 视频生成/图生视频/Wan Vace 14B  扩充电影镜头_1923521881121746946.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_42

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/Wan Vace 14B  视频扩图工作流_1923647335333548033.json、平台全量/GTP4O-荧光吉卜力风格_1932409629588779010.json、平台全量/WAN视频风格转绘_1936768347985858562.json、平台全量/WAN视频风格转绘_1937318918589456385.json、平台全量/Wan2.1 VACE风格视频转绘_1948583334376013825.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：59%

## 共有节点

全部 10 个 workflow 都包含：
- `GetNode`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`
- `easy int`
- `easy positive`

**可变部分**（部分 workflow 才有）：
- `GetImageSize+` —— 9/10 个有
- `GetImageSizeAndCount` —— 9/10 个有
- `GoogleTranslateTextNode` —— 9/10 个有
- `ImageConcatMulti` —— 9/10 个有
- `JoinStrings` —— 9/10 个有
- `MiniCPM_VQA_Polished` —— 9/10 个有
- `WanVideoLoraSelect` —— 9/10 个有
- `WanVideoTeaCache` —— 9/10 个有
- `easy seed` —— 9/10 个有
- `easy showAnything` —— 9/10 个有
- `AddLabel` —— 8/10 个有
- `Bookmark (rgthree)` —— 8/10 个有
- `WanVideoEnhanceAVideo` —— 8/10 个有
- `DepthAnythingV2Preprocessor` —— 7/10 个有
- `ImageFromBatch` —— 7/10 个有
- `Label (rgthree)` —— 7/10 个有
- `PreviewImage` —— 7/10 个有
- `VHS_VideoInfo` —— 7/10 个有
- `ImageResizeKJv2` —— 6/10 个有
- `WanVideoContextOptions` —— 6/10 个有
- `easy anythingIndexSwitch` —— 6/10 个有
- `PrimitiveString` —— 5/10 个有
- `Any Switch (rgthree)` —— 4/10 个有
- `Fast Groups Muter (rgthree)` —— 4/10 个有
- `Note Plus (mtb)` —— 4/10 个有
- `String Literal` —— 4/10 个有
- `EmptyImage` —— 3/10 个有
- `GetImageRangeFromBatch` —— 3/10 个有
- `ImagePadKJ` —— 3/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/10 个有
- `MaskPreview+` —— 3/10 个有
- `Mute / Bypass Relay (rgthree)` —— 2/10 个有
- `Mute / Bypass Repeater (rgthree)` —— 2/10 个有
- `VHS_VideoInfoLoaded` —— 2/10 个有
- `DWPreprocessor` —— 1/10 个有
- `ImageCompositeMasked` —— 1/10 个有
- `ImageRemoveBackground+` —— 1/10 个有
- `ImageResizeKJ` —— 1/10 个有
- `LayerUtility: ImageRemoveAlpha` —— 1/10 个有
- `LoadImage` —— 1/10 个有
- `LoadImageFromUrl` —— 1/10 个有
- `RemBGSession+` —— 1/10 个有
- `WanVideoVRAMManagement` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

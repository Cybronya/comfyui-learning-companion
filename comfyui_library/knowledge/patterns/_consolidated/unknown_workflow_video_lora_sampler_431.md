---
name: unknown_workflow_video_lora_sampler_431
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.669
common_nodes: [GetImageSizeAndCount, LoadWanVideoT5TextEncoder, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/线稿引导花花改款_1951909446714904578.json, 平台全量/🈚️VACE-视频扩展画布-wan-Lightx_1951722601280385026.json, 视频生成/图生视频/MoviiGen + VACE首尾帧-加速版_1923694325656711169.json, 视频生成/图生视频/Q版人物跳舞_1934473934488162306.json, 视频生成/图生视频/Q版动漫小人跳舞工作流_1925467982229590018.json, 视频生成/图生视频/Q版动漫小人跳舞工作流_1932748571013697538.json, 视频生成/图生视频/wan2.1 万相 Q版卡通动漫角色跳舞视频动画_1936291028129206274.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_431

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（平台全量/线稿引导花花改款_1951909446714904578.json、平台全量/🈚️VACE-视频扩展画布-wan-Lightx_1951722601280385026.json、视频生成/图生视频/MoviiGen + VACE首尾帧-加速版_1923694325656711169.json、视频生成/图生视频/Q版人物跳舞_1934473934488162306.json、视频生成/图生视频/Q版动漫小人跳舞工作流_1925467982229590018.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：67%

## 共有节点

全部 7 个 workflow 都包含：
- `GetImageSizeAndCount`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 6/7 个有
- `ImageResizeKJv2` —— 6/7 个有
- `LoadImage` —— 6/7 个有
- `VHS_LoadVideo` —— 6/7 个有
- `WanVideoExperimentalArgs` —— 6/7 个有
- `WanVideoSLG` —— 6/7 个有
- `WanVideoTorchCompileSettings` —— 6/7 个有
- `WanVideoVACEStartToEndFrame` —— 6/7 个有
- `WanVideoTeaCache` —— 5/7 个有
- `AddLabel` —— 4/7 个有
- `EmptyImage` —— 4/7 个有
- `ImageConcatMulti` —— 4/7 个有
- `Bookmark (rgthree)` —— 3/7 个有
- `Label (rgthree)` —— 3/7 个有
- `Fast Groups Bypasser (rgthree)` —— 2/7 个有
- `Any Switch (rgthree)` —— 1/7 个有
- `GetMaskSizeAndCount` —— 1/7 个有
- `ImagePadKJ` —— 1/7 个有
- `ImageResize+` —— 1/7 个有
- `PrimitiveInt` —— 1/7 个有
- `PrimitiveStringMultiline` —— 1/7 个有
- `VHS_VideoInfo` —— 1/7 个有
- `WanVideoUniAnimateDWPoseDetector` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

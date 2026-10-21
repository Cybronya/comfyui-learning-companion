---
name: unknown_workflow_video_sampler_vae_72
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.969
common_nodes: [GetImageSizeAndCount, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoVACEEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1934640445391872001.json, 视频生成/图生视频/1934644328725684226.json, 视频生成/图生视频/1943227565869842433.json, 视频生成/图生视频/1925111334327754753.json, 视频生成/图生视频/1922724321020579841.json, 视频生成/图生视频/1923332542534250497.json, 视频生成/图生视频/1934807918095343617.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_72

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/1934640445391872001.json、视频生成/图生视频/1934644328725684226.json、视频生成/图生视频/1943227565869842433.json、视频生成/图生视频/1925111334327754753.json、视频生成/图生视频/1922724321020579841.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 7 个 workflow 都包含：
- `GetImageSizeAndCount`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoVACEEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJ` —— 6/7 个有
- `WanVideoTextEncode` —— 6/7 个有
- `AddLabel` —— 4/7 个有
- `EmptyImage` —— 4/7 个有
- `ImageConcatMulti` —— 4/7 个有
- `LoadImage` —— 4/7 个有
- `MaskPreview+` —— 4/7 个有
- `PreviewImage` —— 4/7 个有
- `WanVideoTeaCache` —— 4/7 个有
- `WanVideoVACEStartToEndFrame` —— 4/7 个有
- `GetImageRangeFromBatch` —— 3/7 个有
- `ImagePadKJ` —— 3/7 个有
- `LayerUtility: PurgeVRAM V2` —— 3/7 个有
- `VHS_LoadVideo` —— 3/7 个有
- `WanVideoMagCache` —— 3/7 个有
- `WanVideoVACEModelSelect` —— 3/7 个有
- `easy int` —— 3/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/7 个有
- `RH_Translator` —— 2/7 个有
- `Text` —— 1/7 个有
- `WanVideoApplyNAG` —— 1/7 个有
- `WanVideoTextEncodeSingle` —— 1/7 个有
- `easy cleanGpuUsed` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

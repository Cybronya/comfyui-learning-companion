---
name: unknown_workflow_video_sampler_vae_162
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.847333
common_nodes: [DownloadAndLoadSAM2Model, GrowMaskWithBlur, INTConstant, ImageConcatMulti, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, MaskToImage, Mix Color By Mask, PreviewImage, Sam2Segmentation, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVAELoader, easy imageRemBg]
problems: []
missing: []
members: [视频生成/图生视频/VACE视频编辑-灵活编辑区_1956277495895130113.json, 视频生成/图生视频/VACE视频编辑-精准遮罩选择_1956282329440419841.json, 视频生成/图生视频/【大炮视频】VACE视频角色替换_1926909240341073922.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_162

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/VACE视频编辑-灵活编辑区_1956277495895130113.json、视频生成/图生视频/VACE视频编辑-精准遮罩选择_1956282329440419841.json、视频生成/图生视频/【大炮视频】VACE视频角色替换_1926909240341073922.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `DownloadAndLoadSAM2Model`
- `GrowMaskWithBlur`
- `INTConstant`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MaskToImage`
- `Mix Color By Mask`
- `PreviewImage`
- `Sam2Segmentation`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVAELoader`
- `easy imageRemBg`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Muter (rgthree)` —— 2/3 个有
- `PointsEditor` —— 2/3 个有
- `WanVideoFreeInitArgs` —— 2/3 个有
- `WanVideoLoraSelect` —— 2/3 个有
- `CR Text` —— 1/3 个有
- `Florence2ModelLoader` —— 1/3 个有
- `Florence2Run` —— 1/3 个有
- `Florence2toCoordinates` —— 1/3 个有
- `LayerUtility: JoyCaptionBeta1` —— 1/3 个有
- `LayerUtility: JoyCaptionBeta1ExtraOptions` —— 1/3 个有
- `LayerUtility: LoadJoyCaptionBeta1Model` —— 1/3 个有
- `MaskPreview+` —— 1/3 个有
- `Note Plus (mtb)` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有
- `WanVideoSLG` —— 1/3 个有
- `WanVideoTeaCache` —— 1/3 个有
- `WanVideoVACEModelSelect` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

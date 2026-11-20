---
name: unknown_workflow_video_lora_sampler_314
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.665667
common_nodes: [DownloadAndLoadSAM2Model, GetImageRangeFromBatch, GetNode, ImageResizeKJv2, LoadImage, MaskPreview, MochaEmbeds, PointsEditor, Sam2Segmentation, SetNode, VHS_LoadVideo, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/Mocha视频人物替换动作迁移_2002050355389186050.json, 平台全量/wanvideo_MoCha_replace_subject_1982722865655095298.json, 平台全量/wanvideo_MoCha_replace_subject_KJ_02_666_2000937921249148930.json, 平台全量/（（自用）-双参N版）Wan2.1 Mocha V2V人物视频替换V1（优化加速版）_1981010326328053761.json, 数字人/数字人/Mocha一键人物替换，快速_1981583280208265218.json, 数字人/数字人/mocha视频角色替换人物替换更换人物更换任意角色工作流_2003477047525711873.json, 视频生成/图生视频/视频人物替换 Mocha_1979526023647760386.json, 视频生成/图生视频/（单参版）Wan2.1 Mocha V2V人物视频替换V2（优化加速版）_1980912658343968770.json, 视频生成/文生视频/（双参版）Wan2.1 Mocha V2V人物视频替换V2（优化加速版）_1980845806502760449.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_314

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（平台全量/Mocha视频人物替换动作迁移_2002050355389186050.json、平台全量/wanvideo_MoCha_replace_subject_1982722865655095298.json、平台全量/wanvideo_MoCha_replace_subject_KJ_02_666_2000937921249148930.json、平台全量/（（自用）-双参N版）Wan2.1 Mocha V2V人物视频替换V1（优化加速版）_1981010326328053761.json、数字人/数字人/Mocha一键人物替换，快速_1981583280208265218.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：67%

## 共有节点

全部 9 个 workflow 都包含：
- `DownloadAndLoadSAM2Model`
- `GetImageRangeFromBatch`
- `GetNode`
- `ImageResizeKJv2`
- `LoadImage`
- `MaskPreview`
- `MochaEmbeds`
- `PointsEditor`
- `Sam2Segmentation`
- `SetNode`
- `VHS_LoadVideo`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 8/9 个有
- `RMBG` —— 8/9 个有
- `VHS_VideoCombine` —— 8/9 个有
- `Crop Face` —— 6/9 个有
- `GrowMask` —— 6/9 个有
- `ImageConcanate` —— 6/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/9 个有
- `Load RetinaFace` —— 6/9 个有
- `VHS_VideoInfo` —— 6/9 个有
- `CR Prompt Text` —— 3/9 个有
- `GrowMaskWithBlur` —— 3/9 个有
- `Int` —— 3/9 个有
- `JWInteger` —— 3/9 个有
- `PDIMAGE_LongerSize` —— 3/9 个有
- `SaveImage` —— 3/9 个有
- `WanVideoSetBlockSwap` —— 3/9 个有
- `WanVideoTorchCompileSettings` —— 2/9 个有
- `Anything Everywhere` —— 1/9 个有
- `LayerUtility: PurgeVRAM` —— 1/9 个有
- `TT_img_enc` —— 1/9 个有
- `TT_img_enc_v2` —— 1/9 个有
- `easy cleanGpuUsed` —— 1/9 个有
- `easy int` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

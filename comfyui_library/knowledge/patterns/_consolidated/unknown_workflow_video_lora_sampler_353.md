---
name: unknown_workflow_video_lora_sampler_353
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.631
common_nodes: [GetImageRangeFromBatch, GetNode, ImageResizeKJv2, LoadImage, MaskPreview, MochaEmbeds, PointsEditor, PreviewImage, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/AI视频换狗，只需上传小狗照片，MoCha就能一键换狗！_1983104032732540930.json, 平台全量/MoCha一键AI视频换人，一起来唱《万物生来财版》_1981645125153628161.json, 平台全量/MoCha替换视频主角_1992797393477496834.json, 平台全量/Mocha-新的视频角色替换_1982629679557419010.json, 平台全量/Mocha-视频主题替换（单人）工作流_1981536284206342146.json, 平台全量/Mocha人物替换_1999764665200766978.json, 平台全量/Mocha真人转动漫视频生成_1980910280488210434.json, 平台全量/角色迁移（MoCha版）_1985547299260612609.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_353

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（平台全量/AI视频换狗，只需上传小狗照片，MoCha就能一键换狗！_1983104032732540930.json、平台全量/MoCha一键AI视频换人，一起来唱《万物生来财版》_1981645125153628161.json、平台全量/MoCha替换视频主角_1992797393477496834.json、平台全量/Mocha-新的视频角色替换_1982629679557419010.json、平台全量/Mocha-视频主题替换（单人）工作流_1981536284206342146.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：63%

## 共有节点

全部 8 个 workflow 都包含：
- `GetImageRangeFromBatch`
- `GetNode`
- `ImageResizeKJv2`
- `LoadImage`
- `MaskPreview`
- `MochaEmbeds`
- `PointsEditor`
- `PreviewImage`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoSetBlockSwap` —— 7/8 个有
- `GrowMaskWithBlur` —— 6/8 个有
- `SeCModelLoader` —— 6/8 个有
- `SeCVideoSegmentation` —— 6/8 个有
- `Bjornulf_ShowInt` —— 3/8 个有
- `DownloadAndLoadSAM2Model` —— 3/8 个有
- `Label (rgthree)` —— 3/8 个有
- `Sam2Segmentation` —— 3/8 个有
- `GrowMask` —— 2/8 个有
- `ImageConcanate` —— 2/8 个有
- `Int` —— 2/8 个有
- `MathExpression|pysssss` —— 2/8 个有
- `WanVideoContextOptions` —— 2/8 个有
- `easy cleanGpuUsed` —— 2/8 个有
- `easy imageRemBg` —— 2/8 个有
- `Anything Everywhere` —— 1/8 个有
- `DownloadAndLoadFlorence2Model` —— 1/8 个有
- `Fast Groups Bypasser (rgthree)` —— 1/8 个有
- `Float` —— 1/8 个有
- `Florence2Run` —— 1/8 个有
- `Florence2toCoordinates` —— 1/8 个有
- `ImageFromBatch` —— 1/8 个有
- `LayerUtility: PurgeVRAM V2` —— 1/8 个有
- `PlaySound|pysssss` —— 1/8 个有
- `PrimitiveString` —— 1/8 个有
- `RMBG` —— 1/8 个有
- `Switch` —— 1/8 个有
- `ToFloat` —— 1/8 个有
- `VHS_VideoInfo` —— 1/8 个有
- `easy int` —— 1/8 个有
- `easy seed` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

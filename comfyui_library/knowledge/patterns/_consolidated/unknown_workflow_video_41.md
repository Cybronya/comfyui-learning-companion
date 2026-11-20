---
name: unknown_workflow_video_41
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.508429
common_nodes: [GetNode, GroundingDinoModelLoader (segment anything), GroundingDinoSAMSegment (segment anything), ImageToMask, LayerUtility: LaMa, MaskToImage, PreviewImage, SAMModelLoader (segment anything), SetNode, VHS_DuplicateMasks, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/[众馨]视频去水印（全自动）_1986360784395632642.json, 平台全量/一键视频去水印（全自动）_1977940482636611585.json, 平台全量/全自动视频去水印_1962096898872164354.json, 平台全量/全自动视频去水印_2021194445139484674.json, 平台全量/地表最强Flux移除 物体消除_去水印，支持全风格_1935911698371178498.json, 平台全量/视频一键去水印（全自动）_2005908462938849281.json, 平台全量/视频去固定水印高清转化_2067428096940269570.json]
source: knowledge_consolidation
---

# unknown_workflow_video_41

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（平台全量/[众馨]视频去水印（全自动）_1986360784395632642.json、平台全量/一键视频去水印（全自动）_1977940482636611585.json、平台全量/全自动视频去水印_1962096898872164354.json、平台全量/全自动视频去水印_2021194445139484674.json、平台全量/地表最强Flux移除 物体消除_去水印，支持全风格_1935911698371178498.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：51%

## 共有节点

全部 7 个 workflow 都包含：
- `GetNode`
- `GroundingDinoModelLoader (segment anything)`
- `GroundingDinoSAMSegment (segment anything)`
- `ImageToMask`
- `LayerUtility: LaMa`
- `MaskToImage`
- `PreviewImage`
- `SAMModelLoader (segment anything)`
- `SetNode`
- `VHS_DuplicateMasks`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ImageBatchGet` —— 6/7 个有
- `VHS_VideoInfo` —— 6/7 个有
- `CR Text` —— 1/7 个有
- `INTConstant` —— 1/7 个有
- `ImageFromBatch+` —— 1/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/7 个有
- `SaveImage` —— 1/7 个有
- `TT_img_enc` —— 1/7 个有
- `VHS_VideoInfoLoaded` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

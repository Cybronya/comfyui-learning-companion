---
name: unknown_workflow_video_lora_sampler_469
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.585
common_nodes: [GetImageRangeFromBatch, GetNode, GrowMaskWithBlur, ImageConcanate, ImageResizeKJv2, LoadImage, MaskPreview, MochaEmbeds, PreviewImage, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader, easy int]
problems: []
missing: []
members: [数字人/数字人/mocha视频角色替换人物替换更换人物更换任意角色工作流_2003477047525711873.json, 视频生成/图生视频/mocha_指定人物_1990430709800198145.json, 视频生成/图生视频/mocha单人物替换，无需标点_1983354803063562242.json, 视频生成/图生视频/mocha视频角色替换人物替换更换人物更换任意角色工作流_2055888329194917889.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_469

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（数字人/数字人/mocha视频角色替换人物替换更换人物更换任意角色工作流_2003477047525711873.json、视频生成/图生视频/mocha_指定人物_1990430709800198145.json、视频生成/图生视频/mocha单人物替换，无需标点_1983354803063562242.json、视频生成/图生视频/mocha视频角色替换人物替换更换人物更换任意角色工作流_2055888329194917889.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：58%

## 共有节点

全部 4 个 workflow 都包含：
- `GetImageRangeFromBatch`
- `GetNode`
- `GrowMaskWithBlur`
- `ImageConcanate`
- `ImageResizeKJv2`
- `LoadImage`
- `MaskPreview`
- `MochaEmbeds`
- `PreviewImage`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `DownloadAndLoadSAM2Model` —— 3/4 个有
- `Sam2Segmentation` —— 3/4 个有
- `Anything Everywhere` —— 2/4 个有
- `CM_FloatToInt` —— 2/4 个有
- `OnnxDetectionModelLoader` —— 2/4 个有
- `PointsEditor` —— 2/4 个有
- `PoseAndFaceDetection` —— 2/4 个有
- `RMBG` —— 2/4 个有
- `easy float` —— 2/4 个有
- `PrimitiveStringMultiline` —— 1/4 个有
- `Sa2VANodeTpl` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

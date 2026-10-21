---
name: unknown_workflow_video_lora_sampler_448
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.7224
common_nodes: [GetNode, INTConstant, ImageConcatMulti, ImageResizeKJv2, LoadImage, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVACEStartToEndFrame, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1967373379772801025.json, 视频生成/图生视频/1967775311335161858.json, 视频生成/图生视频/1967233972919001089.json, 视频生成/图生视频/1968394134803361794.json, 视频生成/图生视频/2043853929309540354.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_448

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/1967373379772801025.json、视频生成/图生视频/1967775311335161858.json、视频生成/图生视频/1967233972919001089.json、视频生成/图生视频/1968394134803361794.json、视频生成/图生视频/2043853929309540354.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：72%

## 共有节点

全部 5 个 workflow 都包含：
- `GetNode`
- `INTConstant`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `LoadImage`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVACEStartToEndFrame`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Text Multiline` —— 4/5 个有
- `WanVideoScheduler` —— 4/5 个有
- `ColorMatch` —— 2/5 个有
- `CreateCFGScheduleFloatList` —— 2/5 个有
- `ImageStitch` —— 2/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/5 个有
- `LayerUtility: TextJoinV2` —— 1/5 个有
- `PrimitiveBoolean` —— 1/5 个有
- `PrimitiveFloat` —— 1/5 个有
- `RH_Captioner` —— 1/5 个有
- `RH_Translator` —— 1/5 个有
- `Textbox` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有
- `easy ifElse` —— 1/5 个有
- `easy showAnything` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

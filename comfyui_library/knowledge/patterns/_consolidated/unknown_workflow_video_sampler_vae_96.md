---
name: unknown_workflow_video_sampler_vae_96
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.784
common_nodes: [EmptyImage, ImageConcanate, Int, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM V2, LoadWanVideoT5TextEncoder, ShowText|pysssss, TextBox, Textbox, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoFlowEdit, WanVideoLoopArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader, WanVideoVRAMManagement, easy cleanGpuUsed, easy imageSize, easy textSwitch]
problems: []
missing: []
members: [平台全量/视频生视频（参考姿势）_  VACE-A4B_1922900257716453378.json, 视频生成/图生视频/图生视频 _ VACE-14B (CausVid 加速)_1924420521310474241.json, 视频生成/图生视频/图生视频 _ VACE-14B (MoviiGen)_1922900275059900417.json, 视频生成/图生视频/首尾帧 _ VACE-14B (CausVid 加速)_1924340185381654529.json, 视频生成/图生视频/首尾帧 _ VACE-14B_1922900237688475650.json, 视频生成/文生视频/文生视频 _ VACE-14B (CausVid 加速)_1924412501411155969.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_96

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（平台全量/视频生视频（参考姿势）_  VACE-A4B_1922900257716453378.json、视频生成/图生视频/图生视频 _ VACE-14B (CausVid 加速)_1924420521310474241.json、视频生成/图生视频/图生视频 _ VACE-14B (MoviiGen)_1922900275059900417.json、视频生成/图生视频/首尾帧 _ VACE-14B (CausVid 加速)_1924340185381654529.json、视频生成/图生视频/首尾帧 _ VACE-14B_1922900237688475650.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 6 个 workflow 都包含：
- `EmptyImage`
- `ImageConcanate`
- `Int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM V2`
- `LoadWanVideoT5TextEncoder`
- `ShowText|pysssss`
- `TextBox`
- `Textbox`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoFlowEdit`
- `WanVideoLoopArgs`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`
- `WanVideoVRAMManagement`
- `easy cleanGpuUsed`
- `easy imageSize`
- `easy textSwitch`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 5/6 个有
- `MathExpression|pysssss` —— 5/6 个有
- `RH_Captioner` —— 5/6 个有
- `LayerUtility: ColorImage V2` —— 4/6 个有
- `WanVideoLoraSelect` —— 4/6 个有
- `AddLabel` —— 3/6 个有
- `WanVideoVACEStartToEndFrame` —— 3/6 个有
- `easy int` —— 3/6 个有
- `GetImageSizeAndCount` —— 2/6 个有
- `AIO_Preprocessor` —— 1/6 个有
- `ImageRepeat` —— 1/6 个有
- `ImageToMask` —— 1/6 个有
- `LayerUtility: BooleanOperator` —— 1/6 个有
- `LayerUtility: CropByMask` —— 1/6 个有
- `LayerUtility: ImageBlendAdvance` —— 1/6 个有
- `LayerUtility: ImageMaskScaleAs` —— 1/6 个有
- `LayerUtility: SimpleTextImage` —— 1/6 个有
- `Pick From Batch (mtb)` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `RH_LLMAPI_NODE` —— 1/6 个有
- `Text Find and Replace` —— 1/6 个有
- `VHS_LoadVideo` —— 1/6 个有
- `easy ifElse` —— 1/6 个有
- `easy imageSizeBySide` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

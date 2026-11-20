---
name: unknown_workflow_video_sampler_vae_113
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.949
common_nodes: [ImageResizeKJ, LoadImage, LoadWanVideoT5TextEncoder, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/WAN-VACE(控制+参考)_1909069408788951042.json, 平台全量/控制+参考(Wan2.1-VACE-14B)_1923042463525892097.json, 平台全量/视频动作_1965251518830100482.json, 平台全量/视频的参考编辑(Wan2.1-VACE-14B)_1923186830479716353.json, 视频生成/文生视频/制+参考)_1937043927247540225.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_113

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/WAN-VACE(控制+参考)_1909069408788951042.json、平台全量/控制+参考(Wan2.1-VACE-14B)_1923042463525892097.json、平台全量/视频动作_1965251518830100482.json、平台全量/视频的参考编辑(Wan2.1-VACE-14B)_1923186830479716353.json、视频生成/文生视频/制+参考)_1937043927247540225.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 5 个 workflow 都包含：
- `ImageResizeKJ`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 4/5 个有
- `INTConstant` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `Florence2ModelLoader` —— 3/5 个有
- `Florence2Run` —— 3/5 个有
- `GetImageSizeAndCount` —— 3/5 个有
- `GetNode` —— 3/5 个有
- `WanVideoSLG` —— 3/5 个有
- `WanVideoTeaCache` —— 3/5 个有
- `WanVideoVACEModelSelect` —— 3/5 个有
- `LayerUtility: PurgeVRAM` —— 2/5 个有
- `GrowMaskWithBlur` —— 1/5 个有
- `InpaintPreprocessor` —— 1/5 个有
- `LayerMask: LoadFlorence2Model` —— 1/5 个有
- `LayerMask: ObjectDetectorFL2` —— 1/5 个有
- `LayerMask: SAM2Ultra` —— 1/5 个有
- `LayerUtility: PurgeVRAM V2` —— 1/5 个有
- `TextInput_` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

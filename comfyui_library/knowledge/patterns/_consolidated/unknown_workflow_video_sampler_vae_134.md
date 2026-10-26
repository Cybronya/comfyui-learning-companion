---
name: unknown_workflow_video_sampler_vae_134
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.571
common_nodes: [AIO_Preprocessor, DWPreprocessor, GetNode, INTConstant, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoVACEEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/【用AI复刻武侠绝学】Vace+FusionX练成降龙十八掌，姿势+深度+抠图实现人物动作迁移_2057994609967583234.json, 视频生成/图生视频/完美换人图生视频Wan-VACE_V2V_1930978728523051010.json, 视频生成/图生视频/最强高一致性图像参考+姿态引导_1934120963867107329.json, 视频生成/文生视频/ComfyUI Wan 2.1 VACE 多条件 - 更好的 ControlNet 控图视频生成_1931329103214129154.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_134

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/【用AI复刻武侠绝学】Vace+FusionX练成降龙十八掌，姿势+深度+抠图实现人物动作迁移_2057994609967583234.json、视频生成/图生视频/完美换人图生视频Wan-VACE_V2V_1930978728523051010.json、视频生成/图生视频/最强高一致性图像参考+姿态引导_1934120963867107329.json、视频生成/文生视频/ComfyUI Wan 2.1 VACE 多条件 - 更好的 ControlNet 控图视频生成_1931329103214129154.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：57%

## 共有节点

全部 4 个 workflow 都包含：
- `AIO_Preprocessor`
- `DWPreprocessor`
- `GetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoVACEEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 3/4 个有
- `GrowMaskWithBlur` —— 3/4 个有
- `LayerMask: LoadSegmentAnythingModels` —— 3/4 个有
- `LayerMask: SegmentAnythingUltra V3` —— 3/4 个有
- `MaskToImage` —— 3/4 个有
- `Mix Color By Mask` —— 3/4 个有
- `VHS_VideoInfo` —— 3/4 个有
- `WanVideoTextEncode` —— 3/4 个有
- `WanVideoTorchCompileSettings` —— 3/4 个有
- `WanVideoVACEModelSelect` —— 3/4 个有
- `LayerUtility: PurgeVRAM` —— 2/4 个有
- `StringConstantMultiline` —— 2/4 个有
- `WanVideoExperimentalArgs` —— 2/4 个有
- `WanVideoLoraSelect` —— 2/4 个有
- `WanVideoSLG` —— 2/4 个有
- `ImageConcatMulti` —— 1/4 个有
- `Label (rgthree)` —— 1/4 个有
- `RMBG` —— 1/4 个有
- `WanVideoApplyNAG` —— 1/4 个有
- `WanVideoEnhanceAVideo` —— 1/4 个有
- `WanVideoMagCache` —— 1/4 个有
- `WanVideoTextEncodeSingle` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

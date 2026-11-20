---
name: unknown_workflow_video_sampler_vae_177
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.637
common_nodes: [GetImageSizeAndCount, GetNode, LoadWanVideoT5TextEncoder, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/VACE吉卜力视频一键转绘(Depth)_1924277297703284738.json, 平台全量/Wan2.1最新VACE14B首尾帧合生成视频_1905443745997983746.json, 视频生成/图生视频/VACE 动作迁移_1917063491289812993.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_177

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/VACE吉卜力视频一键转绘(Depth)_1924277297703284738.json、平台全量/Wan2.1最新VACE14B首尾帧合生成视频_1905443745997983746.json、视频生成/图生视频/VACE 动作迁移_1917063491289812993.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：64%

## 共有节点

全部 3 个 workflow 都包含：
- `GetImageSizeAndCount`
- `GetNode`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `DepthAnything_V2` —— 2/3 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 2/3 个有
- `ImageResize+` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `VHS_LoadVideo` —— 2/3 个有
- `VHS_VideoInfo` —— 2/3 个有
- `WanVideoLoraSelect` —— 2/3 个有
- `WanVideoVACEModelSelect` —— 2/3 个有
- `WanVideoVACEStartToEndFrame` —— 2/3 个有
- `Any Switch (rgthree)` —— 1/3 个有
- `DWPreprocessor` —— 1/3 个有
- `Fast Groups Muter (rgthree)` —— 1/3 个有
- `ImageConcanate` —— 1/3 个有
- `ImageFromBatch` —— 1/3 个有
- `MaskPreview+` —— 1/3 个有
- `RHHiddenNodes` —— 1/3 个有
- `RH_Translator` —— 1/3 个有
- `easy imageSize` —— 1/3 个有
- `easy int` —— 1/3 个有
- `easy positive` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

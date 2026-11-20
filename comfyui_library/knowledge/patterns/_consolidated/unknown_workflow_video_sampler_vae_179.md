---
name: unknown_workflow_video_sampler_vae_179
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.887
common_nodes: [Fast Groups Bypasser (rgthree), ImageResize+, LoadWanVideoT5TextEncoder, PreviewImage, RIFE VFI, VHS_VideoCombine, WanVideoApplyNAG, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncodeSingle, WanVideoVACEEncode, WanVideoVAELoader, easy cleanGpuUsed, easy getNode, easy setNode]
problems: []
missing: []
members: [平台全量/Wan-VACE  视频遮罩替换_1952757825887006721.json, 平台全量/Wan-VACE视频扩图_1953095902552592385.json, 视频生成/图生视频/Wan-VACE视频物品融合_1953121122667663362.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_179

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/Wan-VACE  视频遮罩替换_1952757825887006721.json、平台全量/Wan-VACE视频扩图_1953095902552592385.json、视频生成/图生视频/Wan-VACE视频物品融合_1953121122667663362.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
- `Fast Groups Bypasser (rgthree)`
- `ImageResize+`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `RIFE VFI`
- `VHS_VideoCombine`
- `WanVideoApplyNAG`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncodeSingle`
- `WanVideoVACEEncode`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy getNode`
- `easy setNode`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 2/3 个有
- `GetImageSizeAndCount` —— 2/3 个有
- `ImageRemoveBackground+` —— 2/3 个有
- `LayerUtility: ImageBlendAdvance` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `MaskToImage` —— 2/3 个有
- `RemBGSession+` —— 2/3 个有
- `VHS_LoadVideo` —— 2/3 个有
- `GrowMask` —— 1/3 个有
- `INPAINT_MaskedFill` —— 1/3 个有
- `ImageConcanate` —— 1/3 个有
- `ImageFromBatch` —— 1/3 个有
- `ImageFromBatch+` —— 1/3 个有
- `ImagePadKJ` —— 1/3 个有
- `LayerMask: LoadFlorence2Model` —— 1/3 个有
- `LayerMask: ObjectDetectorFL2` —— 1/3 个有
- `LayerMask: SAM2Ultra` —— 1/3 个有
- `LayerMask: SAM2VideoUltra` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

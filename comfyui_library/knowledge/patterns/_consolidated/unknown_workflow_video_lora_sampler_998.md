---
name: unknown_workflow_video_lora_sampler_998
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.893
common_nodes: [CR SDXL Aspect Ratio, DWPreprocessor, ImageBlend, LayerUtility: PurgeVRAM V2, LoadImage, LoadWanVideoT5TextEncoder, MyOpenPoseNode, OpenposePreprocessor, PrimitiveString, ReActorFaceSwap, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanVideoBlockSwap, WanVideoDecode, WanVideoImageResizeToClosest, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [平台全量/舞蹈动作迁移(面部保持)_1950737193834860546.json, 数字人/数字人/动作迁移同时保持面部特征_1970663729157337090.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_998

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/舞蹈动作迁移(面部保持)_1950737193834860546.json、数字人/数字人/动作迁移同时保持面部特征_1970663729157337090.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 2 个 workflow 都包含：
- `CR SDXL Aspect Ratio`
- `DWPreprocessor`
- `ImageBlend`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MyOpenPoseNode`
- `OpenposePreprocessor`
- `PrimitiveString`
- `ReActorFaceSwap`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageResizeToClosest`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

---
name: unknown_workflow_video_lora_sampler_846
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.841
common_nodes: [AIO_Preprocessor, ColorMatch, GetImageSizeAndCount, Int, LoadImage, LoadWanVideoT5TextEncoder, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1952324361430740994.json, 视频生成/图生视频/1924401400531308546.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_846

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1952324361430740994.json、视频生成/图生视频/1924401400531308546.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `ColorMatch`
- `GetImageSizeAndCount`
- `Int`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere` —— 1/2 个有
- `CR Text` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `ImageConcanate` —— 1/2 个有
- `ImagePadKJ` —— 1/2 个有
- `ImageResizeKJ` —— 1/2 个有
- `ImageSmartSharpen+` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `RH_Captioner` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有
- `TextInputBasic` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

---
name: unknown_workflow_video_lora_sampler_790
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9535
common_nodes: [DWPreprocessor, ImageResizeKJv2, Int, LoadWanVideoT5TextEncoder, PreviewImage, VHS_LoadVideo, VHS_VideoCombine, WanVideoApplyNAG, WanVideoBlockSwap, WanVideoContextOptions, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeSingle, WanVideoVACEEncode, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/文生图/Wan2.1文生视频+视频转绘_1949717734896082946.json, 视频生成/图生视频/Wan2.1图生视频+视频转绘_1949722105333075970.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_790

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Wan2.1文生视频+视频转绘_1949717734896082946.json、视频生成/图生视频/Wan2.1图生视频+视频转绘_1949722105333075970.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 2 个 workflow 都包含：
- `DWPreprocessor`
- `ImageResizeKJv2`
- `Int`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoApplyNAG`
- `WanVideoBlockSwap`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeSingle`
- `WanVideoVACEEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `DepthAnythingV2Preprocessor` —— 1/2 个有
- `ImageBlend` —— 1/2 个有
- `LoadImage` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

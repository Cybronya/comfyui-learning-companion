---
name: unknown_workflow_video_upscale_lora_27
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.96
common_nodes: [CR Upscale Image, ImageScaleToTotalPixels, Int, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, RHHiddenNodes, VHS_VideoCombine, WanVideoBlockSwap, WanVideoEnhanceAVideo, WanVideoLoraSelect, WanVideoSEDecode, WanVideoSEImageClipEncode, WanVideoSEModelLoader, WanVideoSESampler, WanVideoSLG, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, mxSlider]
problems: []
missing: []
members: [图片生成/图生图/动态壁纸无缝循环_1949641181822623746.json, 视频生成/图生视频/wan2.2动态壁纸无缝循环_1985985160506159105.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_lora_27

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/动态壁纸无缝循环_1949641181822623746.json、视频生成/图生视频/wan2.2动态壁纸无缝循环_1985985160506159105.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：96%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Upscale Image`
- `ImageScaleToTotalPixels`
- `Int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `RHHiddenNodes`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoEnhanceAVideo`
- `WanVideoLoraSelect`
- `WanVideoSEDecode`
- `WanVideoSEImageClipEncode`
- `WanVideoSEModelLoader`
- `WanVideoSESampler`
- `WanVideoSLG`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `mxSlider`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

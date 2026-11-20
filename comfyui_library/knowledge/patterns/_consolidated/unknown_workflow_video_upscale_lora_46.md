---
name: unknown_workflow_video_upscale_lora_46
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.883
common_nodes: [FILM VFI, Fast Groups Muter (rgthree), ImageUpscaleWithModel, Int, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, StringConstantMultiline, UpscaleModelLoader, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageClipEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/文生视频/【万物360度旋转】Wan2.1万相任意物体三视图IP多角度动画视频展示_1915649803047604225.json, 视频生成/文生视频/最新Wan2.1稳定图生视频可在线运行，效果非常棒棒！_1916330952719798273.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_lora_46

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/【万物360度旋转】Wan2.1万相任意物体三视图IP多角度动画视频展示_1915649803047604225.json、视频生成/文生视频/最新Wan2.1稳定图生视频可在线运行，效果非常棒棒！_1916330952719798273.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 2 个 workflow 都包含：
- `FILM VFI`
- `Fast Groups Muter (rgthree)`
- `ImageUpscaleWithModel`
- `Int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `StringConstantMultiline`
- `UpscaleModelLoader`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageClipEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Bypasser (rgthree)` —— 1/2 个有
- `Seed Everywhere` —— 1/2 个有
- `WanVideoEnhanceAVideo` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

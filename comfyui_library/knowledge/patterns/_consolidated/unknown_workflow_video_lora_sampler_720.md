---
name: unknown_workflow_video_lora_sampler_720
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.476
common_nodes: [Anything Everywhere, CLIPLoader, CLIPTextEncode, CLIPVisionLoader, CropFace, DWPreprocessor, FloatConstant, GetImageSizeAndCount, INTConstant, ImageFromBatch, ImageResize+, ImageResizeKJv2, LayerUtility: PurgeVRAM V2, LoadImage, PixelPerfectResolution, PrimitiveStringMultiline, Seed (rgthree), SimpleMath+, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEmbedBridge, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/06 低消耗KJ加速版+全节点注释_2055499286644838401.json, 视频生成/图生视频/Wan Animate 视频动作驱动 动作迁移 低消耗 人物一致 精准版  Remix图生视频_2005823918298595330.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_720

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/06 低消耗KJ加速版+全节点注释_2055499286644838401.json、视频生成/图生视频/Wan Animate 视频动作驱动 动作迁移 低消耗 人物一致 精准版  Remix图生视频_2005823918298595330.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：48%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CropFace`
- `DWPreprocessor`
- `FloatConstant`
- `GetImageSizeAndCount`
- `INTConstant`
- `ImageFromBatch`
- `ImageResize+`
- `ImageResizeKJv2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `PixelPerfectResolution`
- `PrimitiveStringMultiline`
- `Seed (rgthree)`
- `SimpleMath+`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEmbedBridge`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `BatchCropFromMask` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `MathExpression|pysssss` —— 1/2 个有
- `SetNode` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

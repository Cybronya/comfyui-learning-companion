---
name: unknown_workflow_video_lora_sampler_343
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.677667
common_nodes: [ADE_CameraPoseCombo, CameraPoseVisualizer, GetNode, ImageResizeKJv2, LoadImage, PreviewImage, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoFunCameraEmbeds, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1956348088506089473.json, 视频生成/图生视频/2015621060615475201.json, 视频生成/图生视频/2004051872707166210.json, 视频生成/图生视频/2004354618245214209.json, 视频生成/图生视频/1956308864335532034.json, 视频生成/图生视频/1963766587461439490.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_343

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/1956348088506089473.json、视频生成/图生视频/2015621060615475201.json、视频生成/图生视频/2004051872707166210.json、视频生成/图生视频/2004354618245214209.json、视频生成/图生视频/1956308864335532034.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：68%

## 共有节点

全部 6 个 workflow 都包含：
- `ADE_CameraPoseCombo`
- `CameraPoseVisualizer`
- `GetNode`
- `ImageResizeKJv2`
- `LoadImage`
- `PreviewImage`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoFunCameraEmbeds`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageConcatMulti` —— 5/6 个有
- `Primitive integer [Crystools]` —— 5/6 个有
- `Text Multiline` —— 5/6 个有
- `ImpactInt` —— 2/6 个有
- `SimpleMath+` —— 2/6 个有
- `CLIPLoader` —— 1/6 个有
- `CLIPTextEncode` —— 1/6 个有
- `CR Prompt Text` —— 1/6 个有
- `CreateVideo` —— 1/6 个有
- `JWInteger` —— 1/6 个有
- `PreViewVideo` —— 1/6 个有
- `RIFE VFI` —— 1/6 个有
- `WanVideoTextEmbedBridge` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

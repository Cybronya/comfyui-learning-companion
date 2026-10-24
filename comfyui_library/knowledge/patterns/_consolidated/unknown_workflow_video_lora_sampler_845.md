---
name: unknown_workflow_video_lora_sampler_845
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9525
common_nodes: [INTConstant, ImageConcatMulti, ImageResizeKJv2, LoadImage, SimpleMath+, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVACEStartToEndFrame, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/wan2.2官方 VACE 首尾帧 KJ流_1967815071856472066.json, 视频生成/图生视频/wan2_2_fun_vace_图片参考视频-KJ_1967598097377497089.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_845

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/wan2.2官方 VACE 首尾帧 KJ流_1967815071856472066.json、视频生成/图生视频/wan2_2_fun_vace_图片参考视频-KJ_1967598097377497089.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 2 个 workflow 都包含：
- `INTConstant`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `LoadImage`
- `SimpleMath+`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVACEStartToEndFrame`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 1/2 个有
- `ColorMatch` —— 1/2 个有
- `CreateCFGScheduleFloatList` —— 1/2 个有
- `ImpactInt` —— 1/2 个有
- `Int` —— 1/2 个有
- `LoadWanVideoT5TextEncoder` —— 1/2 个有
- `Note Plus (mtb)` —— 1/2 个有
- `Text` —— 1/2 个有
- `WanVideoSetLoRAs` —— 1/2 个有
- `WanVideoTextEncode` —— 1/2 个有
- `WanVideoTextEncodeCached` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

---
name: unknown_workflow_video_upscale_sampler_15
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.889
common_nodes: [GetImageSizeAndCount, ImageResizeKJv2, ImageScale, ImageUpscaleWithModel, LoadImage, LoadWanVideoT5TextEncoder, MimicMotionGetPoses, PlaySound|pysssss, PreviewImage, RIFE VFI, UpscaleModelLoader, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader, easy showAnything]
problems: []
missing: []
members: [数字人/数字人/通义万相VACE版_美女跳舞视频转绘_1933718578392948738.json, 视频生成/图生视频/Wan2.1__VACE版_美女跳舞（动作控制）_1933177373691158529.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_sampler_15

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/通义万相VACE版_美女跳舞视频转绘_1933718578392948738.json、视频生成/图生视频/Wan2.1__VACE版_美女跳舞（动作控制）_1933177373691158529.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 2 个 workflow 都包含：
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `ImageScale`
- `ImageUpscaleWithModel`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MimicMotionGetPoses`
- `PlaySound|pysssss`
- `PreviewImage`
- `RIFE VFI`
- `UpscaleModelLoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Florence2ModelLoader` —— 1/2 个有
- `Florence2Run` —— 1/2 个有
- `JWInteger` —— 1/2 个有
- `OpenposePreprocessor` —— 1/2 个有
- `RH_Captioner` —— 1/2 个有
- `RH_Translator` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有
- `Text Concatenate` —— 1/2 个有
- `easy anythingIndexSwitch` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

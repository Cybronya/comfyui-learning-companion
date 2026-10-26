---
name: unknown_workflow_video_lora_sampler_754
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.888
common_nodes: [ImageResizeKJv2, JWInteger, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoApplyNAG, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeSingle, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/图生视频加运镜_1951201282436571137.json, 视频生成/图生视频/图生视频（WanFusionX）（魔方）_1948023695982899201.json, 视频生成/图生视频/首+尾帧视频转绘（FusionX_VACE无V）(魔方)_1945823469433221121.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_754

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/图生视频加运镜_1951201282436571137.json、视频生成/图生视频/图生视频（WanFusionX）（魔方）_1948023695982899201.json、视频生成/图生视频/首+尾帧视频转绘（FusionX_VACE无V）(魔方)_1945823469433221121.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
- `ImageResizeKJv2`
- `JWInteger`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoApplyNAG`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeSingle`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 2/3 个有
- `SimpleMath+` —— 2/3 个有
- `VHS_LoadVideo` —— 2/3 个有
- `WanVideoImageToVideoEncode` —— 2/3 个有
- `WanVideoMagCache` —— 2/3 个有
- `WanVideoSLG` —— 2/3 个有
- `WanVideoVACEModelSelect` —— 2/3 个有
- `GetImageSizeAndCount` —— 1/3 个有
- `MathExpression|pysssss` —— 1/3 个有
- `WanVideoEncode` —— 1/3 个有
- `WanVideoSetRadialAttention` —— 1/3 个有
- `WanVideoUni3C_ControlnetLoader` —— 1/3 个有
- `WanVideoUni3C_embeds` —— 1/3 个有
- `WanVideoVACEEncode` —— 1/3 个有
- `WanVideoVACEStartToEndFrame` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

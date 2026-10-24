---
name: unknown_workflow_video_lora_sampler_234
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.935125
common_nodes: [CreateCFGScheduleFloatList, INTConstant, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/【kj版+VBVR】Wan2_2首尾帧生视频_2038129032830652418.json, 图片生成/图生图/极简——Wan2.2 KJ 图生视频_1951508080301387777.json, 图片生成/图生图/🐳SVI2.0PRO长视频生成 图生视频 简易版🦋_2005507420082368514.json, 视频生成/图生视频/004.Wan视频之源005.首尾关键帧_2035336872209162242.json, 视频生成/图生视频/WAN2.2图生快速流_1950145303941922817.json, 视频生成/图生视频/Wan2.2 图生视频一键工作流_2032825101573431298.json, 视频生成/图生视频/【VBVR+KJ】最强参考Wan2.2图生视频_分块处理低显存版_2038129014153420801.json, 视频生成/文生视频/光文字流转V1（尾帧实验版）_1966039188808396801.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_234

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/【kj版+VBVR】Wan2_2首尾帧生视频_2038129032830652418.json、图片生成/图生图/极简——Wan2.2 KJ 图生视频_1951508080301387777.json、图片生成/图生图/🐳SVI2.0PRO长视频生成 图生视频 简易版🦋_2005507420082368514.json、视频生成/图生视频/004.Wan视频之源005.首尾关键帧_2035336872209162242.json、视频生成/图生视频/WAN2.2图生快速流_1950145303941922817.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 8 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 7/8 个有
- `WanVideoLoraSelect` —— 7/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/8 个有
- `ImpactInt` —— 5/8 个有
- `SimpleMath+` —— 5/8 个有
- `WanVideoLoraSelectMulti` —— 3/8 个有
- `WanVideoTorchCompileSettings` —— 3/8 个有
- `ImageResizeKJv2` —— 2/8 个有
- `MathExpression|pysssss` —— 2/8 个有
- `PrimitiveStringMultiline` —— 2/8 个有
- `easy convertAnything` —— 2/8 个有
- `CR Text` —— 1/8 个有
- `ImageResize+` —— 1/8 个有
- `JWInteger` —— 1/8 个有
- `ModelScopeImageGeneration` —— 1/8 个有
- `Note Plus (mtb)` —— 1/8 个有
- `SaveImage` —— 1/8 个有
- `WanVideoContextOptions` —— 1/8 个有
- `WanVideoSLG` —— 1/8 个有
- `easy anythingIndexSwitch` —— 1/8 个有
- `easy promptConcat` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

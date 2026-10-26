---
name: unknown_workflow_video_lora_sampler_277
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.983625
common_nodes: [CreateCFGScheduleFloatList, GetImageSizeAndCount, INTConstant, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/【kj版+VBVR】Wan2_2首尾帧生视频_2038129032830652418.json, 图片生成/图生图/极简——Wan2.2 KJ 图生视频_1951508080301387777.json, 图片生成/图生图/🐳SVI2.0PRO长视频生成 图生视频 简易版🦋_2005507420082368514.json, 视频生成/图生视频/Wan2.2 Kj-图生视频工作流_1956914143121039362.json, 视频生成/图生视频/Wan2.2 图生视频一键工作流_2032825101573431298.json, 视频生成/图生视频/【VBVR+KJ】最强参考Wan2.2图生视频_分块处理低显存版_2038129014153420801.json, 视频生成/图生视频/安-Wan2.2 首尾帧频工作流_1965415363951382530.json, 视频生成/文生视频/🐳wan2.2 文生视频 超清臻享版🦋【KJ模型】_1950063356758638593.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_277

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/【kj版+VBVR】Wan2_2首尾帧生视频_2038129032830652418.json、图片生成/图生图/极简——Wan2.2 KJ 图生视频_1951508080301387777.json、图片生成/图生图/🐳SVI2.0PRO长视频生成 图生视频 简易版🦋_2005507420082368514.json、视频生成/图生视频/Wan2.2 Kj-图生视频工作流_1956914143121039362.json、视频生成/图生视频/Wan2.2 图生视频一键工作流_2032825101573431298.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 8 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `GetImageSizeAndCount`
- `INTConstant`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 7/8 个有
- `WanVideoImageToVideoEncode` —— 7/8 个有
- `WanVideoLoraSelect` —— 7/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/8 个有
- `SimpleMath+` —— 5/8 个有
- `ImpactInt` —— 4/8 个有
- `CR Text` —— 2/8 个有
- `Note Plus (mtb)` —— 2/8 个有
- `WanVideoContextOptions` —— 2/8 个有
- `WanVideoLoraSelectMulti` —— 2/8 个有
- `easy convertAnything` —— 2/8 个有
- `ImageResize+` —— 1/8 个有
- `ImageResizeKJv2` —— 1/8 个有
- `WanVideoEmptyEmbeds` —— 1/8 个有
- `WanVideoTorchCompileSettings` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

---
name: unknown_workflow_video_lora_sampler_619
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9414
common_nodes: [GetImageSizeAndCount, INTConstant, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2-KJ版图生视频-首尾帧（强烈推荐）_1953456123129024514.json, 视频生成/图生视频/Wan2.2-KJ版本图生视频_1950370270352687105.json, 视频生成/图生视频/Wan2.2-KJ版本图生视频_1952541764970328066.json, 视频生成/图生视频/Wan2.2图生视频-植物生长蔓延-kijai版工作流_1959544112867389442.json, 视频生成/图生视频/wan2.2图生视频首尾帧（KJ版）_1955148796940488705.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_619

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/Wan2.2-KJ版图生视频-首尾帧（强烈推荐）_1953456123129024514.json、视频生成/图生视频/Wan2.2-KJ版本图生视频_1950370270352687105.json、视频生成/图生视频/Wan2.2-KJ版本图生视频_1952541764970328066.json、视频生成/图生视频/Wan2.2图生视频-植物生长蔓延-kijai版工作流_1959544112867389442.json、视频生成/图生视频/wan2.2图生视频首尾帧（KJ版）_1955148796940488705.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 5 个 workflow 都包含：
- `GetImageSizeAndCount`
- `INTConstant`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateCFGScheduleFloatList` —— 4/5 个有
- `Int` —— 3/5 个有
- `ShowText|pysssss` —— 3/5 个有
- `WanVideoSetRadialAttention` —— 3/5 个有
- `Seed` —— 2/5 个有
- `MathExpression|pysssss` —— 1/5 个有
- `PrimitiveString` —— 1/5 个有
- `QwenLoader` —— 1/5 个有
- `RH_Translator` —— 1/5 个有
- `SimpleMath+` —— 1/5 个有
- `WanVideoPromptExtender` —— 1/5 个有
- `easy promptReplace` —— 1/5 个有
- `ttN int` —— 1/5 个有
- `ttN text` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

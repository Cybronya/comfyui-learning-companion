---
name: unknown_workflow_video_lora_sampler_366
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.966714
common_nodes: [CreateCFGScheduleFloatList, GetImageSizeAndCount, INTConstant, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2-KJ版图生视频-首尾帧（强烈推荐）_1953456123129024514.json, 视频生成/图生视频/Wan2.2-KJ版本图生视频_1950370270352687105.json, 视频生成/图生视频/Wan2.2-KJ版本图生视频_1952541764970328066.json, 视频生成/图生视频/Wan2.2图生视频 KJ加速版（小优化）_1960986667224109058.json, 视频生成/图生视频/wan2.2图生视频首尾帧（KJ版）_1955148796940488705.json, 视频生成/图生视频/wan2.2图生视频（KJ流）加速_1950178102964084737.json, 视频生成/文生视频/Wan2.2文生视频 KJ加速版（小优化）_1960686158676189186.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_366

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/Wan2.2-KJ版图生视频-首尾帧（强烈推荐）_1953456123129024514.json、视频生成/图生视频/Wan2.2-KJ版本图生视频_1950370270352687105.json、视频生成/图生视频/Wan2.2-KJ版本图生视频_1952541764970328066.json、视频生成/图生视频/Wan2.2图生视频 KJ加速版（小优化）_1960986667224109058.json、视频生成/图生视频/wan2.2图生视频首尾帧（KJ版）_1955148796940488705.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 7 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `GetImageSizeAndCount`
- `INTConstant`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 6/7 个有
- `WanVideoImageToVideoEncode` —— 6/7 个有
- `ShowText|pysssss` —— 3/7 个有
- `SimpleMath+` —— 3/7 个有
- `WanVideoSetRadialAttention` —— 3/7 个有
- `Int` —— 2/7 个有
- `RH_Translator` —— 2/7 个有
- `Seed` —— 2/7 个有
- `easy positive` —— 2/7 个有
- `easy seed` —— 2/7 个有
- `MathExpression|pysssss` —— 1/7 个有
- `QwenLoader` —— 1/7 个有
- `WanVideoEmptyEmbeds` —— 1/7 个有
- `WanVideoPromptExtender` —— 1/7 个有
- `ttN int` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

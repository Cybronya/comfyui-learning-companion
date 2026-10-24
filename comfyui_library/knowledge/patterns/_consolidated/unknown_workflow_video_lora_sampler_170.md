---
name: unknown_workflow_video_lora_sampler_170
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.988636
common_nodes: [CreateCFGScheduleFloatList, GetImageSizeAndCount, INTConstant, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2-KJ版图生视频-首尾帧（强烈推荐）_1953456123129024514.json, 视频生成/图生视频/Wan2.2-KJ版本图生视频_1950370270352687105.json, 视频生成/图生视频/Wan2.2-KJ版本图生视频_1952541764970328066.json, 视频生成/图生视频/Wan2.2图生视频 KJ加速版（小优化）_1960986667224109058.json, 视频生成/图生视频/wan2.2图生视频+丝袜美女转圈=艾橘溪_1893899363629051906.json, 视频生成/图生视频/wan2.2图生视频+双模出图(结构+细节)_2052404579370848257.json, 视频生成/图生视频/wan2.2图生视频+美女转圈_2075491553438683138.json, 视频生成/图生视频/wan2.2图生视频+美女转圈。绝绝子，好用！_2031551233101664258.json, 视频生成/图生视频/wan2.2图生视频+美女转圈。绝绝子，好用！_2043583359116382210.json, 视频生成/图生视频/wan2.2图生视频_2080097509229293570.json, 视频生成/文生视频/Wan2.2文生视频 KJ加速版（小优化）_1960686158676189186.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_170

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/Wan2.2-KJ版图生视频-首尾帧（强烈推荐）_1953456123129024514.json、视频生成/图生视频/Wan2.2-KJ版本图生视频_1950370270352687105.json、视频生成/图生视频/Wan2.2-KJ版本图生视频_1952541764970328066.json、视频生成/图生视频/Wan2.2图生视频 KJ加速版（小优化）_1960986667224109058.json、视频生成/图生视频/wan2.2图生视频+丝袜美女转圈=艾橘溪_1893899363629051906.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 11 个 workflow 都包含：
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
- `ImageResizeKJv2` —— 10/11 个有
- `WanVideoImageToVideoEncode` —— 10/11 个有
- `SimpleMath+` —— 9/11 个有
- `Int` —— 7/11 个有
- `LayerUtility: PurgeVRAM` —— 6/11 个有
- `WanVideoSetRadialAttention` —— 3/11 个有
- `Seed` —— 2/11 个有
- `easy positive` —— 2/11 个有
- `easy seed` —— 2/11 个有
- `MathExpression|pysssss` —— 1/11 个有
- `QwenLoader` —— 1/11 个有
- `ShowText|pysssss` —— 1/11 个有
- `WanVideoEmptyEmbeds` —— 1/11 个有
- `WanVideoPromptExtender` —— 1/11 个有
- `ttN int` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

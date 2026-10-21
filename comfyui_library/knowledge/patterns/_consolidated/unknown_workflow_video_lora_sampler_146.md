---
name: unknown_workflow_video_lora_sampler_146
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.981417
common_nodes: [CreateCFGScheduleFloatList, GetImageSizeAndCount, INTConstant, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1953456123129024514.json, 视频生成/图生视频/1950370270352687105.json, 视频生成/图生视频/1952541764970328066.json, 视频生成/图生视频/1960986667224109058.json, 视频生成/图生视频/2005434183445086209.json, 视频生成/图生视频/1893899363629051906.json, 视频生成/图生视频/2052404579370848257.json, 视频生成/图生视频/2075491553438683138.json, 视频生成/图生视频/2031551233101664258.json, 视频生成/图生视频/2043583359116382210.json, 视频生成/图生视频/2080097509229293570.json, 视频生成/图生视频/1955148796940488705.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_146

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/1953456123129024514.json、视频生成/图生视频/1950370270352687105.json、视频生成/图生视频/1952541764970328066.json、视频生成/图生视频/1960986667224109058.json、视频生成/图生视频/2005434183445086209.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 12 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
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
- `Int` —— 8/12 个有
- `SimpleMath+` —— 8/12 个有
- `LayerUtility: PurgeVRAM` —— 6/12 个有
- `WanVideoSetRadialAttention` —— 3/12 个有
- `Seed` —— 2/12 个有
- `ShowText|pysssss` —— 2/12 个有
- `easy seed` —— 2/12 个有
- `MathExpression|pysssss` —— 1/12 个有
- `QwenLoader` —— 1/12 个有
- `RH_Translator` —— 1/12 个有
- `WanVideoPromptExtender` —— 1/12 个有
- `easy positive` —— 1/12 个有
- `ttN int` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

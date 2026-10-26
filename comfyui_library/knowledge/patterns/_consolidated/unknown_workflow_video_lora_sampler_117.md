---
name: unknown_workflow_video_lora_sampler_117
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.894733
common_nodes: [CreateCFGScheduleFloatList, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/8-图转视频 Wan2.2 14b Optional Last Frame_2053486047740350466.json, 视频生成/图生视频/AIwood-Wan2.2首尾帧Kijai版_1952003952139292673.json, 视频生成/图生视频/AIwood-Wan2.2首尾帧Kijai版_2061786208002465793.json, 视频生成/图生视频/AIwood-Wan2.2首尾帧Kijai版_2061806465001803778.json, 视频生成/图生视频/HeGenAI-N8N-Wan2.2图生视频加速版_1968577373975261186.json, 视频生成/图生视频/KJ wan2.2首尾帧+Lightx4step lora_2015424489110118402.json, 视频生成/图生视频/KJ-Wan2.2-6步加速图生视频_1949986819199909890.json, 视频生成/图生视频/KJ-Wan2.2-6步加速文生视频_1950060354116214786.json, 视频生成/图生视频/Wan2.2-lightx2v-6步加速图生视频-KJ版_1950132208273154049.json, 视频生成/图生视频/Work-Fisher_Wan2.2-I2V增强版_1972312939401310209.json, 视频生成/文生视频/Wan2.2-lightx2v-6步加速文生视频_KJ版_1950128875525332993.json, 视频生成/文生视频/Wan2.2-lightx2v-6步加速文生视频_KJ版非常逼真目前最牛_1950206171439390721.json, 视频生成/文生视频/Work-Fisher_Wan2.2增强版合集_1972651753634242561.json, 视频生成/文生视频/rlinhe_Wan2.2增强版合集 by B站 Work-Fisher_1975195105038569473.json, 视频生成/文生视频/漫剧最强工具Wan2.2超强一致性_2049103222916259841.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_117

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/图生视频/8-图转视频 Wan2.2 14b Optional Last Frame_2053486047740350466.json、视频生成/图生视频/AIwood-Wan2.2首尾帧Kijai版_1952003952139292673.json、视频生成/图生视频/AIwood-Wan2.2首尾帧Kijai版_2061786208002465793.json、视频生成/图生视频/AIwood-Wan2.2首尾帧Kijai版_2061806465001803778.json、视频生成/图生视频/HeGenAI-N8N-Wan2.2图生视频加速版_1968577373975261186.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 15 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 13/15 个有
- `GetImageSizeAndCount` —— 12/15 个有
- `ImageResizeKJv2` —— 12/15 个有
- `WanVideoImageToVideoEncode` —— 12/15 个有
- `WanVideoSetBlockSwap` —— 11/15 个有
- `WanVideoSetLoRAs` —— 11/15 个有
- `INTConstant` —— 10/15 个有
- `WanVideoEmptyEmbeds` —— 6/15 个有
- `Fast Groups Bypasser (rgthree)` —— 5/15 个有
- `MathExpression|pysssss` —— 5/15 个有
- `Primitive integer [Crystools]` —— 5/15 个有
- `RIFE VFI` —— 5/15 个有
- `Text Multiline` —— 5/15 个有
- `Int` —— 4/15 个有
- `CreateVideo` —— 3/15 个有
- `PreViewVideo` —— 3/15 个有
- `WanVideoLoraSelectMulti` —— 3/15 个有
- `SaveVideo` —— 2/15 个有
- `Label (rgthree)` —— 1/15 个有
- `Seed (rgthree)` —— 1/15 个有
- `ShellAgentPluginSaveImage` —— 1/15 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

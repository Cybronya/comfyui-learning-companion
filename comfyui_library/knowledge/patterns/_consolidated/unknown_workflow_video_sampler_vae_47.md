---
name: unknown_workflow_video_sampler_vae_47
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.794556
common_nodes: [CreateCFGScheduleFloatList, GetImageSizeAndCount, INTConstant, Int, LoadImage, LoadWanVideoT5TextEncoder, RIFE VFI, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: [RIFE VFI, Text Concatenate, Text Multiline]
members: [视频生成/图生视频/1972625966143062017.json, 视频生成/图生视频/1972651753634242561.json, 视频生成/图生视频/1975195105038569473.json, 视频生成/图生视频/1972312939401310209.json, 视频生成/文生视频/1971802147362893826.json, 视频生成/文生视频/1972625966143062017.json, 视频生成/文生视频/1972651753634242561.json, 视频生成/文生视频/1975195105038569473.json, 视频生成/文生视频/漫剧最强工具Wan2.2超强一致性_2049103222916259841.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_47

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/1972625966143062017.json、视频生成/图生视频/1972651753634242561.json、视频生成/图生视频/1975195105038569473.json、视频生成/图生视频/1972312939401310209.json、视频生成/文生视频/1971802147362893826.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 9 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `GetImageSizeAndCount`
- `INTConstant`
- `Int`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `RIFE VFI`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 8/9 个有
- `WanVideoImageToVideoEncode` —— 8/9 个有
- `WanVideoLoraSelect` —— 8/9 个有
- `Fast Groups Bypasser (rgthree)` —— 7/9 个有
- `WanVideoEmptyEmbeds` —— 6/9 个有
- `WanVideoLoraSelectMulti` —— 6/9 个有
- `RH_LLMAPI_NODE` —— 2/9 个有
- `ShellAgentPluginSaveImage` —— 2/9 个有
- `ShowText|pysssss` —— 2/9 个有
- `Text Concatenate` —— 2/9 个有
- `Text Multiline` —— 2/9 个有
- `Wan22PromptSelector` —— 2/9 个有
- `ImageFromBatch` —— 1/9 个有
- `ImageListToImageBatch` —— 1/9 个有
- `SaveImage` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：RIFE VFI、Text Concatenate、Text Multiline

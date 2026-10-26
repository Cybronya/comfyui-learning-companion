---
name: unknown_workflow_video_lora_sampler_735
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.936667
common_nodes: [CreateCFGScheduleFloatList, GetImageSizeAndCount, INTConstant, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/wan2.2kj流图生视频自动提示词（需要GLM api key））_1950030719999500290.json, 视频生成/图生视频/【橘子AI】Wan 图生视频工作流 -KJ_1978004936166363137.json, 视频生成/文生视频/Wan2.2文生视频-告别PPT式电视剧_1950553795895939073.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_735

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/wan2.2kj流图生视频自动提示词（需要GLM api key））_1950030719999500290.json、视频生成/图生视频/【橘子AI】Wan 图生视频工作流 -KJ_1978004936166363137.json、视频生成/文生视频/Wan2.2文生视频-告别PPT式电视剧_1950553795895939073.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 3 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `GetImageSizeAndCount`
- `INTConstant`
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
- `CLIPLoader` —— 2/3 个有
- `CLIPTextEncode` —— 2/3 个有
- `ImageResizeKJv2` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `WanVideoImageToVideoEncode` —— 2/3 个有
- `WanVideoTextEmbedBridge` —— 2/3 个有
- `CR Text` —— 1/3 个有
- `CR Text Concatenate` —— 1/3 个有
- `GLM_Vision_ImageToPrompt` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `QwenLoader` —— 1/3 个有
- `ShowText` —— 1/3 个有
- `Wan22PromptSelector` —— 1/3 个有
- `WanVideoEmptyEmbeds` —— 1/3 个有
- `WanVideoPromptExtender` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

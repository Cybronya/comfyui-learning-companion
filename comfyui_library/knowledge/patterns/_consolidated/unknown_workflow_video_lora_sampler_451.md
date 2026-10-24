---
name: unknown_workflow_video_lora_sampler_451
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8432
common_nodes: [CreateCFGScheduleFloatList, INTConstant, Int, LoadWanVideoT5TextEncoder, RIFE VFI, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/文生视频/Work-Fisher_Wan2.2增强版合集_1972651753634242561.json, 视频生成/文生视频/rlinhe_Wan2.2增强版合集 by B站 Work-Fisher_1975195105038569473.json, 视频生成/文生视频/wan2.2文生视频 (完整版)_1987398850963025922.json, 视频生成/文生视频/漫剧最强工具Wan2.2超强一致性_2049103222916259841.json, 视频生成/文生视频/通义万相Wan2.2图生视频增强版_1972625966143062017.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_451

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/文生视频/Work-Fisher_Wan2.2增强版合集_1972651753634242561.json、视频生成/文生视频/rlinhe_Wan2.2增强版合集 by B站 Work-Fisher_1975195105038569473.json、视频生成/文生视频/wan2.2文生视频 (完整版)_1987398850963025922.json、视频生成/文生视频/漫剧最强工具Wan2.2超强一致性_2049103222916259841.json、视频生成/文生视频/通义万相Wan2.2图生视频增强版_1972625966143062017.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 5 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `Int`
- `LoadWanVideoT5TextEncoder`
- `RIFE VFI`
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
- `GetImageSizeAndCount` —— 4/5 个有
- `ImageResizeKJv2` —— 4/5 个有
- `LoadImage` —— 4/5 个有
- `WanVideoEmptyEmbeds` —— 4/5 个有
- `WanVideoImageToVideoEncode` —— 4/5 个有
- `Fast Groups Bypasser (rgthree)` —— 3/5 个有
- `WanVideoLoraSelectMulti` —— 3/5 个有
- `CR Text` —— 1/5 个有
- `MathExpression|pysssss` —— 1/5 个有
- `RH_LLMAPI_NODE` —— 1/5 个有
- `ShellAgentPluginSaveImage` —— 1/5 个有
- `ShowText|pysssss` —— 1/5 个有
- `Text Concatenate` —— 1/5 个有
- `Text Multiline` —— 1/5 个有
- `Wan22PromptSelector` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

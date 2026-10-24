---
name: unknown_workflow_video_upscale_lora_20
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.829333
common_nodes: [CR Text, CR Text Concatenate, CreateCFGScheduleFloatList, INTConstant, ImageUpscaleWithModel, JWInteger, JjkText, LoadWanVideoT5TextEncoder, MathExpression|pysssss, RH_Prompter, SimpleMath+, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2 14B 图生视频（自动优化提示词+2K出图）_1961117011273256962.json, 视频生成/图生视频/Wan2.2-14B 图生视频_1951128399853068289.json, 视频生成/文生视频/Wan2.2 14B 文生视频1080P版_1950444010021240833.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_lora_20

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/Wan2.2 14B 图生视频（自动优化提示词+2K出图）_1961117011273256962.json、视频生成/图生视频/Wan2.2-14B 图生视频_1951128399853068289.json、视频生成/文生视频/Wan2.2 14B 文生视频1080P版_1950444010021240833.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 3 个 workflow 都包含：
- `CR Text`
- `CR Text Concatenate`
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `ImageUpscaleWithModel`
- `JWInteger`
- `JjkText`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `RH_Prompter`
- `SimpleMath+`
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
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 2/3 个有
- `ImageScale` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `PlaySound|pysssss` —— 2/3 个有
- `RH_Captioner` —— 2/3 个有
- `RIFE VFI` —— 2/3 个有
- `UpscaleModelLoader` —— 2/3 个有
- `WanVideoImageToVideoEncode` —— 2/3 个有
- `easy anythingIndexSwitch` —— 2/3 个有
- `ttN concat` —— 2/3 个有
- `GetNode` —— 1/3 个有
- `RHHiddenNodes` —— 1/3 个有
- `Seed_` —— 1/3 个有
- `SetNode` —— 1/3 个有
- `WanVideoEmptyEmbeds` —— 1/3 个有
- `WanVideoEnhanceAVideo` —— 1/3 个有
- `WanVideoSLG` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

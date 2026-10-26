---
name: unknown_workflow_video_sampler_vae_156
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.899667
common_nodes: [CR Text, DF_Integer, LoadWanVideoT5TextEncoder, RH_LLMAPI_NODE, ShowText|pysssss, SimpleMath+, StringToInt, Text Multiline, TextSwitchCase, VHS_VideoCombine, WanVideoApplyNAG, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeSingle, WanVideoTorchCompileSettings, WanVideoVAELoader, easy textSwitch]
problems: []
missing: []
members: [视频生成/图生视频/FusionX图生视频_1934554674429108225.json, 视频生成/图生视频/通义万相视频LLM自动提示词+FusionX模型图生视频一统江湖_1934947050259685377.json, 视频生成/文生视频/FusionX文生视频_1934540545190764546.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_156

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/FusionX图生视频_1934554674429108225.json、视频生成/图生视频/通义万相视频LLM自动提示词+FusionX模型图生视频一统江湖_1934947050259685377.json、视频生成/文生视频/FusionX文生视频_1934540545190764546.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 3 个 workflow 都包含：
- `CR Text`
- `DF_Integer`
- `LoadWanVideoT5TextEncoder`
- `RH_LLMAPI_NODE`
- `ShowText|pysssss`
- `SimpleMath+`
- `StringToInt`
- `Text Multiline`
- `TextSwitchCase`
- `VHS_VideoCombine`
- `WanVideoApplyNAG`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeSingle`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy textSwitch`

**可变部分**（部分 workflow 才有）：
- `AnimateDiffCombine` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `WanVideoExperimentalArgs` —— 2/3 个有
- `WanVideoImageToVideoEncode` —— 2/3 个有
- `WanVideoSLG` —— 2/3 个有
- `WanVideoEmptyEmbeds` —— 1/3 个有
- `string_util_StrReplace` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

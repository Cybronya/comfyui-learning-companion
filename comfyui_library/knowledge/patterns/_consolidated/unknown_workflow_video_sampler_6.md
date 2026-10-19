---
name: unknown_workflow_video_sampler_6
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.85175
common_nodes: [CR Text, CreateCFGScheduleFloatList, GetImageSizeAndCount, GetNode, INTConstant, ImpactSwitch, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MathExpression|pysssss, RHHiddenNodes, RIFE VFI, SetNode, VHS_VideoCombine, Wan22PromptSelector, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoSampler, WanVideoTextEncode]
problems: []
missing: []
members: [视频生成/图生视频/1980423615982297089.json, 视频生成/图生视频/2000450911669452801.json, 视频生成/图生视频/2016320506777051137.json, 视频生成/图生视频/2044848219955400706.json, 视频生成/图生视频/2031909424805187585.json, 视频生成/图生视频/2034804172817702913.json, 视频生成/图生视频/1982023011672956929.json, 视频生成/图生视频/1982343398008995841.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_6

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/1980423615982297089.json、视频生成/图生视频/2000450911669452801.json、视频生成/图生视频/2016320506777051137.json、视频生成/图生视频/2044848219955400706.json、视频生成/图生视频/2031909424805187585.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 8 个 workflow 都包含：
- `CR Text`
- `CreateCFGScheduleFloatList`
- `GetImageSizeAndCount`
- `GetNode`
- `INTConstant`
- `ImpactSwitch`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `MathExpression|pysssss`
- `RHHiddenNodes`
- `RIFE VFI`
- `SetNode`
- `VHS_VideoCombine`
- `Wan22PromptSelector`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoSampler`
- `WanVideoTextEncode`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: PurgeVRAM V2` —— 7/8 个有
- `LoadWanVideoT5TextEncoder` —— 7/8 个有
- `WanVideoSetBlockSwap` —— 7/8 个有
- `WanVideoVAELoader` —— 7/8 个有
- `Fast Groups Bypasser (rgthree)` —— 6/8 个有
- `Text Concatenate` —— 6/8 个有
- `AILab_QwenVL` —— 2/8 个有
- `CR Text Concatenate` —— 2/8 个有
- `ImageConcanate` —— 2/8 个有
- `PreviewImage` —— 2/8 个有
- `RH_Nano_Banana_Image2Image` —— 2/8 个有
- `RH_Translator` —— 2/8 个有
- `SaveImage` —— 2/8 个有
- `ShowText|pysssss` —— 2/8 个有
- `RH_LLMAPI_NODE` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

---
name: unknown_workflow_video_lora_sampler_344
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.653286
common_nodes: [GetImageRangeFromBatch, GetNode, GrowMask, ImageResizeKJv2, LoadImage, MaskPreview, MochaEmbeds, PointsEditor, PreviewImage, SeCModelLoader, SeCVideoSegmentation, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader, easy imageRemBg]
problems: []
missing: []
members: [数字人/数字人/图片生成  全能视频 人物替换Mocha 【如爆显存 请使用 Plus模式】 数字人说话唱歌跳_2064208363466092546.json, 视频生成/图生视频/Mocha sec4b视频抠图工作流_1982464273806966785.json, 视频生成/图生视频/人物替换Mocha工作流Wan（支持10s以上）_2013864867756773377.json, 视频生成/图生视频/最新视频角色替换Mocha_1980911162026016770.json, 视频生成/图生视频/角色替换Mocha_1980827522109755393.json, 视频生成/图生视频/角色替换Mocha工作流_1986007241096605697.json, 视频生成/图生视频/🦖Mocha角色替换_1980895212593659906.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_344

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（数字人/数字人/图片生成  全能视频 人物替换Mocha 【如爆显存 请使用 Plus模式】 数字人说话唱歌跳_2064208363466092546.json、视频生成/图生视频/Mocha sec4b视频抠图工作流_1982464273806966785.json、视频生成/图生视频/人物替换Mocha工作流Wan（支持10s以上）_2013864867756773377.json、视频生成/图生视频/最新视频角色替换Mocha_1980911162026016770.json、视频生成/图生视频/角色替换Mocha_1980827522109755393.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：65%

## 共有节点

全部 7 个 workflow 都包含：
- `GetImageRangeFromBatch`
- `GetNode`
- `GrowMask`
- `ImageResizeKJv2`
- `LoadImage`
- `MaskPreview`
- `MochaEmbeds`
- `PointsEditor`
- `PreviewImage`
- `SeCModelLoader`
- `SeCVideoSegmentation`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `easy imageRemBg`

**可变部分**（部分 workflow 才有）：
- `ImageConcanate` —— 6/7 个有
- `WanVideoTorchCompileSettings` —— 6/7 个有
- `Int` —— 4/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/7 个有
- `DF_Int_to_Float` —— 2/7 个有
- `MathExpression|pysssss` —— 2/7 个有
- `RMBG` —— 2/7 个有
- `ACE_ImageFaceCrop` —— 1/7 个有
- `DeepTranslatorTextNode` —— 1/7 个有
- `Fast Groups Bypasser (rgthree)` —— 1/7 个有
- `FlashVSRNode` —— 1/7 个有
- `SimpleMath+` —— 1/7 个有
- `VHS_VideoInfoLoaded` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

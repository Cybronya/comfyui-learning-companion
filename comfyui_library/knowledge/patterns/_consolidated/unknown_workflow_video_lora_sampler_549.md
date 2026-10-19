---
name: unknown_workflow_video_lora_sampler_549
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.54575
common_nodes: [Anything Everywhere, CLIPVisionLoader, CR Text, CogVideoEnhanceAVideo, ColorCorrectOfUtils, CreateCFGScheduleFloatList, FluxResolutionNode, GetNode, ImageCASharpening+, Int, JWInteger, LayerUtility: PurgeVRAM V2, LoadImage, LoadWanVideoT5TextEncoder, MathExpression|pysssss, RHHiddenNodes, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoExperimentalArgs, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoSetBlockSwap, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, easy cleanGpuUsed]
problems: []
missing: [CR Text, CR Text Concatenate, ImageCASharpening+, LayerUtility: PurgeVRAM V2, LayerUtility: TextJoin, MathExpression|pysssss, easy cleanGpuUsed, CR String To Number, easy int, ImageResize+]
members: [视频生成/文生视频/1951450598304591874.json, 视频生成/文生视频/1952274672039743489.json, 视频生成/文生视频/1978980050555015169.json, 视频生成/文生视频/1958341618350899202.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_549

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/1951450598304591874.json、视频生成/文生视频/1952274672039743489.json、视频生成/文生视频/1978980050555015169.json、视频生成/文生视频/1958341618350899202.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：55%

## 共有节点

全部 4 个 workflow 都包含：
- `Anything Everywhere`
- `CLIPVisionLoader`
- `CR Text`
- `CogVideoEnhanceAVideo`
- `ColorCorrectOfUtils`
- `CreateCFGScheduleFloatList`
- `FluxResolutionNode`
- `GetNode`
- `ImageCASharpening+`
- `Int`
- `JWInteger`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `RHHiddenNodes`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoExperimentalArgs`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `CR Text Concatenate` —— 3/4 个有
- `CR String To Number` —— 2/4 个有
- `ImageResize+` —— 2/4 个有
- `ImpactStringSelector` —— 2/4 个有
- `ImpactSwitch` —— 2/4 个有
- `InversionDemoLazyIndexSwitch` —— 2/4 个有
- `JjkText` —— 2/4 个有
- `LayerUtility: TextJoin` —— 2/4 个有
- `RH_Prompter` —— 2/4 个有
- `RH_Translator` —— 2/4 个有
- `RandomPrompt` —— 2/4 个有
- `Seed` —— 2/4 个有
- `ShowText|pysssss` —— 2/4 个有
- `TextCombinerTwo` —— 2/4 个有
- `WanVideoClipVisionEncode` —— 2/4 个有
- `WanVideoEmptyEmbeds` —— 2/4 个有
- `WanVideoImageToVideoEncode` —— 2/4 个有
- `easy int` —— 2/4 个有
- `easy showAnything` —— 2/4 个有
- `easy textSwitch` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、CR Text Concatenate、ImageCASharpening+、LayerUtility: PurgeVRAM V2、LayerUtility: TextJoin

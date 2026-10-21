---
name: unknown_workflow_video_lora_sampler_927
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.543
common_nodes: [Anything Everywhere, CLIPVisionLoader, CR Text, CR Text Concatenate, CogVideoEnhanceAVideo, ColorCorrectOfUtils, CreateCFGScheduleFloatList, FluxResolutionNode, GetNode, ImageCASharpening+, ImpactStringSelector, ImpactSwitch, Int, JWInteger, JjkText, LayerUtility: PurgeVRAM V2, LayerUtility: TextJoin, LoadImage, LoadWanVideoT5TextEncoder, MathExpression|pysssss, RHHiddenNodes, RH_Prompter, RH_Translator, RandomPrompt, Seed, SetNode, ShowText|pysssss, TextCombinerTwo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoExperimentalArgs, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoSetBlockSwap, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, easy cleanGpuUsed]
problems: []
missing: [CR Text, CR Text Concatenate, ImageCASharpening+, LayerUtility: PurgeVRAM V2, LayerUtility: TextJoin, MathExpression|pysssss, easy cleanGpuUsed]
members: [视频生成/文生视频/1951450598304591874.json, 视频生成/文生视频/1952274672039743489.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_927

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/1951450598304591874.json、视频生成/文生视频/1952274672039743489.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：54%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere`
- `CLIPVisionLoader`
- `CR Text`
- `CR Text Concatenate`
- `CogVideoEnhanceAVideo`
- `ColorCorrectOfUtils`
- `CreateCFGScheduleFloatList`
- `FluxResolutionNode`
- `GetNode`
- `ImageCASharpening+`
- `ImpactStringSelector`
- `ImpactSwitch`
- `Int`
- `JWInteger`
- `JjkText`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: TextJoin`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `RHHiddenNodes`
- `RH_Prompter`
- `RH_Translator`
- `RandomPrompt`
- `Seed`
- `SetNode`
- `ShowText|pysssss`
- `TextCombinerTwo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
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

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、CR Text Concatenate、ImageCASharpening+、LayerUtility: PurgeVRAM V2、LayerUtility: TextJoin
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

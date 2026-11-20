---
name: unknown_workflow_generic_1973
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9355
common_nodes: [CR Prompt Text, CR Text Concatenate, LoadAudio, LoadImage, LoadVideo, RHHiddenNodes, RH_LLMAPI_Pro_Node, RH_Nano_Banana2_Gemini31Flash, RH_RhartImageG2TextToImage, RH_RhartVideoSparkvideo20MultimodalVideo, RH_SparkVideoAssetCreate, RH_SparkVideoAssetIdsMerge, SaveImage, SaveVideo, ShellAgentPluginOutputText, Text Multiline, easy showAnything]
problems: []
missing: []
members: [平台全量/短片制作_2055405415717974018.json, 平台全量/资产设计：真人短剧_2057880127467507713.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1973

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/短片制作_2055405415717974018.json、平台全量/资产设计：真人短剧_2057880127467507713.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Prompt Text`
- `CR Text Concatenate`
- `LoadAudio`
- `LoadImage`
- `LoadVideo`
- `RHHiddenNodes`
- `RH_LLMAPI_Pro_Node`
- `RH_Nano_Banana2_Gemini31Flash`
- `RH_RhartImageG2TextToImage`
- `RH_RhartVideoSparkvideo20MultimodalVideo`
- `RH_SparkVideoAssetCreate`
- `RH_SparkVideoAssetIdsMerge`
- `SaveImage`
- `SaveVideo`
- `ShellAgentPluginOutputText`
- `Text Multiline`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Image Flip` —— 1/2 个有
- `Image Tiled` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `RH_Nano_Banana2_Image2Image` —— 1/2 个有
- `RH_RhartVideoSparkvideo20FastMultimodalVideo` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

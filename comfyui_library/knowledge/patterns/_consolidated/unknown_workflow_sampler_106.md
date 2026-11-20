---
name: unknown_workflow_sampler_106
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7615
common_nodes: [CR SDXL Aspect Ratio, LayerUtility: PurgeVRAM, Primitive integer [Crystools], RH_LLMAPI_NODE, RunningHub PosterCraft Pipeline, RunningHub PosterCraft Sampler, SaveImage, StringReplace, Text Multiline, easy compare, easy ifElse, easy showAnything]
problems: []
missing: []
members: [图片生成/文生图/电影海报设计_1938640741998452737.json, 平台全量/电影级海报设计-PosterCraft（美团）_1939579458997166081.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_106

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/电影海报设计_1938640741998452737.json、平台全量/电影级海报设计-PosterCraft（美团）_1939579458997166081.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：76%

## 共有节点

全部 2 个 workflow 都包含：
- `CR SDXL Aspect Ratio`
- `LayerUtility: PurgeVRAM`
- `Primitive integer [Crystools]`
- `RH_LLMAPI_NODE`
- `RunningHub PosterCraft Pipeline`
- `RunningHub PosterCraft Sampler`
- `SaveImage`
- `StringReplace`
- `Text Multiline`
- `easy compare`
- `easy ifElse`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `GoogleTranslateTextNode` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

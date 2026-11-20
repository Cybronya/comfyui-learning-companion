---
name: unknown_workflow_generic_1357
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8605
common_nodes: [CR Text, Dapao_LlamaCaption, Dapao_LlamaCaptionOptions, LoadImage, RH_RhartImageG2ImageToImage, RegexReplace, SaveImage, easy promptConcat]
problems: []
missing: []
members: [图片生成/图生图/G PT-image 2穿搭商品主图 自动提示词_2096107883325902850.json, 图片生成/图生图/服装pod-插画改印花图案_2094219839891140609.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1357

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/G PT-image 2穿搭商品主图 自动提示词_2096107883325902850.json、图片生成/图生图/服装pod-插画改印花图案_2094219839891140609.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Text`
- `Dapao_LlamaCaption`
- `Dapao_LlamaCaptionOptions`
- `LoadImage`
- `RH_RhartImageG2ImageToImage`
- `RegexReplace`
- `SaveImage`
- `easy promptConcat`

**可变部分**（部分 workflow 才有）：
- `HAIGC_SaveImagesToZip` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

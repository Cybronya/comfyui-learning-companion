---
name: unknown_workflow_img2img
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.883
common_nodes: [LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: TextBox, LoadImage, RH_RhartImageG2ImageToImage, RH_RhartImageG2TextToImage, SaveImage, Text, easy showAnything]
problems: []
missing: []
members: [图片生成/文生图/全能图片G2 -内搭超强提示词skill_2087103969670811650.json, 图片生成/文生图/全能图片G2提示词优化版——轻松复刻任意图像_2057341576967450626.json]
source: knowledge_consolidation
---

# unknown_workflow_img2img

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/全能图片G2 -内搭超强提示词skill_2087103969670811650.json、图片生成/文生图/全能图片G2提示词优化版——轻松复刻任意图像_2057341576967450626.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 2 个 workflow 都包含：
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: TextBox`
- `LoadImage`
- `RH_RhartImageG2ImageToImage`
- `RH_RhartImageG2TextToImage`
- `SaveImage`
- `Text`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 1/2 个有
- `RHImg2ImgPromptOptimizer` —— 1/2 个有
- `RHLLMChatNode` —— 1/2 个有
- `RHTxt2ImgPromptOptimizer` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

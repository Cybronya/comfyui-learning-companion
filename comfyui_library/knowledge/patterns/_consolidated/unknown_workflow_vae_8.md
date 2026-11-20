---
name: unknown_workflow_vae_8
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.92
common_nodes: [Int, LoadImage, RHHiddenNodes, SaveImage, Seed_, easy positive]
problems: []
missing: []
members: [图片生成/图生图/QY6-人像衣合换装大师（Qwen-image-Edit）手动版 服装上身，指定模特，一键多图人物_1966477120040022018.json, 图片生成/图生图/QY6-人像衣合换装大师（Qwen-image-Edit）自动版 两张变千张，模特换装，换衣，迁移_1965286906424643586.json]
source: knowledge_consolidation
---

# unknown_workflow_vae_8

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/QY6-人像衣合换装大师（Qwen-image-Edit）手动版 服装上身，指定模特，一键多图人物_1966477120040022018.json、图片生成/图生图/QY6-人像衣合换装大师（Qwen-image-Edit）自动版 两张变千张，模特换装，换衣，迁移_1965286906424643586.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `Int`
- `LoadImage`
- `RHHiddenNodes`
- `SaveImage`
- `Seed_`
- `easy positive`

**可变部分**（部分 workflow 才有）：
- `Mute / Bypass Repeater (rgthree)` —— 1/2 个有
- `PlaySound|pysssss` —— 1/2 个有
- `VAEDecode` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

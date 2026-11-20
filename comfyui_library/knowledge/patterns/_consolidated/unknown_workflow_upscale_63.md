---
name: unknown_workflow_upscale_63
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.712
common_nodes: [APISR_ModelLoader_Zho, APISR_Zho, CCSR_Model_Select, CCSR_Upscale, Image Comparer (rgthree), LoadImage, SUPIR_Upscale, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/SUPIR、APISR、CCSE高清放大_1977254092118609921.json, 平台全量/几种节点放大工作流_1937841957005606913.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_63

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/SUPIR、APISR、CCSE高清放大_1977254092118609921.json、平台全量/几种节点放大工作流_1937841957005606913.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：71%

## 共有节点

全部 2 个 workflow 都包含：
- `APISR_ModelLoader_Zho`
- `APISR_Zho`
- `CCSR_Model_Select`
- `CCSR_Upscale`
- `Image Comparer (rgthree)`
- `LoadImage`
- `SUPIR_Upscale`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `AuraSR.AuraSRUpscaler` —— 1/2 个有
- `PreviewImage` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

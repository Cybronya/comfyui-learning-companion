---
name: unknown_workflow_sampler_vae_85
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [CLIPVisionLoader, LoadImage, LucidFlux_SM_Encode, LucidFlux_SM_KSampler, LucidFlux_SM_Model, SaveImage, VAELoader]
problems: []
missing: []
members: [平台全量/LucidFlux小图放大_1975712924431986689.json, 平台全量/LucidFlux小图放大老照片修复_1975724571519225857.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_85

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/LucidFlux小图放大_1975712924431986689.json、平台全量/LucidFlux小图放大老照片修复_1975724571519225857.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPVisionLoader`
- `LoadImage`
- `LucidFlux_SM_Encode`
- `LucidFlux_SM_KSampler`
- `LucidFlux_SM_Model`
- `SaveImage`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 1/2 个有
- `DualCLIPLoader` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

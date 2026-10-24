---
name: unknown_workflow_controlnet_sampler_3
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9285
common_nodes: [LoadImage, SaveImage, easy comfyLoader, easy controlnetStack, easy kSampler, easy negative, easy positive, easy preSampling, easy stylesSelector]
problems: []
missing: []
members: [图片生成/图生图/破限专用艺术二维码，防检测_1959562406169096193.json, 图片生成/图生图/艺术二维码SD15_1955858256218521602.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_sampler_3

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/破限专用艺术二维码，防检测_1959562406169096193.json、图片生成/图生图/艺术二维码SD15_1955858256218521602.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `LoadImage`
- `SaveImage`
- `easy comfyLoader`
- `easy controlnetStack`
- `easy kSampler`
- `easy negative`
- `easy positive`
- `easy preSampling`
- `easy stylesSelector`

**可变部分**（部分 workflow 才有）：
- `UltimateSDUpscale` —— 1/2 个有
- `UpscaleModelLoader` —— 1/2 个有
- `easy pipeOut` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

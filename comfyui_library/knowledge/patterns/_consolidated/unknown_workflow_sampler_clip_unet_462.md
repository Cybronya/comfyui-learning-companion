---
name: unknown_workflow_sampler_clip_unet_462
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9305
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, KSamplerSelect, ResolutionMaster, SamplerCustom, SaveImage, UNETLoader, VAEDecode, VAELoader, 孤海注释]
problems: []
missing: []
members: [图片生成/文生图/Krea2基础工作流_2071130227035693057.json, 图片生成/文生图/Krea2最强动漫平涂风格工作流_2071710345021976577.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_462

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Krea2基础工作流_2071130227035693057.json、图片生成/文生图/Krea2最强动漫平涂风格工作流_2071710345021976577.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `KSamplerSelect`
- `ResolutionMaster`
- `SamplerCustom`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 1/2 个有
- `StringConcatenate` —— 1/2 个有
- `StringConstant` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

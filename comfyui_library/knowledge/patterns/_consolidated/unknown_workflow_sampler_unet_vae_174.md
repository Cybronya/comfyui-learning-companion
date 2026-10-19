---
name: unknown_workflow_sampler_unet_vae_174
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 1
common_nodes: [BasicGuider, CLIPLoader, LoadImage, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax H3｜OpenVDN DMD8｜首尾帧视频_2098317979074260993.json, 视频生成/文生视频/MiniMax H3｜PDD 8步｜参考生视频_2098326349755805698.json, 视频生成/文生视频/MiniMax H3｜PDD 8步｜首尾帧视频_2098317966491340801.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_174

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3｜OpenVDN DMD8｜首尾帧视频_2098317979074260993.json、视频生成/文生视频/MiniMax H3｜PDD 8步｜参考生视频_2098326349755805698.json、视频生成/文生视频/MiniMax H3｜PDD 8步｜首尾帧视频_2098317966491340801.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `LoadImage`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3PDD8StepSetupT8Advanced` —— 2/3 个有
- `VHS_VideoCombine` —— 2/3 个有
- `CreateVideo` —— 1/3 个有
- `MiniMaxH3VDNExecutionPlanT8Advanced` —— 1/3 个有
- `MiniMaxH3VDNModelComposerT8Advanced` —— 1/3 个有
- `SaveVideo` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

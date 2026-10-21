---
name: unknown_workflow_sampler_clip_unet_224
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8895
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, ResolutionMaster, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Anima8步极速工作流_2055609870266707970.json, 图片生成/文生图/Anima基础工作流_2061831530498060289.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_224

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Anima8步极速工作流_2055609870266707970.json、图片生成/文生图/Anima基础工作流_2061831530498060289.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `ResolutionMaster`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EasyCache` —— 1/2 个有
- `FaceDetailer` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `SAMLoader` —— 1/2 个有
- `UltralyticsDetectorProvider` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 21 | - | 2 | 48% |
| Prompt 约束强度(CFG) | 2.5 | - | 2 | 40% |
| 采样算法 | euler_ancestral | - | 2 | 50% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 21，样本不足，未给区间，2 个样本，取值分散，一致性仅 48%
- Prompt 约束强度(CFG) 中位数 2.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 40%
- 采样算法 最常用 euler_ancestral，2 个样本，一致性 50%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

---
name: unknown_workflow_lora_sampler_clip_158
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.562
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, Label (rgthree), LoraLoaderModelOnly, Note Plus (mtb), PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [Label (rgthree), Note Plus (mtb)]
members: [图片生成/文生图/1951536173342773249.json, 图片生成/文生图/1952624573403607042.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_158

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1951536173342773249.json、图片生成/文生图/1952624573403607042.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：56%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `Label (rgthree)`
- `LoraLoaderModelOnly`
- `Note Plus (mtb)`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere` —— 1/2 个有
- `EmptyHunyuanLatentVideo` —— 1/2 个有
- `EmptyLatentImage` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `ModelPassThrough` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有
- `SetNode` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 2 | 50% |
| Prompt 约束强度(CFG) | 30 | - | 2 | 100% |
| 采样算法 | 2 | - | 2 | 50% |
| 调度器 | res_2s | - | 2 | 100% |
| 重绘幅度 | bong_tangent | - | 2 | 100% |
| 宽度 | 1920 | - | 1 | 100% |
| 高度 | 1088 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，2 个样本，一致性 50%
- Prompt 约束强度(CFG) 中位数 30，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 2，样本不足，未给区间，2 个样本
- 调度器 最常用 res_2s，2 个样本，一致性 100%
- 重绘幅度 最常用 bong_tangent，2 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 30，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 这些节点还没有知识卡，系统对它们的理解有限：Label (rgthree)、Note Plus (mtb)
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

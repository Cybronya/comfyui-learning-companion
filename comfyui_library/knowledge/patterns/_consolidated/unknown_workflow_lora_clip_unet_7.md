---
name: unknown_workflow_lora_clip_unet_7
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.553
common_nodes: [Anything Everywhere, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, Int, LoraLoaderModelOnly, SaveImage, UNETLoader, VAELoader]
problems: []
missing: [workflow>0, workflow>HAOTU]
members: [图片生成/文生图/1904522837061767169.json, 图片生成/文生图/1951943157778993154.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_clip_unet_7

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1904522837061767169.json、图片生成/文生图/1951943157778993154.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：55%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `Int`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere3` —— 1/2 个有
- `FluxGuidance` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `workflow>0` —— 1/2 个有
- `workflow>HAOTU` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 1536 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1536，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：workflow>0、workflow>HAOTU
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

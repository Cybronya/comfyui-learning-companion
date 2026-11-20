---
name: unknown_workflow_sampler_clip_unet_487
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9705
common_nodes: [CLIPLoader, CLIPTextEncode, CR SDXL Aspect Ratio, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/泠月luna_固定人物出图。Z-image Base_luna_v4_ckpt16_2043661655762014209.json, 图片生成/文生图/满血版QWen-Image中文渲染-ComfyUI_1954857769355534338.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_487

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/泠月luna_固定人物出图。Z-image Base_luna_v4_ckpt16_2043661655762014209.json、图片生成/文生图/满血版QWen-Image中文渲染-ComfyUI_1954857769355534338.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：97%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR SDXL Aspect Ratio`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 1/2 个有
- `CR Text Concatenate` —— 1/2 个有
- `TTResolutionSelector` —— 1/2 个有
- `Text Multiline` —— 1/2 个有
- `workflow>lora pipe` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 14 | - | 2 | 57% |
| Prompt 约束强度(CFG) | 1.75 | - | 2 | 57% |
| 采样算法 | res_2s | - | 2 | 50% |
| 调度器 | bong_tangent | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 14，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 1.75，样本不足，未给区间，2 个样本
- 采样算法 最常用 res_2s，2 个样本，一致性 50%
- 调度器 最常用 bong_tangent，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

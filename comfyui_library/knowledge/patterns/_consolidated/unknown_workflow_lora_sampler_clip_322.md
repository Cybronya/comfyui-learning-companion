---
name: unknown_workflow_lora_sampler_clip_322
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.895
common_nodes: [CLIPTextEncode, CR Prompt Text, CheckpointLoaderSimple, DuckDecodeNode, DuckHideNode, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, PreviewImage, QwenImageLatentAspectRatio, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/文生图/文生图多样化，RedZImage_2004922799263285249.json, 图片生成/文生图/极速文生图，多样化，差异化，Red-Z-Image_2004551496664580098.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_322

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/文生图多样化，RedZImage_2004922799263285249.json、图片生成/文生图/极速文生图，多样化，差异化，Red-Z-Image_2004551496664580098.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CR Prompt Text`
- `CheckpointLoaderSimple`
- `DuckDecodeNode`
- `DuckHideNode`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `QwenImageLatentAspectRatio`
- `SaveImage`
- `VAEDecode`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 2 | 100% |
| Prompt 约束强度(CFG) | 9 | - | 2 | 100% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler | - | 2 | 100% |
| 重绘幅度 | ddim_uniform | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 9，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，2 个样本，一致性 100%
- 重绘幅度 最常用 ddim_uniform，2 个样本，一致性 100%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

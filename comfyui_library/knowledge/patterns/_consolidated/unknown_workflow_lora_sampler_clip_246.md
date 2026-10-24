---
name: unknown_workflow_lora_sampler_clip_246
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.827
common_nodes: [CLIPTextEncode, DualCLIPLoader, Florence2ModelLoader, Florence2Run, FluxSamplerParams+, LoadImage, LoraLoader, SaveImage, ShowText|pysssss, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/flux图生图细节修复(反推提示词+提示词优化)_1911768650767106049.json, 图片生成/图生图/万物洗图_2038456629854736385.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_246

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/flux图生图细节修复(反推提示词+提示词优化)_1911768650767106049.json、图片生成/图生图/万物洗图_2038456629854736385.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `Florence2ModelLoader`
- `Florence2Run`
- `FluxSamplerParams+`
- `LoadImage`
- `LoraLoader`
- `SaveImage`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 1/2 个有
- `ImageScale` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `RH_Prompter` —— 1/2 个有
- `TextCombinerTwo` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.8 | - | 2 | 75% |
| LoRA 文本强度 | 0.8 | - | 2 | 75% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.8，样本不足，未给区间，2 个样本
- LoRA 文本强度 中位数 0.8，样本不足，未给区间，2 个样本
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

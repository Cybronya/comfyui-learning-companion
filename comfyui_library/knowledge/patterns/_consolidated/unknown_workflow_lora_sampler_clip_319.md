---
name: unknown_workflow_lora_sampler_clip_319
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8845
common_nodes: [BasicGuider, BasicScheduler, Bjornulf_ShowStringText, CLIPTextEncode, DualCLIPLoader, EG_FX_BDAPI, EmptyLatentImage, Fast Groups Muter (rgthree), Joy_caption, Joy_caption_load, KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader, ttN concat]
problems: []
missing: []
members: [图片生成/文生图/文生图+图生图（超强款）Flux超强工作流_1920133263510142977.json, 图片生成/文生图/文生图+图生图（超强款）Flux超强工作流_2054447855447879682.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_319

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/文生图+图生图（超强款）Flux超强工作流_1920133263510142977.json、图片生成/文生图/文生图+图生图（超强款）Flux超强工作流_2054447855447879682.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `Bjornulf_ShowStringText`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EG_FX_BDAPI`
- `EmptyLatentImage`
- `Fast Groups Muter (rgthree)`
- `Joy_caption`
- `Joy_caption_load`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `ttN concat`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | - | 2 | 100% |
| 高度 | 1024 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 768，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

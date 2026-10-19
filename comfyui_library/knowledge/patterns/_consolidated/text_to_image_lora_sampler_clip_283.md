---
name: text_to_image_lora_sampler_clip_283
type: Text To Image
frequency: 2
level: weak
coverage: 0.9165
common_nodes: [CLIPTextEncode, CLIPTextEncodeFlux, DualCLIPLoader, EmptyLatentImage, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/1955513316471816194.json, 图片生成/文生图/1985255145997017090.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_283

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1955513316471816194.json、图片生成/文生图/1985255145997017090.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPTextEncodeFlux`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere3` —— 1/2 个有
- `DF_Text_Box` —— 1/2 个有
- `FluxResolutionNode` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有
- `RandomPrompt` —— 1/2 个有
- `TeaCache` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 864 | - | 2 | 89% |
| 高度 | 1280 | - | 2 | 80% |
| 采样步数 | 22.5 | - | 2 | 89% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 50% |
| 调度器 | simple | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 864，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- 高度 中位数 1280，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- 采样步数 中位数 22.5，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 50%
- 调度器 最常用 simple，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

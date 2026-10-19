---
name: text_to_image_sampler_clip_unet_28
type: Text To Image
frequency: 2
level: weak
coverage: 0.909
common_nodes: [CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, FluxGuidance, KSampler, PreviewImage, SaveImage, UnetLoaderGGUF, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/1961449815852957697.json, 图片生成/文生图/FLUX GGUF Q4 更节约显存，出图更快_1829532907324231681.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_28

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1961449815852957697.json、图片生成/文生图/FLUX GGUF Q4 更节约显存，出图更快_1829532907324231681.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `KSampler`
- `PreviewImage`
- `SaveImage`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAELoader`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 768 | - | 2 | 100% |
| 高度 | 1024 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 768，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

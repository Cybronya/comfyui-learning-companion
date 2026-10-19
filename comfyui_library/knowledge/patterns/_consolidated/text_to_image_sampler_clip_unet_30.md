---
name: text_to_image_sampler_clip_unet_30
type: Text To Image
frequency: 2
level: weak
coverage: 0.847
common_nodes: [CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, FluxGuidance, KSampler, LoadImage, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [PlaySound|pysssss]
members: [图片生成/文生图/1978296045392257025.json, 视频生成/图生视频/1947265490784784385.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_30

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1978296045392257025.json、视频生成/图生视频/1947265490784784385.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextImageScale` —— 1/2 个有
- `FluxPromptEnhance` —— 1/2 个有
- `Kontext Inpainting Conditioning` —— 1/2 个有
- `LoraLoader` —— 1/2 个有
- `PlaySound|pysssss` —— 1/2 个有
- `RH_Translator` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 24 | - | 2 | 83% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | beta | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 1280 | - | 2 | 80% |
| 高度 | 1152 | - | 2 | 67% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 24，样本不足，未给区间，2 个样本，取值集中（一致性 83%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 1280，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- 高度 中位数 1152，样本不足，未给区间，2 个样本
- 这些节点还没有知识卡，系统对它们的理解有限：PlaySound|pysssss
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

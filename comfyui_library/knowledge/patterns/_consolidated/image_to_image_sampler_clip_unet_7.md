---
name: image_to_image_sampler_clip_unet_7
type: Image To Image
frequency: 2
level: weak
coverage: 1
common_nodes: [CLIPTextEncodeFlux, ConditioningZeroOut, DualCLIPLoader, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/1930828932625399809.json, 图片生成/文生图/1959641912976289793.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_7

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1930828932625399809.json、图片生成/文生图/1959641912976289793.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncodeFlux`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyLatentImage` —— 1/2 个有
- `ImageUpscaleWithModel` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `RH_Translator` —— 1/2 个有
- `RepeatLatentBatch` —— 1/2 个有
- `UpscaleModelLoader` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 18 | - | 2 | 89% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | normal | - | 2 | 50% |
| 重绘幅度 | 0.4 | - | 2 | 88% |
| 宽度 | 768 | - | 1 | 100% |
| 高度 | 1024 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 18，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 50%
- 重绘幅度 中位数 0.4，样本不足，未给区间，2 个样本，取值集中（一致性 88%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

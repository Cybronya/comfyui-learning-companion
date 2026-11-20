---
name: text_to_image_lora_sampler_clip_690
type: Text To Image
frequency: 2
level: weak
coverage: 0.9545
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, EmptyLatentImage, KSampler, LoraLoaderModelOnly, ResolutionSelector, SaveImage, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/文生图/【API】ANIMA文生图_2111986830584410113.json, 图片生成/文生图/【API】Krea2文生图（巨构）_2111986910141964289.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_690

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/【API】ANIMA文生图_2111986830584410113.json、图片生成/文生图/【API】Krea2文生图（巨构）_2111986910141964289.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `ResolutionSelector`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 1/2 个有
- `Display Any (rgthree)` —— 1/2 个有
- `JoinStringMulti` —— 1/2 个有
- `PlaySound|pysssss` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `Seed (rgthree)` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | - | 2 | 40% |
| Prompt 约束强度(CFG) | 3 | - | 2 | 33% |
| 采样算法 | dpmpp_2m | - | 2 | 50% |
| 调度器 | beta57 | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 512 | - | 2 | 100% |
| 高度 | 512 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，样本不足，未给区间，2 个样本，取值分散，一致性仅 40%
- Prompt 约束强度(CFG) 中位数 3，样本不足，未给区间，2 个样本，取值分散，一致性仅 33%
- 采样算法 最常用 dpmpp_2m，2 个样本，一致性 50%
- 调度器 最常用 beta57，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

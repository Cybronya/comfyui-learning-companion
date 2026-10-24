---
name: text_to_image_lora_sampler_clip_633
type: Text To Image
frequency: 2
level: weak
coverage: 0.85
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, ConditioningZeroOut, EmptyLatentImage, ImpactSwitch, JC, KSampler, LoraLoaderModelOnly, RHUploadZip, SaveImage, ShowText|pysssss, Text Load Line From File, Text Multiline, UNETLoader, VAEDecode, VAELoader, easy promptConcat]
problems: []
missing: []
members: [图片生成/文生图/Z-image 批量洗图，自动反推，文生图，批量生图三合一_2075736828098994178.json, 图片生成/文生图/福利鉴 · Z-Image 同风格生成_2082002632369070082.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_633

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Z-image 批量洗图，自动反推，文生图，批量生图三合一_2075736828098994178.json、图片生成/文生图/福利鉴 · Z-Image 同风格生成_2082002632369070082.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `ImpactSwitch`
- `JC`
- `KSampler`
- `LoraLoaderModelOnly`
- `RHUploadZip`
- `SaveImage`
- `ShowText|pysssss`
- `Text Load Line From File`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy promptConcat`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | - | 2 | 100% |
| 高度 | 1920 | - | 2 | 100% |
| 采样步数 | 10 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | ddim | - | 2 | 100% |
| 调度器 | sgm_uniform | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1080，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1920，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 10，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 ddim，2 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

---
name: text_to_image_lora_sampler_clip_676
type: Text To Image
frequency: 2
level: weak
coverage: 0.9165
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, EmptyLatentImage, FluxGuidance, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Flux风格选择器加速生图_2078378029721677826.json, 图片生成/文生图/亚洲人脸 脸模005 美女 模特 电商_1935524742722158593.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_676

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Flux风格选择器加速生图_2078378029721677826.json、图片生成/文生图/亚洲人脸 脸模005 美女 模特 电商_1935524742722158593.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Int` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `ModelSamplingFlux` —— 1/2 个有
- `RH_Translator` —— 1/2 个有
- `easy stylesSelector` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | - | 2 | 67% |
| 高度 | 1024 | - | 2 | 50% |
| 采样步数 | 16 | - | 2 | 75% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | normal | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 768，样本不足，未给区间，2 个样本
- 高度 中位数 1024，样本不足，未给区间，2 个样本
- 采样步数 中位数 16，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

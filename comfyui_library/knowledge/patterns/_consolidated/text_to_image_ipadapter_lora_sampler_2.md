---
name: text_to_image_ipadapter_lora_sampler_2
type: Text To Image
frequency: 2
level: weak
coverage: 0.818
common_nodes: [CLIPTextEncode, CR Text, CR Text Concatenate, CR Text Input Switch, CheckpointLoaderSimple, EmptyLatentImage, FluxResolutionNode, IPAdapterAdvanced, IPAdapterUnifiedLoader, Image Comparer (rgthree), Int, KSampler, LatentPixelScale, LoadImage, LoraLoaderModelOnly, PreviewImage, PrimitiveFloat, SaveImage, ShowText|pysssss, VAEDecode, WD14Tagger|pysssss, ttN concat]
problems: []
missing: []
members: [图片生成/文生图/动漫壁纸 卡通风格屏保 高质量动漫壁纸一键生成_2079406854928687105.json, 图片生成/文生图/高质量动漫壁纸一键生成_1939667309999132674.json]
source: knowledge_consolidation
---

# text_to_image_ipadapter_lora_sampler_2

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/动漫壁纸 卡通风格屏保 高质量动漫壁纸一键生成_2079406854928687105.json、图片生成/文生图/高质量动漫壁纸一键生成_1939667309999132674.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CR Text`
- `CR Text Concatenate`
- `CR Text Input Switch`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `FluxResolutionNode`
- `IPAdapterAdvanced`
- `IPAdapterUnifiedLoader`
- `Image Comparer (rgthree)`
- `Int`
- `KSampler`
- `LatentPixelScale`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `PrimitiveFloat`
- `SaveImage`
- `ShowText|pysssss`
- `VAEDecode`
- `WD14Tagger|pysssss`
- `ttN concat`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 720 | - | 2 | 100% |
| 高度 | 1280 | - | 2 | 100% |
| 采样步数 | 30 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 3.5 | - | 2 | 100% |
| 采样算法 | euler_ancestral | - | 2 | 100% |
| 调度器 | sgm_uniform | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 720，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1280，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 30，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 3.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，2 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

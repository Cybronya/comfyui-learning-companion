---
name: text_to_image_controlnet_sampler_clip_32
type: Text To Image
frequency: 2
level: weak
coverage: 0.875
common_nodes: [CLIPTextEncode, ConditioningZeroOut, ControlNetApplyAdvanced, ControlNetLoader, DualCLIPLoaderGGUF, EmptyLatentImage, FluxGuidance, KSampler, LayerUtility: ImageRemoveAlpha, LayerUtility: TextImage V2, LineArtPreprocessor, PreviewImage, SaveImage, SetUnionControlNetType, UnetLoaderGGUF, VAEDecode, VAELoader, easy imageSize]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/B8、文字平面海报_1993286200475795458.json, 平台全量/艺术字体_1932289816170233858.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_sampler_clip_32

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/B8、文字平面海报_1993286200475795458.json、平台全量/艺术字体_1932289816170233858.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DualCLIPLoaderGGUF`
- `EmptyLatentImage`
- `FluxGuidance`
- `KSampler`
- `LayerUtility: ImageRemoveAlpha`
- `LayerUtility: TextImage V2`
- `LineArtPreprocessor`
- `PreviewImage`
- `SaveImage`
- `SetUnionControlNetType`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAELoader`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `ACE_TextTranslate` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `PreviewAny` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | - | 2 | 100% |
| 高度 | 512 | - | 2 | 100% |
| ControlNet 权重 | 0.65 | - | 2 | 77% |
| 采样步数 | 7.5 | - | 2 | 67% |
| Prompt 约束强度(CFG) | 1.5 | - | 2 | 67% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | sgm_uniform | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.65，样本不足，未给区间，2 个样本
- 采样步数 中位数 7.5，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 1.5，样本不足，未给区间，2 个样本
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

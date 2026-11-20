---
name: unknown_workflow_controlnet_lora_sampler_29
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.909
common_nodes: [CLIPTextEncode, CR Text, CR Text Concatenate, CheckpointLoaderSimple, ControlNetApplySD3, ControlNetLoader, EmptySD3LatentImage, Float, FluxGuidance, GetImageSize, Image Comparer (rgthree), ImageScaleBy, Joy_caption_two, Joy_caption_two_load, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, ShowText|pysssss, VAEDecode]
problems: []
missing: []
members: [图片生成/图生图/FLUX高清修复官方版，适合多种风格人像_1915025578699780098.json, 平台全量/flux丨Upscaler高清修复+增加细节_1899718436807725058.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_lora_sampler_29

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/FLUX高清修复官方版，适合多种风格人像_1915025578699780098.json、平台全量/flux丨Upscaler高清修复+增加细节_1899718436807725058.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CR Text`
- `CR Text Concatenate`
- `CheckpointLoaderSimple`
- `ControlNetApplySD3`
- `ControlNetLoader`
- `EmptySD3LatentImage`
- `Float`
- `FluxGuidance`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `Joy_caption_two`
- `Joy_caption_two_load`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `ShowText|pysssss`
- `VAEDecode`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | normal | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| ControlNet 权重 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

---
name: text_to_image_upscale_lora_sampler_66
type: Text To Image
frequency: 2
level: weak
coverage: 0.5055
common_nodes: [Anything Everywhere, CLIPSetLastLayer, CLIPTextEncode, CLIPTextEncodeSDXL, CheckpointLoaderSimple, DuckHideNode, EmptyLatentImage, GetNode, ImageScaleBy, ImageUpscaleWithModel, JoinStringMulti, KSampler, KSamplerAdvanced, LoraLoaderModelOnly, SaveImage, SaveLatent, SetNode, UpscaleModelLoader, VAEDecode, VAEEncode, easy positive]
problems: []
missing: []
members: [图片生成/文生图/动漫文生图合集版1_2062038484747116546.json, 图片生成/文生图/动漫文生图合集版2_2063455251587485697.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_66

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/动漫文生图合集版1_2062038484747116546.json、图片生成/文生图/动漫文生图合集版2_2063455251587485697.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：51%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere`
- `CLIPSetLastLayer`
- `CLIPTextEncode`
- `CLIPTextEncodeSDXL`
- `CheckpointLoaderSimple`
- `DuckHideNode`
- `EmptyLatentImage`
- `GetNode`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `JoinStringMulti`
- `KSampler`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `SaveImage`
- `SaveLatent`
- `SetNode`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `easy positive`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 2 | 100% |
| Prompt 约束强度(CFG) | 30 | - | 2 | 100% |
| 采样算法 | 4 | - | 2 | 100% |
| 调度器 | ddim | - | 2 | 100% |
| 重绘幅度 | ddim_uniform | - | 2 | 100% |
| 宽度 | 768 | - | 2 | 100% |
| 高度 | 1216 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 30，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 ddim，2 个样本，一致性 100%
- 重绘幅度 最常用 ddim_uniform，2 个样本，一致性 100%
- 宽度 中位数 768，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1216，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 30，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

---
name: image_to_image_lora_sampler_unet_50
type: Image To Image
frequency: 12
level: moderate
coverage: 0.88475
common_nodes: [CFGNorm, CLIPLoader, ConditioningZeroOut, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, ReferenceLatent, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen 2511-角色全身侧面站立图_2082270603360428034.json, 图片生成/图生图/Qwen 2511-角色全身正面站立图_2082264674363592706.json, 图片生成/图生图/Qwen-Image-Edit ComfyUI 原生工作流 1图_2089987209536561154.json, 图片生成/图生图/Qwen-Image-Edit ComfyUI 原生工作流 2图_2089986353214873602.json, 图片生成/图生图/Qwen-Image-Edit ComfyUI 原生工作流 3图_2089973995432136705.json, 图片生成/图生图/Qwen-Image-Edit ComfyUI 原生工作流_1971196767998033922.json, 图片生成/图生图/Three-View Drawings三视图 qwen_image_edit_2511_2093148144774246401.json, 图片生成/图生图/qwen2511移除主体_无痕局部重绘_消除指定物体__2067436200457236481.json, 图片生成/图生图/qwen2511移除主体_无痕局部重绘_消除指定物体__2067516185725460482.json, 图片生成/图生图/删除人物保留衣服_2006911696627048449.json, 平台全量/三视图 _ qwen_image_edit_2511_2092836991758061570.json, 平台全量/人像全身白底图_2092249632813441026.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_50

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/Qwen 2511-角色全身侧面站立图_2082270603360428034.json、图片生成/图生图/Qwen 2511-角色全身正面站立图_2082264674363592706.json、图片生成/图生图/Qwen-Image-Edit ComfyUI 原生工作流 1图_2089987209536561154.json、图片生成/图生图/Qwen-Image-Edit ComfyUI 原生工作流 2图_2089986353214873602.json、图片生成/图生图/Qwen-Image-Edit ComfyUI 原生工作流 3图_2089973995432136705.json…）

- **类型**：Image To Image
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 12 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `ReferenceLatent`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyLatentImage` —— 9/12 个有
- `FluxKontextImageScale` —— 6/12 个有
- `Image Comparer (rgthree)` —— 5/12 个有
- `GetImageSize` —— 3/12 个有
- `YK_LoadImageFromURL` —— 3/12 个有
- `CR Text` —— 2/12 个有
- `LayerUtility: TextJoin` —— 2/12 个有
- `ResizeImageMaskNode` —— 2/12 个有
- `TTResolutionSelector` —— 2/12 个有
- `GenerateNoise` —— 1/12 个有
- `LGNoiseInjectionLatent` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 20 | 12 | 39% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | euler | - | 12 | 100% |
| 调度器 | simple | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |
| 宽度 | 1440 | 512 - 1680 | 9 | 65% |
| 高度 | 768 | 512 - 1920 | 9 | 55% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 20，12 个样本，取值分散，一致性仅 39%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，12 个样本，一致性 100%
- 调度器 最常用 simple，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 宽度 中位数 1440，观测区间 512 - 1680，9 个样本
- 高度 中位数 768，观测区间 512 - 1920，9 个样本
- 高发问题（16/12 个样本）：Steps较低可能导致细节不足

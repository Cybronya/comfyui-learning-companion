---
name: unknown_workflow_upscale_lora_sampler_97
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6445
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, CR Text Concatenate, ConditioningZeroOut, Fast Groups Bypasser (rgthree), GetNode, Image Comparer (rgthree), ImageConcanate, ImageLoader, ImageSharpen, ImageUpscaleWithModel, Int, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoraLoaderModelOnly, MultiplePathsInput, PDIMAGE_LongerSize, PreviewImage, SaveImage, SetNode, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/Z-image图生图 + Qwen2 VQL自动洗图2K版_2004204501164847106.json, 图片生成/图生图/Z-image洗图 + Qwen2 VQL自动洗图 一键反推提示词 2K高清修复洗图重绘图像_2048569628921700354.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_97

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Z-image图生图 + Qwen2 VQL自动洗图2K版_2004204501164847106.json、图片生成/图生图/Z-image洗图 + Qwen2 VQL自动洗图 一键反推提示词 2K高清修复洗图重绘图像_2048569628921700354.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：64%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `CR Text Concatenate`
- `ConditioningZeroOut`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageConcanate`
- `ImageLoader`
- `ImageSharpen`
- `ImageUpscaleWithModel`
- `Int`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoraLoaderModelOnly`
- `MultiplePathsInput`
- `PDIMAGE_LongerSize`
- `PreviewImage`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Float` —— 1/2 个有
- `PrimitiveFloat` —— 1/2 个有
- `Qwen2_VQA` —— 1/2 个有
- `Qwen3_VQA` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

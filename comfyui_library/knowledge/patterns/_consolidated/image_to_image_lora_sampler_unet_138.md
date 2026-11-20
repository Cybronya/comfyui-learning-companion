---
name: image_to_image_lora_sampler_unet_138
type: Image To Image
frequency: 5
level: strong
coverage: 0.8606
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/多角度视角_1998365944550424577.json, 图片生成/图生图/头像生成_2044697290111193089.json, 图片生成/图生图/溶图打光-透视纠正_1980932243189317633.json, 数字人/数字人/QWEN image edit_最新上睫毛终极版_ 许老师版_1985625300958621698.json, 数字人/数字人/qwenImage终极版万能生图_许老师版_1988925629787672578.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_138

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/多角度视角_1998365944550424577.json、图片生成/图生图/头像生成_2044697290111193089.json、图片生成/图生图/溶图打光-透视纠正_1980932243189317633.json、数字人/数字人/QWEN image edit_最新上睫毛终极版_ 许老师版_1985625300958621698.json、数字人/数字人/qwenImage终极版万能生图_许老师版_1988925629787672578.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 4/5 个有
- `FastCanvas` —— 3/5 个有
- `FastCanvasTool` —— 3/5 个有
- `Image Comparer (rgthree)` —— 3/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/5 个有
- `TextEncodeQwenImageEditPlus` —— 3/5 个有
- `easy imageRemBg` —— 3/5 个有
- `ConditioningZeroOut` —— 2/5 个有
- `FluxKontextImageScale` —— 2/5 个有
- `LayerUtility: CropByMask V2` —— 2/5 个有
- `NunchakuQwenImageDiTLoader` —— 2/5 个有
- `TextEncodeQwenImageEdit` —— 2/5 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 2/5 个有
- `AILab_QwenVL` —— 1/5 个有
- `CombineImagesForQwen3VL` —— 1/5 个有
- `GoogleTranslateTextNode` —— 1/5 个有
- `ImageResizePresetNode` —— 1/5 个有
- `ImageScaleBy` —— 1/5 个有
- `PreviewAny` —— 1/5 个有
- `RMBG` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 5 | 69% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 60% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 60%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（11/5 个样本）：Steps较低可能导致细节不足

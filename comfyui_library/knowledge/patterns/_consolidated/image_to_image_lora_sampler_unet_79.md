---
name: image_to_image_lora_sampler_unet_79
type: Image To Image
frequency: 7
level: moderate
coverage: 0.925143
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/23yinhuatiqu_2049394645003669506.json, 图片生成/图生图/2D转3D丨风格转换丨插画、照片一键转换_1980952858050908162.json, 图片生成/图生图/KIWI-qwen-Edit-照片转线稿图_1963555215508328450.json, 图片生成/图生图/KIWI-qwen-Edit-照片转线稿图_1963568662437400578.json, 图片生成/图生图/Qwen Image Edit图片编辑_1958360119752998914.json, 图片生成/图生图/XX2256_1989184998232174594.json, 图片生成/图生图/印花提取-V5优化版_1994271715236790274.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_79

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/反推提示词/23yinhuatiqu_2049394645003669506.json、图片生成/图生图/2D转3D丨风格转换丨插画、照片一键转换_1980952858050908162.json、图片生成/图生图/KIWI-qwen-Edit-照片转线稿图_1963555215508328450.json、图片生成/图生图/KIWI-qwen-Edit-照片转线稿图_1963568662437400578.json、图片生成/图生图/Qwen Image Edit图片编辑_1958360119752998914.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `TextEncodeQwenImageEdit` —— 6/7 个有
- `ImageScaleToTotalPixels` —— 5/7 个有
- `CR Text` —— 4/7 个有
- `EmptyLatentImage` —— 4/7 个有
- `CR Text Concatenate` —— 3/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/7 个有
- `Anything Everywhere3` —— 2/7 个有
- `ImageConcatMulti` —— 2/7 个有
- `PrimitiveFloat` —— 2/7 个有
- `Anything Everywhere` —— 1/7 个有
- `DF_Get_image_size` —— 1/7 个有
- `InpaintModelConditioning` —— 1/7 个有
- `Prompts Everywhere` —— 1/7 个有
- `TextEncodeQwenImageEditPlus` —— 1/7 个有
- `easy cleanGpuUsed` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 5 - 25 | 7 | 47% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 3.5 | 7 | 54% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 1152 | 512 - 1536 | 4 | 58% |
| 高度 | 2480 | 512 - 2480 | 4 | 57% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 5 - 25，7 个样本，取值分散，一致性仅 47%
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 3.5，7 个样本
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 1152，观测区间 512 - 1536，4 个样本
- 高度 中位数 2480，观测区间 512 - 2480，4 个样本

---
name: image_to_image_lora_sampler_unet_10
type: Image To Image
frequency: 6
level: strong
coverage: 0.743667
common_nodes: [CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [CR Text, LayerUtility: ImageScaleByAspectRatio, easy imageConcat]
members: [图片生成/文生图/1958882089787666433.json, 图片生成/文生图/Qwen-Image-Edit-一键转宫崎骏风_2095060097503420418.json, 图片生成/文生图/Qwen（千问）图像处理（文生图，图生图，水印去除）_1990338995290820610.json, 图片生成/文生图/【ComfyUI全注释】真人转动漫_卡通_漫画，3种风格一条流搞定_2060023079732072450.json, 图片生成/文生图/人物换衣服加速版qwen edit plus+全节点注释_2055669100139040769.json, 图片生成/文生图/千问 手办盲盒超火模型_1993973079732846594.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_10

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/1958882089787666433.json、图片生成/文生图/Qwen-Image-Edit-一键转宫崎骏风_2095060097503420418.json、图片生成/文生图/Qwen（千问）图像处理（文生图，图生图，水印去除）_1990338995290820610.json、图片生成/文生图/【ComfyUI全注释】真人转动漫_卡通_漫画，3种风格一条流搞定_2060023079732072450.json、图片生成/文生图/人物换衣服加速版qwen edit plus+全节点注释_2055669100139040769.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：74%

## 共有节点

全部 6 个 workflow 都包含：
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
- `CFGNorm` —— 5/6 个有
- `ImageScaleToTotalPixels` —— 4/6 个有
- `TextEncodeQwenImageEdit` —— 3/6 个有
- `TextEncodeQwenImageEditPlus` —— 3/6 个有
- `easy imageConcat` —— 3/6 个有
- `CR Simple Image Compare` —— 2/6 个有
- `CR Text` —— 2/6 个有
- `ConditioningZeroOut` —— 2/6 个有
- `Image Comparer (rgthree)` —— 2/6 个有
- `PrimitiveStringMultiline` —— 2/6 个有
- `LayerUtility: ImageScaleByAspectRatio` —— 1/6 个有
- `RepeatLatentBatch` —— 1/6 个有
- `ResizeLongestToNode` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 6 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、LayerUtility: ImageScaleByAspectRatio、easy imageConcat

---
name: image_to_image_sampler_vae_19
type: Image To Image
frequency: 8
level: moderate
coverage: 0.962125
common_nodes: [CLIPLoader, KSampler, LoadImage, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/LH-DMT版本-2.生图片类-023.Z_image_turbo图生图_2016484447947853825.json, 图片生成/图生图/Magic-Wan2.2-V2洗图工作流_1994768271901700098.json, 图片生成/图生图/Magic-Wan2.2-洗图工作流_1995468058045112322.json, 图片生成/图生图/Multiple-angles 一致性多角度_2073250359262404610.json, 图片生成/图生图/Qwen image edit plus和自己相拥_1970442909982093313.json, 图片生成/图生图/Qwen-Edit-2511 人物姿势模仿工作流_2091518524282990593.json, 图片生成/图生图/Qwen-Image-Edit 2509：冬日萌宠童话，一键入画，定格魔法瞬间！_1987879653480271873.json, 图片生成/文生图/人像数据集生成_2073290538132004866.json]
source: knowledge_consolidation
---

# image_to_image_sampler_vae_19

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/LH-DMT版本-2.生图片类-023.Z_image_turbo图生图_2016484447947853825.json、图片生成/图生图/Magic-Wan2.2-V2洗图工作流_1994768271901700098.json、图片生成/图生图/Magic-Wan2.2-洗图工作流_1995468058045112322.json、图片生成/图生图/Multiple-angles 一致性多角度_2073250359262404610.json、图片生成/图生图/Qwen image edit plus和自己相拥_1970442909982093313.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `UNETLoader` —— 7/8 个有
- `ImageScaleToTotalPixels` —— 6/8 个有
- `LoraLoaderModelOnly` —— 6/8 个有
- `ModelSamplingAuraFlow` —— 6/8 个有
- `CFGNorm` —— 5/8 个有
- `CLIPTextEncode` —— 5/8 个有
- `TextEncodeQwenImageEditPlus` —— 5/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/8 个有
- `CR Prompt List` —— 2/8 个有
- `CR Text` —— 2/8 个有
- `PreviewImage` —— 2/8 个有
- `SaveImageKJ` —— 2/8 个有
- `StringConcatenate` —— 2/8 个有
- `Text Multiline` —— 2/8 个有
- `DWPreprocessor` —— 1/8 个有
- `NunchakuQwenImageDiTLoader` —— 1/8 个有
- `PrimitiveStringMultiline` —— 1/8 个有
- `TextEncodeQwenImageEdit` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 9 | 8 | 69% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 50% |
| 重绘幅度 | 1 | 0.23 - 1 | 8 | 59% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 9，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 0.23 - 1，8 个样本
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足

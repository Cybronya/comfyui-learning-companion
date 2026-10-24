---
name: image_to_image_sampler_clip_checkpoint_12
type: Image To Image
frequency: 3
level: moderate
coverage: 0.760667
common_nodes: [Anything Everywhere, CLIPTextEncode, CheckpointLoaderSimple, Cut By Mask, DownloadAndLoadFlorence2Model, FaceParse(FaceParsing), FaceParsingModelLoader(FaceParsing), FaceParsingProcessorLoader(FaceParsing), FaceParsingResultsParser(FaceParsing), Florence2Run, GrowMaskWithBlur, Image Comparer (rgthree), ImageCompositeMasked, KSampler, LayerMask: PersonMaskUltra V2, LoadImage, MaskPreview+, MaskToImage, PreviewImage, SaveImage, SetLatentNoiseMask, ShowText|pysssss, VAEDecode, VAEEncode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/去除AI感还原真实皮肤_1924357130613420033.json, 图片生成/图生图/去除AI感还原真实皮肤_2058059091548917761.json, 图片生成/图生图/提升皮肤质感_1903026007530442754.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_checkpoint_12

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/去除AI感还原真实皮肤_1924357130613420033.json、图片生成/图生图/去除AI感还原真实皮肤_2058059091548917761.json、图片生成/图生图/提升皮肤质感_1903026007530442754.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：76%

## 共有节点

全部 3 个 workflow 都包含：
- `Anything Everywhere`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `Cut By Mask`
- `DownloadAndLoadFlorence2Model`
- `FaceParse(FaceParsing)`
- `FaceParsingModelLoader(FaceParsing)`
- `FaceParsingProcessorLoader(FaceParsing)`
- `FaceParsingResultsParser(FaceParsing)`
- `Florence2Run`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `ImageCompositeMasked`
- `KSampler`
- `LayerMask: PersonMaskUltra V2`
- `LoadImage`
- `MaskPreview+`
- `MaskToImage`
- `PreviewImage`
- `SaveImage`
- `SetLatentNoiseMask`
- `ShowText|pysssss`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `CR Combine Prompt` —— 2/3 个有
- `CR Simple Image Compare` —— 2/3 个有
- `Power Lora Loader (rgthree)` —— 2/3 个有
- `LoraLoader` —— 1/3 个有
- `Text Concatenate (JPS)` —— 1/3 个有
- `Text _O` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 5 - 30 | 3 | 46% |
| Prompt 约束强度(CFG) | 0.7 | 0.7 - 1 | 3 | 82% |
| 采样算法 | dpmpp_2m | - | 3 | 100% |
| 调度器 | karras | - | 3 | 100% |
| 重绘幅度 | 0.3 | 0.3 - 0.3 | 3 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 30，观测区间 5 - 30，3 个样本，取值分散，一致性仅 46%
- Prompt 约束强度(CFG) 中位数 0.7，观测区间 0.7 - 1，3 个样本，取值集中（一致性 82%）
- 采样算法 最常用 dpmpp_2m，3 个样本，一致性 100%
- 调度器 最常用 karras，3 个样本，一致性 100%
- 重绘幅度 中位数 0.3，观测区间 0.3 - 0.3，3 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 0.7，低于常用下限 1（CFG 过低可能导致 Prompt 约束不足、结果偏离描述）

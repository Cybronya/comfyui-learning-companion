---
name: image_to_image_sampler_clip_checkpoint_5
type: Image To Image
frequency: 7
level: moderate
coverage: 0.762571
common_nodes: [Anything Everywhere, CLIPTextEncode, CheckpointLoaderSimple, Cut By Mask, FaceParse(FaceParsing), FaceParsingModelLoader(FaceParsing), FaceParsingProcessorLoader(FaceParsing), FaceParsingResultsParser(FaceParsing), GrowMaskWithBlur, Image Comparer (rgthree), ImageCompositeMasked, KSampler, LayerMask: PersonMaskUltra V2, LoadImage, MaskPreview+, MaskToImage, PreviewImage, SaveImage, SetLatentNoiseMask, VAEDecode, VAEEncode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/去除AI感还原真实皮肤_1924357130613420033.json, 图片生成/图生图/去除AI感还原真实皮肤_2058059091548917761.json, 图片生成/图生图/提升皮肤质感_1903026007530442754.json, 平台全量/EKKIVOK - REAL SKIN FINAL_1868944134554951682.json, 平台全量/「去除疑似ai」一键提升真实质感_1891363051776413698.json, 平台全量/皮肤加质感V1_1949735799690584065.json, 平台全量/磨皮大师 EKKIVOK - REAL SKIN FINAL_1851168136954531842.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_checkpoint_5

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/去除AI感还原真实皮肤_1924357130613420033.json、图片生成/图生图/去除AI感还原真实皮肤_2058059091548917761.json、图片生成/图生图/提升皮肤质感_1903026007530442754.json、平台全量/EKKIVOK - REAL SKIN FINAL_1868944134554951682.json、平台全量/「去除疑似ai」一键提升真实质感_1891363051776413698.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：76%

## 共有节点

全部 7 个 workflow 都包含：
- `Anything Everywhere`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `Cut By Mask`
- `FaceParse(FaceParsing)`
- `FaceParsingModelLoader(FaceParsing)`
- `FaceParsingProcessorLoader(FaceParsing)`
- `FaceParsingResultsParser(FaceParsing)`
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
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `DownloadAndLoadFlorence2Model` —— 6/7 个有
- `Florence2Run` —— 6/7 个有
- `ShowText|pysssss` —— 6/7 个有
- `CR Combine Prompt` —— 5/7 个有
- `CR Simple Image Compare` —— 5/7 个有
- `Power Lora Loader (rgthree)` —— 4/7 个有
- `LoraLoader` —— 3/7 个有
- `Text Concatenate (JPS)` —— 2/7 个有
- `Text _O` —— 2/7 个有
- `LoraLoaderModelOnly` —— 1/7 个有
- `workflow/Florence2` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 5 - 30 | 7 | 51% |
| Prompt 约束强度(CFG) | 0.7 | 0.7 - 1 | 7 | 83% |
| 采样算法 | dpmpp_2m | - | 7 | 100% |
| 调度器 | karras | - | 7 | 100% |
| 重绘幅度 | 0.3 | 0.3 - 0.4 | 7 | 89% |
| LoRA 模型强度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 30，观测区间 5 - 30，7 个样本
- Prompt 约束强度(CFG) 中位数 0.7，观测区间 0.7 - 1，7 个样本，取值集中（一致性 83%）
- 采样算法 最常用 dpmpp_2m，7 个样本，一致性 100%
- 调度器 最常用 karras，7 个样本，一致性 100%
- 重绘幅度 中位数 0.3，观测区间 0.3 - 0.4，7 个样本，取值集中（一致性 89%）
- LoRA 模型强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 0.7，低于常用下限 1（CFG 过低可能导致 Prompt 约束不足、结果偏离描述）

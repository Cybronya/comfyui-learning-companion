---
name: image_to_image_controlnet_ipadapter_lora_2
type: Image To Image
frequency: 4
level: moderate
coverage: 0.839
common_nodes: [Anything Everywhere, BrushNet, BrushNetLoader, CLIPSetLastLayer, CLIPTextEncode, CLIPVisionLoader, CannyEdgePreprocessor, CheckpointLoaderSimple, ConstrainImage|pysssss, ControlNetApplySD3, ControlNetLoader, DownloadAndLoadFlorence2Model, Florence2Run, GrowMaskWithBlur, IPAdapterAdvanced, IPAdapterModelLoader, Image Comparer (rgthree), KSampler, LoadImage, LoraLoaderModelOnly, MaskComposite, MaskFastGrow, MaskPreview+, PreviewImage, SaveImage, SetLatentNoiseMask, ShowText|pysssss, TransparentImage, VAEDecode, VAEEncode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/人物一键换场景（保留细节和颜色）_1914556012412764162.json, 图片生成/图生图/人物一键换场景（保留细节和颜色）_1914570575552151553.json, 图片生成/图生图/人物换场景-保留细节和服装颜色_1915320264366686210.json, 图片生成/图生图/电商产品一键换背景+高清放大（保留细节）_1929775368075427842.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_ipadapter_lora_2

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/人物一键换场景（保留细节和颜色）_1914556012412764162.json、图片生成/图生图/人物一键换场景（保留细节和颜色）_1914570575552151553.json、图片生成/图生图/人物换场景-保留细节和服装颜色_1915320264366686210.json、图片生成/图生图/电商产品一键换背景+高清放大（保留细节）_1929775368075427842.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 4 个 workflow 都包含：
- `Anything Everywhere`
- `BrushNet`
- `BrushNetLoader`
- `CLIPSetLastLayer`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CannyEdgePreprocessor`
- `CheckpointLoaderSimple`
- `ConstrainImage|pysssss`
- `ControlNetApplySD3`
- `ControlNetLoader`
- `DownloadAndLoadFlorence2Model`
- `Florence2Run`
- `GrowMaskWithBlur`
- `IPAdapterAdvanced`
- `IPAdapterModelLoader`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskComposite`
- `MaskFastGrow`
- `MaskPreview+`
- `PreviewImage`
- `SaveImage`
- `SetLatentNoiseMask`
- `ShowText|pysssss`
- `TransparentImage`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `SDXLPromptStyler` —— 3/4 个有
- `SUPIR_Upscale` —— 3/4 个有
- `InspyrenetRembg` —— 2/4 个有
- `easy imageRemBg` —— 2/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 8 - 30 | 4 | 61% |
| Prompt 约束强度(CFG) | 3 | 1 - 3 | 4 | 65% |
| 采样算法 | euler_ancestral | - | 4 | 75% |
| 调度器 | exponential | - | 4 | 75% |
| 重绘幅度 | 1 | 0.4 - 1 | 4 | 69% |
| ControlNet 权重 | 0.8 | 0.8 - 0.8 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 30，观测区间 8 - 30，4 个样本
- Prompt 约束强度(CFG) 中位数 3，观测区间 1 - 3，4 个样本
- 采样算法 最常用 euler_ancestral，4 个样本，一致性 75%
- 调度器 最常用 exponential，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 0.4 - 1，4 个样本
- ControlNet 权重 中位数 0.8，观测区间 0.8 - 0.8，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足

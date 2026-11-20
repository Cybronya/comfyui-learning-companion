---
name: image_to_image_controlnet_upscale_lora_11
type: Image To Image
frequency: 2
level: weak
coverage: 0.716
common_nodes: [AIO_Preprocessor, CLIPTextEncode, CR Text, CannyEdgePreprocessor, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, ControlNetLoaderAdvanced, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), ImageUpscaleWithModel, JWImageResizeByShorterSide, KSampler, LayerMask: LoadFlorence2Model, LayerUtility: Florence2Image2Prompt, LineArtPreprocessor, LoadImage, LoraLoader, PreviewImage, SaveImage, ShowText|pysssss, Text List, Text List to Text, UltimateSDUpscale, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, WD14Tagger|pysssss]
problems: []
missing: []
members: [图片生成/图生图/IP形象转3D专用_V3_1911957199407775746.json, 图片生成/图生图/IP形象转3D专用_V3_2114314072631103490.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_upscale_lora_11

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/IP形象转3D专用_V3_1911957199407775746.json、图片生成/图生图/IP形象转3D专用_V3_2114314072631103490.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：72%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPTextEncode`
- `CR Text`
- `CannyEdgePreprocessor`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `ControlNetLoaderAdvanced`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `ImageUpscaleWithModel`
- `JWImageResizeByShorterSide`
- `KSampler`
- `LayerMask: LoadFlorence2Model`
- `LayerUtility: Florence2Image2Prompt`
- `LineArtPreprocessor`
- `LoadImage`
- `LoraLoader`
- `PreviewImage`
- `SaveImage`
- `ShowText|pysssss`
- `Text List`
- `Text List to Text`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `WD14Tagger|pysssss`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 15 | - | 2 | 67% |
| Prompt 约束强度(CFG) | 5.75 | - | 2 | 78% |
| 采样算法 | euler_ancestral | - | 2 | 50% |
| 调度器 | karras | - | 2 | 100% |
| 重绘幅度 | 0.33 | - | 2 | 91% |
| ControlNet 权重 | 0.7 | - | 2 | 100% |
| LoRA 模型强度 | 0.8 | - | 2 | 100% |
| LoRA 文本强度 | 0.9 | - | 2 | 89% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 15，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 5.75，样本不足，未给区间，2 个样本
- 采样算法 最常用 euler_ancestral，2 个样本，一致性 50%
- 调度器 最常用 karras，2 个样本，一致性 100%
- 重绘幅度 中位数 0.33，样本不足，未给区间，2 个样本，取值集中（一致性 91%）
- ControlNet 权重 中位数 0.7，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 0.9，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

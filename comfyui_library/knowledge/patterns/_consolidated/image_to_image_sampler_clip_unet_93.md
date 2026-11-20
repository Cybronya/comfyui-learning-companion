---
name: image_to_image_sampler_clip_unet_93
type: Image To Image
frequency: 5
level: strong
coverage: 0.8424
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Kontext人物换姿势【解决一致性】_1960154534800732161.json, 图片生成/图生图/Kontext修复光影【基础流】_1945485356567339009.json, 图片生成/图生图/Kontext双图拼接融合_1997506582562934786.json, 图片生成/图生图/Kontext打光_1947600328860622849.json, 图片生成/图生图/Kontext预设提示词（基础流）_1950124188273172481.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_93

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Kontext人物换姿势【解决一致性】_1960154534800732161.json、图片生成/图生图/Kontext修复光影【基础流】_1945485356567339009.json、图片生成/图生图/Kontext双图拼接融合_1997506582562934786.json、图片生成/图生图/Kontext打光_1947600328860622849.json、图片生成/图生图/Kontext预设提示词（基础流）_1950124188273172481.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextImageScale` —— 4/5 个有
- `Image Comparer (rgthree)` —— 4/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/5 个有
- `Anything Everywhere3` —— 3/5 个有
- `FluxGuidance` —— 3/5 个有
- `LayerUtility: ImageScaleRestore` —— 3/5 个有
- `PreviewImage` —— 3/5 个有
- `ImageStitch` —— 2/5 个有
- `LoraLoaderModelOnly` —— 2/5 个有
- `AIO_Preprocessor` —— 1/5 个有
- `ImageCrop` —— 1/5 个有
- `LoadKontextPresets` —— 1/5 个有
- `Note _O` —— 1/5 个有
- `PrimitiveInt` —— 1/5 个有
- `RH_LLMAPI_NODE` —— 1/5 个有
- `Text Multiline` —— 1/5 个有
- `easy showAnything` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）

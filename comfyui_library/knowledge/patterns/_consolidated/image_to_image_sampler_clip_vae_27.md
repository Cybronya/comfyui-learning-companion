---
name: image_to_image_sampler_clip_vae_27
type: Image To Image
frequency: 6
level: strong
coverage: 0.961667
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Kontext人物 苹果 EMoji 风格_1948220912014372865.json, 图片生成/图生图/Kontext光影融合_1995291619001819137.json, 图片生成/图生图/Kontext单姿势图直接出图_1944080635831128065.json, 图片生成/图生图/Kontext改单图 - Nunchaku 加速_1954810310865633282.json, 图片生成/图生图/flux_kontext_dev_一键打光，为照片增加电影光照效果_1941898475904856065.json, 图片生成/图生图/【全能图片G4o同款】Flux Kontext 图像编辑加速版_1948192407916544002.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_27

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Kontext人物 苹果 EMoji 风格_1948220912014372865.json、图片生成/图生图/Kontext光影融合_1995291619001819137.json、图片生成/图生图/Kontext单姿势图直接出图_1944080635831128065.json、图片生成/图生图/Kontext改单图 - Nunchaku 加速_1954810310865633282.json、图片生成/图生图/flux_kontext_dev_一键打光，为照片增加电影光照效果_1941898475904856065.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/6 个有
- `RH_Translator` —— 5/6 个有
- `NunchakuFluxDiTLoader` —— 4/6 个有
- `ShowText|pysssss` —— 4/6 个有
- `LayerUtility: ImageMaskScaleAs` —— 3/6 个有
- `UNETLoader` —— 3/6 个有
- `easy imageConcat` —— 3/6 个有
- `AIO_Preprocessor` —— 1/6 个有
- `DeepTranslatorTextNode` —— 1/6 个有
- `LoraLoaderModelOnly` —— 1/6 个有
- `RH_LLMAPI_NODE` —— 1/6 个有
- `RepeatLatentBatch` —— 1/6 个有
- `easy imageRemBg` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 6 | 83% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，6 个样本，取值集中（一致性 83%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）

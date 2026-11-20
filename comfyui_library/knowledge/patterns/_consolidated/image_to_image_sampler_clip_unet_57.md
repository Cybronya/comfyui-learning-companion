---
name: image_to_image_sampler_clip_unet_57
type: Image To Image
frequency: 7
level: strong
coverage: 0.906714
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, PreviewImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Kontext Dev照片转绘【10种画风随意切换】_2013861706304331778.json, 图片生成/图生图/Kontext [dev] 漫画线稿上色_1939123701302677506.json, 图片生成/图生图/Kontext dev 线稿上色_1940218293493911554.json, 图片生成/图生图/Kontext+Dev照片转绘扁平矢量卡通风格V2_2047228009656094722.json, 图片生成/图生图/Kontext，改变相机角度，改变镜头，改变角度，Change Camera Angle_1977589854961836034.json, 图片生成/图生图/像素风画转画_2080593953581260802.json, 图片生成/图生图/照片转扁平插画风（超强设计感）Kontext+Dev_2029482820351037441.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_57

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Kontext Dev照片转绘【10种画风随意切换】_2013861706304331778.json、图片生成/图生图/Kontext [dev] 漫画线稿上色_1939123701302677506.json、图片生成/图生图/Kontext dev 线稿上色_1940218293493911554.json、图片生成/图生图/Kontext+Dev照片转绘扁平矢量卡通风格V2_2047228009656094722.json、图片生成/图生图/Kontext，改变相机角度，改变镜头，改变角度，Change Camera Angle_1977589854961836034.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConstrainImage|pysssss` —— 6/7 个有
- `SUPIR_Upscale` —— 6/7 个有
- `LoraLoaderModelOnly` —— 5/7 个有
- `RH_Translator` —— 4/7 个有
- `String` —— 4/7 个有
- `CR Text Concatenate` —— 3/7 个有
- `DeepTranslatorTextNode` —— 3/7 个有
- `easy showAnything` —— 2/7 个有
- `ttN concat` —— 2/7 个有
- `CR Text` —— 1/7 个有
- `Int` —— 1/7 个有
- `MuyeTextEditOutput` —— 1/7 个有
- `Note _O` —— 1/7 个有
- `RepeatLatentBatch` —— 1/7 个有
- `TeaCache` —— 1/7 个有
- `easy anythingIndexSwitch` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 20 - 25 | 7 | 93% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 20 - 25，7 个样本，取值集中（一致性 93%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）

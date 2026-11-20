---
name: image_to_image_sampler_clip_unet_45
type: Image To Image
frequency: 8
level: strong
coverage: 0.778375
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, ImageStitch, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/KonText一句话P图！提示词改图=开源版=艾橘溪_1928485579321909249.json, 图片生成/图生图/KonText一句话改图，技术有限，创意无限！_1941126778633273346.json, 图片生成/图生图/Kontext Dev 人物妆容修改_1942405018597142529.json, 图片生成/图生图/Kontext Dev 基础工作流ZGL_1943863852666617858.json, 图片生成/图生图/Kontext Dev 模型｜多人场景动作融合_1938995027278548994.json, 图片生成/图生图/flux_1_kontex终于等来了，模型基础效果_1938275066096582657.json, 图片生成/图生图/flux_kontext_dev_单图-提示词更听话_1938613725001605122.json, 图片生成/图生图/【非API】 Kontext Dev 模型｜多图融合_1938484652631851009.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_45

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/KonText一句话P图！提示词改图=开源版=艾橘溪_1928485579321909249.json、图片生成/图生图/KonText一句话改图，技术有限，创意无限！_1941126778633273346.json、图片生成/图生图/Kontext Dev 人物妆容修改_1942405018597142529.json、图片生成/图生图/Kontext Dev 基础工作流ZGL_1943863852666617858.json、图片生成/图生图/Kontext Dev 模型｜多人场景动作融合_1938995027278548994.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImageStitch`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 7/8 个有
- `PreviewImage` —— 7/8 个有
- `FluxKontextImageScale` —— 6/8 个有
- `RH_Translator` —— 4/8 个有
- `LoadImageOutput` —— 3/8 个有
- `ImageResizeKJv2` —— 2/8 个有
- `LayerMask: BiRefNetUltraV2` —— 2/8 个有
- `LayerMask: LoadBiRefNetModel` —— 2/8 个有
- `ShowText|pysssss` —— 2/8 个有
- `Kontext Inpainting Conditioning` —— 1/8 个有
- `LayerUtility: ImageScaleRestore V2` —— 1/8 个有
- `LayerUtility: PurgeVRAM` —— 1/8 个有
- `RH_LLMAPI_NODE` —— 1/8 个有
- `easy showAnything` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 8 | 81% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，8 个样本，取值集中（一致性 81%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）

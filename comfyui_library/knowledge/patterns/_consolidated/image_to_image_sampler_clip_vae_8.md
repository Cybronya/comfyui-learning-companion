---
name: image_to_image_sampler_clip_vae_8
type: Image To Image
frequency: 16
level: strong
coverage: 0.931563
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux1-Kontext人物衣服提取为白底图_1953725855308632065.json, 图片生成/图生图/Flux1-Kontext单图编辑_1948147511820201986.json, 图片生成/图生图/Flux1-Kontext双图编辑_1945116357434253314.json, 图片生成/图生图/Flux1-Kontext移除物品_1949271916276850690.json, 图片生成/图生图/Flux1-kontext图像转绘--低多边形风格_1948042005027913729.json, 图片生成/图生图/Kontext+参考姿势PoseLORA图像编辑_1961115777162219521.json, 图片生成/图生图/Kontext_Linart 参考线稿引导，图像一致编辑：目前最稳定图像质量最好的控制lLORA_1961475674605338626.json, 图片生成/图生图/Kontext_OpenPose  参考姿态引导图像一致编辑：目前最稳定图像质量最好的控制lLORA_1960914316209917953.json, 图片生成/图生图/Kontext_OpenPose_参考姿态引导图像一致编辑_目前最稳定图像质量最好的控制lLORA_2074058797412347905.json, 图片生成/图生图/Kontext姿势Pose引导图像编辑_1960656741799198721.json, 图片生成/图生图/Kontext姿势参考-Flux-UnionPro-CN2_1961975841964146689.json, 图片生成/图生图/Kontext最新姿势参考改图_1960974269314469890.json, 图片生成/图生图/Kontext最新姿势参考改图_1961618107724926977.json, 图片生成/图生图/Kontext最新姿势迁移_1961618061616988161.json, 图片生成/图生图/Kontext深度Depth引导图像编辑_1957761851306209281.json, 图片生成/图生图/Kontext线稿lineart 引导图像编辑_1961994378770366466.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_8

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/图生图/Flux1-Kontext人物衣服提取为白底图_1953725855308632065.json、图片生成/图生图/Flux1-Kontext单图编辑_1948147511820201986.json、图片生成/图生图/Flux1-Kontext双图编辑_1945116357434253314.json、图片生成/图生图/Flux1-Kontext移除物品_1949271916276850690.json、图片生成/图生图/Flux1-kontext图像转绘--低多边形风格_1948042005027913729.json…）

- **类型**：Image To Image
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 16 个 workflow 都包含：
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
- `ImageStitch` —— 15/16 个有
- `UNETLoader` —— 15/16 个有
- `Text Multiline` —— 14/16 个有
- `LoraLoaderModelOnly` —— 13/16 个有
- `TeaCache` —— 12/16 个有
- `AIO_Preprocessor` —— 11/16 个有
- `ImageScaleDownToSize` —— 11/16 个有
- `PreviewImage` —— 11/16 个有
- `ShowText|pysssss` —— 11/16 个有
- `GetImageSizeAndCount` —— 10/16 个有
- `ImageCrop` —— 10/16 个有
- `ImageConcatMulti` —— 7/16 个有
- `FluxKontextImageScale` —— 6/16 个有
- `RH_Translator` —— 4/16 个有
- `UnetLoaderGGUF` —— 4/16 个有
- `RHHiddenNodes` —— 3/16 个有
- `easy imageRemBg` —— 3/16 个有
- `ControlNetApplyAdvanced` —— 1/16 个有
- `ControlNetLoader` —— 1/16 个有
- `ImageConcanate` —— 1/16 个有
- `MZ_Flux1PartialLoad_Patch` —— 1/16 个有
- `RH_Captioner` —— 1/16 个有
- `Text Concatenate` —— 1/16 个有
- `ttN concat` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 16 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 16 | 100% |
| 采样算法 | euler | - | 16 | 100% |
| 调度器 | simple | - | 16 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 16 | 100% |
| ControlNet 权重 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，16 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，16 个样本，一致性 100%
- 调度器 最常用 simple，16 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）

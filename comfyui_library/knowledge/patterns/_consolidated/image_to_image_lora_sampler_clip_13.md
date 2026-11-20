---
name: image_to_image_lora_sampler_clip_13
type: Image To Image
frequency: 11
level: strong
coverage: 0.918091
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux1-Kontext人物衣服提取为白底图_1953725855308632065.json, 图片生成/图生图/Flux1-Kontext单图编辑_1948147511820201986.json, 图片生成/图生图/Flux1-Kontext双图编辑_1945116357434253314.json, 图片生成/图生图/Flux1-Kontext扩图_1950434435030278145.json, 图片生成/图生图/Flux1-Kontext移除物品_1949271916276850690.json, 图片生成/图生图/Kontext+参考姿势PoseLORA图像编辑_1961115777162219521.json, 图片生成/图生图/Kontext_Linart 参考线稿引导，图像一致编辑：目前最稳定图像质量最好的控制lLORA_1961475674605338626.json, 图片生成/图生图/Kontext_OpenPose  参考姿态引导图像一致编辑：目前最稳定图像质量最好的控制lLORA_1960914316209917953.json, 图片生成/图生图/Kontext_OpenPose_参考姿态引导图像一致编辑_目前最稳定图像质量最好的控制lLORA_2074058797412347905.json, 图片生成/图生图/Kontext姿势Pose引导图像编辑_1960656741799198721.json, 图片生成/图生图/Kontext姿势参考-Flux-UnionPro-CN2_1961975841964146689.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_13

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/Flux1-Kontext人物衣服提取为白底图_1953725855308632065.json、图片生成/图生图/Flux1-Kontext单图编辑_1948147511820201986.json、图片生成/图生图/Flux1-Kontext双图编辑_1945116357434253314.json、图片生成/图生图/Flux1-Kontext扩图_1950434435030278145.json、图片生成/图生图/Flux1-Kontext移除物品_1949271916276850690.json…）

- **类型**：Image To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Text Multiline` —— 10/11 个有
- `ImageStitch` —— 9/11 个有
- `UNETLoader` —— 9/11 个有
- `ImageConcatMulti` —— 8/11 个有
- `TeaCache` —— 8/11 个有
- `PreviewImage` —— 7/11 个有
- `AIO_Preprocessor` —— 6/11 个有
- `FluxKontextImageScale` —— 6/11 个有
- `ImageScaleDownToSize` —— 6/11 个有
- `ShowText|pysssss` —— 6/11 个有
- `GetImageSizeAndCount` —— 5/11 个有
- `ImageCrop` —— 5/11 个有
- `UnetLoaderGGUF` —— 5/11 个有
- `RH_Translator` —— 4/11 个有
- `easy imageRemBg` —— 2/11 个有
- `ControlNetApplyAdvanced` —— 1/11 个有
- `ControlNetLoader` —— 1/11 个有
- `Image Comparer (rgthree)` —— 1/11 个有
- `LayerUtility: ExtendCanvas` —— 1/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/11 个有
- `PrimitiveInt` —— 1/11 个有
- `RH_Captioner` —— 1/11 个有
- `Text Concatenate` —— 1/11 个有
- `ttN concat` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 11 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| ControlNet 权重 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）

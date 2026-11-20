---
name: image_to_image_lora_sampler_unet_10
type: Image To Image
frequency: 25
level: strong
coverage: 0.8816
common_nodes: [CLIPLoader, FluxKontextMultiReferenceLatentMethod, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, QwenMultiangleCameraNode, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/图生图/Qwen2511-控制角度工作流_2077302736273629186.json, 图片生成/图生图/Qwen2511多角度控制_2009846604588654594.json, 图片生成/图生图/Qwen2511控制照片角度工作流_2016442774928756738.json, 图片生成/图生图/Qwen_Edit_2511_Multiangle图片角度自由控制_2077221377760911362.json, 图片生成/图生图/Qwen_Edit_2511多角度_2055560720015732738.json, 图片生成/图生图/Qwen_Edit_2511多角度同出_2056331114276540418.json, 图片生成/图生图/Qwen_Multiangle_2511图片角度自由控制_2010971058458861569.json, 图片生成/图生图/Qwen_Multiangle_2511图片角度自由控制_2038483773788000257.json, 图片生成/图生图/Qwen_Multiangle_2511自由控制图片角度_2038555716276981761.json, 图片生成/图生图/qwen  分镜 精准镜头视角控制器  模特套图 商品套图_2046923407031275521.json, 图片生成/图生图/qwen_image_edit  _ 精准镜头控制器 _ 模特套图_2037780822270418946.json, 图片生成/图生图/qwen_image_edit 精准镜头控制器  模特套图 商品套图_2034504749021663233.json, 图片生成/图生图/qwen_image_edit 精准镜头视角控制器  模特套图 商品套图_2037729340846252034.json, 图片生成/图生图/人物场景多视图一键生成_2014235660437164034.json, 图片生成/图生图/可视化摄像机角度调节，一键生成图像多视角_2004504081580388354.json, 图片生成/图生图/场景多视角_2016036160287543298.json, 图片生成/图生图/场景多视角镜头_2010978287455051777.json, 图片生成/图生图/场景生成多视角_2013145425766780929.json, 图片生成/图生图/场景生成多视角_2101477990000582658.json, 图片生成/图生图/多角度切换相机控制 复刻场景 Qwen 人物产品多角度_2069217388083634178.json, 图片生成/图生图/（5张图）Qwen_Multiangle_2511图片角度自由控制(5张）_2041794648401776641.json, 图片生成/文生图/Qwen_Multiangle_2511图片多角度自由控制_2049765326316945410.json, 图片生成/文生图/图片多角度工作流_2009868602559696897.json, 图片生成/文生图/图片角度自由控制Qwen_Multiangle_2511工作流_2050169351910772738.json, 平台全量/2511+多角度+灯光调节合并工作流_2022537103359348738.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_10

> 由 `engine/knowledge_consolidation` 从 25 个 workflow 归纳得出（图片生成/图生图/Qwen2511-控制角度工作流_2077302736273629186.json、图片生成/图生图/Qwen2511多角度控制_2009846604588654594.json、图片生成/图生图/Qwen2511控制照片角度工作流_2016442774928756738.json、图片生成/图生图/Qwen_Edit_2511_Multiangle图片角度自由控制_2077221377760911362.json、图片生成/图生图/Qwen_Edit_2511多角度_2055560720015732738.json…）

- **类型**：Image To Image
- **样本数**：25
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 25 个 workflow 都包含：
- `CLIPLoader`
- `FluxKontextMultiReferenceLatentMethod`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `QwenMultiangleCameraNode`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 22/25 个有
- `VAEDecode` —— 22/25 个有
- `easy promptList` —— 19/25 个有
- `easy showAnything` —— 15/25 个有
- `ImageScaleToTotalPixels` —— 12/25 个有
- `FluxKontextImageScale` —— 11/25 个有
- `PreviewImage` —— 8/25 个有
- `ShowText|pysssss` —— 7/25 个有
- `Image Comparer (rgthree)` —— 3/25 个有
- `VAEDecodeTiled` —— 3/25 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/25 个有
- `StringConcatenate` —— 2/25 个有
- `ColorCorrect` —— 1/25 个有
- `ImageBlend` —— 1/25 个有
- `QwenMultiangleLightningNode` —— 1/25 个有
- `SDPoseOODLoader` —— 1/25 个有
- `SDPoseOODProcessor` —— 1/25 个有
- `String` —— 1/25 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 25 | 69% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 25 | 100% |
| 采样算法 | euler | - | 25 | 96% |
| 调度器 | simple | - | 25 | 96% |
| 重绘幅度 | 1 | 1 - 1 | 25 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 27/25 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 3/25 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，25 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，25 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，25 个样本，一致性 96%
- 调度器 最常用 simple，25 个样本，一致性 96%
- 重绘幅度 中位数 1，观测区间 1 - 1，25 个样本，取值集中（一致性 100%）
- 高发问题（27/25 个样本）：Steps较低可能导致细节不足

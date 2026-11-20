---
name: image_to_image_lora_sampler_unet_21
type: Image To Image
frequency: 20
level: moderate
coverage: 0.9261
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/白底图换背景_2044055501784223746.json, 图片生成/图生图/真人转动漫  真人转卡通  真人转漫画_2096660074356887553.json, 图片生成/图生图/真人转动漫  真人转卡通 真人转漫画   真人转3D Q版卡通_2053901548941529090.json, 图片生成/图生图/真人转卡通  真人转漫画 真人转动漫  Q版卡通  Q版风格化_2053721157651714049.json, 图片生成/图生图/真人转卡通  真人转漫画 真人转动漫  Q版卡通  Q版风格化_2053845599967031297.json, 图片生成/图生图/真人转卡通  真人转漫画 真人转动漫  Q版卡通  Q版风格化_2053867268517449729.json, 图片生成/图生图/真人转卡通  真人转漫画 真人转动漫  Q版卡通  Q版风格化_2053869198199279618.json, 图片生成/图生图/真人转卡通 真人转漫画 真人转动漫  真人转3D Q版卡通_2053848663335677953.json, 图片生成/图生图/真人转卡通 真人转漫画 真人转动漫  真人转3D Q版卡通_2053871652357844993.json, 图片生成/图生图/真人转卡通 真人转漫画 真人转动漫  真人转3D Q版卡通_2053877533954854913.json, 图片生成/图生图/空气手势_1981375615989358593.json, 图片生成/图生图/空白工作流_2042557859346522114.json, 图片生成/图生图/老照片修复qwen2511千问2511加速版_2003646847212265474.json, 图片生成/图生图/自定义编辑视角_2010740914263695362.json, 图片生成/图生图/衣服提取衣服_2058616474121625602.json, 图片生成/图生图/衣服提取衣服qwen2511千问2511加速版_2004402979652468737.json, 图片生成/图生图/课程演示-去水印_2075540632856260610.json, 图片生成/图生图/豆包图片去水印_高清修复_2082761030039588866.json, 图片生成/文生图/Qwen Edit 2511 图片去水印 全节点注释_2077810588885020674.json, 平台全量/010.物品提取_2005434734215917570.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_21

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（图片生成/图生图/白底图换背景_2044055501784223746.json、图片生成/图生图/真人转动漫  真人转卡通  真人转漫画_2096660074356887553.json、图片生成/图生图/真人转动漫  真人转卡通 真人转漫画   真人转3D Q版卡通_2053901548941529090.json、图片生成/图生图/真人转卡通  真人转漫画 真人转动漫  Q版卡通  Q版风格化_2053721157651714049.json、图片生成/图生图/真人转卡通  真人转漫画 真人转动漫  Q版卡通  Q版风格化_2053845599967031297.json…）

- **类型**：Image To Image
- **样本数**：20
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 20 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 10/20 个有
- `TextEncodeQwenImageEdit` —— 10/20 个有
- `TextEncodeQwenImageEditPlus` —— 10/20 个有
- `FluxKontextMultiReferenceLatentMethod` —— 8/20 个有
- `CR Text` —— 7/20 个有
- `ImageConcanate` —— 6/20 个有
- `ReferenceLatent` —— 5/20 个有
- `Image Comparer (rgthree)` —— 2/20 个有
- `> Text Replace` —— 1/20 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/20 个有
- `PreviewImage` —— 1/20 个有
- `PrimitiveFloat` —— 1/20 个有
- `PrimitiveInt` —— 1/20 个有
- `QwenMultiangleCameraNode` —— 1/20 个有
- `RH_Translator` —— 1/20 个有
- `TextBox` —— 1/20 个有
- `easy showAnything` —— 1/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 24 | 20 | 43% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 20 | 43% |
| 采样算法 | euler | - | 20 | 100% |
| 调度器 | simple | - | 20 | 95% |
| 重绘幅度 | 1 | 1 - 1 | 20 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/20 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 24，20 个样本，取值分散，一致性仅 43%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，20 个样本，取值分散，一致性仅 43%
- 采样算法 最常用 euler，20 个样本，一致性 100%
- 调度器 最常用 simple，20 个样本，一致性 95%
- 重绘幅度 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
- 高发问题（18/20 个样本）：Steps较低可能导致细节不足

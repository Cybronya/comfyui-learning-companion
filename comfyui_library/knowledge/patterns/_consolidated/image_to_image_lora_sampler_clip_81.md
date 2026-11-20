---
name: image_to_image_lora_sampler_clip_81
type: Image To Image
frequency: 5
level: strong
coverage: 0.8576
common_nodes: [Anything Everywhere, Anything Everywhere3, CLIPLoader, CLIPTextEncode, ConstrainImage|pysssss, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Wan2.2洗图（多图）_1975838748871143426.json, 平台全量/Wan2.2 去除Ai感 高清放大+风格化重绘 模特人物洗图 超级细节修复 超真实 去AI塑料感_2015965266944987137.json, 平台全量/Wan2.2 洗图 超级修复_1954148423886880769.json, 平台全量/图片增加细节  Wan2.2去除AI塑料感   细节修复放大 皮肤质感加强 提升真实感 超级细节修复_2026816795868401665.json, 平台全量/高度一致性图像放大-Hypir  细节修复放大 Wan2.2 模特人物洗图 超级细节修复 超真实 去_2004099440631791618.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_81

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Wan2.2洗图（多图）_1975838748871143426.json、平台全量/Wan2.2 去除Ai感 高清放大+风格化重绘 模特人物洗图 超级细节修复 超真实 去AI塑料感_2015965266944987137.json、平台全量/Wan2.2 洗图 超级修复_1954148423886880769.json、平台全量/图片增加细节  Wan2.2去除AI塑料感   细节修复放大 皮肤质感加强 提升真实感 超级细节修复_2026816795868401665.json、平台全量/高度一致性图像放大-Hypir  细节修复放大 Wan2.2 模特人物洗图 超级细节修复 超真实 去_2004099440631791618.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 5 个 workflow 都包含：
- `Anything Everywhere`
- `Anything Everywhere3`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConstrainImage|pysssss`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 3/5 个有
- `Joy_caption_two` —— 3/5 个有
- `Joy_caption_two_load` —— 3/5 个有
- `LayerUtility: JoyCaptionBeta1` —— 2/5 个有
- `LayerUtility: JoyCaptionBeta1ExtraOptions` —— 2/5 个有
- `LayerUtility: LoadJoyCaptionBeta1Model` —— 2/5 个有
- `CR Text Concatenate` —— 1/5 个有
- `PreviewAny` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `RH_Captioner` —— 1/5 个有
- `TextInput_` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | res_multistep | - | 5 | 60% |
| 调度器 | simple | - | 5 | 60% |
| 重绘幅度 | 0.25 | 0.2 - 0.42 | 5 | 67% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_multistep，5 个样本，一致性 60%
- 调度器 最常用 simple，5 个样本，一致性 60%
- 重绘幅度 中位数 0.25，观测区间 0.2 - 0.42，5 个样本

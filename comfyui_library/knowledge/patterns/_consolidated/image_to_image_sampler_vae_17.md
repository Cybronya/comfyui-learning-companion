---
name: image_to_image_sampler_vae_17
type: Image To Image
frequency: 9
level: weak
coverage: 0.939
common_nodes: [CFGNorm, CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/灯光调节器-qwen_image_edit_2511_2011441135843024897.json, 图片生成/图生图/灯光调节器-qwen_image_edit_2511_2099327221906362369.json, 图片生成/图生图/灯光调节器-qwen_image_edit_2511_2099667042474479618.json, 图片生成/图生图/顶级图像编辑模型 Qwen-Image-Edit-2511工作流_2005170734341255169.json, 图片生成/图生图/风格转换qwen2511最新图像编辑换装千问2511追赶nano+全能图片V1(1)_2004060386825519105.json, 图片生成/图生图/👾怪獸-QWEN-EDIT-2511+重打光强化版👾_2014642307299020802.json, 图片生成/图生图/👾怪獸-千问Edit单图编辑👾_1979934217855471618.json, 图片生成/图生图/🥯千问Edit 2509版 多图稳定编辑版🥯_1971769285058162689.json, 图片生成/图生图/🥯千问新王炸！2509模型图片姿势完美迁移🥯_1970302455412125698.json]
source: knowledge_consolidation
---

# image_to_image_sampler_vae_17

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/灯光调节器-qwen_image_edit_2511_2011441135843024897.json、图片生成/图生图/灯光调节器-qwen_image_edit_2511_2099327221906362369.json、图片生成/图生图/灯光调节器-qwen_image_edit_2511_2099667042474479618.json、图片生成/图生图/顶级图像编辑模型 Qwen-Image-Edit-2511工作流_2005170734341255169.json、图片生成/图生图/风格转换qwen2511最新图像编辑换装千问2511追赶nano+全能图片V1(1)_2004060386825519105.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 9 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextMultiReferenceLatentMethod` —— 6/9 个有
- `UNETLoader` —— 6/9 个有
- `LoraLoaderModelOnly` —— 5/9 个有
- `CR Text` —— 4/9 个有
- `QwenMultiangleLightningNode` —— 4/9 个有
- `Anything Everywhere3` —— 3/9 个有
- `ImageConcanate` —— 3/9 个有
- `RHHiddenNodes` —— 3/9 个有
- `ImageConcatMulti` —— 2/9 个有
- `Note Plus (mtb)` —— 2/9 个有
- `PreviewImage` —— 2/9 个有
- `TextEncodeQwenImageEdit` —— 2/9 个有
- `AIO_Preprocessor` —— 1/9 个有
- `Fast Groups Bypasser (rgthree)` —— 1/9 个有
- `RH_LLMAPI_NODE` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 25 | 9 | 17% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 9 | 60% |
| 采样算法 | euler | - | 9 | 89% |
| 调度器 | simple | - | 9 | 78% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 25，9 个样本，取值分散，一致性仅 17%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，9 个样本
- 采样算法 最常用 euler，9 个样本，一致性 89%
- 调度器 最常用 simple，9 个样本，一致性 78%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（7/9 个样本）：Steps较低可能导致细节不足

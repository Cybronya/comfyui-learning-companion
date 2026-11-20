---
name: unknown_workflow_lora_sampler_vae_5
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.976667
common_nodes: [DWPreprocessor, EmptyLatentImage, GetImageSizeAndCount, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, Text Multiline, TextEncodeQwenImageEditPlus, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/( NSF W本地解码)Qwen Edit 2511 Aio V16编辑（姿势迁移-sex tacular）_2007708424666095618.json, 图片生成/图生图/(（自用）-F2P一致性版)Qwen-Edit Aio V7.1模型双图编辑(姿势迁移)_1985320686849769473.json, 图片生成/图生图/Qwen Edit 2511 +CN+F2P新图比例双参姿势控制V1_2007451297615712258.json, 图片生成/图生图/Qwen Edit 2511 Aio V18编辑V1（姿势迁移）_2007475103805739010.json, 图片生成/图生图/Qwen Edit 2511 Union Control姿势编辑V1(动作弱控制)_2004949901496774657.json, 图片生成/图生图/Qwen Edit 2511 Union Control姿势编辑V1(强控制)_2004946550256271362.json, 图片生成/图生图/Qwen Edit 2511 Union Control姿势编辑_2005190245438160898.json, 图片生成/图生图/QwenEdit 2511+CN+F2P 原比例PAD扩展版姿势控制V1_2007453446366040066.json, 图片生成/图生图/【阿良绘】单人+多人双流：Qwen Edit 2511+Union姿势编辑控制V1.0_2006242000118489089.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_vae_5

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/( NSF W本地解码)Qwen Edit 2511 Aio V16编辑（姿势迁移-sex tacular）_2007708424666095618.json、图片生成/图生图/(（自用）-F2P一致性版)Qwen-Edit Aio V7.1模型双图编辑(姿势迁移)_1985320686849769473.json、图片生成/图生图/Qwen Edit 2511 +CN+F2P新图比例双参姿势控制V1_2007451297615712258.json、图片生成/图生图/Qwen Edit 2511 Aio V18编辑V1（姿势迁移）_2007475103805739010.json、图片生成/图生图/Qwen Edit 2511 Union Control姿势编辑V1(动作弱控制)_2004949901496774657.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 9 个 workflow 都包含：
- `DWPreprocessor`
- `EmptyLatentImage`
- `GetImageSizeAndCount`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `Text Multiline`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 8/9 个有
- `VAELoader` —— 8/9 个有
- `CR Prompt Text` —— 7/9 个有
- `ImageConcanate` —— 7/9 个有
- `TT_img_enc` —— 7/9 个有
- `TT_img_enc_v2` —— 7/9 个有
- `ControlNetApplySD3` —— 6/9 个有
- `ControlNetLoader` —— 6/9 个有
- `DuckHideNode` —— 6/9 个有
- `SetUnionControlNetType` —— 6/9 个有
- `UNETLoader` —— 6/9 个有
- `CheckpointLoaderSimple` —— 3/9 个有
- `PreviewImage` —— 3/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/9 个有
- `Anything Everywhere` —— 1/9 个有
- `DF_Get_image_size` —— 1/9 个有
- `DepthAnything_V2` —— 1/9 个有
- `Float` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 9 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 89% |
| 调度器 | beta57 | - | 9 | 89% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 768 | 512 - 768 | 9 | 85% |
| 高度 | 768 | 512 - 768 | 9 | 85% |
| ControlNet 权重 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 89%
- 调度器 最常用 beta57，9 个样本，一致性 89%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 768，观测区间 512 - 768，9 个样本，取值集中（一致性 85%）
- 高度 中位数 768，观测区间 512 - 768，9 个样本，取值集中（一致性 85%）
- ControlNet 权重 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（10/9 个样本）：Steps较低可能导致细节不足

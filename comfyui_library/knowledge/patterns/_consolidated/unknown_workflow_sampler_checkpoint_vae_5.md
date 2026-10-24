---
name: unknown_workflow_sampler_checkpoint_vae_5
type: Unknown Workflow
frequency: 13
level: strong
coverage: 0.945231
common_nodes: [CR Prompt Text, CheckpointLoaderSimple, EmptyLatentImage, GetImageSizeAndCount, ImageScaleToTotalPixels, KSampler, LoadImage, SaveImage, TT_img_enc, TT_img_enc_v2, TextEncodeQwenImageEditPlus, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/单图_2000211503481581570.json, 图片生成/图生图/单图姿势参照_2002974605021200385.json, 图片生成/图生图/（4图版-（自用）-F2P）同景同人随机Qwen-Edit Aio V7.1图像编辑_1985321438334828546.json, 图片生成/图生图/（4图版-（自用））同景同人随机Qwen-Edit Aio V5.1图像编辑_1980187963835453441.json, 图片生成/图生图/（4图版（自用））同景同人随机Qwen-Edit Aio V5.2图像编辑_1982145252280680449.json, 图片生成/图生图/（4图版（自用））同景同人随机Qwen-Edit Aio V5模型单图编辑_1978397445258366978.json, 图片生成/图生图/（F2P（自用））Qwen-Edit Aio V5.3模型单图编辑（人脸加强版）_1983522663635329025.json, 图片生成/图生图/（F2P（自用））Qwen-Edit Aio V7.1模型单图编辑（人脸加强版）_1985316929172873218.json, 图片生成/图生图/（自用）N版Qwen-Edit Aio V5.2模型单图编辑_1982145267631833089.json, 图片生成/图生图/（自用）Qwen-Edit 2511 Aio V16单图编辑_2003877704216813569.json, 图片生成/图生图/（自用）Qwen-Edit Aio V4模型单图编辑_1977754904884379650.json, 图片生成/图生图/（自用）Qwen-Edit Aio V5.1模型单图编辑_1980187947175677954.json, 图片生成/图生图/（自用）Qwen-Edit Aio V5模型单图编辑_1978125941199233025.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_checkpoint_vae_5

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/单图_2000211503481581570.json、图片生成/图生图/单图姿势参照_2002974605021200385.json、图片生成/图生图/（4图版-（自用）-F2P）同景同人随机Qwen-Edit Aio V7.1图像编辑_1985321438334828546.json、图片生成/图生图/（4图版-（自用））同景同人随机Qwen-Edit Aio V5.1图像编辑_1980187963835453441.json、图片生成/图生图/（4图版（自用））同景同人随机Qwen-Edit Aio V5.2图像编辑_1982145252280680449.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 13 个 workflow 都包含：
- `CR Prompt Text`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `GetImageSizeAndCount`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `TT_img_enc`
- `TT_img_enc_v2`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `Text Multiline` —— 10/13 个有
- `Float` —— 5/13 个有
- `LoraLoaderModelOnly` —— 5/13 个有
- `ImageConcanate` —— 4/13 个有
- `RH_LLMAPI_NODE` —— 4/13 个有
- `Text Concatenate` —— 4/13 个有
- `DuckHideNode` —— 3/13 个有
- `AIO_Preprocessor` —— 1/13 个有
- `PreviewImage` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 13 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 13 | 100% |
| 采样算法 | euler_ancestral | - | 13 | 100% |
| 调度器 | beta | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |
| 宽度 | 768 | 768 - 768 | 13 | 100% |
| 高度 | 768 | 768 - 768 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，13 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，13 个样本，一致性 100%
- 调度器 最常用 beta，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 宽度 中位数 768，观测区间 768 - 768，13 个样本，取值集中（一致性 100%）
- 高度 中位数 768，观测区间 768 - 768，13 个样本，取值集中（一致性 100%）
- 高发问题（13/13 个样本）：Steps较低可能导致细节不足

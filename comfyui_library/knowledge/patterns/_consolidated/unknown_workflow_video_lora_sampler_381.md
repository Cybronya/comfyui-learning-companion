---
name: unknown_workflow_video_lora_sampler_381
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.9444
common_nodes: [CLIPLoader, CLIPTextEncode, GetImageRangeFromBatch, ImageConcanate, JWInteger, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, ModelSamplingSD3, PathchSageAttentionKJ, PreviewImage, RepeatImageBatch, SaveImage, TrimVideoLatent, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanVaceToVideo]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Wan2.1-姿势控制图生图_1949810093015654401.json, 图片生成/图生图/Wan2.1-深度控制图生图_1949810038555721730.json, 图片生成/图生图/Wan2.1一致性扩图图生图V1_1947268029098905601.json, 图片生成/图生图/Wan2.1姿势控制人物一致性图生图V1_1947250426543509506.json, 图片生成/图生图/Wan2.1深度控制人物一致性图生图V0.5_1947263708557905922.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_381

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Wan2.1-姿势控制图生图_1949810093015654401.json、图片生成/图生图/Wan2.1-深度控制图生图_1949810038555721730.json、图片生成/图生图/Wan2.1一致性扩图图生图V1_1947268029098905601.json、图片生成/图生图/Wan2.1姿势控制人物一致性图生图V1_1947250426543509506.json、图片生成/图生图/Wan2.1深度控制人物一致性图生图V0.5_1947263708557905922.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `GetImageRangeFromBatch`
- `ImageConcanate`
- `JWInteger`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `RepeatImageBatch`
- `SaveImage`
- `TrimVideoLatent`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanVaceToVideo`

**可变部分**（部分 workflow 才有）：
- `PDIMAGE_LongerSize` —— 4/5 个有
- `CR Prompt Text` —— 3/5 个有
- `DWPreprocessor` —— 2/5 个有
- `DepthAnything_V2` —— 2/5 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 2/5 个有
- `DF_Get_image_size` —— 1/5 个有
- `ImagePadKJ` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 6 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | uni_pc | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 6，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足

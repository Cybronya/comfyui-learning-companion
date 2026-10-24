---
name: unknown_workflow_lora_sampler_unet_61
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.920667
common_nodes: [CFGNorm, CLIPLoader, ConditioningZeroOut, EmptyLatentImage, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/QWEN Edit 2509 多图 人物一致性 工作流！超简单_1984218554033717250.json, 图片生成/图生图/双图 多图融合 图生图 图片编辑 商品展示_2045373556841779201.json, 图片生成/图生图/商品展示 多图融合 图生图 图片编辑_2044378332166361089.json, 图片生成/图生图/图生图 图片编辑 多图编辑_2044337548310355970.json, 图片生成/图生图/图生图 图片编辑 多图编辑_2044346249851179010.json, 图片生成/图生图/图生图 图片编辑 多图编辑_2044369934167314434.json, 图片生成/图生图/图生图 图片编辑 多图编辑_2108489817746137089.json, 图片生成/图生图/局部重绘  图生图  洗图_2046470428926943233.json, 图片生成/图生图/极速三宫格工作流！超简单_1983748538079354881.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_61

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/QWEN Edit 2509 多图 人物一致性 工作流！超简单_1984218554033717250.json、图片生成/图生图/双图 多图融合 图生图 图片编辑 商品展示_2045373556841779201.json、图片生成/图生图/商品展示 多图融合 图生图 图片编辑_2044378332166361089.json、图片生成/图生图/图生图 图片编辑 多图编辑_2044337548310355970.json、图片生成/图生图/图生图 图片编辑 多图编辑_2044346249851179010.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 9 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJ` —— 2/9 个有
- `LayerMask: BiRefNetUltraV2` —— 2/9 个有
- `LayerMask: LoadBiRefNetModelV2` —— 2/9 个有
- `LayerUtility: ColorImage V2` —— 2/9 个有
- `LayerUtility: ImageBlend` —— 2/9 个有
- `easy promptLine` —— 2/9 个有
- `CR Overlay Text` —— 1/9 个有
- `GetImageRangeFromBatch` —— 1/9 个有
- `ImageConcatMulti` —— 1/9 个有
- `ImageListToImageBatch` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1280 | 9 | 90% |
| 高度 | 1536 | 760 - 1536 | 9 | 78% |
| 采样步数 | 8 | 8 - 8 | 9 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1280，9 个样本，取值集中（一致性 90%）
- 高度 中位数 1536，观测区间 760 - 1536，9 个样本
- 采样步数 中位数 8，观测区间 8 - 8，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足

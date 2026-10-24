---
name: unknown_workflow_lora_sampler_vae_9
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.882556
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/QwenImageEdit去除视频首帧字幕&水印_2013817473283395585.json, 图片生成/图生图/image2511 双图参考+姿势参考_2047986409801256962.json, 图片生成/图生图/qwen2509图生图工作流_2082074109466472449.json, 图片生成/图生图/qwen2511_三图参考_2082339908525580289.json, 图片生成/图生图/qwen2511_单图编辑_2082340988181377026.json, 图片生成/图生图/qwen2511_角色参考（单人、双人、三人）_2038433092590899201.json, 图片生成/图生图/qwen2511写真姿势~_2053388737001861121.json, 图片生成/图生图/qwenImage2511 制作人物卡_2081256495148261378.json, 图片生成/图生图/参考图生图_2039898551551004673.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_vae_9

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/QwenImageEdit去除视频首帧字幕&水印_2013817473283395585.json、图片生成/图生图/image2511 双图参考+姿势参考_2047986409801256962.json、图片生成/图生图/qwen2509图生图工作流_2082074109466472449.json、图片生成/图生图/qwen2511_三图参考_2082339908525580289.json、图片生成/图生图/qwen2511_单图编辑_2082340988181377026.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 9 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 8/9 个有
- `FluxKontextImageScale` —— 8/9 个有
- `FluxKontextMultiReferenceLatentMethod` —— 8/9 个有
- `LoadImage` —— 8/9 个有
- `UNETLoader` —— 8/9 个有
- `PrimitiveInt` —— 7/9 个有
- `PreviewImage` —— 4/9 个有
- `DWPreprocessor` —— 1/9 个有
- `DiffusionModelLoaderKJ` —— 1/9 个有
- `ImageStitch` —— 1/9 个有
- `PrimitiveStringMultiline` —— 1/9 个有
- `VAEEncode` —— 1/9 个有
- `VHS_LoadVideo` —— 1/9 个有
- `easy promptConcat` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 9 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 89% |
| 调度器 | simple | - | 9 | 89% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 89%
- 调度器 最常用 simple，9 个样本，一致性 89%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（10/9 个样本）：Steps较低可能导致细节不足

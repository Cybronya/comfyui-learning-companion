---
name: unknown_workflow_lora_sampler_unet_168
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.91575
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/QWEN2511双人合影_2002768332413648897.json, 图片生成/图生图/Qwen-Edit-2509-10个方向灯光工作流_1990236290165690369.json, 图片生成/图生图/QwenEdit2511双图参考_2005975910811652098.json, 图片生成/图生图/QwenImage2511+SDpose 编辑图片人物姿态_2056328465883947009.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_168

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/QWEN2511双人合影_2002768332413648897.json、图片生成/图生图/Qwen-Edit-2509-10个方向灯光工作流_1990236290165690369.json、图片生成/图生图/QwenEdit2511双图参考_2005975910811652098.json、图片生成/图生图/QwenImage2511+SDpose 编辑图片人物姿态_2056328465883947009.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyLatentImage` —— 3/4 个有
- `FluxKontextImageScale` —— 3/4 个有
- `FluxKontextMultiReferenceLatentMethod` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `PrimitiveInt` —— 2/4 个有
- `AspectRatio` —— 1/4 个有
- `CheckpointLoaderSimple` —— 1/4 个有
- `ConditioningZeroOut` —— 1/4 个有
- `EmptySD3LatentImage` —— 1/4 个有
- `GenerateNoise` —— 1/4 个有
- `LGNoiseInjectionLatent` —— 1/4 个有
- `SDPoseDrawKeypoints` —— 1/4 个有
- `SDPoseKeypointExtractor` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1280 | 3 | 89% |
| 高度 | 1280 | 832 - 1824 | 3 | 69% |
| 采样步数 | 7 | 4 - 8 | 4 | 74% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1280，3 个样本，取值集中（一致性 89%）
- 高度 中位数 1280，观测区间 832 - 1824，3 个样本
- 采样步数 中位数 7，观测区间 4 - 8，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足

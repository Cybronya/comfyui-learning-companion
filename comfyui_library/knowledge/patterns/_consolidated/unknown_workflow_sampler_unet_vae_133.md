---
name: unknown_workflow_sampler_unet_vae_133
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.913875
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/【开源】Qwen image 2.1 文生图_2102002816368857089.json, 图片生成/文生图/【遇见AI】qwen image 2.1 turbo大模型基础文生图_2108863368416292866.json, 图片生成/文生图/【遇见AI】qwen image 2.1 官方turbo加速lora文生图基础流_2108863647031320578.json, 图片生成/文生图/【遇见AI】qwen image 2.1文生图基础流_2101841432792363010.json, 图片生成/文生图/千问2.1文生图_2101907864641167362.json, 图片生成/文生图/图像编辑（多图）-qwen image 2.1_2101936015538737153.json, 数字人/数字人/qwen_image_2_1_角色三视图生成(自定义服装)_2108073982967762946.json, 数字人/数字人/千问工作流_2102229006685917186.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_133

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/【开源】Qwen image 2.1 文生图_2102002816368857089.json、图片生成/文生图/【遇见AI】qwen image 2.1 turbo大模型基础文生图_2108863368416292866.json、图片生成/文生图/【遇见AI】qwen image 2.1 官方turbo加速lora文生图基础流_2108863647031320578.json、图片生成/文生图/【遇见AI】qwen image 2.1文生图基础流_2101841432792363010.json、图片生成/文生图/千问2.1文生图_2101907864641167362.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 6/8 个有
- `SaveImageAdvanced` —— 3/8 个有
- `ComfySwitchNode` —— 2/8 个有
- `LoraLoaderModelOnly` —— 2/8 个有
- `QwenImage21Cache` —— 2/8 个有
- `Text` —— 2/8 个有
- `CR Text` —— 1/8 个有
- `easy promptList` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 8 - 25 | 8 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 88% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 8 | 100% |
| 高度 | 1024 | 1024 - 1024 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 25，观测区间 8 - 25，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 88%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，8 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，8 个样本，取值集中（一致性 100%）
